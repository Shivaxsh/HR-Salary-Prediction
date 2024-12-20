import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import compress_pickle

# Load cleaned dataset
data = pd.read_csv('hr_data_cleaned.csv')

# Define features and target
X = data[['Age', 'Years of Experience', 'Current Salary']]
y = data['Current Salary'] * 1.2  # Assuming a 20% salary hike when switching jobs

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Save the model using compress-pickle
compress_pickle.dump(model, 'salary_prediction_model.pkl')
print("Model saved as 'salary_prediction_model.pkl'.")
