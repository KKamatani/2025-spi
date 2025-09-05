---
layout: splash
title: "確率過程の統計推測の最近の展開"
header:
  overlay_image: "/assets/hero.jpg"
  overlay_filter: 0.0
  actions:
    - label: "Overview"
      url: "#overview"
    - label: "Program"
      url: "#program"
    - label: "Abstracts"
      url: "#talks"
excerpt: "2025年10月21日（火）・10月22日（水）｜統計数理研究所"
---

## Overview {#overview}

- **日時**：2025年10月21日（火）・10月22日（水）
- **会場**：
- JST CREST （代表：吉田朋広）


---

## Program 案（各 40 分） {#program}


### 1日目｜2025年10月21日（火）

<div class="program" markdown="1">
| Time | Speaker | Notes |
| --- | --- | --- |
| 10:30–11:10 | [**白石 博（慶應義塾大学理工学部数理科学科）**](#t01) | 40分 |
| 11:10–11:50 | [**松田 孟留（東京大学、理研CBS）**](#t02) | 40分 |
| 11:50–12:30 | [**村上 大輔（統計数理研究所）**](#t03) | 40分 |
| 12:30–13:50 | **昼食休憩**                           | 80分            |
| 13:50–14:30 | [**松田 安昌（東北大学大学院経済学研究科）**](#t04) | 40分 |
| 14:30–15:10 | [**内田 雅之（大阪大学）**](#t05) | 40分 |
| 15:10–15:30 | **休憩**                               | 20分        |
| 15:30–16:10 | [**吉田 朋広（東京大学大学院数理科学研究科）**](#t06) | 40分 |
| 16:10–16:50 | [**清水 泰隆（早稲田大学）**](#t07) | 40分 |
| 16:50       | **終了**                               |                 |
{: .program }

### 2日目｜2025年10月22日（水）

| Time           | Speaker                                  | Notes   |
| ------------- | ----------------------------------- | ---- |
| 10:30–11:10   | [**杉本 知之（大阪大学基礎工学研究科）**](#t08)    | 40分  |
| 11:10–11:50   | [**栗﨑 正博（理化学研究所 AIPセンター）**](#t09) | 40分  |
| 11:50–12:30   | [**仲北 祥悟（東京大学大学院総合文化研究科）**](#t10) | 40分  |
| 12:30–13:50   | **昼食休憩**                            | 80分  |
| 13:50–14:30   | [**菅澤 翔之助（慶應義塾大学）**](#t11)        | 40分  |
| 14:30–15:10   | [**入江 薫（東京大学経済学部）**](#t12)        | 40分  |
| 15:10–15:30   | **休憩**                              | 20分 |
| 15:30–16:10   | [**庄 建倉（統計数理研究所）**](#t13)         | 40分  |
| 16:10–16:50   | [**栗木 哲（統計数理研究所）**](#t14)         | 40分  |
| 16:50         | **終了**                              |      |
{: .program }


<style>
.talks details { border:1px solid rgba(0,0,0,.08); border-radius:12px; padding:.6rem .8rem; margin:.6rem 0; background:#fff }
.talks summary { cursor:pointer; list-style:none; font-weight:600; }
.talks summary::-webkit-details-marker { display:none }
.talks .meta { color:#64748b; font-weight:500; margin-left:.4rem; font-size:.9rem }
.talks .slot { font-feature-settings:"tnum"; font-variant-numeric:tabular-nums }
.talks .to-top { font-size:.85rem; color:#64748b; text-decoration:none }
.talks .to-top:hover { text-decoration:underline }
</style>


## Abstracts {#talks}

<div class="talks" markdown="1">
<details id="t01" markdown="1">
<summary>白石博（慶應義塾大学理工学部数理科学科） — <em>Non-asymptotic analysis for random forest kernel</em></summary>
<p>Athey et.al(2019) が提案したGeneralized Random Forests (GRF) では、局所推定方程式の解として定義されたパラメータ関数を、Random Forest(RF)で構成された重み関数を用いた統計量の最小化解として定義する。この重み関数はデータ駆動型の統計量であるため、従来のカーネル関数を用いたノンパラメトリック推定の理論を使うには工夫が必要となる。本研究では、RFを構成する決定木をある二項分岐過程として定式化し、重み関数を近似する非確率的な関数を導出する。これにより、GRF推定量の漸近理論に、Nadaraya-Watsonタイプの推定理論が活用できることが期待される。</p>
<p><a class="to-top" href="#program">↑ プログラムに戻る</a></p>
</details>

<details id="t02" markdown="1">
<summary>松田 孟留（東京大学、理研CBS） — <em>特異値縮小による適応的ノンパラメトリック推定</em></summary>
<p>関数推定や密度推定などのノンパラメトリック推定問題はガウス列モデル（可算無限次元の正規分布）の平均パラメータの推定問題に帰着される。この問題のミニマックスリスクは真の滑らかさやスケールに依存するが、これらの情報を用いることなく漸近的にミニマックスリスクを達成する適応的な推定量としてブロック型James--Stein推定量が知られている。本研究では、複数の関数や密度を同時に推定する状況を想定し、多変量版のガウス列モデルにおける適応的推定を考える。James--Stein推定量の行列への一般化であるEfron--Morris推定量は、低ランク行列の空間への縮小を行う経験ベイズ推定量である。Efron--Morris推定量がみたすオラクル不等式を導出し、ブロック型Efron--Morris推定量が任意の二乗損失（正定値二次形式）のもとで適応的ミニマックスであることを示す。すなわち、Efron--Morris推定量の特異値縮小は真の滑らかさとスケールに加えて相関構造にも適応する。</p>
<p><a class="to-top" href="#program">↑ プログラムに戻る</a></p>
</details>

<details id="t03" markdown="1">
<summary>村上大輔（統計数理研究所） — <em>局所モデルの段階的合成に基づく空間過程モデリング</em></summary>
<p>本研究では、空間データの予測や不確実性評価に広く用いられるGaussian process（GP）の計算負荷や柔軟性の課題を克服するために、局所モデルに基づく新たな空間過程モデルを提案する。提案モデルは、多数の局所モデルを合成することで得られる単一スケールの空間過程を、マルチスケールに統合することにより空間過程をモデル化する。その学習は、広域的パターンから局所的パターンへと段階的に進め、損失関数の改善が止まった時点で終了する逐次的手法を採用している。尤度に基づくGPとは異なり、提案手法の学習はholdout validationに基づくため、random forest（RF）やneural networkなどの学習と容易に統合可能である。また、GPとは異なり、共分散行列の逆行列計算を必要とせず、計算効率や並列性にも優れる。モンテカルロ実験により、提案手法の予測精度が既存の近似GPを上回ることを確認した。また、RFと統合した提案手法の予測精度が通常のRFを上回ることなども確認した。最後に、提案手法を首都圏における住宅地価格分析に応用することで、その実用性を検証する。</p>
<p><a class="to-top" href="#program">↑ プログラムに戻る</a></p>
</details>

<details id="t04" markdown="1">
<summary>松田安昌（東北大学大学院経済学研究科） — <em>Density-valued ARMA models by spline mixtures</em></summary>
<p>In this talk,  we propose a framework for modeling time series of probability density functions by extending auto-regressive moving average (ARMA) models to density-valued data. The method is based on a transformation approach, wherein each density function on a compact domain $[0,1]^d$ is approximated by a B-spline mixture representation. Through generalized logit and softmax mappings, the space of density functions is transformed into an unconstrained Euclidean space, enabling the application of classical time series techniques. We define ARMA-type dynamics in the transformed space. Estimation is carried out via least squares for density-valued AR models and Whittle likelihood for ARMA models, with asymptotic normality derived under the joint divergence of the time horizon and basis dimension. The proposed methodology is applied to spatio-temporal human population data in Tokyo, where meaningful temporal structures in the distributional dynamics are successfully captured.</p>
<p><a class="to-top" href="#program">↑ プログラムに戻る</a></p>
</details>

<details id="t05" markdown="1">
<summary>内田雅之（大阪大学） — <em>微小ノイズをもつ2 次元空間線形放物型 SPDEのパラメータ推定</em></summary>
<p>本研究では、微小ノイズをもつ2次元空間の2階線形放物型確率偏微分方程式（SPDE）のパラメータ推定について考察する。SPDEの駆動過程にはQ-Wiener過程を用い、データは時間および2次元空間上で高頻度に観測されるとする。本SPDEには、拡散、移流、反応の3種類のパラメータが含まれており、パラメータ推定は以下の手順で行う。(i) 時間および2次元空間におけるデータの増分（triple increments）を用いて、拡散および移流パラメータに対するコントラスト関数を構成し、そこから最小コントラスト推定量（MCE）を導出する。(ii) 高頻度時空間データと得られたMCEを用いて座標過程を近似し、その近似座標過程に基づいて反応パラメータの適応的推定量（AE）を導出する。さらに、提案する推定量（MCEおよびAE）の漸近的性質を示し、数値実験によってその漸近挙動の妥当性を検証する。</p>
<p><a class="to-top" href="#program">↑ プログラムに戻る</a></p>
</details>

<details id="t06" markdown="1">
<summary>吉田朋広（東京大学大学院数理科学研究科） — <em>TBA</em></summary>
<p>TBA</p>
<p><a class="to-top" href="#program">↑ プログラムに戻る</a></p>
</details>

<details id="t07" markdown="1">
<summary>清水泰隆（早稲田大学） — <em>M-estimation for Gaussian processes with time-inhomogeneous drifts</em></summary>
<p>本研究では，高頻度観測下で時間非一様なドリフトをもつガウス過程に対するコントラストベースの推定法を提案する．観測過程は，決定論的ドリフト関数と定常ガウス過程（パラメトリックなカーネルをもつ）の和としてモデル化される．本手法は，隣接する差分に基づく局所コントラスト関数を構成することで，行列の反転を回避し，計算効率の高い推定を実現する．さらに，一般的なエルゴード性の下で推定量の一致性と漸近正規性を保証する．加えて，局所コントラストのみでは識別できないカーネルパラメータについては，モーメント法を導入することで識別性を回復できることを示す．</p>
<p><a class="to-top" href="#program">↑ プログラムに戻る</a></p>
</details>

<details id="t08" markdown="1">
<summary>杉本知之（大阪大学基礎工学研究科） — <em>セミ競合リスクのもとでの2変量生存コピュラによる推測と修正ログランク法</em></summary>
<p>セミ競合リスクのもとでの2変量生存時間コピュラモデルによる推定方式や2群比較を議論する．セミ競合リスクのもとでのいくつかの既存研究では，回帰モデルなどより発展的な手法も提案されているが，計算上の難点も多い．また既存研究による推定量の構造は，非競合リスクと比べて非常に複雑であるため，より簡明に解釈できる形式にすることにも関心がある．本報告では，計算上の難点を緩和して，セミ競合リスクのもとでのEMアルゴリズム推定，およびログランク法の修正を構成し，周辺生存関数の推定や周辺ハザード比の推測に応用する．いくつかのシミュレーション実験を行い，推定アルゴリズムの性能を調べる．ただし，標準誤差推定においては，依然として計算上の難点があるため，通常ジャックナイフおよび無限小ジャックナイフ等による問題解決をはかる．またこの推測に基づく漸近的な議論も行う．</p>
<p><a class="to-top" href="#program">↑ プログラムに戻る</a></p>
</details>

<details id="t09" markdown="1">
<summary>栗﨑正博（理化学研究所 AIPセンター） — <em>非線形フィルタリングの漸近展開</em></summary>
<p>フィルタリングとは、時系列モデルの一部の成分が観測不可能な場合に、観測可能な成分を用いて観測不可能な成分の情報(条件付き期待値)を推定する問題を指す。モデルが線形の場合、フィルタリングの解は解析的に書ける一方、非線形の場合には有限次元で計算できないことが知られている。非線形のフィルタリングに対する既存のアプローチはいくつかあるが、高精度を求めれば計算負荷が増大し、計算量を抑えれば線形近似に依存するため十分な精度保証が得られないというトレードオフがある。本発表では、非線形フィルターの漸近展開という新たな手法を提案し、システムノイズが小さい場合に、非線形フィルターが解析的に展開できることを示す。この展開においては、展開次数を上げることにより真のフィルターが任意精度で近似できる一方、係数の計算は常微分方程式に帰着され、PDE的方法やモンテカルロ近似に比べて大幅に計算量を削減することが可能となる。</p>
<p><a class="to-top" href="#program">↑ プログラムに戻る</a></p>
</details>

<details id="t10" markdown="1">
<summary>仲北祥悟（東京大学大学院総合文化研究科） — <em>独立同分布な経路観測に基づく高次元Ornstein–Uhlenbeck過程のスパース推定</em></summary>
<p>本発表では、独立同分布な経路が多数観測される状況で、高次元Ornstein–Uhlenbeck過程のドリフト係数に対するスパース推定を議論する。パラメータ次元が大きい状況での推定手法として、観測期間が十分長いとする設定におけるスパース推定の理論・方法が近年議論されている。しかし実データ解析では、モデリングの対象となる現象を長時間追跡できるとは限らない場合も多い。本発表では、独立に同じ法則に従うOrnstein–Uhlenbeck過程について、その経路の本数に対する漸近設定を考え、スパース推定を構成する。理論的には非漸近上界を示し、また実証としては計算機による実験で、スパース推定がうまく機能することを見る。</p>
<p><a class="to-top" href="#program">↑ プログラムに戻る</a></p>
</details>

<details id="t11" markdown="1">
<summary>菅澤翔之助（慶應義塾大学） — <em>ベイズ的関数データクラスタリングにおける誤差分布の特定</em></summary>
<p>ノンパラメトリックベイズ法による関数データクラスタリングは、経験的に過剰な数のクラスターが得られることが多い。既存の研究では、この問題はディリクレ過程などの分割事前分布に起因するとされ、より柔軟な分割構造をもつ確率過程の導入が提案されてきた。本研究では、ベイズ的定式化における誤差分布の特定化に着目し、従来のモデルで仮定される独立ノイズ構造に焦点を当てる。事後分布の理論解析を通じて、関数データが本来もつ相関構造を無視した独立誤差分布を仮定すると、データ情報が過度に事後分布へ反映されることが、クラスター数の過剰推定の要因であることを明らかにする。これに対する解決策として、ガウス過程による誤差分布の導入を提案し、マルコフ連鎖モンテカルロ法による推定アルゴリズムを提示する。また、誤差構造を適切にモデル化することで、関数クラスタリングの性能が向上することを数値実験により示す。</p>
<p><a class="to-top" href="#program">↑ プログラムに戻る</a></p>
</details>

<details id="t12" markdown="1">
<summary>入江薫（東京大学経済学部） — <em>Sequential Bayesian Predictive Synthesis</em></summary>
<p>Dynamic Bayesian predictive synthesis is a formal approach to coherently synthesizing multiple predictive distributions into a single distribution. In sequential analysis, the computation of the synthesized predictive distribution has heavily relied on the repeated use of the Markov chain Monte Carlo method. To realize the real-time monitoring and forecasting, we provide a custom, Rao-Blackwellized particle filter for the linear and Gaussian synthesis, supplemented by timely interventions by the MCMC method to avoid<br>the problem of particle degeneracy. In an example of predicting US inflation rate, where a<br>sudden burst is observed in 2020-2022, the fast computation of the proposed method enables the calibration of the predictive synthesis and flexible adaptative even in the presense of the structural change.</p>
<p><a class="to-top" href="#program">↑ プログラムに戻る</a></p>
</details>

<details id="t13" markdown="1">
<summary>庄建倉（統計数理研究所） — <em>A General Framework for Residual Analysis</em></summary>
<p>Residual analysis provides an important and powerful tool for model diagnostics and improvement. It allows the evaluation of model fit without the need to formulate new, computationally expensive alternatives, while highlighting both the strengths and limitations of existing models. Building on recent developments in innovation-based residuals for spatial and spatiotemporal point processes, as well as extensions to hidden Markov models and state-space models, this study demonstrates the general principles of innovational residual analysis and its role in advancing statistical modeling. Through some application examples, I illustrate how appropriately constructed residual statistics can guide the refinement of model formulation and lead to more robust statistical inference for different types of models.</p>
<p><a class="to-top" href="#program">↑ プログラムに戻る</a></p>
</details>

<details id="t14" markdown="1">
<summary>栗木哲（統計数理研究所） — <em>Tube formula for spherically contoured random fields with subexponential marginals</em></summary>
<p>It is widely known that the tube method, or equivalently the Euler characteristic heuristic, provides a very accurate approximation for the tail probability that the supremum of a smooth Gaussian random field exceeds a threshold value c. The relative approximation error Δ(c) is exponentially small as a function of c when c tends to infinity. On the other hand, little is known about non-Gaussian random fields.<br>   In this paper, we obtain the approximation error of the tube method applied to the canonical isotropic random fields on a unit sphere defined by u↦⟨u,ξ⟩, u∈M⊂𝕊n−1, where ξ is a spherically contoured random vector. These random fields have statistical applications in multiple testing and simultaneous regression inference when the unknown variance is estimated. The decay rate of the relative error Δ(c) depends on the tail of the distribution of ‖ξ‖2 and the critical radius of the index set M. If this distribution is subexponential but not regularly varying, Δ(c)→0 as c→∞. However, in the regularly varying case, Δ(c) does not vanish and hence is not negligible. To address this limitation, we provide simple upper and lower bounds for Δ(c) and for the tube formula itself. Numerical studies are conducted to assess the accuracy of the asymptotic approximation.<br>(Joint work with E. Spodarev)</p>
<p><a class="to-top" href="#program">↑ プログラムに戻る</a></p>
</details>

</div>




<script>
(() => {
  const hero = document.querySelector('.page__hero--overlay');
  if (!hero) return;
  const SPEED = 0.35;
  let ticking = false;
  function update() {
    const y = window.scrollY || window.pageYOffset;
    hero.style.backgroundPosition = `center calc(50% + ${y * SPEED}px)`;
    ticking = false;
  }
  function onScroll() {
    if (!ticking) {
      requestAnimationFrame(update);
      ticking = true;
    }
  }
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const isMobile = window.matchMedia('(max-width: 900px)').matches;
  if (reduce || isMobile) return;
  window.addEventListener('scroll', onScroll, { passive: true });
  update();
})();
</script>
