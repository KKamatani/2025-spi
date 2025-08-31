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

## プログラム（12 講演・各 45 分） {#program}

### 1日目｜2025年10月21日（火）

<div class="program" markdown="1">
| 時間帯      | 内容                                   | 備考   |
| ---        | ---                                    | ---    |
| 10:30–10:40 | **開会挨拶**                           | 10分   |
| 10:40–11:25 | 口頭発表 **①**                         | 45分   |
| 11:25–12:10 | 口頭発表 **②**                         | 45分   |
| 12:10–13:30 | **昼食休憩**                           | 80分   |
| 13:30–14:15 | 口頭発表 **③**                         | 45分   |
| 14:15–15:00 | 口頭発表 **④**                         | 45分   |
| 15:00–15:20 | **休憩**                               | コーヒー |
| 15:20–16:05 | 口頭発表 **⑤**                         | 45分   |
| 16:05–16:50 | 口頭発表 **⑥**                         | 45分   |
| 16:50–17:10 | **総合討論**                           | 20分   |
| 17:10       | **終了**                               |        |
{: .program }

### 2日目｜2025年10月22日（水）

| 時間帯      | 内容           | 備考   |
| ---        | ---            | ---    |
| 10:30–10:40 | **連絡事項**   | 10分   |
| 10:40–11:25 | 口頭発表 **⑦** | 45分   |
| 11:25–12:10 | 口頭発表 **⑧** | 45分   |
| 12:10–13:30 | **昼食休憩**   | 80分   |
| 13:30–14:15 | 口頭発表 **⑨** | 45分   |
| 14:15–15:00 | 口頭発表 **⑩** | 45分   |
| 15:00–15:20 | **休憩**       | コーヒー |
| 15:20–16:05 | 口頭発表 **⑪** | 45分   |
| 16:05–16:50 | 口頭発表 **⑫** | 45分   |
| 16:50–17:10 | **総括・閉会挨拶** | 20分 |
| 17:10       | **終了**       |        |
{: .program }

<style>
/* 見た目をすっきりさせる（必要なら微調整OK） */
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
