# Crop Production Prediction

This project focuses on building a machine learning model to predict crop production (in tons) using agricultural parameters such as area harvested, yield, year, crop type, and region. A Streamlit-based application is also provided to interactively predict production values.

---

## Project Objective

To develop a regression-based ML model that predicts crop production (in tons) based on:

- Area (Region)
- Crop type
- Year
- Area harvested (in hectares)
- Yield (in kg/ha)

This model supports better decision-making in agriculture planning, food security, and agri-business.

---

## Skills Covered

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning (Regression)
- Streamlit App Development
- Data Visualization

---

## Domain

**Agriculture** — analyzing and predicting food production using data science.

---

## Problem Statement

Agricultural production directly affects food security, resource planning, and economic stability. This project predicts crop production using historical data (from FAOSTAT), helping governments, NGOs, and agri-businesses with informed decision-making.

---

## Business Use Cases

1. **Food Security & Planning** — Prevent shortages with reliable production forecasts.
2. **Policy Making** — Design subsidies, insurance, and disaster plans.
3. **Supply Chain Optimization** — Plan logistics based on predicted production.
4. **Price Forecasting** — Help farmers make better market decisions.
5. **Precision Agriculture** — Guide optimal crop selection.
6. **Agri-tech Solutions** — Build data-driven tools for farming.

---

## Exploratory Data Analysis

EDA was performed in `EDA_Analysis.ipynb` and includes:

- Crop & Region-wise Distribution
- Trends over Years (1961–2022)
- Yield vs Area Harvested vs Production
- Outlier Detection
- Productivity Ratios
- Comparative Analysis across crops and regions

---

## Model Development

Multiple regression models were trained and evaluated to predict crop production:

- **Linear Regression**
- **Random Forest Regressor**
- **Gradient Boosting Regressor**
- **XGBoost Regressor**

After comparing performance using evaluation metrics (R² score, MSE, and MAE), the **Random Forest Regressor** consistently outperformed the other models.

 **The Random Forest model was selected as the final model and saved as `model_rf.pkl` for deployment.**

Label Encoders were also saved for:

- **Area** (`le_area.pkl`)
- **Crop Item** (`le_item.pkl`)

---

## Evaluation Metrics

Each model's performance was evaluated using:

- **R² Score** – Coefficient of determination
- **Mean Squared Error (MSE)**
- **Mean Absolute Error (MAE)**

 **Final Decision**:  
The Random Forest Regressor had the best trade-off between accuracy and generalization, and was chosen as the final model for the app.

---

## Streamlit Web App

The prediction interface is built using **Streamlit** in `app.py`.

### Features

- **Select Area** (Region)
- **Select Crop**
- **Select Year** (1961–2022 slider)
- **Enter Area Harvested (ha)**
- **Enter Yield (kg/ha)**

### Output

Shows the **estimated crop production (in tons)** when you click "Predict".

To run the app locally:

```bash
pip install -r requirements.txt
streamlit run app.py
````

---

## Dataset

 **File**: `dataset/FAOSTAT_data.xlsx`

 **Source**: [Crop Dataset](https://www.fao.org/faostat/en/#data)

 **Time Range**: 1961–2022

### Columns Overview

| Column  | Description                          |
| ------- | ------------------------------------ |
| Area    | Country/Region                       |
| Item    | Crop name                            |
| Year    | Calendar year                        |
| Element | Area harvested, Yield, or Production |
| Value   | Quantity (ha, kg/ha, or tons)        |
| Flag    | Metadata indicator                   |

---

## Deliverables

- Cleaned dataset for training and analysis
- EDA & model comparison in notebook
- Trained model & encoders (`.pkl` files)
- Streamlit web application
- Complete documentation (`README.md`)

---

## Requirements

- Create and Install dependencies inside conda base environment:

```bash
conda env create -p C:\conda_envs\crop-production-prediction -f environment.yaml
```

- Activate the conda environment

```bash
conda activate C:\conda_envs\crop-production-prediction
```

- Register the environment as a Jupyter kernel

```bash
python -m ipykernel install --user --name crop-production-prediction --display-name "Python (crop-production-prediction)"
```

- Open the jupyter notebook

```bash
jupyter notebook
```

---

## How to Use

1. Clone this repository.
2. Open `EDA_Analysis.ipynb` to explore data and model building.
3. Run the app using:

   ```bash
   streamlit run app.py
   ```

4. Enter your inputs and get the production estimate instantly.

---

## References

- [FAOSTAT Official Site](https://www.fao.org/faostat/en/#data)
- [Streamlit Documentation](https://docs.streamlit.io/)
