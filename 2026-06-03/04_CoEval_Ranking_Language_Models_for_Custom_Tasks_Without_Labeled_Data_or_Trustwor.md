# CoEval: Ranking Language Models for Custom Tasks Without Labeled Data or Trustworthy Benchmarks

- **Source**: arXiv
- **URL**: https://arxiv.org/abs/2606.03650v1
- **Time**: 2026-06-02
- **Heat**: 

## Summary

CoEval: Ranking Language Models for Custom Tasks Without Labeled Data or Trustworthy Benchmarks

## Content

Authors: Alexander Apartsin, Yehudit Aperstein
## Abstract
Choosing or ranking language models for a specific application is hardest when no task-specific labeled data exists, and standard public benchmarks cannot be trusted, their items having likely leaked into pretraining, so scores reflect memorization rather than fitness. We present CoEval, an open-source, reusable framework that closes this gap end to end: from only a description of a task or domain, teacher models synthesize a fresh, attribute-controlled benchmark with no human labels, contamination-free because items are generated anew on each run, and a cross-family judge ensemble ranks candidate models with no human raters. Validated where ground truth exists, CoEval recovers the true model ranking and tracks ground-truth correctness at ho=0.86. The label-free judging needs no human calibration because judge-panel composition (vendor diversity), not size, drives reliability: a small, well-chosen cross-family panel is most reliable, while a single judge can be anti-correlated with ground truth (judge-choice regret 0.35) and the ensemble never is. Generated items show zero verbatim 13-gram overlap with five major public benchmarks; the panel cancels verbosity bias and precludes same-family self-preference. A four-task study produced 7,978 evaluations for USD 5.89. The same declarative pipeline applies to any domain and is cheap enough to re-run on every model release: a label-free, contamination-free leaderboard any team can regenerate for its own application.

## Links

