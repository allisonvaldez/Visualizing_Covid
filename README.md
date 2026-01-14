# 🗳️ 2012 FEC Election Data Analysis (Python + Pandas)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-yellow)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

An exploratory data analysis project examining **Federal Election Commission (FEC)** contribution data from the 2012 U.S. presidential election.  
This project uses **Python, Pandas, and Matplotlib** to clean, transform, and visualize political donation patterns across candidates, occupations, and geographic regions.

The goal is to turn a large, messy real‑world dataset into clear insights about how money flowed into the 2012 election.

---

## 🔍 Overview

This project explores questions such as:

- Which candidates received the most contributions  
- How donation amounts varied by occupation and employer  
- Geographic patterns in political giving  
- How small vs. large donors differed across campaigns  

The analysis demonstrates strong fundamentals in **data cleaning**, **aggregation**, **visualization**, and **storytelling with data**.

---

## 📊 Features

### 🧹 Data Cleaning & Preparation
- Loaded and cleaned raw FEC contribution data  
- Standardized employer and occupation fields  
- Removed invalid or incomplete entries  
- Converted monetary values and dates into usable formats  

### 📈 Analysis & Visualizations
- Total contributions by candidate  
- Top occupations and employers for each campaign  
- Distribution of donation amounts  
- Geographic trends using state‑level aggregation  
- Clear, well‑labeled charts designed for readability  

---

## 🔑 Key Findings

### 🗳️ Candidate Contribution Totals
- Barack Obama and Mitt Romney received the majority of individual contributions in the 2012 election cycle.  
- Romney’s campaign attracted more large‑dollar donations, while Obama received a higher volume of small‑dollar contributions.

### 💼 Occupation & Industry Trends
- High‑earning professions such as finance, investment, law, and consulting contributed disproportionately to Romney.  
- Education, healthcare, and public‑sector workers contributed more frequently to Obama.  
- “Retired” and “Self‑Employed” were among the largest donor categories overall.

### 🏢 Employer Patterns
- Major financial institutions and corporate employers leaned toward Romney.  
- Universities, hospitals, and tech‑adjacent employers leaned toward Obama.  
- Donation patterns reflected clear industry‑level political alignment.

### 💵 Donation Amount Behavior
- Obama’s donor base included more small‑dollar contributions (under $200).  
- Romney’s donor base skewed toward larger contributions, often $1,000+.  
- The distribution of donation amounts revealed distinct fundraising strategies.

### 🌎 Geographic Insights
- Coastal states such as California, New York, and Massachusetts contributed heavily to Obama.  
- Southern and Midwestern states contributed more to Romney.  
- State‑level aggregation highlighted clear regional political divides.

### 📈 Fundraising Peaks
- Both campaigns saw donation spikes around debates, primaries, and major campaign events.  
- Obama’s fundraising was more consistent month‑to‑month, while Romney’s showed sharper peaks.

### 🧹 Data Quality Observations
- Employer and occupation fields required extensive cleaning due to inconsistent formatting.  
- Many entries needed correction or removal (e.g., “INFORMATION REQUESTED,” “NONE,” “RETIRED”).  
- Normalizing these fields significantly improved the accuracy of occupation and employer analysis.

---

## 🧪 Tech Stack

- **Python**  
- **Pandas** for data cleaning and transformation  
- **Matplotlib** for visualization  
- **Jupyter Notebook** for exploration and documentation  

---

## 📁 Project Structure

```
2012_FEC/
│
├── data/
│   └── fec_2012.csv
│
├── notebooks/
│   └── fec_analysis.ipynb
│
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/allisonvaldez/2012_FEC.git
cd 2012_FEC
```

### 2. Install dependencies
```bash
pip install pandas matplotlib
```

### 3. Open the notebook
```bash
jupyter notebook notebooks/fec_analysis.ipynb
```

---

## 🧠 What I Learned

- How to clean and standardize large, messy real‑world datasets  
- How to aggregate and analyze political contribution data  
- How to design clear, informative visualizations  
- How to communicate insights through data storytelling  
- How to structure a reproducible analysis workflow  

---

## 📌 Future Enhancements

- Add interactive charts using Plotly  
- Build a small dashboard (Streamlit or Flask)  
- Add geographic heatmaps  
- Compare multiple election cycles  

---

## 👤 Author

**Allison Valdez**  
Full‑Stack Software Engineer  
GitHub: https://github.com/allisonvaldez  
LinkedIn: https://www.linkedin.com/in/alyv/
