# Final End-to-End Data Analytics Pipeline (SQL · Python · Tableau)

## Project Overview
This project implements a complete, decision-driven data analytics pipeline to optimize vehicle
inventory for a small car dealership.

Starting from a large, noisy dataset (~19,000 vehicles), the project applies structured data
curation, business-driven filtering, and rule-based selection to produce a final inventory of
14 optimal vehicles targeted at middle-class buyers.

The emphasis of this project is not visualization alone, but **how analytical decisions are made,
validated, and explained across the pipeline**.

---

## Business Problem
A small dealership cannot stock hundreds of vehicles.  
The goal is to determine **which limited set of cars provides the best balance of affordability,
condition, safety, and market relevance**.

Constraints include:
- Maximum price threshold
- Preference for lower mileage
- Emphasis on safety features (airbags)
- Representation across manufacturers
- Avoidance of low-volume or statistically unreliable models

---

## Data Pipeline & Decision Logic

### 1. Data Curation & Reduction (SQL)
- Original dataset contains ~19,000 vehicles
- SQL is used to:
  - Identify high-volume manufacturers
  - Select the most statistically representative model-year combinations
  - Reduce the dataset to a focused, analytically reliable subset

This step ensures later decisions are based on **signal, not noise**.

### 2. Rule-Based Selection (Python)
Python applies explicit business rules to select **one optimal vehicle per model**:
- Price ceiling enforcement
- Mileage minimization
- Safety prioritization (airbags)
- Tie-breaking using production year and price

This stage represents the **core decision-making logic** of the project.

### 3. Visualization & Validation (Tableau)
Tableau is used to:
- Validate that selection logic produces coherent results
- Compare pricing and mileage across the final inventory
- Communicate *why* each vehicle was selected, not just *which* vehicles

The dashboard visualizes the **final, validated output** of the pipeline.

---

## Project Structure
- `data/` → Curated SQLite dataset used across all stages
- `sql/` → SQL queries for dataset reduction and filtering
- `python/` → Python logic implementing business rules
- `dashboard/` → Tableau dashboard file
- `docs/` → Full project documentation (scoping, EDA, datafolio)

---

## Documentation
This repository includes full written documentation covering:
- Problem scoping and business context
- Data curation and exploratory analysis
- Rationale behind selection criteria
- Final insights and recommendations

These documents explain **not just what was done, but why it was done**.

---

## Tools Used
- SQL (SQLite)
- Python (pandas)
- Tableau
