# Naive Bayes Project - Weather Prediction

# Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load Dataset
df = pd.read_csv("weather_prediction_dataset.csv")

# Display First 5 Records
print("Dataset Preview:\n")
print(df.head())

# Features (Independent Variables) and Target (Dependent Variable)
X = df.drop("RainTomorrow", axis=1)
y = df["RainTomorrow"]

# Split Dataset into Training and Testing Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and Train Naive Bayes Model
model = GaussianNB()
model.fit(X_train, y_train)

# Predict on Test Data
y_pred = model.predict(X_test)

# Model Evaluation
print("\nAccuracy Score:", accuracy_score(y_test, y_pred))

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

# -----------------------------------------
# Predict New Weather Data
# -----------------------------------------

# Sample Input:
# Temperature = 25°C
# Humidity = 60%
# WindSpeed = 24 km/h
# Pressure = 991 hPa

sample = pd.DataFrame(
    [[25, 60, 24, 991]],
    columns=X.columns
)

# Make Prediction
prediction = model.predict(sample)

# Display Result
if prediction[0] == 1:
    print("\nPrediction: Rain Expected Tomorrow")
else:
    print("\nPrediction: No Rain Tomorrow")