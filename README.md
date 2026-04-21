# Airbnb NYC Price Analysis

**What drives Airbnb nightly prices in New York City?**

This project investigates neighbourhood-level signals of desirability and safety as predictors of Airbnb listing prices. Five factors were tested — median household income, distance to the CBD, crime density, listing competition, and tree coverage — using a multi-method analytical framework across six integrated datasets.

---

## Key Findings

| Rank | Factor | Insight |
|------|--------|---------|
| 1 | **Median household income** | Strongest predictor across 3 of 4 models — high-income areas bundle restaurants, services, and safety perception |
| 2 | **Distance to CBD** | Non-linear effect: steep premium near Midtown/Lower Manhattan, flattens outward — caught by tree-based models, missed by linear |
| 3 | **Listing density** | Supply-side pressure modestly compresses prices |
| 4–5 | **Crime density** (shooting + arrest) | Contributes, but partially correlated with income |
| 6 | **Tree coverage** | Weakest predictor — directionally positive but not a primary driver |

---

## Datasets

| Dataset | Source | Records |
|---------|--------|---------|
| Airbnb Listings NYC 2019 | Inside Airbnb | ~49,000 listings |
| NYPD Shooting Incident Data (Historic) | NYC Open Data | 2006–2019 |
| NYPD Arrests Data (Historic) | NYC Open Data | 2013–2019 |
| NYC Street Tree Census 2015 | NYC Open Data | ~680,000 trees |
| Median Household Income by NTA | NYC Open Data | 195 neighbourhoods |
| NYC Population by Neighbourhood | NYC Open Data | 195 neighbourhoods |
| MTA Subway Turnstile Usage 2019 | MTA | Station-level ridership |

All datasets were joined at neighbourhood (NTA) level using spatial polygon mapping and fuzzy name matching.

---

## Architecture

Data management follows the **ANSI/SPARC three-schema model**:

- **Internal layer** — raw datasets loaded into a SQLite database
- **Conceptual layer** — full logical tables (listings, shootings, arrests, trees)
- **External layer** — four SQL views (`v_airbnb`, `v_shooting`, `v_arrests`, `v_trees`) exposing only analysis-relevant columns, with PII stripped and temporal filters pushed down to SQL

This separation enforces logical data independence: analysis code is insulated from raw schema changes.

---

## Methods

- **Spearman rank correlation** — monotonic relationship detection (non-parametric)
- **Stepwise R² drop** — measures each variable's marginal contribution to a linear model
- **Machine learning feature importance** — Decision Tree, Random Forest, and XGBoost used as cross-model robustness check (not for prediction)

---

## Limitations

- Temporal mismatch: Airbnb data is 2019, tree census is 2015, crime spans 2006–2019
- Per-capita crime rates use 2010 census population — gentrified neighbourhoods may have distorted figures
- Crime data only captures reported incidents; under-reporting introduces systematic bias
- Fuzzy string matching for neighbourhood joins introduces a small risk of incorrect linkages
- Omitted variables: transit access, school quality, amenities, and tourism proximity are absent
- All findings are associational — no causal claims

---

## Stack

- **Python** — `pandas`, `numpy`, `scipy`, `sklearn`, `xgboost`, `matplotlib`, `seaborn`, `geopandas`
- **SQLite** — data ingestion and view-based access control
- **Jupyter Notebook** — end-to-end analysis in [`SC3021 NYC Airbnb.ipynb`](SC3021%20NYC%20Airbnb.ipynb)

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Repository Structure

```
airbnb_nyc/
├── SC3021 NYC Airbnb.ipynb            # Main analysis notebook
├── requirements.txt                   # Python dependencies
├── speech_script.md                   # Presentation script
└── src/                               # Raw datasets
    ├── AB_NYC_2019.csv
    ├── Airbnb_NYC.csv
    ├── NYPD_Shooting_Incident_Data__Historic_.csv
    ├── NYPD_Arrests_Data__Historic_ (1).csv
    ├── new_york_tree_census_2015.csv
    ├── new_york_tree_species.csv
    ├── medianincome.csv
    ├── New_York_City_Population_By_Neighborhood_Tabulation_Areas.csv
    ├── Total Population.csv
    ├── MTA_Subway_Turnstile_Usage_Data__2019.csv
    └── nycgeo.json
```
