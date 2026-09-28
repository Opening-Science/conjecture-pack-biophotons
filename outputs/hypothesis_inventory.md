# Hypothesis inventory v2 — causal hierarchy with verified evidence

The field's claims as scoped, testable hypotheses on a six-level causal hierarchy (generation → optical state → propagation → receiver → correlation → prediction), each with an operational null and estimand. Restructured after the adversarial cross-model review: the old H4 is split into a source claim (H4a) and a receiver-null family (H4b, whose evidence is by definition the refutation record of H1/H5 — mapped, not double-counted); nesting is explicit (H1 ⊂ H5; H7 is a mechanism for H5/H6, not their rival); H2 carries operational sub-claims sharing its evidence pool. Compare witness totals only within a level.

**Counting units.** Two are reported per claim: *works* (distinct papers with ≥1 adversarially verified witness of that stance — the conservative, Codex-recommended unit; primary-only excludes reviews, books and other secondary types) and *sentences* (verified witnesses; 733 rows). Corpus-wide, deduplicated at work level across all claims: **207 supporting vs 31 refuting works (6.7:1; primary-only 200:29)**, against 438:41 verified sentences (10.7:1) — the asymmetry shrinks under work-level deduplication but stands. Per-claim work counts below overlap across entries that share an evidence pool; compare only within a level. All figures are computed from the knowledgebase at generation time and remain pipeline-conditional observations, not publication-bias estimates.

**The entailment tier (strictest).** Every verified stance sentence was additionally judged for ENTAILMENT of its claim as scoped (Codex finding 8): secondhand review assertions, theory-only results and narrow-sub-case nulls downgrade to *partial*. Under this standard the corpus holds just **22 sentences (15 works) fully entailing support and 8 sentences (6 works) fully entailing refutation** across the 15 registry claims — the field's first-hand, scope-matched evidential core is 21 papers. Everything else is secondhand restatement, theory, or adjacent evidence.


## Level 1 — Generation mechanism

### H4a — Known oxidative pathways (ROS-driven lipid/protein oxidation producing triplet carbonyls and singlet oxygen) account for the dominant fraction of spontaneous UPE intensity in aerobic, non-photosynthetic cells (380–700 nm)

*Evidence pool inherited from H4; stance judgments were made against that claim's text, not this entry's narrower scope.*

**Null:** After quenching the named pathways, the residual emission fraction exceeds a pre-agreed threshold (e.g. >20%), or spectra are inconsistent with the named emitters  
**Estimand:** Fraction of band-integrated emission removed by targeted pathway perturbation, with spectral consistency check  
**Origin:** Cilento/Cadenas; Pospíšil–Prasad programme

**Evidence (verified):** 3 supporting / 2 refuting works (primary-only 2/2); full-entailment works 0S/0R; sentence witnesses 3S/3R/2D

EDITORIAL: the well-supported core of old H4; deliberately says nothing about function.

**Strongest verified support:**

- "Conversely, L-arginine did not seem to elicit UPE when added to non-diabetic serum under similar conditions. *** Data revealed the interaction between methylglyoxal glycation and L-arginine generated harmful O-2 as a by-product and subsequently could exacerbate the oxidative stress status of diabeti"  
  — Ultraweak Photon Emission as a Non-Invasive Health Assessment: A Syste (2014), ~p.7 `W2109151393`
- "Much evidence confirms that mitochondrial oxidative metabolism is the primary source of biophoton production in ­neurons8."  
  — Simulation of nerve fiber based on anti-resonant reflecting optical wa (2022), ~p.1 `W4308920644`
- "It has been demonstrated that biological systems release photons as a result of their oxidative metabolism; this release is termed biophoton emission (Popp, 1994)."  
  — Discrimination of biological systems with photon emission: steps towar (2019), ~p.12 `W3084164447`

**Strongest verified refutation:**

- "These results support the hypothesis that biophotonic radiation is not just a by-product of metabolism, but a revealing parameter of the electrodynamic coherence and energy potential of a biological system (Popp et al., 2011; Van Wijk et al., 2014). 36 South Florida Journal of Development, Miami, v."  
  — Biophotonic evaluation of water treated by biodynamization: comparison (2025), ~p.33 `W4416736719`
- "From this perspective, the results of this study support the hypothesis that biophotonic radiation is not only a by-product of metabolism, but also a direct indicator of the electrodynamic coherence and overall energy potential of a biological system (Popp et al., 2011; Van Wijk et al., 2014). 7 GEN"  
  — Comparative analysis of ultra-weak photon emission in the 380–630 nm b (2026), ~p.9 `W7128597566`


### H10 — Interfacial/structured water in cells materially alters UPE generation or storage relative to bulk-water chemistry (scoped to UPE-relevant observables)

*(relates to H2)*

**Null:** UPE observables are fully accounted for by bulk-water reaction kinetics at 310 K  
**Estimand:** A named UPE observable that differs between bulk and interfacial preparations under matched chemistry  
**Origin:** Del Giudice/Preparata; Pollack

**Evidence (verified):** 18 supporting / 2 refuting works (primary-only 17/2); full-entailment works 0S/0R; sentence witnesses 32S/5R/14D

EDITORIAL: reputationally delicate; kept only in its UPE-scoped form; condensed-matter objections stated.

**Strongest verified support:**

- "Pollack et al. demonstrated that radiant energy can generate an exclusion zone (EZ) in a water interface that possesses the correct type of hydrophilic/hydrophobic balance [65, 125]."  
  — Biological effects and medical applications of infrared radiation (2017), ~p.16 `W2607303579`
- "The width and electron donor capacity of EZ water in fact is increased when water is irradiated with lowintensive light; the maxi mum effect was observed when the samples were irra diated with IR radiation in the range of 2–3 μm [48]."  
  — The stable nonequilibrium state of bicarbonate aqueous systems (2012), ~p.8 `W1964318044`
- "This positive potential is measured directly and is also consistent with pH measurements, which show an extreme drop of pH immediately beyond the exclusion zone, often to less than pH 3."  
  — Molecules, Water, and Radiant Energy: New Clues for the Origin of Life (2009), ~p.4 `W2083775816`

**Strongest verified refutation:**

- "The negative charge did not distribute uniformly over the structure and optimization of the structure resulted in a “bulk-type water aggregate”, showing it to be unstable.[50] Elia et al. suggest that perturbations near the EZ surface can cause clumps of EZ water to disperse in the bulk liquid, resu"  
  — Exclusion Zone Phenomena in Water—A Critical Review of Experimental Fi (2020), ~p.3 `W3043384831`
- "Carboxylate, amino and polystyrene microspheres failed to reveal an exclusion zone in any of those metals."  
  — UNEXPECTED PRESENCE OF SOLUTE-FREE ZONES AT METAL-WATER INTERFACES (2012), ~p.6 `W2154517613`



## Level 2 — Emitted optical state & spectrum

### H2 — UPE from at least one biological system carries a non-classical or partially coherent optical signature (umbrella claim; see operational sub-claims H2.g2, H2.sq)

*(relates to H10)*

**Null:** All measured photostatistics are reproduced by classical light models given the detector's characterized dead time, afterpulsing and efficiency  
**Estimand:** Per sub-claim; umbrella retained only as evidence pool  
**Origin:** Popp 1970s–80s; Bajpai

**Evidence (verified):** 14 supporting / 7 refuting works (primary-only 13/7); full-entailment works 0S/3R; sentence witnesses 15S/9R/50D

EDITORIAL: no broadly accepted dataset exists; Bajpai's own 2013 time-series analysis found independent detection events without periodicity.

**Strongest verified support:**

- "By carefully analyzing this signal, it becomes evident that the decay characteristics of biophoton luminescence exhibits a non-exponential pattern, which provides compelling evidence for the inherent coherence present in the emission.98,99 In the quantum realm, coherence signiﬁes that subatomic part"  
  — Biophoton signaling in mediation of cell-to-cell communication and rad (2024), ~p.2 `W4399870880`
- "Reprinted from Ref. [15]. classical information theory, they presumed to rule out practically all mechanisms of UV UPE-induced mitosis based on transmissions of con- tinuous electromagnetic waves without spectral selectivity, further re- inforcing Gurwitsch’s conclusion that UV UPE-induced mitosis r"  
  — Open quantum systems theory of ultraweak ultraviolet photon emissions: (2024), ~p.3 `W4404871602`
- "Some results evidence that squeezed photon states are produced also in biophoton emission (Popp 1998; Popp et al. 2002)."  
  — Ultra-Weak Photon Emission from Biological Systems (2023), ~p.437 `W4389669809`

**Strongest verified refutation:**

- "There is no evidence of either coherent ﬁelds in biological systems or any coherent properties of UPE from them."  
  — Revisiting the mitogenetic effect of ultra-weak photon emission (2015), ~p.11 `W1920668343`
- "The conclusion of our review is twofold; while the phenomenon of UPE from biological systems can be considered experimen- tally well established, no reliable evidence for the coherence or nonclassicality of UPE was actually achieved up to now."  
  — Biophotons, coherence and photocount statistics: A critical review (2015), ~p.1 `W2141663490`
- "Given the current state of the experimental evidence, the hypothesis that biological photon emission comes from a coherent field seems unlikely to be true."  
  — Endogenous Chemiluminescence from Germinating Arabidopsis Thaliana See (2018), ~p.2 `W2898432932`


### H2.g2 — Second-order coherence g2(0) of UPE from a defined preparation deviates from 1 beyond detector artifacts

*(child of **H2**)*

*Evidence pool inherited from H2; stance judgments were made against that claim's text, not this entry's narrower scope.*

**Null:** Detector-corrected g2(0) = 1 within uncertainty  
**Estimand:** g2(0) with characterized dead-time/afterpulse correction and stated integration time at 10–100 cps  
**Origin:** modern quantum-optics framing

**Evidence (verified):** 14 supporting / 7 refuting works (primary-only 13/7); full-entailment works 0S/3R; sentence witnesses 15S/9R/50D

EDITORIAL: never measured with SPAD/SNSPD-grade correction; the decisive, currently missing measurement.

**Strongest verified support:**

- "By carefully analyzing this signal, it becomes evident that the decay characteristics of biophoton luminescence exhibits a non-exponential pattern, which provides compelling evidence for the inherent coherence present in the emission.98,99 In the quantum realm, coherence signiﬁes that subatomic part"  
  — Biophoton signaling in mediation of cell-to-cell communication and rad (2024), ~p.2 `W4399870880`
- "Reprinted from Ref. [15]. classical information theory, they presumed to rule out practically all mechanisms of UV UPE-induced mitosis based on transmissions of con- tinuous electromagnetic waves without spectral selectivity, further re- inforcing Gurwitsch’s conclusion that UV UPE-induced mitosis r"  
  — Open quantum systems theory of ultraweak ultraviolet photon emissions: (2024), ~p.3 `W4404871602`
- "Some results evidence that squeezed photon states are produced also in biophoton emission (Popp 1998; Popp et al. 2002)."  
  — Ultra-Weak Photon Emission from Biological Systems (2023), ~p.437 `W4389669809`

**Strongest verified refutation:**

- "There is no evidence of either coherent ﬁelds in biological systems or any coherent properties of UPE from them."  
  — Revisiting the mitogenetic effect of ultra-weak photon emission (2015), ~p.11 `W1920668343`
- "The conclusion of our review is twofold; while the phenomenon of UPE from biological systems can be considered experimen- tally well established, no reliable evidence for the coherence or nonclassicality of UPE was actually achieved up to now."  
  — Biophotons, coherence and photocount statistics: A critical review (2015), ~p.1 `W2141663490`
- "Given the current state of the experimental evidence, the hypothesis that biological photon emission comes from a coherent field seems unlikely to be true."  
  — Endogenous Chemiluminescence from Germinating Arabidopsis Thaliana See (2018), ~p.2 `W2898432932`


### H2.sq — UPE photocount distributions from defined preparations are better fit by squeezed-state models than by classical mixtures, with model-comparison statistics

*(child of **H2**)*

*Evidence pool inherited from H2; stance judgments were made against that claim's text, not this entry's narrower scope.*

**Null:** Classical (super-Poissonian mixture) models fit at least as well under proper model selection  
**Estimand:** Pre-registered model comparison (AIC/Bayes) on raw photocount time series with detector model included  
**Origin:** Bajpai squeezed-state programme

**Evidence (verified):** 14 supporting / 7 refuting works (primary-only 13/7); full-entailment works 0S/3R; sentence witnesses 15S/9R/50D

EDITORIAL: original fits never independently reproduced; raw IIB-era datasets survive only with individuals.

**Strongest verified support:**

- "By carefully analyzing this signal, it becomes evident that the decay characteristics of biophoton luminescence exhibits a non-exponential pattern, which provides compelling evidence for the inherent coherence present in the emission.98,99 In the quantum realm, coherence signiﬁes that subatomic part"  
  — Biophoton signaling in mediation of cell-to-cell communication and rad (2024), ~p.2 `W4399870880`
- "Reprinted from Ref. [15]. classical information theory, they presumed to rule out practically all mechanisms of UV UPE-induced mitosis based on transmissions of con- tinuous electromagnetic waves without spectral selectivity, further re- inforcing Gurwitsch’s conclusion that UV UPE-induced mitosis r"  
  — Open quantum systems theory of ultraweak ultraviolet photon emissions: (2024), ~p.3 `W4404871602`
- "Some results evidence that squeezed photon states are produced also in biophoton emission (Popp 1998; Popp et al. 2002)."  
  — Ultra-Weak Photon Emission from Biological Systems (2023), ~p.437 `W4389669809`

**Strongest verified refutation:**

- "There is no evidence of either coherent ﬁelds in biological systems or any coherent properties of UPE from them."  
  — Revisiting the mitogenetic effect of ultra-weak photon emission (2015), ~p.11 `W1920668343`
- "The conclusion of our review is twofold; while the phenomenon of UPE from biological systems can be considered experimen- tally well established, no reliable evidence for the coherence or nonclassicality of UPE was actually achieved up to now."  
  — Biophotons, coherence and photocount statistics: A critical review (2015), ~p.1 `W2141663490`
- "Given the current state of the experimental evidence, the hypothesis that biological photon emission comes from a coherent field seems unlikely to be true."  
  — Endogenous Chemiluminescence from Germinating Arabidopsis Thaliana See (2018), ~p.2 `W2898432932`


### H11 — UPE spectral distribution carries state-specific information beyond total intensity (measurement-feature claim feeding H3/H8/H9)

*(relates to H3,H8,H9)*

**Null:** Band ratios add no discriminative power over intensity once filter and detector artifacts are controlled  
**Estimand:** State discrimination from band ratios vs intensity-only, same instrument; requires <50 nm resolution capability that currently does not exist  
**Origin:** Popp; Kobayashi imaging line

**Evidence (verified):** 18 supporting / 1 refuting works (primary-only 17/1); full-entailment works 1S/1R; sentence witnesses 22S/1R/4D

EDITORIAL: physically under-tested — no published spectrum beats ~50 nm resolution; angular/polarization dimensions never measured at all.

**Strongest verified support:**

- "This has been demonstrated most notably with the emission spectra of model systems such as luminol,364 81 but also with bioluminescent organisms such as bacteria365 and ﬁreﬂies.251,252,261,366 In most cases, the bioluminescence spectrum obtained from chemiexcited molecule is identical to the ﬂuoresc"  
  — Chemi- and Bioluminescence of Cyclic Peroxides (2018), ~p.83 `W2790280419`
- "The results showed that the spectral distribution of UPE from the lesion side of the body surface of tumor mice was signiﬁcantly different from that of healthy controls, regardless of whether visible morphological changes at the lesion site and which stages of the breast cancer development were invo"  
  — Biophoton signaling in mediation of cell-to-cell communication and rad (2024), ~p.3 `W4399870880`
- "Mitogenetic spectral analysis of tumors demonstrated that alive surface cells of tumor with active metabolism had glycolytic and nucleolytic (related to the splitting of nucleic acid by phosphatase) spectra, while internal necrotizing tissues were the sources of radiation typical for proteolysis [13"  
  — Historical review of early researches on mitogenetic radiation: from d (2018), ~p.14 `W2979283984`

**Strongest verified refutation:**

- "The experimental stu- dies so far performed have revealed some characterizing features of this biological emission [19]: • the spectral distribution ranges from 14 15 10 /10 Hz , namely covering the optical and the ultraviolet (UV) re- gion of electromagnetic spectrum; • the form of the spectrum is "  
  — Zero-Point Field, QED Coherence, Living Systems and Biophotons Emissio (2015), ~p.9 `W2004094183`



## Level 3 — Propagation & transport

### H7 — Cytoskeletal or myelinated structures guide biological photons with transport efficiency materially above unguided tissue propagation (mechanism claim serving H5/H6, not their rival)

*(relates to H5,H6)*

**Null:** Measured/modelled guided transport gains are negligible against scattering losses at physiological geometries  
**Estimand:** Direct transport measurement with external light injection in the candidate structure  
**Origin:** Jibu/Hameroff; Kurian; Zarkeshian

**Evidence (verified):** 18 supporting / 0 refuting works (primary-only 18/0); full-entailment works 0S/0R; sentence witnesses 34S/0R/9D

EDITORIAL: theory-rich, experiment-poor; no direct measurement on either side yet.

**Strongest verified support:**

- "Proposals to test the hypothesis Although there is already some experimental evidence of biophoton propagation in the brain and axons (12, 43, 44), it would nevertheless be very interesting to test the light guidance of axons directly in-vitro and in-vivo."  
  — Are there optical communication channels in the brain (2018), ~p.8 `W2751268700`
- "It is found that such a complex waveguide of natural origin is capable of supporting the propagation of weakly attenuated modes in the indicated ranges."  
  — Propagation of Electromagnetic Waves along a Compact Nerve Fiber in th (2023), ~p.1 `W4364320658`
- "Demonstration of light guidance by individual Mu¨ ller cells measured in a modiﬁed dual-beam laser trap."  
  — Müller cells are living optical fibers in the vertebrate retina (2007), ~p.4 `W2032105712`



## Level 4 — Receiver effects & photon-mediated causality

### H4b — (Null family) Under optical-only coupling, emitted UPE produces no receiver-side biological response above chance in any validated preparation

*(relates to H1,H5,H6)*

*Evidence pool: the verified refutation record of H1,H5 (stance-inverted null family); all judgments were made against those claims' texts.*

**Null:** A pre-registered optical-coupling experiment shows a replicable receiver effect with photon-budget plausibility  
**Estimand:** Receiver-response effect size under optical-only coupling vs sham, blinded, with measured transmitted flux  
**Origin:** the sceptical position (Hollaender & Claus lineage)

**Evidence (verified):** 9 supporting / 42 refuting works (primary-only 7/40); full-entailment works 2S/3R; sentence witnesses 10S/80R/31D

EDITORIAL: evidence for H4b is by definition the refutation record of H1/H5 (mapped, not rescanned); demonstrating ROS chemistry (H4a) is NOT evidence for H4b.

**Strongest verified support:**

- "Yet these authors failed to observe the main (biological) mitogenetic effect [167, 170]."  
  — Historical review of early researches on mitogenetic radiation: from d (2018), ~p.18 `W2979283984`
- "Much later, this skeptical attitude resulted in signiﬁcant oblivion of the fundamental works and perception of the whole area as pseudoscience. 2 Mitogenetic Rays 17 Here are the main drawbacks of biological detection of MGR: 2.2.3.3.1 Subjectiveness As the very effect was “detected” by people, visu"  
  — Ultra-Weak Photon Emission from Biological Systems (2023), ~p.18 `W4389669809`
- ""Mitogenetic radiation" was therefore considered some kind of artifact."  
  — Properties of biophotons and their theoretical implications. (2003), ~p.2 `W146728166`

**Strongest verified refutation:**

- "Partial evidence for the existence of mitogenetic radiation."  
  — Revisiting the mitogenetic effect of ultra-weak photon emission (2015), ~p.20 `W1920668343`
- "In the 1930s, evidence for the existence of mitogenetic radiation took another leap forward when a group of scientists detected this radiation using modiﬁed GeigereMüller detectors (Audubert,1938; Rajewsky, 1931; Siebert and Seffert, 1933)."  
  — Electromagnetic cellular interactions (2010), ~p.2 `W2043432757`
- "Detectors were more sensitive to polarized radiation, i.e. mitogenetic effect was observed at the longer inductor- detector distances [138]."  
  — Historical review of early researches on mitogenetic radiation: from d (2018), ~p.15 `W2979283984`


### H1 — UV-band emission from dividing cells increases mitosis rate in optically coupled detector cell populations (mitogenetic radiation), in at least one reproducible preparation

*(child of **H5**; relates to H4b)*

**Null:** Division rates of optically coupled detector cultures equal sham-coupled controls under blinded, chemically separated, UV-transparent conditions  
**Estimand:** Difference in division/budding rate, detector vs sham, with window transmission spectrum reported  
**Origin:** Gurwitsch 1923

**Evidence (verified):** 32 supporting / 8 refuting works (primary-only 30/6); full-entailment works 0S/2R; sentence witnesses 62S/9R/23D

EDITORIAL: the founding instance of H5; a century old, no accepted replication; Babcock 2024 calls for redoing positive AND negative controls.

**Strongest verified support:**

- "Partial evidence for the existence of mitogenetic radiation."  
  — Revisiting the mitogenetic effect of ultra-weak photon emission (2015), ~p.20 `W1920668343`
- "In the 1930s, evidence for the existence of mitogenetic radiation took another leap forward when a group of scientists detected this radiation using modiﬁed GeigereMüller detectors (Audubert,1938; Rajewsky, 1931; Siebert and Seffert, 1933)."  
  — Electromagnetic cellular interactions (2010), ~p.2 `W2043432757`
- "Detectors were more sensitive to polarized radiation, i.e. mitogenetic effect was observed at the longer inductor- detector distances [138]."  
  — Historical review of early researches on mitogenetic radiation: from d (2018), ~p.15 `W2979283984`

**Strongest verified refutation:**

- "Yet these authors failed to observe the main (biological) mitogenetic effect [167, 170]."  
  — Historical review of early researches on mitogenetic radiation: from d (2018), ~p.18 `W2979283984`
- "Much later, this skeptical attitude resulted in signiﬁcant oblivion of the fundamental works and perception of the whole area as pseudoscience. 2 Mitogenetic Rays 17 Here are the main drawbacks of biological detection of MGR: 2.2.3.3.1 Subjectiveness As the very effect was “detected” by people, visu"  
  — Ultra-Weak Photon Emission from Biological Systems (2023), ~p.18 `W4389669809`
- ""Mitogenetic radiation" was therefore considered some kind of artifact."  
  — Properties of biophotons and their theoretical implications. (2003), ~p.2 `W146728166`


### H5 — At least one non-chemical, non-electrical cell-to-cell influence is mediated by emitted photons, demonstrable under optical-only coupling in a defined preparation

*(relates to H4b,H7)*

**Null:** All reported distant interactions disappear under optical decoupling, blinding, or verified-flux accounting  
**Estimand:** Pre-registered replication of the strongest candidate (Musumeci 1999 yeast protocol) with transmitted-flux measurement; window material must be specified  
**Origin:** Gurwitsch; Kaznacheev; Fels; Trushin

**Evidence (verified):** 12 supporting / 1 refuting works (primary-only 12/1); full-entailment works 3S/0R; sentence witnesses 18S/1R/8D

EDITORIAL: positive reports and failures both documented; Wainwright 2/7; Prasad 2014 negative under tightened controls; the field's cleanest pre-registration candidate.

**Strongest verified support:**

- "Also Beloussov et al. demonstrated optical interactions of ﬁsh eggs and embryos via UPE (Beloussov et al., 2002b, 2003, and chapter in Beloussov et al., 2000)."  
  — Electromagnetic cellular interactions (2010), ~p.11 `W2043432757`
- "Examples: - Gurwitsch's mitogenetic radiation (1920s): long-distance light signaling between the apical regions of onion bulbs, which may have induced cell division. - Kobayashi et al. [46]: non-chemical interactions between different plant cell cultures were demonstrated, which were reduced by opti"  
  — Ultra-Weak Photon Emission: From Oxidative Metabolism to DNA -Based Co (2025), ~p.6 `W4415948863`
- "The higher values of R (around 2.57 ± 0.68) were observed in cases (## 1-8) in which one of the partners at the start of the optical interactions was at the earliest de- velopmental stage (before start of the cleavage di vi- sions) while the other partner was at the intermediate (blastula - gastrula"  
  — Biophotonic patterns of optical interactions between fish eggs and emb (2003), ~p.4 `W2418169692`

**Strongest verified refutation:**

- "Based on the current literature, there is no convincing empirical evidence that DNA functions as a biophotonic communication system."  
  — Ultra-Weak Photon Emission: From Oxidative Metabolism to DNA -Based Co (2025), ~p.11 `W4415948863`



## Level 5 — Correlational state measurement

### H6 — Intracranial UPE intensity co-varies with neural activity beyond global metabolic rate in at least one preparation (slice or in vivo, invasive measurement)

*(relates to H7,H12,H4a)*

**Null:** UPE tracks oxidative metabolism only; no residual activity-correlation after controlling metabolic rate  
**Estimand:** Partial correlation of UPE with electrophysiological activity controlling oxygen consumption, same preparation  
**Origin:** Dai; Salari/Simon groups

**Evidence (verified):** 74 supporting / 8 refuting works (primary-only 74/8); full-entailment works 7S/0R; sentence witnesses 158S/10R/116D

EDITORIAL: extracranial claims are a separate, artifact-threatened matter (Salari 2026); the defensible core is invasive and metabolic.

**Strongest verified support:**

- "PAPER www.rsc.org/pps | Photochemical & Photobiological Sciences Biophotons as neural communication signals demonstrated by in situ biophoton autography Yan Sun, Chao Wang and Jiapei Dai* Received 7th October 2009, Accepted 8th December 2009 First published as an Advance Article on the web 21st Janu"  
  — Biophotons as neural communication signals demonstrated by in situ bio (2010), ~p.1 `W2056591841`
- "Kobayashi et al. [66] also studied photon emission from brain slices and observed suppressive effects of KCl and glu- cose deprivation, while stimulating effects of glutamate and rote- none (inhibitor of the mitochondrial electron transport chain) were observed on the intensity of ultra-weak photon "  
  — Ultra-weak photon emission from biological samples: Definition, mechan (2014), ~p.6 `W1995699286`
- "Dotta et al. [65] first showed that during brief intervals, when volunteers (n = 8) sat in a dark room and imagined white light, there was a repeatable, reliable and very statistically significant increase in the UPE from the right brain hemisphere while there was no change in the left hemisphere (T"  
  — Human ultra-weak photon emission as non-invasive spectroscopic tool fo (2021), ~p.9 `W3126963047`

**Strongest verified refutation:**

- "These results showed that neither entropy nor CV changed across tasks within PMTs and that they only weakly distinguished between back- ground vs. brain UPE signals for some tasks."  
  — Exploring ultraweak photon emissions as optical markers of brain activ (2025), ~p.4 `W4407397928`
- "Acute intensity changes corresponding to neuronal activation even by addition of 1 mM glutamate were observed to be absent except for a gradual increase of photon emission."  
  — In vivo imaging of spontaneous ultraweak photon emission from a rat’s  (1999), ~p.7 `W2160984073`
- "In contrasts, it is plausible that externally measured ultraweak biophoton emission from cells and neurons is princi- pally produced from natural oxidation processes on the surfaces of cellular membranes as demonstrated by Blake et al."  
  — Near death experiences: a multidisciplinary hypothesis (2013), ~p.5 `W2065332094`


### H12 — Mental states or directed intention modulate human surface UPE beyond the physiological covariates they engage (overlaps H6 conceptually; kept for the anomalous-claims record)

*(relates to H6,H8)*

**Null:** UPE changes during mental tasks are fully mediated by blood flow, temperature and movement  
**Estimand:** Mediation analysis with covariate recording; pre-registered; artifact-first design  
**Origin:** ISLIS line; Dotta/Persinger; Rubik

**Evidence (verified):** 11 supporting / 0 refuting works (primary-only 10/0); full-entailment works 3S/0R; sentence witnesses 16S/0R/3D

EDITORIAL: the field's worked example of artifact-first analysis; confounds are the entire question.

**Strongest verified support:**

- "The results supported the hypothesis that the human UPE can be influenced by meditation, because a significant decrease in UPE was observed during meditation (Table 1)."  
  — Human ultra-weak photon emission as non-invasive spectroscopic tool fo (2021), ~p.8 `W3126963047`
- "Studies carried out by Wijk et al. about the effects of transcendental meditation on UPE intensity demonstrated it."  
  — Human Ultraweak Photon Emission: Key Analytical Aspects, Results and F (2018), ~p.10 `W2906242287`
- "TM practitioners demonstrated lower emissions than OMT practitioners in 11 of 12 anatomical locations, indicating systematic group differences; p = 0.0032. * Current data using noninvasive photon emission recordings suggest that, in addition to intensity and wavelength, the UPE of subjects may event"  
  — Ultraweak Photon Emission as a Non-Invasive Health Assessment: A Syste (2014), ~p.9 `W2109151393`



## Level 6 — Out-of-sample prediction & diagnostics

### H3 — Delayed-luminescence decay parameters predict an external quality/physiology criterion out-of-sample in at least one matrix (defined instrument + excitation protocol)

*(relates to H9,H8)*

**Null:** Blinded out-of-sample prediction does not beat baseline assays (germination test, viability stain) on the same samples  
**Estimand:** AUC / prediction-error vs baseline, blinded, pre-registered; excitation protocol fully specified  
**Origin:** Catania school; Chinese herbal-QC line

**Evidence (verified):** 18 supporting / 0 refuting works (primary-only 16/0); full-entailment works 0S/0R; sentence witnesses 21S/0R/3D

EDITORIAL: never validated blind; cross-instrument comparability unestablished; chlorophyll-afterglow conflation must be excluded in plant matrices.

**Strongest verified support:**

- "It has been shown that the measurement of delayed luminescence emitted from the biological samples provide valid and predictive information about the functional status of biological systems22."  
  — An Experimental Investigation of Ultraweak Photon Emission from Adult  (2020), ~p.2 `W2999575750`
- "In the last decade, several papers have demonstrated that the ultraweak delayed luminescence (DL) is closely connected to the diﬀerentiation stage of the biological system [12–15]."  
  — Spectral analysis of laser-induced ultraweak delayed luminescence in c (2005), ~p.1 `W2054078053`
- "In this respect it was recently demonstrated that the ultraweak delayed luminescence is closely connected to the differentiation stage of the biological systems19."  
  — Laser-ultraviolet-A induced ultra weak photon emission in human skin c (2008), ~p.5 `W2308866`


### H8 — Surface UPE adds incremental predictive power for a defined systemic state (oxidative-stress criterion) beyond skin temperature, perfusion and environment, in humans

*(relates to H3,H11)*

**Null:** Incremental predictive power ≈ 0 once the named covariates are controlled (pre-specified margin)  
**Estimand:** ΔAUC / partial R² over covariate-only model, blinded, test-retest reliability reported  
**Origin:** Inaba/Kobayashi; Van Wijk; Tsuchida

**Evidence (verified):** 13 supporting / 1 refuting works (primary-only 11/1); full-entailment works 0S/0R; sentence witnesses 14S/1R/2D

EDITORIAL: gate is standardization; no test-retest reliability figures published; covariate-controlled analyses are the missing genre.

**Strongest verified support:**

- "UPE imaging of the facial skin of volunteers revealed regional variations in oxidative stress."  
  — Oxidative stress in human facial skin observed by ultraweak photon emi (2020), ~p.1 `W3035757108`
- "Another study demonstrated a difference in the spectral patterns of UPE from the body surface between human breast cancer-bearing nude mice and healthy control ­mice26."  
  — Ultraviolet A irradiation induces ultraweak photon emission with chara (2020), ~p.2 `W3111078497`
- "The results showed that the spectral distribution of UPE from the lesion side of the body surface of tumor mice was signiﬁcantly different from that of healthy controls, regardless of whether visible morphological changes at the lesion site and which stages of the breast cancer development were invo"  
  — Biophoton signaling in mediation of cell-to-cell communication and rad (2024), ~p.3 `W4399870880`

**Strongest verified refutation:**

- "There was no significant diﬀerences for other three body sites between the healthy and diabetes group. 3.5 Identification of the healthy group and type 2 diabetes group by PCA analysis of UPE data Principal component analysis (PCA) is a statistical procedure that uses an orthogonal transformation to"  
  — Ultra-weak photon emission in healthy subjects and patients with type  (2017), ~p.5 `W2594646273`


### H9 — Seed/plant autoluminescence predicts vigour, stress state or product quality out-of-sample beyond standard assays in at least one crop/matrix

*(relates to H3)*

**Null:** No incremental predictive power over standard germination/quality assays under blinded evaluation  
**Estimand:** Blinded field/greenhouse validation with pre-registered endpoints (the Frontiers 2025–26 line's own ask)  
**Origin:** Popp school; Gallep; herbal-QC line

**Evidence (verified):** 31 supporting / 2 refuting works (primary-only 30/2); full-entailment works 1S/0R; sentence witnesses 43S/2R/20D

EDITORIAL: nearest-term application; validation explicitly requested by its own literature.

**Strongest verified support:**

- "(Zhao et al., 2017b) on spontaneous UPE of herbal medicines also showed that UPE parameters could reﬂect the content of speciﬁc active compounds in the same herb in different growth periods."  
  — The application and trend of ultra-weak photon emission in biology and (2023), ~p.7 `W4321242749`
- "Ultra-weak photon emission and 1O2 generation in germinating soybean in response to wounding were observed using a high-sensitivity imaging system based on an intensiﬁed charge-coupled device and a highly sensitive single photon counter by Chen and co-workers [14]."  
  — Spectral Distribution of Ultra-Weak Photon Emission as a Response to W (2020), ~p.8 `W3037707140`
- "To fill in this gap, we demonstrate here on A. thaliana that the intensity of endogenous chemiluminescence increases during the germination stage."  
  — Endogenous Chemiluminescence from Germinating Arabidopsis Thaliana See (2018), ~p.1 `W2898432932`

**Strongest verified refutation:**

- "On the 10th day (10d) of germination, even though the photon emission count of AA C exceeded that of C original by 11.2%, still there was no significant difference between them."  
  — Effect of low frequency magnetic field (LFMF) on germination and vigou (2024), ~p.6 `W4404967714`
- "Interestingly, despite examining fruits of various external colours, no significant corre- lation was found between the colour of the fruit and the time required for UPE stabilisation."  
  — Influence of External Light on Ultra-Weak Photon Emission of Fruits: F (2025), ~p.8 `W4408461558`

