import pandas as pd

# Load the dataset
df = pd.read_csv('/Users/alenm/Downloads/marketing_campaign.csv', sep='\t')
# 1. Handle missing values (e.g., 'Income')
df['Income'] = df['Income'].fillna(df['Income'].median())

# 2. Remove duplicate rows
df.drop_duplicates(inplace=True)

# 3. Standardize text values
df['Education'] = df['Education'].replace({
    '2n Cycle': '2nd Cycle', 'Basic': 'Basic',
    'Graduation': 'Graduation', 'Master': 'Master', 'PhD': 'PhD'
})

df['Marital_Status'] = df['Marital_Status'].replace({
    'Single': 'Single', 'Together': 'Together', 'Married': 'Married',
    'Divorced': 'Divorced', 'Widow': 'Widow',
    'Alone': 'Alone', 'Absurd': 'Absurd', 'YOLO': 'YOLO'
})

# 4. Convert 'Dt_Customer' to datetime format
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y', errors='coerce')

# 5. Rename column headers (lowercase and underscores)
df.columns = [col.lower().replace(' ', '_') for col in df.columns]

# 6. Fix data types
df['year_birth'] = pd.to_numeric(df['year_birth'], errors='coerce').astype('Int64')
df['income'] = pd.to_numeric(df['income'], errors='coerce')

# Optional: Check final structure
print(df.dtypes)
print(df.head())
