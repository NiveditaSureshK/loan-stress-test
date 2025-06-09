# Unsecured & Small-Business Loan Stress Test

## Goal
Simulate **1 000 macro-economic scenarios**, forecast credit losses on SME loans *and* credit-card receivables, and estimate **worst-case CET1 erosion** over 12 quarters.

## Why It Matters
Annual **CCAR/DFAST** filings require banks to prove capital resilience. Automating this analysis shortens prep cycles and surfaces capital pressure points in near real time.

## Key Deliverables
1. **Monte-Carlo scenario generator** (GDP ∆, unemployment).  
2. **Panel PD & LGD models** for SMEs; **LightGBM PD model** for cards.  
3. **Tableau waterfall dashboard** + one-page PDF summary generated via Papermill.

## Success Metric
```text
worst_case_cet1 = min(CET1_q) – CET1_start

## Quick Start

```bash
# create and activate the project environment
conda env create -f environment.yml
conda activate stress

# install the package in editable mode
python -m pip install -e .