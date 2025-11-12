import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- 1. CONFIGURATION (Updated for top_movies.csv) ---
FILE_PATH = 'top_movies.csv'
REVENUE_COL = 'Gross'
YEAR_COL = 'Released_Year'
GROUP_COL = 'Director' 
TITLE_COL = 'Series_Title'
# NOTE: 'Budget' column is missing, so 'Profit' calculation is removed.
# Analysis now focuses on Gross Revenue.

# --- 2. DATA LOADING & CLEANING ---

def load_and_clean_data(file_path):
    """Loads data, cleans Gross column, and prepares Year column."""
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"ERROR: File not found at path: {file_path}")
        return None

    print("\n--- Initial Data Info ---")
    df.info()

    # Cleaning Gross Column (Remove commas and convert to numeric)
    if REVENUE_COL in df.columns:
        df[REVENUE_COL] = pd.to_numeric(
            df[REVENUE_COL].astype(str).str.replace('[,]', '', regex=True),
            errors='coerce'
        )
    else:
        print(f"ERROR: Column '{REVENUE_COL}' not found.")
        return None

    # Prepare Year Column (Already present, just ensure it's numeric)
    if YEAR_COL in df.columns:
        df[YEAR_COL] = pd.to_numeric(df[YEAR_COL], errors='coerce')
    else:
        print(f"ERROR: Column '{YEAR_COL}' not found.")
        return None

    # Drop rows with critical missing values (Revenue and Year)
    df.dropna(subset=[REVENUE_COL, YEAR_COL], inplace=True)
    
    print("\n--- Data Cleaning Complete ---")
    print(df[[TITLE_COL, REVENUE_COL, YEAR_COL]].head())
    
    return df

# --- 3. VISUALIZATION FUNCTIONS (Focus changed to Gross Revenue) ---

def plot_top_grossing_movies(df_cleaned):
    """Generates Horizontal Bar Chart for Top 10 Grossing Movies."""
    print("\n--- Generating Top 10 Gross Revenue Chart ---")
    top_10 = df_cleaned.sort_values(REVENUE_COL, ascending=False).head(10)

    plt.figure(figsize=(12, 7))
    plt.barh(
        top_10[TITLE_COL],
        top_10[REVENUE_COL] / 10**6, # Revenue in Millions
        color='teal'
    )
    plt.title('Top 10 Highest Grossing Movies (IMDb List)', fontsize=16)
    plt.xlabel('Gross Revenue (in Million USD)', fontsize=12)
    plt.gca().invert_yaxis()
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    plt.show()

def plot_director_gross_vs_year(df_cleaned):
    """Generates Scatter Plot for Director's Average Gross vs. Year."""
    print("\n--- Generating Director Gross Scatter Plot ---")
    # For a scatter plot using available data, let's look at a director's gross vs IMDB rating
    
    df_plot = df_cleaned.copy()
    # Group by Director and calculate their total gross and average rating
    director_stats = df_plot.groupby(GROUP_COL).agg(
        Total_Gross=(REVENUE_COL, 'sum'),
        Avg_Rating=('IMDB_Rating', 'mean'),
        Movie_Count=(TITLE_COL, 'count')
    )
    
    # Filter out directors with less than 2 movies for cleaner data
    director_stats = director_stats[director_stats['Movie_Count'] >= 2]
    
    plt.figure(figsize=(10, 6))
    plt.scatter(
        director_stats['Avg_Rating'],  # X-axis: Average Rating
        director_stats['Total_Gross'] / 10**6,  # Y-axis: Total Gross in Millions
        s=director_stats['Movie_Count'] * 50, # Marker size proportional to movie count
        alpha=0.6,
        color='darkorange'
    )
    plt.title("Director's Total Gross vs. Average IMDB Rating (Bubble Size = Movie Count)", fontsize=12)
    plt.xlabel('Average IMDB Rating', fontsize=12)
    plt.ylabel('Total Gross (in Million USD)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

def plot_yearly_revenue_trend(df_cleaned):
    """Generates Line Plot for Average Revenue Trend Over Years."""
    print("\n--- Generating Yearly Revenue Trend Chart ---")
    yearly_trend = df_cleaned.groupby(YEAR_COL)[REVENUE_COL].mean()

    plt.figure(figsize=(12, 6))
    plt.plot(
        yearly_trend.index,
        yearly_trend.values / 10**6, # Average Revenue in Millions
        marker='o',
        linestyle='-',
        color='blue'
    )
    plt.title('Average Movie Gross Revenue Trend Over Years', fontsize=16)
    plt.xlabel('Release Year', fontsize=12)
    plt.ylabel('Average Revenue (in Million USD)', fontsize=12)
    plt.grid(axis='y', linestyle=':', alpha=0.7)
    plt.xticks(rotation=45)
    plt.show()

def plot_top_directors(df_cleaned):
    """Generates Bar Chart for Top 5 Directors by Total Gross Revenue."""
    print("\n--- Generating Top Director Gross Chart ---")
    
    director_gross = df_cleaned.groupby(GROUP_COL)[REVENUE_COL].sum()
    top_5_directors = director_gross.nlargest(5)

    plt.figure(figsize=(10, 6))
    plt.bar(
        top_5_directors.index,
        top_5_directors.values / 10**9, # Total Gross in Billions
        color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    )
    plt.title('Top 5 Directors by Total Gross Revenue', fontsize=16)
    plt.xlabel('Director', fontsize=12)
    plt.ylabel('Total Gross Revenue (in Billions USD)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.show()

# --- 4. MAIN EXECUTION ---

if __name__ == "__main__":
    
    # 1. Load and Clean Data
    movie_df = load_and_clean_data(FILE_PATH)
    
    if movie_df is not None:
        # 2. Run All Visualizations
        plot_top_grossing_movies(movie_df)
        plot_director_gross_vs_year(movie_df)
        plot_yearly_revenue_trend(movie_df)
        plot_top_directors(movie_df)
    
    print("\n--- Analysis Complete ---")