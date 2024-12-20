import pandas as pd

# Load dataset
data = pd.read_csv('hr_data.csv')

# Check for duplicates and remove them
data.drop_duplicates(inplace=True)

# Check for missing values
print("Missing values before cleaning:\n", data.isnull().sum())

# Handle missing values if any (for this synthetic data, it's unlikely to have missing values)
data.fillna(method='ffill', inplace=True)

# Save cleaned data
data.to_csv('hr_data_cleaned.csv', index=False)
print("Cleaned dataset saved as 'hr_data_cleaned.csv'.")

