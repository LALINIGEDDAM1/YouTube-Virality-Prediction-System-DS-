import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("="*60)
print("PHASE 8 : DATA VISUALIZATION DASHBOARD")
print("="*60)

# Load dataset
df = pd.read_csv(r"C:\Projects\Youtube_trending(Datascience)\final_dataset.csv")

# Recreate columns if needed
df["engagement_rate"] = (df["likes"] + df["comment_count"]) / df["views"]
df["viral"] = (df["views"] > df["views"].median()).astype(int)

sns.set_style("whitegrid")

# 1 Views Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["views"], bins=50)
plt.title("Views Distribution")
plt.show()

# 2 Likes vs Views
plt.figure(figsize=(8,5))
sns.scatterplot(x=df["views"], y=df["likes"])
plt.title("Likes vs Views")
plt.show()

# 3 Engagement Rate Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["engagement_rate"], bins=50)
plt.title("Engagement Rate Distribution")
plt.show()

# 4 Viral Count
plt.figure(figsize=(6,4))
sns.countplot(x=df["viral"])
plt.title("Viral vs Non-Viral Videos")
plt.xticks([0,1],["Non Viral","Viral"])
plt.show()

# 5 Top Categories
top_cat = df.groupby("category_id")["views"].mean().sort_values(ascending=False)[:10]

plt.figure(figsize=(8,5))
top_cat.plot(kind="bar")
plt.title("Top 10 Categories By Average Views")
plt.show()

print("\nPHASE 8 COMPLETED SUCCESSFULLY")
