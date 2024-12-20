import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Define parameters
num_entries = 200000

def generate_data(num_entries):
    data = []
    for _ in range(num_entries):
        name = fake.name()
        age = random.randint(22, 60)  # Assuming HR professionals are between 22 and 60 years old
        experience = random.randint(0, age - 21)  # Experience starts at 0 years
        current_salary = random.randint(20000, 200000)  # Current salary in a reasonable range
        data.append([name, age, experience, current_salary])
    return data

# Generate dataset
data = generate_data(num_entries)
columns = ['Name', 'Age', 'Years of Experience', 'Current Salary']

# Save to CSV
dataset = pd.DataFrame(data, columns=columns)
dataset.to_csv('hr_data.csv', index=False)
print("Dataset generated and saved as 'hr_data.csv'.")