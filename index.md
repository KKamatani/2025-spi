---
layout: splash
title: "確率過程の統計推測の最近の展開"
header:
  overlay_image: "/assets/hero.jpg"
  overlay_filter: 0.0
  actions:
    - label: "概要"
      url: "#overview"
    - label: "プログラム"
      url: "#program"
    - label: "発表詳細"
      url: "#talks"
excerpt: "2025年10月21日（火）・10月22日（水）｜統計数理研究所"
---



## 概要 {#overview}

- **日時**：2025年10月21日（火）・10月22日（水）
- **会場**：統計数理研究所 大会議室
- JST CREST （代表：吉田朋広）

---

## プログラム案（各 40 分） {#program}

### 1日目｜2025年10月21日（火）

<div class="program" markdown="1">
| 時間帯      | 内容                                   | 備考            |
| ---        | ---                                    | ---             |
| 10:30–11:10 | 口頭発表 **①（白石 博）**              | 40分            |
| 11:10–11:50 | 口頭発表 **②（松田 孟留）**            | 40分            |
| 11:50–12:30 | 口頭発表 **③（村上 大輔）**            | 40分            |
| 12:30–13:50 | **昼食休憩**                           | 80分            |
| 13:50–14:30 | 口頭発表 **④（松田 安昌）**            | 40分            |
| 14:30–15:10 | 口頭発表 **⑤（内田 雅之）**            | 40分・オンライン |
| 15:10–15:30 | **休憩**                               | コーヒー        |
| 15:30–16:10 | 口頭発表 **⑥（吉田 朋広）**            | 40分            |
| 16:10–16:50 | 口頭発表 **⑦（清水 泰隆）**            | 40分〔午後遅め〕|
| 16:50       | **終了**                               |                 |
{: .program }

### 2日目｜2025年10月22日（水）

| 時間帯           | 内容                 | 備考   |
| ------------- | ------------------ | ---- |
| 10:30–11:10   | 口頭発表 **⑧（杉本 知之）**  | 40分  |
| 11:10–11:50   | 口頭発表 **⑨（栗﨑 正博）**  | 40分  |
| 11:50–12:30   | 口頭発表 **⑩（仲北 祥悟）**  | 40分  |
| 12:30–13:50   | **昼食休憩**           | 80分  |
| 13:50–14:30   | 口頭発表 **⑪（菅澤 翔之助）** | 40分  |
| 14:30–15:10   | 口頭発表 **⑫（入江 薫）**   | 40分  |
| 15:10–15:30   | **休憩**             | コーヒー |
| 15:30–16:10   | 口頭発表 **⑬（庄 建倉）**   | 40分  |
| 16:10–16:50   | 口頭発表 **⑭（栗木 哲）**   | 40分  |
| 16:50         | **終了**             |      |
| {: .program } |                    |      |


<style>
.talks details { border:1px solid rgba(0,0,0,.08); border-radius:12px; padding:.6rem .8rem; margin:.6rem 0; background:#fff }
.talks summary { cursor:pointer; list-style:none; font-weight:600; }
.talks summary::-webkit-details-marker { display:none }
.talks .meta { color:#64748b; font-weight:500; margin-left:.4rem; font-size:.9rem }
.talks .slot { font-feature-settings:"tnum"; font-variant-numeric:tabular-nums }
.talks .to-top { font-size:.85rem; color:#64748b; text-decoration:none }
.talks .to-top:hover { text-decoration:underline }
</style>

## 発表詳細 {#talks}

<div class="talks" markdown="1">

<details id="t01" markdown="1">
TBA
<p><a class="to-top" href="#program">↑ プログラムに戻る</a></p>
</details>

</div>




<script>
(() => {
  const hero = document.querySelector('.page__hero--overlay');
  if (!hero) return;

  const SPEED = 0.35; // 背景が本文の何倍ゆっくり動くか（0.2〜0.5くらいで調整）
  let ticking = false;

  function update() {
    const y = window.scrollY || window.pageYOffset;
    // 背景のY位置をスクロールに応じて少しだけずらす
    hero.style.backgroundPosition = `center calc(50% + ${y * SPEED}px)`;
    ticking = false;
  }
  function onScroll() {
    if (!ticking) {
      requestAnimationFrame(update);
      ticking = true;
    }
  }

  // モバイルや低性能・低視覚負荷設定では無効化
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const isMobile = window.matchMedia('(max-width: 900px)').matches;
  if (reduce || isMobile) return;

  window.addEventListener('scroll', onScroll, { passive: true });
  update();
})();
</script>
