print("Starting KITSUNE training...")
import pandas as pd
import joblib
import os
import sys

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Allow Python to find the src folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.url_features import analyze_url

# Load the dataset
dataset = pd.read_csv("datasets/PhiUSIIL_Phishing_URL_Dataset.csv")

print("Dataset loaded successfully!")
print("Total URLs:", len(dataset))
# Extract features from each URL
feature_list = []

print("\nExtracting URL features...")

for index, row in dataset.iterrows():

    features = analyze_url(row["URL"])

    feature_list.append(features)

    # Progress update every 5000 URLs
    if (index + 1) % 5000 == 0:
        print(f"Processed {index + 1} URLs")

print("\nFeature extraction complete!")

# Convert extracted features into a DataFrame
X = pd.DataFrame(feature_list)

# Convert True/False values to 1/0
X = X.replace({True: 1, False: 0})

# Labels (Safe = 0, Phishing = 1)
y = dataset["label"]
print(y.value_counts())

print("\nSample labels:")
print(dataset[["URL", "label"]].head(20))

print("\nTraining data created!")
print("Features shape:", X.shape)
print("Labels shape:", y.shape)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nDataset split complete!")
print("Training samples:", len(X_train))
print("Testing samples :", len(X_test))

# Create the AI model
model = RandomForestClassifier(random_state=42)

print("\nTraining KITSUNE AI...")

# Train the model
model.fit(X_train, y_train)

print("Training complete!")

# Make predictions
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"\nModel Accuracy: {accuracy:.4f}")

# Save the trained model
joblib.dump(model, "models/kitsune_model.pkl")

print("\nKITSUNE AI model saved successfully!")
print("\n========== MODEL TEST ==========")

test_urls = [
    "https://www.google.com",
    "http://google.com@evil-site.com/login",
    "http://192.168.1.10/login",
    "http://paypal-secure-login-update.com/login.php?id=12345"
]

for url in test_urls:
    features = analyze_url(url)

    import pandas as pd
    X_test_url = pd.DataFrame([features])

    # Convert booleans to integers
    for column in X_test_url.columns:
        if X_test_url[column].dtype == bool:
            X_test_url[column] = X_test_url[column].astype(int)

    prediction = model.predict(X_test_url)[0]
    probability = model.predict_proba(X_test_url)[0]

    print("\nURL:", url)
    print("Prediction:", prediction)
    print("Probability:", probability)