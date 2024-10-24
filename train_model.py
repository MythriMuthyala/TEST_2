import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load dataset
data = pd.read_csv('heart.csv')  # Update the filename if necessary

# Prepare feature and target variables
X = data.drop(columns='target')  # Features (drop the target column)
y = data['target']  # Target variable (heart disease or not)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"Classification Report:\n {classification_report(y_test, y_pred)}")

# Save the model
joblib.dump(model, 'heart_disease_model.pkl')

print("Model saved as 'heart_disease_model.pkl'")