# 🧮 U.S. Carbon Footprint Estimator

This is a Streamlit web app to help estimate carbon dioxide (CO₂) emissions based on **electricity (kWh)** and **natural gas (therms)** usage in the **United States**, using **state-specific emission factors** from EPA's eGRID data.

## 🔍 Features

- Select U.S. state for localized emission factor
- Input electricity and gas consumption
- See CO₂ emissions (kg & metric tons)
- Download CSV report

## 🚀 Getting Started

1. Clone the repo:

```bash
git clone https://github.com/your-username/carbon_app.git
cd carbon_app

2. Install requirements

pip install -r requirements.txt

3. Run the app:

streamlit run app.py

 ##Project Files

app.py: Streamlit interface
carbon_utils.py: Emissions logic
us_state_electricity_emission_factors_full.csv: Emission factors by U.S. state
requirements.txt: Python dependencies
