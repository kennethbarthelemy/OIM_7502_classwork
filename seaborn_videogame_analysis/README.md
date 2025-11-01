# Seaborn Video Game Sales Analysis  

This project explores and visualizes a Kaggle dataset of **video game sales and ratings** using **Seaborn** and **Matplotlib**.  
The goal is to demonstrate the power of Seaborn for statistical data visualization through structured, section-by-section analysis.

---

## Project Overview  

**Objective:**  
To analyze global video game data and highlight insights about platform performance, publisher output, and score relationships while comparing Seaborn’s simplicity to traditional Matplotlib.

**Tools & Libraries Used:**  
- Python  
- Pandas  
- Seaborn  
- Matplotlib  
- Jupyter Notebook  

**Dataset:**  
`game_sales_data.csv` (Kaggle — *Video Game Sales Data*)  
Contains information on game title, platform, publisher, critic scores, user scores, total shipments, and year of release.

---

## Analysis Sections  

### **Section 1: Dataset Overview**  
- Loaded and inspected the dataset structure (`df.info()` and `df.head()`).
- Identified missing values in critic and user scores.  
- Justified using ~2000 valid score rows for meaningful visualizations.

### **Section 2: Platform & Publisher Insights**  
- **Top Platforms by Count** → Countplot showing which platforms host the most games.  
- **Top Platforms by Shipments** → Barplot visualizing total copies sold per platform.  
- **Games Released Over Time (Top 10 Platforms)** →  
  A stacked histogram using Seaborn’s `displot`, showing clearer year-to-platform trends compared to the cluttered Matplotlib version.  
  - Demonstrates how Seaborn simplifies multi-category plots.  
- **Top Publishers by Game Count** → Identified publishers with the largest number of released games.

### **Section 3: Score Insights & Correlations**  
- **Distribution of Critic Scores** → Histogram + KDE curve visualizing score concentration.  
- **User vs. Critic Score Comparison** → Boxplot comparing variability between the two.
- Highlighted **Top 10 Best-Selling Games** and overlaid their **User Scores** as data labels.  


### **Section 4: Correlations, Conclusion and Example **   
- **Correlation Heatmap** → Showed relationships among `Critic_Score`, `User_Score`, `Total_Shipped`, and `Year`.  
- **Score vs. Sales Relationship** → Scatterplot indicating weak correlation between ratings and copies shipped.
- Call of Duty game examples
- Conclusiom

---

## Key Learnings  

- **Seaborn simplifies** most complex visualizations that would require many lines in Matplotlib.  
- The library provides **automatic styling, palettes, and statistical context**.  
- Combining Seaborn + Matplotlib is useful for custom titles, legends, or annotations — but for many tasks, **Seaborn alone is cleaner and faster**.  
- Demonstrated how Seaborn’s `displot`, `barplot`, and `heatmap` functions streamline multi-variable and correlation visualizations.

---

## Example Visuals  

- `Top 10 Platforms by Total Shipments` (Barplot)  
- `Games Released Over Time (Top 10 Platforms)` (Stacked Histogram)  
- `User Score Distribution by Platform` (Boxplot)  
- `Correlation Heatmap` (Critic vs. User Scores vs. Shipments)  
- `Top 10 Games by Units Shipped with User Scores` (Barplot with labels)

---

## Author  

**Kenneth Barthelemy**  
MBA Candidate, Babson College  
*Course: Advanced Programming (OIM-7502)*  
*Instructor: Prof. Matt Macarty*  

## Folder Structure  
seaborn_videogame_analysis/
seaborn_videogameanalysis_kenneth.ipynb   # Jupyter Notebook
game_sales_data.csv                        # Dataset (from Kaggle)
README.md                                  # This documentation

---

### How to View
You can explore the analysis by opening the Jupyter Notebook in this folder or previewing it on GitHub.  
Each section contains annotated code cells and graph explanations highlighting how Seaborn enhances data visualization.
