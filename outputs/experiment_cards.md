# Experiment cards

Certified hypotheses from the hypothesis engine, rendered as experiments a laboratory could cost. Certified means the reasoning survived a step-by-step audit against the corpus it cites — not that the hypothesis is true. Every card names the measurement that would settle it and the measurement area whose procedure makes that measurement defensible.

17 cards in this run.


---

## C017 — Q2 [L2]

**Claim.** For day-3 germinating Vigna radiata, source-intrinsic second- and third-order factorial cumulants of 400–750 nm UPE obey the calibrated Bernoulli-thinning laws κ2(η)=η²κ2(1) and κ3(η)=η³κ3(1) across optical transmissions η=0.10, 0.25, 0.50 and 1.00.

**Negative result looks like.** The biological-sample cumulants reject the thinning laws at the preregistered 0.01 level or show the same transmission-dependent residuals as detector controls, indicating that the apparent statistics cannot be assigned to the emitted field.

**The deciding number.** The joint chi-square lack-of-fit statistic for κr(η)=η^rκr(1), r=2,3, after propagation of quantum-efficiency, dark-count, crosstalk and dead-time uncertainties

**Scope.** population: Independent batches of day-3 germinating Vigna radiata seeds; condition: Dark-adapted spontaneous emission recorded in stationary 30-minute blocks; comparator: Empty chamber and intensity-matched Poisson LED measured through the same four transmissions; outcome: Detector-corrected second- and third-order factorial cumulants of counts in preregistered 50 ms, 200 ms and 1 s bins

**Measurement.** Place calibrated neutral-density filters before all detection optics, randomize filter order within each stationary recording block, and acquire photon-number histograms simultaneously with environmental and empty-chamber controls. Estimate factorial cumulants with a preregistered detector-response matrix calibrated using a pulsed Poisson source; test the two thinning equations jointly at every bin width and in held-out seed batches.

**Instrument.** Calibrated visible-sensitive multi-pixel SNSPD or other photon-number-resolving array covering 400–750 nm, with independently measured wavelength-dependent efficiency, pixel crosstalk, timing jitter and dead-time

**Measurement area.** Calibration, spectral responsivity, traceability and uncertainty; Photocount statistics, estimator choice and non-stationarity

**Grounded in.** 3 corpus works: `W2141663490`, `W2412356141`, `W3126489816`

**Provenance.** Proposed by codex-solo; nearest existing registry claim H2.g2 at similarity 0.081.

**Audit.** Step 0's claim that the mung-bean photocount distribution's 'form changes with bin size' cannot be checked (W2412356141 has no abstract) and is not needed, and no power argument is offered for estimating a third-order factorial cumulant at eta=0.10 where the signal scales as 1e-3; the load-bearing binomial-thinning identity kappa_r(eta)=eta^r*kappa_r(1) is exactly correct and W3126489816's sub-30 photons/s/cm2 detectivity is verbatim.; The thinning computation and experiment are sound, but the t


---

## C027 — Q3 [L4]

**Claim.** In clonally split Paramecium caudatum populations exposed for 48 hours in darkness, the growth effect of a live emitter population across a sealed quartz optical path will be reproduced within a preregistered 20% equivalence margin by photon-for-photon replay of its absolutely calibrated 300–750 nm emission, while an opaque shutter will abolish the effect.

**Negative result looks like.** The live-emitter contrast is absent, survives the opaque shutter, or is not equivalent within ±20% to the photon-matched replay contrast.

**The deciding number.** The ratio of the replay-versus-sham growth contrast to the live-emitter-versus-shutter growth contrast, with equivalence bounds 0.80–1.20, together with the shutter residual contrast.

**Scope.** population: Clonal P. caudatum receiver populations started at 5 cells/mL.; condition: Forty-eight-hour exposure in darkness across double-sealed quartz compartments with independent gas spaces, tested by at least three blinded laboratories.; comparator: Live-emitter coupling, opaque-shutter coupling, emitter-free sham, and attenuated multi-LED replay matched to the live emitter's spectrum and receiver-plane photon flux.; outcome: Receiver population growth, expressed as log cell-number change from 0 to 48 hours.

**Measurement.** Pre-register and distribute identical clonal cultures and coded exposure cartridges to three laboratories. Randomize receivers among live-emitter, opaque-shutter, sham, and replay arms. Quantify sister emitter cultures continuously, propagate measured window transmission and geometry to receiver-plane photon dose, and replay the resulting spectrum and time course from a calibrated attenuated LED array. Automated image cytometry performs blinded 0- and 48-hour cell counts.

**Instrument.** Absolutely calibrated cooled photon-counting PMT or silicon-SPAD spectrometer covering 300–750 nm, high-albedo integrating cavity, calibrated quartz transmission standards, attenuated multiwavelength LED replay source, and automated bright-field cell counter.

**Measurement area.** Imaging detectors, SPAD arrays and photon transfer calibration; Photomultiplier photon counting and delayed luminescence; Calibration, spectral responsivity, traceability and uncertainty

**Grounded in.** 3 corpus works: `W2092319343`, `W2258592615`, `W3161989600`

**Provenance.** Proposed by codex-solo; nearest existing registry claim H1 at similarity 0.027.

**Audit.** Step 2's second clause - that the Ulbricht-cavity paper 'identifies missing absolute photon reporting as a major measurement gap' - appears nowhere in its abstract, though its detection of growth-onset yeast UPE does supply the feasibility the step actually needs.; The cited cavity study supports sensitive detection of growth-associated yeast emission but its abstract does not identify missing absolute photon reporting as a major measurement gap.


---

## C028 — Q3 [L4]

**Claim.** For optically coupled P. caudatum, the dose-normalized receiver-growth effects in four spectral bands will form the same action-spectrum ranking under live-emitter coupling and synthetic photon replay, with Spearman rho at least 0.8 and at least one familywise-error-controlled nonzero band effect.

**Negative result looks like.** No band has a corrected nonzero effect, or the live-emitter and replay action spectra have Spearman rho below 0.8.

**The deciding number.** The four-band vector of growth contrast per received photon and its Spearman correlation between natural and replay exposures.

**Scope.** population: Clonal P. caudatum emitter and receiver populations.; condition: Forty-eight-hour dark exposure through sealed quartz paths partitioned into 260–340, 340–450, 450–600, and 600–750 nm bands.; comparator: Equal receiver-plane photon counts delivered by filtered live emitters versus narrowband synthetic replay, with opaque and zero-photon controls.; outcome: Dose-normalized difference in receiver log growth for each spectral band.

**Measurement.** Measure the live-emitter spectrum and filter transmission in the complete exposure cartridge, then expose randomized receivers through one band at a time. In a second factorial arm, use narrowband LEDs attenuated to the same receiver-plane photon count. Estimate band-specific growth contrasts with a preregistered hierarchical model and compare the two action-spectrum vectors.

**Instrument.** Absolutely calibrated solar-blind UV PMT for 260–400 nm plus a cooled red-sensitive photon-counting PMT or EMCCD spectrometer for 340–750 nm, monochromator or interference-filter wheel, and attenuated UV/visible LED array.

**Measurement area.** Imaging detectors, SPAD arrays and photon transfer calibration; Photomultiplier photon counting and delayed luminescence; Detection outside the visible band

**Grounded in.** 4 corpus works: `W2092319343`, `W2043432757`, `W2095038636`, `W1523504261`

**Provenance.** Proposed by codex-solo; nearest existing registry claim H1 at similarity 0.078.

**Audit.** Step 1 assigns the 'mitogenetic emission is ultraviolet / limited modern evidence for 280-390 nm' judgement to Cifra's feasibility paper, whose abstract addresses only emission intensity and ambient signal-to-noise and never mentions Gurwitsch or any UV band.; The cited feasibility-analysis abstract discusses weak emission and poor signal-to-noise but does not state the claimed historical 190–250 nm range or limited evidence for 280–390 nm emission.


---

## C029 — Q3 [L4]

**Claim.** At identical total photon count and spectrum, replaying the measured one-second-scale temporal order of P. caudatum UPE will change receiver growth relative to replaying a within-10-minute-block permutation of the same photon sequence.

**Negative result looks like.** The original-order and temporally permuted replays produce the same receiver growth within a preregistered ±5% equivalence margin.

**The deciding number.** The original-minus-permuted difference in 48-hour log growth, with total and band-specific delivered photon counts constrained to equality.

**Scope.** population: Clonal P. caudatum receivers started at 5 cells/mL and emitter populations measured in the same growth phase.; condition: Forty-eight-hour dark exposure to multi-band LED replay generated from time-tagged natural-emission records.; comparator: Original-order replay versus block-permuted replay, with photon count in every spectral channel and every 10-minute block held exactly constant.; outcome: Difference in receiver log growth at 48 hours.

**Measurement.** Record emitter photons with two independent time-tagging detector channels to reject detector bursts, construct original and block-permuted multi-band replay files, and expose coded receiver cultures using the same LED hardware. Verify equality of delivered counts with an independent monitor detector and score growth blindly.

**Instrument.** Dual time-correlated single-photon-counting PMTs or SPADs covering 300–750 nm with one-second or finer time tags, spectrally multiplexed attenuated LED replay, and calibrated monitor photodetector.

**Measurement area.** Imaging detectors, SPAD arrays and photon transfer calibration; Photomultiplier photon counting and delayed luminescence; Calibration, spectral responsivity, traceability and uncertainty

**Grounded in.** 3 corpus works: `W7124764611`, `W1523504261`, `W2769035647`

**Provenance.** Proposed by codex-solo; nearest existing registry claim H2.g2 at similarity 0.054.

**Audit.** Every citation is exact - the DEA anomalous-diffusion and long-range-memory result, postulate I of the light-interaction framework, and the 300 Hz pulse-frequency dependence at 810 nm / 38 mJ cm-2 - and within-block permutation provably conserves photon count per wavelength channel and per 10-minute block, isolating sub-block ordering.; The abstracts support measurable UPE temporal structure, emitter modulation, and frequency-dependent cellular responses, while count-preserving permutation provi


---

## C030 — Q3 [L4]

**Claim.** The reported suppression of 5-cells/mL P. caudatum indicator growth by 50–300-cells/mL neighbors is an analog photon-dose response whose between-density variation is fully explained by absolutely measured 300–750 nm receiver fluence, with no residual emitter-density effect.

**Negative result looks like.** Growth suppression is not monotonic with measured photon fluence, or emitter density improves held-out prediction after photon dose is included.

**The deciding number.** The cross-validated dose-response function f(N_receiver) and the incremental held-out log-likelihood contributed by emitter-density labels after f(N_receiver), with less than two AIC-equivalent units treated as no residual contribution.

**Scope.** population: P. caudatum indicators started at 5 cells/mL, paired with emitters started at 50, 100, 200, or 300 cells/mL.; condition: Forty-eight-hour exposure in darkness through sealed optical paths and a crossed series of calibrated neutral-density attenuations.; comparator: Different emitter densities adjusted to overlapping receiver-plane photon doses, plus opaque, sham, and synthetic-replay controls.; outcome: Indicator log growth and its dose-response relationship to received photon fluence.

**Measurement.** Repeat the published 5-versus-50/100/200/300-cells/mL design using double-sealed cartridges. Cross density with neutral-density filters chosen to make different densities deliver overlapping photon fluences. Measure transmitted photons continuously in matched cartridges, reproduce selected doses synthetically, and compare dose-only and dose-plus-density models by preregistered leave-batch-out validation.

**Instrument.** Absolutely calibrated photon-counting PMT or SPAD system covering 300–750 nm, high-albedo integrating cavity, calibrated neutral-density filters, monitor detector, and automated cell-count imaging.

**Measurement area.** Imaging detectors, SPAD arrays and photon transfer calibration; Photomultiplier photon counting and delayed luminescence; Calibration, spectral responsivity, traceability and uncertainty

**Grounded in.** 3 corpus works: `W2765089583`, `W2095038636`, `W3161989600`

**Provenance.** Proposed by codex-solo; nearest existing registry claim H4b at similarity 0.029.

**Audit.** All three citations state precisely what the steps claim (Fels' 5-versus-50/100/200/300 cells/mL suppression and its abolition by graphite shielding, the weak-emission/SNR obstacle, the 50%-efficiency cavity detecting yeast at growth onset), and crossing emitter density with neutral-density attenuation to produce overlapping doses genuinely separates photon-dose sufficiency from density-linked confounding.; The reported density-dependent suppression and graphite control support the premise, and 


---

## C031 — Q3 [L4]

**Claim.** After equalizing total 300–750 nm photon count, replay of the joint spectral-temporal UPE template from a 300-cells/mL P. caudatum population will suppress growth of 5-cells/mL receivers by at least 10% more than replay of the template from a 50-cells/mL population.

**Negative result looks like.** The normalized high-density template suppresses growth by less than 10% relative to the normalized low-density template, or the difference disappears once photon count is equalized.

**The deciding number.** One minus the ratio of 48-hour receiver growth under the normalized 300-cells/mL template to growth under the normalized 50-cells/mL template.

**Scope.** population: Clonal P. caudatum receivers started at 5 cells/mL.; condition: Forty-eight-hour dark exposure to photon replays derived from emitters started at 50 or 300 cells/mL.; comparator: Low-density and high-density emitter templates normalized to identical integrated receiver-plane photon count, plus spectrally flattened and temporally shuffled versions.; outcome: Percent difference in receiver population growth at 48 hours.

**Measurement.** Acquire replicated, time-resolved spectra from 50- and 300-cells/mL emitters, normalize templates to the same receiver-plane photon total, and replay them to blinded 5-cells/mL receivers. Factorially flatten spectrum or shuffle time to determine which component carries any density-dependent effect.

**Instrument.** Time-tagged photon-counting spectrometer covering 300–750 nm, calibrated multiwavelength LED or monochromator replay system capable of single-photon-level attenuation, and automated cell counter.

**Measurement area.** Calibration, spectral responsivity, traceability and uncertainty

**Grounded in.** 4 corpus works: `W2765089583`, `W2092319343`, `W7124764611`, `W1523504261`

**Provenance.** Proposed by codex-solo; nearest existing registry claim H10 at similarity 0.038.

**Audit.** Each cited claim is verbatim in its abstract (density-graded indicator suppression; effects positive or negative depending on cuvette material and cell number; long-memory UPE dynamics; emitter modulation as postulate I), and normalising the 50- and 300-cells/mL templates to equal integrated counts makes any residual difference a clean test of spectral-temporal structure.; The cited density-dependent effects and evidence for structured biological emission ground the prediction, and photon-normal


---

## C032 — Q3 [L4]

**Claim.** A photon-matched P. caudatum growth signal will retain at least half of its dark-condition effect when superposed on spectrally matched Poisson background light delivering ten times the signal photon count, indicating receiver-side filtering rather than dependence on an unrealistically noise-free channel.

**Negative result looks like.** At tenfold background, the replay-attributable growth contrast is less than 50% of its dark-condition value or is statistically indistinguishable from zero.

**The deciding number.** The ratio of the replay-versus-background-only growth contrast at tenfold background to the replay-versus-sham contrast in darkness.

**Scope.** population: Clonal P. caudatum receivers started at 5 cells/mL.; condition: Forty-eight-hour replay exposure under backgrounds of 0, 1, 10, and 100 times the measured UPE photon count.; comparator: Identical UPE replay with no background, spectrally matched Poisson background, temporally structured background, and background-only controls.; outcome: Receiver growth contrast attributable to the fixed UPE replay at each background level.

**Measurement.** First establish a photon-matched replay effect in darkness. Repeat the coded exposure with independently generated Poisson and structured backgrounds at defined multiples of the signal dose, continuously verify both components with a monitor detector, and estimate the preregistered signal-by-background interaction across laboratories.

**Instrument.** Absolutely calibrated photon-counting PMT or SPAD covering 300–750 nm, two independently driven attenuated multiwavelength LED sources for signal and background, optical combiner, and monitor spectrometer.

**Measurement area.** Imaging detectors, SPAD arrays and photon transfer calibration; Photomultiplier photon counting and delayed luminescence; Calibration, spectral responsivity, traceability and uncertainty

**Grounded in.** 2 corpus works: `W2092319343`, `W2095038636`

**Provenance.** Proposed by codex-solo; nearest existing registry claim H4b at similarity 0.014.

**Audit.** Both citations are exact, but the SBR computation and the ratio estimand presuppose a dark-condition photon-matched replay effect that no cited work establishes, leaving the estimand's denominator an assumption the protocol must first manufacture in its own stage one.; The literature establishes darkness-dependent coupling claims and ambient signal-to-noise as the relevant obstacle, while controlled matched backgrounds directly measure the receiver's noise-tolerance curve.


---

## C042 — Q4 [L1]

**Claim.** In Alzheimer and vascular-dementia model brain preparations, GluN2B blockade will restore the UPE spectral centroid toward wild type more than a mitochondria-targeted antioxidant that is titrated to produce the same reduction in total ROS and total photon counts.

**Negative result looks like.** At matched ROS and total photon output, ifenprodil produces no greater spectral recovery than the antioxidant, making the disease-associated spectrum compatible with generic oxidative emission.

**The deciding number.** D = centroid recovery under ifenprodil minus centroid recovery under the ROS-matched antioxidant, with D greater than zero required in both disease models.

**Scope.** population: Acute brain slices and matched synaptosomes from Alzheimer-model, vascular-dementia-model, and wild-type mice.; condition: Glutamate challenge followed by vehicle, ifenprodil, or a titrated mitochondria-targeted antioxidant, with doses matched within each preparation for ROS reduction and broadband photon-count reduction.; comparator: Wild-type vehicle, disease-model vehicle, and disease-model antioxidant arms matched to the ifenprodil arm on ROS and total UPE intensity.; outcome: Recovery of corrected spectral centroid and the 650–900/400–650 nm photon ratio toward the wild-type distribution.

**Measurement.** Run the three-arm intervention in randomized wells from each animal, quantify mitochondrial ROS, lipid peroxidation, oxygen consumption, and UPE spectra simultaneously, and estimate donor-stratified difference-in-differences for both disease models.

**Instrument.** Calibrated 400–900 nm photon-counting spectrograph with cooled EMCCD/SPAD detection, plus plate-compatible ROS, lipid-peroxidation, and oxygen-consumption assays.

**Measurement area.** Imaging detectors, SPAD arrays and photon transfer calibration; Calibration, spectral responsivity, traceability and uncertainty; Oxidative stress chemistry and its spectral bands

**Grounded in.** 3 corpus works: `W4386377286`, `W1977345460`, `W4408688794`

**Provenance.** Proposed by codex-solo; nearest existing registry claim H11 at similarity 0.064.

**Audit.** All three citations assert exactly what the steps claim (reduced, blueshifted glutamate-induced UPE in AD and VaD models partially reversed by ifenprodil; OGD-plus-azide block versus partial TTX block; anesthetic UPE tracking oxidative and thiol markers), and matching the antioxidant arm on both ROS and broadband photon output makes receptor-specific spectral recovery separable from generic oxidative emission.; The cited studies support disease-associated spectral changes, partial ifenprodil rev


---

## C043 — Q4 [L5]

**Claim.** In dark-adapted healthy adults performing light-free auditory tasks, the forehead-specific coupling between UPE and EEG will show a positive 650–900 nm excess over 400–600 nm after subtracting cheek-skin emission, shuttered-detector events, ambient leakage, temperature, and perfusion effects.

**Negative result looks like.** The corrected 650–900 nm forehead coupling is not above zero, is no larger than corrected 400–600 nm coupling, or appears equally in cheek, shuttered, empty-chair, or sham-marker analyses.

**The deciding number.** Delta coupling = partial coupling(forehead EEG,UPE minus cheek and shutter controls) in 650–900 nm minus the corresponding corrected coupling in 400–600 nm.

**Scope.** population: One hundred healthy adults measured after at least sixty minutes of monitored dark adaptation.; condition: Eyes-closed auditory oddball and mental-arithmetic blocks delivered without displays or indicator lights, interleaved with matched rest blocks.; comparator: A cheek-facing skin channel, an optically shuttered matched detector, empty-chair runs, randomized sham task markers, and the 400–600 nm band.; outcome: Task-locked partial coupling of forehead photon counts with preregistered EEG-band power after subtraction of skin, common-mode, and physiological covariates.

**Measurement.** Use a preregistered two-stage design: estimate detector and physiological nuisance coefficients from rest, empty-chair, shutter, and skin-control runs, freeze them, then test the corrected NIR-versus-visible coupling in blinded auditory-task blocks and an untouched replication cohort.

**Instrument.** Synchronized multichannel low-dark-count single-photon detectors covering 400–900 nm with dichroic 400–600 and 650–900 nm channels, plus EEG, scalp thermography, perfusion monitoring, and calibrated ambient-light sensors.

**Measurement area.** Detection outside the visible band; Calibration, spectral responsivity, traceability and uncertainty; Human-subject measurement and clinical-claim requirements

**Grounded in.** 4 corpus works: `W4407397928`, `W4417010158`, `W7168813583`, `W2483916403`

**Provenance.** Proposed by codex-solo; nearest existing registry claim H8 at similarity 0.055.

**Audit.** The same unsupported 'calls for larger samples and distinct task designs' attribution recurs in step 0, and step 1 assigns a specific stimulus-light-traverses-skull rationale to a protocol paper for which the corpus holds no abstract, which is unverifiable rather than false.; Step 2 is unverifiable because the title-only protocol record does not assert the claimed visual-stimulus light-transmission confound, but the remaining evidence and controls support the experiment.


---

## C047 — Q5 [L5]

**Claim.** Under properly light-tight conditions with absolute-unit reporting, the excess surface photon flux measured from a human head is reproduced within a factor of two by a thermally and optically matched inanimate phantom, establishing that reported extracranial 'brain UPE' magnitudes are set by the measurement environment rather than by the brain.

**Negative result looks like.** Head excess flux exceeds phantom excess flux by more than a factor of two, in a band where scalp and skull transmit and the detector responds, and this persists across sessions and seal conditions - i.e. a genuine biological head signal survives the phantom control and the contamination explanation fails.

**The deciding number.** Ratio Phi_head / Phi_phantom in absolute photons s-1 cm-2 per spectral band, with 95% CI; plus the fraction of previously published head-UPE magnitudes reproduced by the phantom arm.

**Scope.** population: Healthy adult volunteers (n >= 15), occipital and temporal scalp; plus a head phantom matched for surface reflectance, emissivity and surface temperature 35-37 C, plus an empty light-tight chamber; condition: Photon counting in a fully dark-adapted, verified light-tight enclosure, 400-700 nm on a PMT arm and 600-1000 nm on a silicon SPAD/EMCCD arm, with dark count rate, QE and collection geometry declared and the result reported in photons s-1 cm-2; comparator: Matched phantom in the identical chamber and session; empty-chamber blank; and the same protocol run with a deliberately imperfect seal to quantify the contamination channel; outcome: Absolute surface photon flux density (photons s-1 cm-2, per band) for head, phantom and blank, with 95% CI

**Measurement.** In one light-tight, verified-sealed chamber, alternate within a single session between (i) a dark-adapted volunteer's scalp, (ii) a temperature-controlled head phantom at 36 C with matched surface reflectance, and (iii) an empty chamber, randomising order across >=15 volunteers. Run two detector arms simultaneously on the same surface patch: a cooled PMT (400-700 nm) and a silicon SPAD or EMCCD (600-1000 nm). Report every result as photons s-1 cm-2 with declared eta(lambda), D, dead time and collection solid angle. Add a deliberate calibrated leak condition to measure the contamination transfer function. Decision rule: contamination explanation is supported if Phi_head / Phi_phantom <= 2 in every band; refuted if the ratio exceeds 2 in a transmitting, detector-responsive band and replicates across sessions.

**Instrument.** Cooled PMT photon counter 400-700 nm with measured QE and dark rate <25 cps, plus a silicon SPAD module or back-illuminated EMCCD covering 600-1000 nm at QE >90%; verified light-tight enclosure with a calibrated leak port; temperature-controlled head phantom.

**Measurement area.** Imaging detectors, SPAD arrays and photon transfer calibration; Photomultiplier photon counting and delayed luminescence; Calibration, spectral responsivity, traceability and uncertainty

**Grounded in.** 8 corpus works: `W7168813583`, `W4417459026`, `W3217353367`, `W3174216096`, `W2138303176`, `W4409735377`, `W4404240787`, `W3126489816`

**Provenance.** Proposed by baseline-claude; nearest existing registry claim H8 at similarity 0.038.

**Audit.** The whole of step 1 - quantum efficiency 0.23 applied and 22 counts/s of dark rate subtracted - appears nowhere in the cited abstract, and step 5 offers explicitly visible-band EMCCD demonstrations as evidence for the 600-1000 nm reach that step 4 argues the design requires.; Step 2's exact quantum-efficiency and dark-count conversion is absent from the supplied abstract, but the abstract directly supports the central contamination hypothesis and the controlled phantom comparison remains discrim


---

## C052 — Q5 [L5]

**Claim.** After two hours of thermal equilibration, cooled PMT dark counts collected over 48 hours will be Poisson-compatible enough that every six-hour block has a Fano factor of 0.8–1.2 and its empirical one-sided 95% blank threshold is no more than 10% above the Poisson-derived threshold.

**Negative result looks like.** At least one detector has a six-hour block with Fano factor outside 0.8–1.2 or an empirical 95% threshold more than 10% above the Poisson threshold.

**The deciding number.** For each detector and block, F=Var(C)/Mean(C) and RLOD=Q0.95,empirical/Q0.95,Poisson.

**Scope.** population: At least three low-dark-count PMT models tested in three light-tight UPE chambers; condition: Fixed gain and detector temperature, two-hour equilibration, followed by continuous 48-hour shuttered acquisition in 60-second bins; comparator: Empirical block-specific blank distribution versus a stationary Poisson model with the same mean; outcome: Fano factor and the ratio of empirical to Poisson one-sided 95% thresholds, also expressed as photon s^-1 cm^-2 after calibration

**Measurement.** Distribute an identical acquisition protocol to three laboratories, log detector and chamber temperatures, acquire continuous shuttered counts, and analyze preregistered six-hour blocks without removing bursts except under explicit hardware-fault rules. Convert thresholds using each detector's wavelength-dependent efficiency and collection geometry.

**Instrument.** Thermoelectrically cooled photon-counting PMTs sensitive over approximately 300–800 nm, with electronic shutters, temperature logging, and traceable low-flux efficiency calibration.

**Measurement area.** Photomultiplier photon counting and delayed luminescence; Calibration, spectral responsivity, traceability and uncertainty; Photocount statistics, estimator choice and non-stationarity

**Grounded in.** 4 corpus works: `W3157775700`, `W2808116502`, `W4391831883`, `W3161989600`

**Provenance.** Proposed by codex-solo; nearest existing registry claim H4a at similarity 0.0.

**Audit.** Step 2 credits the brief UPE review with stating that dark counts are central to instrument choice and that SNR of at least one is commonly required, neither of which its abstract says, while the load-bearing citations (dark count yields ordinary scaling; basal and wound photocount states approximate Poisson) are verbatim exact.; Step 3 is non-load-bearing but unsupported because the supplied review abstract does not mention detector dark counts or an SNR threshold of one.


---

## C061 — Q6 [L6]

**Claim.** In adults spanning the full range of skin pigmentation, calibrated 350–650 nm UPE emitted 1–3 minutes after a standardized suberythemal UVA exposure will add at least 0.10 to out-of-sample R² for predicting 24-hour erythema beyond UVA dose, baseline erythema, skin lightness, skin temperature and perfusion.

**Negative result looks like.** The cross-validated incremental R² from adding 1–3-minute UPE is less than 0.10, or its bootstrap 95% confidence interval includes zero.

**The deciding number.** ΔR² = R²clinical+UPE − R²clinical in a locked external-validation cohort.

**Scope.** population: Adults with prospectively balanced skin-lightness strata; condition: Standardized suberythemal solar-simulated UVA exposure after controlled acclimation and dark adaptation; comparator: Prediction model containing UVA dose, baseline colorimetry, skin lightness L*, temperature and perfusion but no UPE; outcome: Change in colorimeter-measured erythema a* at 24 hours

**Measurement.** Pre-register a multicentre dose-response study with a locked acquisition window, sham-exposed neighboring skin, photon-reference calibration, blinded 24-hour colorimetry and a completely held-out validation centre; fit the clinical model first and add only the pre-specified background-subtracted 1–3-minute photon radiance.

**Instrument.** Calibrated photon-counting photomultiplier or cooled EMCCD covering 350–650 nm in a light-tight chamber, plus a skin colorimeter, thermometer and perfusion monitor.

**Measurement area.** Imaging detectors, SPAD arrays and photon transfer calibration; Photomultiplier photon counting and delayed luminescence; Detection outside the visible band

**Grounded in.** 3 corpus works: `W3092282708`, `W4306729560`, `W7165757820`

**Provenance.** Proposed by codex-solo; nearest existing registry claim H8 at similarity 0.092.

**Audit.** Step 0 (1-3 min post-UV UPE increasing dose-dependently and highly correlated with cutaneous redness at 24 h, with a Trolox-suppressible LPO link) and step 1 (L* positively correlated with UVA-induced UPE, detectable to 2 h) are verbatim exact, but step 2 attributes 'thermal and optical confounds and lacks standardized protocols' to the Reiki/Healing-Touch biomarker review, which asserts nothing of the kind.; The thermal-confound and protocol-standardization claim is absent from the supplied bio


---

## C063 — Q6 [L6]

**Claim.** In patients with erythropoietic protoporphyria, the calibrated initial 350–650 nm UPE burst following a standardized low-dose solar-simulated exposure will improve prediction of the 24-hour phototoxic skin reaction by at least 0.10 AUC beyond erythrocyte protoporphyrin IX, plasma iron, exposure dose and skin lightness.

**Negative result looks like.** The UPE-augmented model improves externally validated AUC by less than 0.10 or has a non-positive lower 95% confidence bound.

**The deciding number.** ΔAUC = AUCclinical+initial-burst-UPE − AUCclinical for the pre-specified 24-hour phototoxic-reaction endpoint.

**Scope.** population: Adolescents and adults with biochemically or genetically confirmed erythropoietic protoporphyria; condition: Dermatologist-supervised low-dose solar-simulated exposure of a fixed skin site, measured before and during routine treatment; comparator: Clinical model containing erythrocyte PPIX, plasma iron, exposure dose and L* but no UPE; outcome: Pre-specified 24-hour phototoxic reaction defined by blinded erythema colorimetry and a standardized pain threshold

**Measurement.** Pre-register a repeated-measures dermatology study using a safe dose ladder, fixed anatomical site, sham-exposed control site and blinded 24-hour assessment; lock the initial-burst integration window before enrollment and validate the model at a second EPP centre.

**Instrument.** Calibrated photon-counting PMT covering 350–650 nm with second-scale acquisition in a light-tight skin chamber, plus colorimetry and a calibrated solar simulator.

**Measurement area.** Photomultiplier photon counting and delayed luminescence; Calibration, spectral responsivity, traceability and uncertainty; Human-subject measurement and clinical-claim requirements

**Grounded in.** 3 corpus works: `W1977870833`, `W3092282708`, `W4306729560`

**Provenance.** Proposed by codex-solo; nearest existing registry claim H8 at similarity 0.021.

**Audit.** All three citations are verbatim supported - 14 EPP patients whose post-solar-simulated initial burst correlated with plasma iron and erythrocyte PPIX and inversely with plasma zinc, early post-UV UPE correlated with 24 h erythema through lipid peroxidation, and L*-dependence of UVA-induced UPE - and the pre-registered held-out Delta-AUC against a PPIX/iron/dose/L* model at a second EPP centre would genuinely discriminate the claim.; The abstracts support EPP initial-burst associations, early UP


---

## C065 — Q6 [L6]

**Claim.** In fresh colorectal cancer resections, a pre-specified spontaneous UPE radiance-map classifier will identify histopathology-positive tissue regions in held-out patients with AUC at least 0.85 and sensitivity at least 0.90 at specificity at least 0.80.

**Negative result looks like.** Patient-held-out AUC is below 0.85, or sensitivity is below 0.90 when specificity is fixed at 0.80.

**The deciding number.** Patient-clustered external-validation AUC and sensitivity at the pre-specified 0.80-specificity operating point.

**Scope.** population: Adults undergoing primary colorectal cancer resection; condition: Unfixed fresh resection slices imaged within 30 minutes in darkness without optical excitation; comparator: Adjacent pathology-negative tissue from the same specimen and a gross-inspection-only baseline classifier; outcome: Region-level malignant versus non-malignant status on co-registered blinded histopathology

**Measurement.** Prospectively collect consecutive resections, image dark-adapted fresh slices for a fixed duration, co-register the radiance map with whole-mount histology, and validate a locked spatial-temporal classifier in specimens from a second hospital.

**Instrument.** Cryogenically cooled photon-counting EMCCD covering approximately 350–800 nm with calibrated collection optics and a light-tight specimen chamber.

**Measurement area.** Imaging detectors, SPAD arrays and photon transfer calibration; Calibration, spectral responsivity, traceability and uncertainty; Sample environment, background and artefact control

**Grounded in.** 3 corpus works: `W2055110733`, `W3016463384`, `W3126489816`

**Provenance.** Proposed by codex-solo; nearest existing registry claim H4a at similarity 0.026.

**Audit.** All three citations are verbatim accurate and honestly qualified - 982 +/- 513 versus 625 +/- 419 counts/min/cm2 with the frozen-sample and n = 14 / n = 6 limitations stated in the step itself, 90% cell-line discrimination explicitly flagged as not established on fresh human specimens, and EMCCD SNR-3 detection below 30 photons/s/cm2 - and patient-clustered validation against co-registered whole-mount histology at a second hospital is decisive.; The cited studies support detectable tumor-associa


---

## C069 — Q7 [L5]

**Claim.** After normalising out total flux and the anatomical silhouette, whole-body and whole-organ UPE images acquired under the field's standard protocol contain reproducible spatial structure at 5 mm scale, with split-half intraclass correlation exceeding 0.3 and exceeding the shot-noise-matched simulated null.

**Negative result looks like.** Split-half ICC lies at or below the 95th percentile of the shot-noise-matched simulated null at every scale, i.e. published UPE images carry no reproducible spatial information beyond total intensity and body outline - the pictures are display artefacts of a counting measurement.

**The deciding number.** Split-half ICC of the residual spatial map at 5 mm scale, minus the 95th percentile of the matched simulated null, with CI.

**Scope.** population: Human hand and upper body (>= 20 imaging sessions across >= 20 subjects) and mice (>= 10 animals), imaged under the standard protocol: light-tight box, >= 60 min dark adaptation, 15-30 min accumulation, 2x2 to 4x4 binning, cosmic-ray filtering.; condition: Each acquisition stored as individual frames and split into two interleaved half-datasets, each flux-normalised and masked to the silhouette.; comparator: 1000 synthetic image pairs drawn from a Poisson process with the same total counts, the same silhouette, and the measured flat-field, dark-current and EM excess-noise statistics of the same camera.; outcome: Split-half intraclass correlation of the flux-normalised residual map at 5, 10 and 20 mm smoothing scales, and its excess over the simulated null distribution.

**Measurement.** Re-analyse archived raw frame stacks plus a prospective cohort. Interleave frames into two half-datasets, flux-normalise, mask to the silhouette, smooth at 5/10/20 mm, and compute the ICC between halves. Compare against 1000 Poisson surrogate image pairs matched on total counts, silhouette and measured detector noise. Repeat the whole procedure at 30 and 90 min dark adaptation and with the subject replaced by a matched inert phantom.

**Instrument.** Any deep-cooled CCD, EMCCD or qCMOS photon-counting camera over 400-900 nm that stores individual frames rather than a single accumulated exposure; no new hardware required.

**Measurement area.** Imaging detectors, SPAD arrays and photon transfer calibration; Photocount statistics, estimator choice and non-stationarity; Human-subject measurement and clinical-claim requirements

**Grounded in.** 13 corpus works: `W2165767379`, `W3174216096`, `W2132454423`, `W2039224325`, `W4409735377`, `W2009372666`, `W4406075774`, `W3126489816`

**Provenance.** Proposed by baseline-claude; nearest existing registry claim H4b at similarity 0.029.

**Audit.** The detectivity arithmetic is exact throughout ((3/1.275)^2 = 5.54 cm2 s giving 5.5 s, 554 s and 15.4 h, plus the 44.4 cm2 s cross-check) and the 85 photons/s/cm2 skin flux is stated verbatim in two cited abstracts, but step 4 cites a photosystem-II protein-hydroperoxide singlet-oxygen paper for the '30 min dark adaptation eliminates delayed-luminescence interference' practice, which that abstract never mentions.; The spatial split-half test is sound, but step 5 misattributes a 30-minute dark-ad


---

## C075 — Q7 [L5]

**Claim.** At equal excess emitted photon numbers, spatially resolved UPE analysis will detect an unknown focal oxidative lesion occupying 5% of an ex vivo porcine-skin field more accurately than spatially summed counts, while summed counts will perform at least as well for a diffuse whole-field perturbation.

**Negative result looks like.** There is no positive focal-versus-diffuse interaction in the advantage of spatial analysis over summed counts.

**The deciding number.** D=[AUC(spatial)-AUC(sum)]focal-[AUC(spatial)-AUC(sum)]diffuse; the claim requires D greater than 0.10 with a bootstrap 95% confidence interval excluding zero.

**Scope.** population: Excised porcine-ear skin specimens; condition: Fenton-reagent oxidative perturbations applied either focally to 5% of the field or diffusely over the entire field, with dose adjusted to equalize excess photons; comparator: A spatial generalized-likelihood-ratio detector versus the sum of all pixels from the same camera frames; outcome: Detection AUC at fixed exposure and false-positive rate for focal and diffuse perturbations

**Measurement.** Randomize focal, diffuse, vehicle, and untreated conditions across skin specimens; acquire blinded dark-corrected frames; equalize excess detected counts by titrating dose in pilot specimens; then compare preregistered spatial and summed-count detectors on held-out specimens.

**Instrument.** Deep-cooled high-quantum-efficiency EMCCD, 350–800 nm broadband, with selectable 1×1 to 8×8 hardware binning

**Measurement area.** Imaging detectors, SPAD arrays and photon transfer calibration; Human-subject measurement and clinical-claim requirements; Oxidative stress chemistry and its spectral bands

**Grounded in.** 3 corpus works: `W4321104258`, `W2039224325`, `W1995699286`

**Provenance.** Proposed by codex-solo; nearest existing registry claim H8 at similarity 0.025.

**Audit.** Step 2's use of the same raw frames for both detectors is exactly the right control for isolating the information carried by photon coordinates, but step 0's 'porcine skin' and 'two-dimensional' attributions are absent from the cited abstract, which reports only a marked UPE difference under exogenous Fenton reagent in unspecified skin.; Step 1 is non-load-bearingly overstated because the abstract neither identifies the skin as porcine nor clearly attributes its protein-modification findings to 


---

## C078 — Q7 [L6]

**Claim.** For superficial subcutaneous murine tumors, spatial UPE heterogeneity will predict the histologic viable-tumor fraction out of sample with at least 0.10 greater R-squared than whole-tumor photon counts, tumor volume, and skin temperature alone.

**Negative result looks like.** Spatial UPE features add no more than 0.10 to held-out R-squared for viable-tumor fraction, or their coefficients fail to generalize across animals and cell lines.

**The deciding number.** Delta R-squared=R-squared(spatial-plus-baseline)-R-squared(baseline) under animal-level, cell-line-stratified cross-validation; the claim requires delta R-squared of at least 0.10 with a positive bootstrap confidence interval.

**Scope.** population: Mice bearing superficial subcutaneous AH109A, TE4, or TE9 tumors; condition: Serial spontaneous UPE imaging at one, two, and three weeks after transplantation under controlled dark adaptation; comparator: A baseline model using integrated tumor counts, tumor volume, time point, and skin temperature versus the same model plus preregistered spatial UPE features; outcome: Histologic viable-tumor fraction and its spatial correspondence to the terminal UPE map

**Measurement.** Acquire serial broadband UPE and thermal images under fixed geometry, perform terminal whole-tumor sectioning with blinded viable/necrotic annotation, register histology to the final optical image, and compare preregistered baseline and spatial models using animal-level held-out predictions.

**Instrument.** Back-thinned deep-cooled EMCCD with 400–800 nm response and calibrated macro lens, plus a long-wave infrared camera for surface temperature

**Measurement area.** Imaging detectors, SPAD arrays and photon transfer calibration; Calibration, spectral responsivity, traceability and uncertainty; Human-subject measurement and clinical-claim requirements

**Grounded in.** 2 corpus works: `W2009372666`, `W4409735377`

**Provenance.** Proposed by codex-solo; nearest existing registry claim H8 at similarity 0.045.

**Audit.** The anchor abstract supplies the population, timepoints and outcome verbatim (AH109A/TE4/TE9, weeks 1-3, biophoton distribution compared with histological findings, intensity reflecting tumour viability, r = 0.73 against size), the >90% quantum-efficiency imaging citation is exact, and keeping integrated counts and tumour volume in both models makes Delta-R2 a clean estimate of the information in the spatial distribution.; The cited tumor study directly relates murine tumor UPE to size and histo
