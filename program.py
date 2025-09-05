# -*- coding: utf-8 -*-
"""
アブストラクト・タイトルリストの生成コード
入力:  data.csv
出力:  talks.html
"""

import csv, re, html
from pathlib import Path
from typing import Dict, List, Optional

# ==== 設定 ====
CSV_PATH = Path("data.csv")
OUT_PATH = Path("talks.html")
ALLOW_EMPTY_ABSTRACT = False  # True にすると抄録空でも掲載

# 列名の明示マップ（必要なら設定）: 右辺にCSVの実際の列見出し
MANUAL_MAP: Dict[str, str] = {
    # "name": "氏名",
    # "affil": "所属",
    # "title": "発表タイトル",
    # "abstract": "アブストラクト",
    # "order": "Order",
}

# ==== ユーティリティ ====
def _norm(s: str) -> str:
    import re
    return re.sub(r"\s+", "", s).lower()

def pick_column(headers: List[str], candidates: List[str]) -> Optional[str]:
    nheaders = [_norm(h) for h in headers]
    for cand in candidates:
        nc = _norm(cand)
        for i, nh in enumerate(nheaders):
            if nh == nc:
                return headers[i]
        for i, nh in enumerate(nheaders):
            if nc in nh:
                return headers[i]
    return None

def ensure_mapping(headers: List[str]) -> Dict[str, Optional[str]]:
    if MANUAL_MAP:
        base = {"name": None, "affil": None, "title": None, "abstract": None, "order": None}
        base.update(MANUAL_MAP)
        return base
    m: Dict[str, Optional[str]] = {}
    m["name"]     = pick_column(headers, ["氏名","お名前","名前","発表者","speaker","name"])
    m["affil"]    = pick_column(headers, ["所属","大学","所属・役職","affiliation","institution","university"])
    m["title"]    = pick_column(headers, ["タイトル","題目","発表タイトル","発表題目","title"])
    m["abstract"] = pick_column(headers, ["アブストラクト","要旨","概要","abstract"])
    m["order"]    = pick_column(headers, ["order","順番","番号","セッション番号","sort"])
    return m

def html_escape_preserve(text: str) -> str:
    if text is None:
        return ""
    s = html.escape(str(text), quote=False)  # &,<,> のみ
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    return s.replace("\n", "<br>")  # 改行は <br>

def is_breakish(name: str, title: str) -> bool:
    s = f"{name or ''} {title or ''}"
    return any(k in s for k in ["休憩","昼食","ランチ","終了","閉会","開会","挨拶"])

# ==== メイン ====
def main():
    # CSV読込
    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        headers = reader.fieldnames or []
    if not rows:
        raise RuntimeError("CSVが空です。")

    mp = ensure_mapping(headers)
    for k in ("name","title","abstract","order"):
        if not mp.get(k):
            raise RuntimeError(f"必須列 '{k}' が検出できません。列名を確認するか MANUAL_MAP を設定してください。\n検出: {mp}\nCSV列: {headers}")

    # 行の抽出と検証（Order 絶対 / break 除外 / abstract 必須）
    talks = []
    missing_orders = []
    for r in rows:
        name = (r.get(mp["name"]) or "").strip()
        title = (r.get(mp["title"]) or "").strip()
        abstr = (r.get(mp["abstract"]) or "").strip()
        affil = (r.get(mp["affil"]) or "").strip() if mp.get("affil") else ""

        if not name and not title:
            continue
        if is_breakish(name, title):
            continue
        if not ALLOW_EMPTY_ABSTRACT and not abstr:
            continue

        ord_raw = r.get(mp["order"])
        try:
            order = int(str(ord_raw).strip())
        except Exception:
            missing_orders.append(name or title)
            continue

        talks.append({
            "order": order,
            "name": name,
            "affil": affil,
            "title": title,
            "abstract": abstr,
        })

    if missing_orders:
        raise RuntimeError("Order 未指定/不正の発表があります（break 以外）：\n- " + "\n- ".join(missing_orders))

    # Order で絶対順に
    talks.sort(key=lambda x: x["order"])

    # 出力生成（<div class="talks" markdown="1"> … </div>）
    out_lines = []
    out_lines.append('<div class="talks" markdown="1">')
    tid = 1
    for t in talks:
        name = t["name"]
        aff  = t["affil"]
        title = html_escape_preserve(t["title"])
        abstr = html_escape_preserve(t["abstract"])
        disp_name = f"{name}（{aff}）" if aff else name
        tid_str = f"t{tid:02d}"
        out_lines.append(f'<details id="{tid_str}" markdown="1">')
        out_lines.append(f'<summary>{disp_name} — <em>{title}</em></summary>')
        out_lines.append(f"<p>{abstr}</p>")
        out_lines.append('<p><a class="to-top" href="#program">↑ プログラムに戻る</a></p>')
        out_lines.append("</details>\n")
        tid += 1
    out_lines.append("</div>\n")

    OUT_PATH.write_text("\n".join(out_lines), encoding="utf-8")
    print(f"✅ 出力: {OUT_PATH.resolve()}")

if __name__ == "__main__":
    main()
