import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

print("="*60)
print("PHASE 5 : VIRALITY PREDICTION MODEL")
print("="*60)

# Load dataset
df = pd.read_csv(r"C:\Projects\Youtube_trending(Datascience)\final_dataset.csv")

# Create Engagement Rate
df["engagement_rate"] = (df["likes"] + df["comment_count"]) / df["views"]

# Create Viral Label
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

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(n_estimators=150, random_state=42)
model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

# Evaluation
print("\nAccuracy:", accuracy_score(y_test, pred))
print("\nClassification Report:\n", classification_report(y_test, pred))

# Feature Importance
plt.figure()
plt.barh(features, model.feature_importances_)
plt.title("Feature Importance")
plt.show()

print("PHASE 5 COMPLETED SUCCESSFULLY")
