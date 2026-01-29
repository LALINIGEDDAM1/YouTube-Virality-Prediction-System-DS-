import pandas as pd

print("="*60)
print("PHASE 2 : DATA CLEANING & STANDARDIZATION")
print("="*60)

# Load dataset
file_path = r"C:\Projects\Youtube_trending(Datascience)\youtube.csv"
df = pd.read_csv(file_path)

print("\nInitial Shape:", df.shape)

# 1. Drop useless index column
if "index" in df.columns:
    df.drop(columns=["index"], inplace=True)

# 2. Rename columns to standard style
df.columns = df.columns.str.lower()

# 3. Convert dates
df["publish_date"] = pd.to_datetime(df["publish_date"], errors="coerce")
df["trending_date"] = pd.to_datetime(df["trending_date"], errors="coerce")

# 4. Remove rows with negative engagement
df = df[(df["views"] >= 0) &
        (df["likes"] >= 0) &
        (df["dislikes"] >= 0) &
        (df["comment_count"] >= 0)]

# 5. Remove videos that are removed or errored
df = df[df["video_error_or_removed"] == False]

# 6. Reset index
df.reset_index(drop=True, inplace=True)

print("After Cleaning Shape:", df.shape)

# 7. Save cleaned dataset
output_path = r"C:\Projects\Youtube_trending(Datascience)\clean_youtube.csv"
df.to_csv(output_path, index=False)

print("\nCleaned dataset saved as clean_youtube.csv")

print("\nPHASE 2 COMPLETED")
