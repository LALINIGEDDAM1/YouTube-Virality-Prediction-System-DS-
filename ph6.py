import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

print("="*60)
print("PHASE 6 : VIRAL SCORE GENERATOR")
print("="*60)

# Load dataset
df = pd.read_csv(r"C:\Projects\Youtube_trending(Datascience)\final_dataset.csv")

# Recreate engagement rate
df["engagement_rate"] = (df["likes"] + df["comment_count"]) / df["views"]

# Viral label
df["viral"] = (df["views"] > df["views"].median()).astype(int)

features = [
    "views",
    "likes",
    "dislikes",
    "comment_count",
    "title_length",
    "capital_count",
    "sentiment",
    "engagement_rate"
]

X = df[features]
y = df["viral"]

# Train model
model = RandomForestClassifier(n_estimators=150, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "viral_model.pkl")
print("Model Saved Successfully")

# Predict probability
sample = X.sample(1)
prob = model.predict_proba(sample)[0][1]

print("\nSample Video Data:")
print(sample)

print(f"\nViral Probability Score: {round(prob*100,2)} %")

if prob > 0.7:
    print("Prediction: HIGHLY LIKELY TO GO VIRAL")
elif prob > 0.4:
    print("Prediction: MODERATE CHANCE")
else:
    print("Prediction: LOW CHANCE")

print("\nPHASE 6 COMPLETED SUCCESSFULLY")
