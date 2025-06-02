import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Ensure the models folder exists
os.makedirs("models", exist_ok=True)

# Load data
data = pd.read_csv("data/housing.csv")

# Features and target
X = data[['total_rooms']]  # Or whatever features you want
y = data['median_house_value']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

print("Model is created")

# Save model
with open("models/house_model.pkl", "wb") as f:
    pickle.dump(model, f)
