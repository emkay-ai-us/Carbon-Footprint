# 🇺🇸 U.S. Carbon Footprint Estimator 🌱

This project is a simple but powerful tool that allows individuals and small businesses in the United States to estimate their **Scope 1 and Scope 2 greenhouse gas (GHG) emissions** based on **electricity** and **natural gas** consumption.

🖥️ Built with **Python + Streamlit**, it uses **official EPA eGRID emission factors** to provide CO₂ estimates in real time — helping users raise awareness and start their sustainability journey.

---

## 🔍 What It Does

- ✅ Estimates CO₂ emissions from:
  - 🔌 Electricity use (kWh)
  - 🔥 Natural gas use (therms)
- ✅ Uses **state-specific emission factors** for accurate Scope 2 calculations
- ✅ Outputs results in:
  - Kilograms of CO₂ (kg CO₂)
  - Metric Tons of CO₂ (tCO₂)
- ✅ Allows download of emission summary as CSV
- ✅ Fully deployed as a **Streamlit web app**

---

## 🧪 Sample Use Cases

- 🏢 A small business in Texas wants to estimate its monthly office emissions.
- 🧑‍🏫 A teacher uses it to demonstrate carbon impact in a classroom.
- 🧑‍💻 An individual uploads utility bills and sees their personal footprint.

---

## 📊 How It Works

The app uses the following formulae:

```
Electricity CO₂ = kWh × state emission factor (kg CO₂ / kWh)  
Natural Gas CO₂ = therms × 5.3 (kg CO₂ / therm)
```

Emission factors are sourced from the **EPA eGRID 2023** dataset and vary by U.S. state.

---

## 🚀 Try It Live

🟢 [🌍 Streamlit App (Live)](https://your-streamlit-link-here)

📁 [📦 GitHub Repository](https://github.com/yourusername/carbon-footprint-estimator)

---

## 📂 Project Structure

```
├── app.py                 # Streamlit application code
├── data/
│   └── epa_emission_factors.csv
├── utils/
│   └── calculator.py      # Calculation logic (optional)
├── requirements.txt       # Dependencies
└── README.md              # This file
```

---

## 📦 Installation (Local Use)

```bash
git clone https://github.com/yourusername/carbon-footprint-estimator.git
cd carbon-footprint-estimator
pip install -r requirements.txt
streamlit run app.py
```

---

## 💡 Future Enhancements

- [ ] Support Scope 3 inputs (e.g., transport, flights)
- [ ] Add bar chart of emissions over time
- [ ] Allow CSV upload for batch analysis
- [ ] Add renewable % offset calculator

---

## 👋 About the Creator

I’m an AI/ML engineer and educator with over 28 years of experience, now focusing on **climate tech**. This is my first open-source project in sustainability, designed to help individuals and SMEs take the first step toward emissions awareness.

Feel free to (https://www.linkedin.com/in/muthukumaran-maruthappa-501825100/) if you'd like to collaborate!

---

## 📜 License

This project is licensed under the MIT License.
