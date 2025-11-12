# 🎬 IMDb Top 1000 Movies - Box Office Analysis

## 📖 Project Overview
This project performs **Exploratory Data Analysis (EDA)** on the **IMDb Top 1000 Movies Dataset** using **Pandas**, **NumPy**, and **Matplotlib**.  
The goal is to clean and analyze the dataset, derive meaningful insights, and visualize patterns related to **Gross Revenue**, **Release Years**, and **Directors' performance**.

---

## 🎯 Objectives
- Clean and preprocess the raw IMDb dataset.  
- Analyze movie performance across different years.  
- Identify the most successful directors by total box office revenue.  
- Examine relationships between IMDb ratings and financial success.  
- Visualize findings using informative plots.

---

## 🧰 Technologies & Libraries Used
| Library | Purpose |
|----------|----------|
| **Pandas** | Data loading, cleaning, manipulation, and aggregation |
| **NumPy** | Efficient numerical and array-based computations |
| **Matplotlib** | Creating clean, informative, and customizable visualizations |

---

## ⚙️ Installation & Setup

### Step 1: Install Required Libraries
Make sure Python (>=3.8) is installed, then run the following command in your terminal:

```bash
pip install pandas numpy matplotlib
```

### Step 2: Folder Structure
The following files must exist in the same directory:

| File Name | Description |
|------------|-------------|
| `top_movies.csv` | Raw dataset containing IMDb Top 1000 movie details |
| `movie_analysis.py` | Main Python script containing data analysis and visualization logic |

### Step 3: Run the Script
In your terminal, navigate to the project directory and execute:

```bash
python movie_analysis.py
```

---

## 📊 Key Analysis & Visualizations

After executing the script, four main visualizations are generated:

### 1️⃣ Top 10 Highest Grossing Movies (Bar Chart)
**Purpose:**  
Highlights the movies with the highest box office revenue.

**Insight:**  
Helps identify which films dominate global earnings and their corresponding IMDb scores.

---

### 2️⃣ Director's Total Gross vs. Average IMDb Rating (Scatter Plot)
**Purpose:**  
Compares each director’s total revenue with the average IMDb rating of their movies.  
The **bubble size** represents the number of movies directed.

**Insight:**  
Reveals whether critical acclaim (ratings) aligns with commercial success (revenue).

---

### 3️⃣ Average Movie Gross Revenue Trend Over the Years (Line Plot)
**Purpose:**  
Shows how the average gross revenue of top movies has changed over time.

**Insight:**  
Demonstrates industry growth, the effect of inflation, and evolving audience preferences.

---

### 4️⃣ Top 5 Directors by Total Gross Revenue (Bar Chart)
**Purpose:**  
Ranks the top five directors with the highest cumulative gross revenue.

**Insight:**  
Highlights the most financially successful directors in the dataset.

---

## 🧹 Data Cleaning & Preparation
Key data preprocessing steps included:
1. Handling missing or null values.  
2. Converting financial figures (Gross Revenue) into consistent numeric formats.  
3. Extracting relevant features such as release year, director, and IMDb rating.  
4. Grouping and aggregating data for comparative analysis.  

---

## 🧠 Insights & Findings
- Some directors consistently produce high-grossing films across multiple decades.  
- IMDb ratings do not always correlate strongly with box office success.  
- There is a noticeable rise in gross revenues over time, reflecting inflation and global box office expansion.  
- Certain genres and production studios dominate specific periods in cinema history.

---

## 🚀 Future Enhancements
- Add **genre-based** and **country-based** revenue analysis.  
- Use **Seaborn** or **Plotly** for interactive and more advanced visualizations.  
- Integrate **regression models** to predict box office success based on movie attributes.  
- Perform **sentiment analysis** on movie descriptions or reviews.  

---

## 🧩 Project Benefits
This project serves as a great beginner-friendly EDA case study to:
- Learn how to work with large datasets.  
- Apply real-world data cleaning techniques.  
- Build meaningful data visualizations and interpret them effectively.  

---

## 👨‍💻 Authors
- **Sankalp Satpathi**  
- **Lakshya Agrawal**  
- **Aditya Sarkar**  

**Tools Used:** Python, Pandas, NumPy, Matplotlib  
**Dataset:** IMDb Top 1000 Movies  
**License:** MIT  

---

⭐ *If you found this project helpful, consider giving it a star on GitHub!*  
