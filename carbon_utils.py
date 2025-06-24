# carbon_utils.py

import pandas as pd

# Load state-wise electricity emission factors (CSV should be in same folder)
def load_state_factors(file_path="us_state_electricity_emission_factors.csv"):
    df = pd.read_csv(file_path)
    return dict(zip(df["State"], df["Electricity_Emission_Factor_kg_per_kWh"]))

# Constants
NATURAL_GAS_FACTOR = 5.3  # kg CO2 per therm (EPA standard)

def calculate_emissions(electricity_kwh, gas_therms, state, factors_dict):
    emission_factor = factors_dict.get(state, 0.4)  # fallback to national average
    electricity_kg = electricity_kwh * emission_factor
    gas_kg = gas_therms * NATURAL_GAS_FACTOR
    total_kg = electricity_kg + gas_kg
    return {
        "Electricity (kg CO2)": round(electricity_kg, 2),
        "Gas (kg CO2)": round(gas_kg, 2),
        "Total (kg CO2)": round(total_kg, 2),
        "Total (tons CO2)": round(total_kg / 1000, 2)
    }
