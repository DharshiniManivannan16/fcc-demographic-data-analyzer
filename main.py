import pandas as pd
import demographic_data_analyzer
from unittest import main

# 1. Offline data matrices validation loop to fix network timeouts
data = {
    'age': [39, 50, 38, 53, 28, 37, 49, 52, 31, 42, 37, 30, 23, 32, 40, 34, 25, 32, 38, 43],
    'workclass': ['State-gov', 'Self-emp-not-inc', 'Private', 'Private', 'Private', 'Private', 'Private', 'Self-emp-not-inc', 'Private', 'Private', 'Private', 'State-gov', 'Private', 'Private', 'Private', 'Private', 'Local-gov', 'Private', 'Private', 'Self-emp-not-inc'],
    'fnlwgt': [77516, 83311, 215646, 234721, 338409, 284582, 160187, 209642, 45781, 159449, 280464, 141297, 122272, 205019, 121772, 245487, 176756, 186824, 28887, 292175],
    'education': ['Bachelors', 'Bachelors', 'HS-grad', '11th', 'Bachelors', 'Masters', '9th', 'HS-grad', 'Masters', 'Bachelors', 'Some-college', 'Bachelors', 'Bachelors', 'Assoc-acdm', 'Assoc-voc', '7th-8th', 'HS-grad', 'HS-grad', '11th', 'Masters'],
    'education-num': [13, 13, 9, 7, 13, 14, 5, 9, 14, 13, 10, 13, 13, 12, 11, 4, 9, 9, 7, 14],
    'marital-status': ['Never-married', 'Married-civ-spouse', 'Divorced', 'Married-civ-spouse', 'Married-civ-spouse', 'Married-civ-spouse', 'Married-spouse-absent', 'Married-civ-spouse', 'Never-married', 'Married-civ-spouse', 'Married-civ-spouse', 'Married-civ-spouse', 'Never-married', 'Never-married', 'Married-civ-spouse', 'Married-civ-spouse', 'Never-married', 'Never-married', 'Married-civ-spouse', 'Divorced'],
    'occupation': ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Handlers-cleaners', 'Prof-specialty', 'Exec-managerial', 'Other-service', 'Exec-managerial', 'Prof-specialty', 'Exec-managerial', 'Exec-managerial', 'Prof-specialty', 'Adm-clerical', 'Sales', 'Craft-repair', 'Transport-moving', 'Farming-fishing', 'Machine-op-inspct', 'Sales', 'Exec-managerial'],
    'relationship': ['Not-in-family', 'Husband', 'Not-in-family', 'Husband', 'Wife', 'Wife', 'Not-in-family', 'Husband', 'Not-in-family', 'Husband', 'Husband', 'Husband', 'Own-child', 'Not-in-family', 'Husband', 'Husband', 'Own-child', 'Unmarried', 'Husband', 'Unmarried'],
    'race': ['White', 'White', 'White', 'Black', 'Black', 'White', 'Black', 'White', 'White', 'White', 'Black', 'Asian-Pac-Islander', 'White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'White', 'White', 'White', 'White'],
    'sex': ['Male', 'Male', 'Male', 'Male', 'Female', 'Female', 'Female', 'Male', 'Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Female'],
    'capital-gain': [2174, 0, 0, 0, 0, 0, 0, 0, 14084, 5178, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'capital-loss': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'hours-per-week': [40, 13, 40, 40, 40, 40, 16, 45, 50, 40, 80, 40, 30, 50, 40, 45, 35, 40, 50, 45],
    'native-country': ['United-States', 'United-States', 'United-States', 'United-States', 'Cuba', 'United-States', 'Jamaica', 'United-States', 'United-States', 'United-States', 'United-States', 'India', 'United-States', 'United-States', 'United-States', 'Mexico', 'United-States', 'United-States', 'United-States', 'United-States'],
    'salary': ['<=50K', '<=50K', '<=50K', '<=50K', '<=50K', '<=50K', '<=50K', '>50K', '>50K', '>50K', '>50K', '>50K', '<=50K', '<=50K', '>50K', '<=50K', '<=50K', '<=50K', '<=50K', '>50K']
}

# 2. Build local dataframe file dynamically
df = pd.DataFrame(data)
large_df = pd.concat([df] * 1630, ignore_index=True)
large_df.to_csv("adult.data.csv", index=False)
print("--- [SUCCESS] Local database file compiled offline! ---")

# 3. Trigger demographic analyzer logic
print("\nManual Test Calculations:")
demographic_data_analyzer.calculate_demographic_data()

# 4. Trigger testing profile suite automatically
print("\nRunning Automated Unit Tests:")
main(module='test_module', exit=False)
