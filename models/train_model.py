import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
dataset = pd.read_csv("datasets/PhiUSIIL_Phishing_URL_Dataset.csv")

# Separate features and labels
X = dataset.drop("label", axis=1)
y = dataset["label"]

# Keep only numeric columns
X = X.select_dtypes(include=["number"])

print(X.dtypes)

print("Features shape:", X.shape)
print("Labels shape:", y.shape)

print("\nFirst 5 labels:")
print(y.head())

# Split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining samples:", len(X_train))
print("Testing samples :", len(X_test))

# Create the AI model
model = RandomForestClassifier(random_state=42)

# Train the model
print("\nTraining the model...")
model.fit(X_train, y_train)

print("Training complete!")

# Make predictions
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", accuracy)
# Save the trained model
joblib.dump(model, "models/kitsune_model.pkl")

print("Model saved successfully!")