# app.py

import streamlit as st
import pandas as pd
from carbon_utils import calculate_emissions, load_state_factors

# Load emission factor data
factors = load_state_factors()

# Streamlit app layout
st.set_page_config(page_title="U.S. Carbon Footprint Estimator", layout="centered")
st.title("🌍 U.S. Carbon Footprint Estimator")
st.markdown("Estimate CO₂ emissions based on your electricity and natural gas usage.")

# User inputs
state = st.selectbox("Select your U.S. State", sorted(factors.keys()))
electricity = st.number_input("Electricity Used (in kWh)", min_value=0.0, value=1000.0)
gas = st.number_input("Natural Gas Used (in Therms)", min_value=0.0, value=50.0)

# Calculate button
if st.button("Calculate Emissions"):
    result = calculate_emissions(electricity_kwh=electricity, gas_therms=gas, state=state, factors_dict=factors)
    st.subheader("📊 Estimated Emissions")
    st.write(f"**Electricity Emissions**: {result['Electricity (kg CO2)']} kg CO₂")
    st.write(f"**Gas Emissions**: {result['Gas (kg CO2)']} kg CO₂")
    st.write(f"**Total Emissions**: {result['Total (kg CO2)']} kg CO₂ / {result['Total (tons CO2)']} metric tons")

    # Optional CSV export
    csv_df = pd.DataFrame([{
        "State": state,
        "Electricity (kWh)": electricity,
        "Natural Gas (therms)": gas,
        **result
    }])
    st.download_button("Download CSV Report", data=csv_df.to_csv(index=False), file_name="carbon_report.csv", mime="text/csv")
