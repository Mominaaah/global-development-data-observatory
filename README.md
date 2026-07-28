# 🌍 Global Development Data Observatory

A professional Data Analytics project built with Python that collects, processes, analyzes, and visualizes global development indicators using the World Bank API.

---

## Features

- Automated ETL Pipeline
- World Bank API Integration
- Data Cleaning with Pandas
- Data Validation
- Growth Rate Analysis
- Automated Analytical Insights
- Multiple Visualizations
- Development Group Comparison
- Interactive Dashboard (Coming Soon)

---

## Technologies

- Python
- Pandas
- Requests
- Matplotlib
- Plotly
- Streamlit
- World Bank API

---

## Dataset

Data is collected directly from the World Bank Open Data API.

Countries analyzed:

- Developed Countries
- Developing Countries
- Least Developed Countries

Indicators:

- GDP
- GDP per Capita
- Population
- Unemployment Rate

---

## Project Structure

```text
src/
│
├── api/
├── config/
├── etl/
├── analysis/
├── visualization/
└── dashboard/
```

---

## How to Run

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the ETL

```bash
python -m src.etl.download_data
python -m src.etl.run_etl
```

Run analysis

```bash
python -m src.analysis.analyze_data
```

Run dashboard

```bash
streamlit run src/dashboard/app.py
```

---

## Author

**Momina Ramzan**