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

The performance of this stress-testing engine is evaluated using the **worst-case CET1 depletion**, defined as:

```python
worst_case_cet1 = min(CET1_q) - CET1_start

Where:

CET1_start: The Common Equity Tier 1 capital ratio at the beginning of the stress testA more negative value of worst_case_cet1 signals a greater drop in regulatory capital, indicating higher portfolio risk under stress. The model helps identify weak spots in SME and credit card portfolios and supports CET1 buffer planning.

CET1_q: A list or array of projected CET1 values over time across multiple Monte Carlo scenarios

min(CET1_q): Represents the worst-case CET1 outcome under simulated macroeconomic shocks

A more negative value of worst_case_cet1 signals a greater drop in regulatory capital, indicating higher portfolio risk under stress. The model helps identify weak spots in SME and credit card portfolios and supports CET1 buffer planning.

## Quick Start

```bash
# create and activate the project environment
conda env create -f environment.yml
conda activate stress

# install the package in editable mode
python -m pip install -e .
