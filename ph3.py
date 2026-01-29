import pandas as pd
import matplotlib.pyplot as plt

print("="*60)
print("PHASE 3 : EXPLORATORY DATA ANALYSIS")
print("="*60)

# Load cleaned data
df = pd.read_csv(r"C:\Projects\Youtube_trending(Datascience)\clean_youtube.csv")

# Create Engagement Rate
df["engagement_rate"] = (df["likes"] + df["comment_count"]) / df["views"]

# Top Categories
top_categories = df["category_id"].value_counts().head(10)

plt.figure()
top_categories.plot(kind="bar")
plt.title("Top 10 Trending Categories")
plt.xlabel("Category ID")
plt.ylabel("Video Count")
plt.show()

# Views Distribution
plt.figure()
plt.hist(df["views"], bins=50)
plt.title("Views Distribution")
plt.xlabel("Views")
plt.ylabel("Frequency")
plt.show()

# Engagement Rate Distribution
plt.figure()
plt.hist(df["engagement_rate"], bins=50)
plt.title("Engagement Rate Distribution")
plt.xlabel("Engagement Rate")
plt.ylabel("Frequency")
plt.show()

# Best Publishing Day
best_day = df["published_day_of_week"].value_counts()

plt.figure()
best_day.plot(kind="bar")
plt.title("Best Day To Publish")
plt.xlabel("Day")
plt.ylabel("Number of Videos")
plt.show()

print("\nPHASE 3 COMPLETED")
