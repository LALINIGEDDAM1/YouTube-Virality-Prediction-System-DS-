import joblib
import pandas as pd
import re

print("="*60)
print("PHASE 7 : USER INPUT VIRALITY PREDICTOR")
print("="*60)

# Load model
model = joblib.load("viral_model.pkl")

# User Inputs
views = int(input("Enter Expected Views: "))
likes = int(input("Enter Expected Likes: "))
dislikes = int(input("Enter Expected Dislikes: "))
comments = int(input("Enter Expected Comments: "))
title = input("Enter Video Title: ")

# Feature Engineering
title_length = len(title)
capital_count = len(re.findall(r'[A-Z]', title))
engagement_rate = (likes + comments) / views

sentiment = 0.5  # default neutral

input_df = pd.DataFrame([[views, likes, dislikes, comments,
                           title_length, capital_count,
                           sentiment, engagement_rate]],
                         columns=[
                             "views","likes","dislikes",
                             "comment_count","title_length",
                             "capital_count","sentiment",
                             "engagement_rate"
                         ])

# Prediction
prob = model.predict_proba(input_df)[0][1]

print("\nViral Probability Score:", round(prob*100,2), "%")

if prob > 0.7:
    print("Prediction: HIGHLY LIKELY TO GO VIRAL")
elif prob > 0.4:
    print("Prediction: MODERATE CHANCE")
else:
    print("Prediction: LOW CHANCE")

print("\nPHASE 7 COMPLETED SUCCESSFULLY")
