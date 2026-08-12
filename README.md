# Global Development & SDG Observatory

> An interactive data analytics platform for exploring global development disparities, economic performance, social indicators, and Sustainable Development Goal (SDG)-related patterns across countries and development groups.

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)](https://pandas.pydata.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![World Bank API](https://img.shields.io/badge/Data-World%20Bank%20API-009FDA)](https://data.worldbank.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Overview

The **Global Development & SDG Observatory** is an end-to-end data analytics project designed to analyze development patterns and disparities across countries belonging to different development groups.

The project collects data from the **World Bank API**, processes and validates the data through an ETL pipeline, performs analytical calculations, and presents the results through an interactive **Streamlit dashboard**.

Rather than focusing on a single country or metric, the platform provides a comparative view of development across:

- Developed countries
- Developing countries
- Least Developed Countries

The goal is to transform raw development data into meaningful analytical insights that can help users understand economic, demographic, employment, infrastructure, education, and human-development differences.

## Project Objectives

The main objectives of this project are to:

- Collect development indicators programmatically using the World Bank API.
- Build a reproducible ETL pipeline for data ingestion and transformation.
- Compare development indicators across 15 countries.
- Compare development groups to identify structural development gaps.
- Calculate a composite development index.
- Analyze country-level development performance.
- Explore indicators relevant to the United Nations Sustainable Development Goals.
- Generate automated analytical insights.
- Provide an interactive dashboard for exploration and comparison.

## Countries Covered

The project currently analyzes **15 countries** divided into three development groups.

### Developed Countries

| Country | Code |
|---|---|
| United States | USA |
| Germany | DEU |
| Japan | JPN |
| Canada | CAN |
| Australia | AUS |

### Developing Countries

| Country | Code |
|---|---|
| Pakistan | PAK |
| India | IND |
| China | CHN |
| Brazil | BRA |
| Nigeria | NGA |

### Least Developed Countries

| Country | Code |
|---|---|
| Afghanistan | AFG |
| Nepal | NPL |
| Ethiopia | ETH |
| Uganda | UGA |
| Malawi | MWI |

## Indicators

The platform currently works with **7 development indicators**:

| Indicator | Description |
|---|---|
| GDP | Gross Domestic Product |
| GDP Per Capita | GDP per person |
| Population | Total population |
| Unemployment | Unemployment rate |
| Life Expectancy | Average expected lifespan |
| Electricity Access | Access to electricity |
| School Enrollment | Secondary school enrollment |

These indicators provide a multidimensional view of development rather than relying on GDP alone.

# Data Pipeline

The project follows an end-to-end data engineering and analytics workflow:

```text
              World Bank API
                    │
                    ▼
             Data Extraction
                    │
                    ▼
              Raw JSON Data
                    │
                    ▼
              Data Processing
                    │
                    ▼
               Data Cleaning
                    │
                    ▼
            Master Development
                  Dataset
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
     Analytical Layer      Dashboard
          │                   │
          ▼                   ▼
 Development Index      Streamlit App
 Peer Gap Analysis
 Trends & Growth
 SDG Analysis
 Automated Insights
```

## ETL Pipeline

### 1. Extract

Development data is retrieved programmatically from the World Bank API.

The extraction layer supports:

- Multiple countries
- Multiple indicators
- Automatic API requests
- Request error handling
- Timeout handling
- Retry logic
- Raw JSON storage

---

### 2. Transform

The raw API responses are transformed into structured datasets.

The processing layer:

- Extracts usable observations
- Converts API responses into tabular data
- Handles missing values
- Identifies indicators
- Associates countries with development groups
- Creates standardized CSV datasets

---

### 3. Load

Processed datasets are stored in:

```text
data/processed/
```

The main analytical dataset is:

```text
development_data.csv
```

A derived development index dataset is also generated:

```text
development_index.csv
```

---

# Analytical Features

## 1. Development Index

The project includes a composite **Development Index** designed to provide a comparative representation of development performance across countries.

The index incorporates multiple development dimensions rather than evaluating countries using a single economic metric.

The resulting dataset allows countries to be compared based on their overall development performance.


## 2. Development Gap Analysis

The dashboard provides comparisons between development groups.

This allows users to explore differences between:

- Developed countries
- Developing countries
- Least Developed Countries

The analysis helps identify disparities across economic and social indicators.

## 3. Country Profiles

Users can explore individual countries and examine their development indicators over time.

Country-level analysis provides a more detailed perspective than group-level averages.

## 4. Trends & Comparisons

The platform allows users to investigate historical indicator trends and compare countries across different development dimensions.

Examples include:

- GDP trends
- GDP per capita trends
- Population changes
- Unemployment patterns
- Life expectancy
- Electricity access
- School enrollment
  

## 🇺🇳 5. SDG Development Lens

The project includes an **SDG Development Lens** connecting selected development indicators with broader Sustainable Development Goal themes.

The analysis provides a data-driven perspective on areas such as:

- Economic development
- Employment
- Education
- Infrastructure
- Human development

> Note: The project uses selected World Bank indicators as analytical proxies and is not intended to reproduce the official UN SDG indicator framework.

## 6. Automated Insights

The dashboard includes an automated insights layer that identifies notable patterns in the development data.

Examples of insights include:

- Highest and lowest performing countries
- Differences between development groups
- Indicator-level disparities
- Significant development gaps
- Comparative country performance

This converts raw analytical results into more accessible observations for dashboard users.

---

# Dashboard

The interactive Streamlit dashboard is organized into several analytical views:

### Global Overview

Provides a high-level summary of global development indicators.

### Country Profile

Allows users to explore individual countries.

### Development Gap

Compares development performance across development groups.

### Trends & Comparisons

Explores historical trends and country comparisons.

### 🇺🇳 SDG Development Lens

Examines development indicators through an SDG-oriented perspective.

### Automated Insights

Provides automatically generated analytical observations.

# Technology Stack

| Technology     | Purpose                             |
| -------------- | ----------------------------------- |
| Python         | Core programming language           |
| Pandas         | Data manipulation and analysis      |
| Requests       | World Bank API requests             |
| Matplotlib     | Data visualization                  |
| Streamlit      | Interactive dashboard               |
| World Bank API | Development data source             |
| Git & GitHub   | Version control and project hosting |

---

# Project Structure

```text
global-development-data-observatory/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── api/
│   │   └── world_bank.py
│   │
│   ├── analysis/
│   │   └── development_index.py
│   │
│   ├── dashboard/
│   │   ├── app.py
│   │   └── pages/
│   │       ├── overview.py
│   │       ├── country_profile.py
│   │       ├── development_gap.py
│   │       ├── trends.py
│   │       ├── sdg_lens.py
│   │       └── insights.py
│   │
│   ├── etl/
│   │   ├── download_data.py
│   │   ├── process_data.py
│   │   ├── run_etl.py
│   │   └── combine_data.py
│   │
│   ├── utils/
│   │   └── config.py
│   │
│   └── visualization/
│
├── notebooks/
├── reports/
├── tests/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/Mominaaah/global-development-data-observatory.git
```

```bash
cd global-development-data-observatory
```

## 2. Create a virtual environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Run the ETL pipeline

Download development data:

```bash
python -m src.etl.download_data
```

Process the raw API data:

```bash
python -m src.etl.run_etl
```

Combine the processed datasets:

```bash
python -m src.etl.combine_data
```

## Run the Development Index

```bash
python -m src.analysis.development_index
```

## Launch the Dashboard

The Streamlit application is located in:

```text
src/dashboard/app.py
```

Run:

```bash
streamlit run src/dashboard/app.py
```

The dashboard will then be available locally through Streamlit.

---

# Data Source

The project uses publicly available development indicators from the:

**World Bank Open Data**

[https://data.worldbank.org/](https://data.worldbank.org/)

The project retrieves indicator observations through the **World Bank API**.

The data belongs to the respective data provider and is used here for analytical and educational purposes.

---

# Key Questions Explored

The project is designed to answer questions such as:

- How different are development outcomes between country groups?
- Which countries have the highest GDP per capita?
- How do development indicators change over time?
- Which countries experience larger development gaps?
- How does access to electricity vary across development groups?
- How do life expectancy and education indicators differ?
- Which countries demonstrate stronger overall development performance?
- What development patterns can be identified from multiple indicators simultaneously?

# Why This Project Matters

Development cannot be represented by a single metric.

A country's GDP may be high while social or infrastructure outcomes remain uneven. Similarly, a country with lower GDP may demonstrate improvements in areas such as electricity access, education, or life expectancy.

This project therefore uses a **multidimensional analytical approach** to provide a broader view of development.

The platform combines economic, demographic, employment, infrastructure, education, and human-development indicators into one analytical environment.

# Future Improvements

Planned improvements include:

- [ ] Docker containerization
- [ ] Public cloud deployment
- [ ] Live dashboard URL
- [ ] Automated scheduled data refresh
- [ ] Additional World Bank indicators
- [ ] Expanded country coverage
- [ ] More SDG-aligned indicators
- [ ] Advanced forecasting
- [ ] Improved data quality monitoring
- [ ] Automated pipeline execution
- [ ] Additional interactive visualizations

# Project Status

**Current Status: Active Development**

The core data pipeline, analytical layer, development index, and interactive dashboard have been implemented.

The next phase focuses on deployment, reproducibility, and further analytical enhancements.

# Author

**Momina Ramzan**

Computer Science Graduate | Data Analytics & Data Engineering

Interested in:

- Data Analytics
- Data Engineering
- Business Intelligence
- Development Data
- Data-driven decision making

---

# Acknowledgements

- World Bank Open Data for providing publicly accessible development datasets.
- Streamlit for the interactive dashboard framework.
- Python open-source ecosystem for the analytical and data-processing tools used in this project.

---

## ⭐ If you find this project useful

Consider giving the repository a ⭐ on GitHub.
