The Fatality of Shark Attacks
**1. Project Overview**

This project analyzes global shark attack data to examine whether provoked shark attacks are associated with higher fatality rates compared to unprovoked attacks. The study applies exploratory data analysis and statistical testing while controlling for country, year and activity

**2. Research Question**

Are provoked shark attacks more likely to result in fatal outcomes than unprovoked shark attacks?

**3. Hypotheses**

Null Hypothesis (H₀):
There is no statistically significant difference in fatality rates between provoked and unprovoked shark attacks.

Alternative Hypothesis (H₁):
Provoked shark attacks are associated with higher fatality rates compared to unprovoked shark attacks.

**Dataset Description**

The dataset contains global historical records of shark–human interactions from 1900 to the present.
To ensure statistical relevance, the analysis focuses on the top 15 countries with the highest number of recorded incidents.

**Key Variables**

Type (Provoked / Unprovoked) – Independent variable
Fatality (Yes / No) – Dependent variable
Country – Control variable
Year – Control variable
Activity – Control variable
Sex – Additional control variable

**Data Cleaning and Preparation**

The dataset initially contained inconsistent formatting, missing values, and noise.
The following steps were performed:
1. Standardization of text fields (lowercasing, trimming whitespace)
2. Logical handling of missing values and ambiguous entries
3. Replacement of unclear categories with “Unknown”
4. Removal of exact duplicate records
5. Grouping of similar activity categories
6. Filtering of dataset to include only provoked and unprovoked attack types
7. These steps ensured consistency and reliability prior to statistical analysis.

**Methodology**

The analysis included:

Exploratory Data Analysis (grouping, pivot tables, and visualizations)
Country-level comparison of attack frequency and fatality rates
Time trend analysis by decade
Chi-Square Test of Independence to evaluate the association between attack type and fatality outcome
The statistical test was conducted while controlling for country, year, activity, and sex.

**Results**

The Chi-Square Test of Independence produced the following result:

Chi-square statistic: 101.05
Degrees of freedom: 1
p-value: 8.98 × 10⁻²⁴
Since the p-value is significantly less than 0.05, the null hypothesis is rejected.

**Conclusion**

There is a statistically significant association between attack type and fatality outcome. Provoked and unprovoked attacks differ in fatality patterns.

**Limitations**

Variability in global reporting standards
Missing or ambiguous fatality entries
Potential misclassification of attack type

**Future Opportunities for Research**

Future research could extend this analysis by:
Applying logistic regression modeling to control for multiple variables simultaneously
Adjusting fatality rates for exposure (e.g., coastal population or tourism data)
Incorporating environmental or climate-related variables
Conducting species-level analysis of sharks

**How to Run the Project**

1. Clone the repository
2. Install required libraries:

pandas
matplotlib
seaborn
scipy

3. Open Mini_Project_1.ipynb

4. Run all cells sequentially

**Authors**

Victoria
Alex
Rado
