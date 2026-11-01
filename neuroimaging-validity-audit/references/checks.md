# Targeted audit checks

Select checks relevant to the claim; this is not a mandatory checklist for every
paper. Evidence of a risk factor alone does not establish its effect on results.

## Documents and numerical consistency

- Reconcile enrollment, exclusions, analysis samples, missingness, denominators,
  degrees of freedom, and repeated observations.
- Check test statistic/p-value/interval/effect-size compatibility only when test
  type, tails, corrections, and degrees of freedom are sufficiently specified.
  Allow rounding; confirm PDF extraction before calling a discrepancy an error.
- Compare abstract, text, figures, tables, supplement, preregistration, and code.
  Identify exploratory versus confirmatory claims and documented deviations.
- Distinguish a significant/nonsignificant pair from a tested interaction, and
  non-rejection from equivalence. Avoid observed post-hoc power as evidence.
- Reconstruct multiplicity across regions, contrasts, outcomes, and follow-ups;
  an unknown analysis history is not proof of selective reporting.

## Task activation and cognitive interpretation

- Inspect contrast weights and task demands: inhibition, attention, rarity,
  difficulty, time-on-task, errors, motor output, and baseline content.
- Check independent ROI definitions versus selection on the tested effect.
  Distinguish circular effect-size estimation from legitimate selected displays.
- Match spatial claims to voxel/cluster inference and correction scope; cluster
  significance does not make every voxel a separately established finding.
- Ask whether reverse inference, causal necessity, or regional specificity needs
  evidence beyond the reported activation contrast.
- For nulls, examine precision, measurement quality, and whether subtraction or
  nuisance adjustment could remove the intended signal.

## Prediction and decoding

- Establish the target generalization unit: trials, runs, participants, families,
  sites, or time. Inspect overlap and dependence across training/test partitions.
- Trace feature selection, imputation, scaling, harmonization, nuisance regression,
  hyperparameter selection, and model selection relative to those partitions.
  Judge leakage against the intended deployment setting, not a blanket rule.
- Check label confounds, temporal autocorrelation, repeated test-set use,
  appropriate baselines, and exchangeability of permutation schemes.
- Successful decoding establishes information available to a model; identifying
  a particular represented construct requires excluding pertinent alternatives.
- Saved predictions permit metric checks but cannot prove training was clean.

## Brain–behavior and individual differences

- Check ROI/feature selection independence, influential units, confounding,
  restriction of range, exclusions, and effective sample size.
- Assess reliability of the actual contrast or score, not only its components.
  Robust mean activation does not establish reliable participant rankings.
- Quantify uncertainty where possible; an imprecise null cannot establish absence.
  Do not blindly disattenuate correlations using uncertain reliability estimates.
- A group-effect sample-size recommendation does not automatically transfer to
  between-person associations, or vice versa.

## Longitudinal and dense sampling

- Separate sessions from independent participants and within-person from
  between-person estimands. Check trends, autocorrelation, seasonality, and
  time-varying confounds.
- Inspect blocked/temporal splits and resampling exchangeability. Many observations
  from one participant do not by themselves establish population generalization.

## Meta-analysis, ontology, and methods papers

- Trace sample overlap, multiple effects per study, inclusion decisions, and
  dependence. Inspect whether labels operationalize the construct claimed.
- For benchmarks, inspect ground truth, tuning/test separation, baseline fairness,
  and whether the metric actually measures the advertised benefit.
- Treat corpus coverage and publication selection as limitations to evaluate,
  not automatically demonstrated bias.

## Cheap checks by available artifact

| Artifact | Useful checks | Important boundary |
|---|---|---|
| Participant ROI/behavior tables | Refit associations and direct contrasts; intervals; influence; justified covariates | Cannot validate upstream ROI independence from values alone |
| Out-of-fold predictions and IDs | Metrics; uncertainty at correct unit; subgroup/site differences; duplicate IDs | Cannot exclude all training leakage |
| First-level contrast/variance images | Selected group models; participant influence | Holds preprocessing and first-level modeling fixed |
| Events and design matrices | Contrast estimability; collinearity; behavioral confounds | Does not verify image alignment or actual execution |
| Unthresholded group maps | Signs, reported coordinates, map/table agreement | Does not recover participant variability |
| Repeated measurements | Reliability and temporal dependence | Requires a model suited to the intended estimand |

For permutations/bootstrap, verify that resampling respects dependence and the
null statistic actually varies. For simulations, include known-positive and
known-negative conditions and record assumptions. For sensitivity analyses,
report all attempted defensible alternatives, including ones strengthening the
claim, without selecting a preferred result by significance.
