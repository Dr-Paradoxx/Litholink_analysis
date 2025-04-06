# Litholink Analysis

## Overview
The **RenalStoneInsights** project is designed to analyze clinical data derived from the Litholink study, focusing on the impact of kidney stone type and pH levels on key biochemical markers and patient demographics. This repository contains tools to clean raw Excel data, perform rigorous statistical analyses, build predictive models, and generate insightful visualizations—all aimed at improving the understanding and management of kidney stone disease.

## Objectives
- **Data Cleaning:** Import and preprocess raw data from an Excel file with two sheets:
  - **Litholink_main:** Contains critical variables such as Ca24, SSCaP, Ca24kg, Ca24Cr24, Cit24, Serum_Ca, Age, and BMI.
  - **Variability Study:** Contains same-day urine sample pairs used to assess intra-patient variability.
- **Statistical Analysis:** 
  - Perform regression analyses to examine the association between stone type (CaP, Brushite, CaOx), pH category (High/Low), and various clinical outcomes.
  - Conduct ANOVA and Tukey HSD tests to compare variability among stone types.
- **Visualization:** Generate professional plots (boxplots, bar charts) to illustrate data distributions and variability trends.
- **Predictive Modeling:** (Optional) Develop regression models to predict key outcomes based on demographic and clinical variables.

## Methodology
1. **Data Preparation:**  
   - Load the raw Excel file and extract data from the `Litholink_main` and `Variability Study` sheets.
   - Clean the datasets by selecting relevant variables, handling missing data, and standardizing data types.
2. **Regression Analysis:**  
   - Build separate regression models for markers such as Ca24, Cit24, SSCaP, Ca24Kg, Ca24Cr24, and Serum_Ca.
   - Evaluate the effect of stone category, pH category, gender, age, and BMI on these markers.  
   - **Key Findings:**  
     - Stone category shows strong and statistically significant associations with most clinical markers (p-values < 0.001).
     - Demographic factors like age and BMI also play an important role.
3. **Variability Analysis:**  
   - Assess the intra-patient variability in same-day urine samples using the coefficient of variation (CV) and standard deviation.
   - ANOVA and post-hoc Tukey HSD tests reveal significant differences in Ca24 variability among stone types.
4. **Visualization:**  
   - Generate clear, publication-quality plots to visualize differences in distributions and variability across groups.

## Importance in Healthcare
Understanding the relationship between stone composition and clinical variables is essential for:
- **Enhanced Diagnosis:** Improved identification of kidney stone subtypes based on objective clinical markers.
- **Personalized Treatment:** Tailoring interventions to individual patient profiles can reduce recurrence rates and improve outcomes.
- **Optimized Resource Allocation:** Efficient use of healthcare resources by targeting high-risk groups for intensive management.
- **Evidence-Based Practice:** Supporting clinical decisions with robust statistical evidence leads to more effective and sustainable patient care strategies.

## Results Summary
- **Regression Analyses:**  
  - Significant associations were observed between stone type and key markers such as Ca24, Cit24, SSCaP, and others.
  - Regression coefficients indicate that different stone categories (Brush, CaOx, CaP) impact clinical outcomes significantly.
- **Variability Study:**  
  - Variability in same-day urine samples (e.g., CV for Ca24) differed among stone types, with ANOVA revealing significant differences (F = 4.4143, p = 0.01321) and Tukey HSD tests confirming significant pairwise differences.
- **Visualization Outputs:**  
  - Generated plots (saved in the `plots/` directory) provide a clear visual summary of the data distributions and variability trends.

## Project Structure
RenalStoneInsights/
├── data/
│   ├── raw/               
│   └── processed/         
├── notebooks/             
├── src/                   
│   ├── data_cleaning.py
│   ├── analysis.py
│   ├── modeling.py
│   └── visualization.py
├── tests/                 
├── .gitignore             
├── LICENSE                
├── README.md              
├── requirements.txt       
├── setup.py               
└── main.py                

## How to Run
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/RenalStoneInsights.git
   cd RenalStoneInsights

2. **Install Dependencies:**
    ```bash
     pip install -r requirements.txt

3. Run the Main Analysis:
   ```bash
   python main.py

4.	Run Tests:
   ```bash
   python -m unittest discover tests
