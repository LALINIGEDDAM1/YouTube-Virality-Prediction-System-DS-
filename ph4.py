import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

print("="*60)
print("PHASE 4 : TEXT & SENTIMENT ANALYSIS")
print("="*60)

# Load cleaned data
df = pd.read_csv(r"C:\Projects\Youtube_trending(Datascience)\clean_youtube.csv")

# Title Length
df["title_length"] = df["title"].apply(len)

# Capital letters count
df["capital_count"] = df["title"].apply(lambda x: sum(1 for c in x if c.isupper()))

# Sentiment Score
df["sentiment"] = df["title"].apply(lambda x: TextBlob(x).sentiment.polarity)

# Plot Title Length
plt.figure()
plt.hist(df["title_length"], bins=40)
plt.title("Title Length Distribution")
plt.show()

# Plot Sentiment
plt.figure()
plt.hist(df["sentiment"], bins=40)
plt.title("Title Sentiment Distribution")
plt.show()

# Save enriched dataset
df.to_csv(r"C:\Projects\Youtube_trending(Datascience)\final_dataset.csv", index=False)

print("final_dataset.csv created")
print("PHASE 4 COMPLETED")
