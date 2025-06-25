# Data Cleaning on Marketing Campaign Dataset

## Objective:
To clean and preprocess the marketing_campaign.csv dataset by applying common data cleaning techniques such as handling missing values, removing duplicates, standardizing text fields, formatting dates, renaming columns, and fixing inconsistent data types. This ensures the dataset is ready for further analysis or modeling.

 ## Dataset Used:
Name: marketing_campaign.csv

## Tasks Performed:
### Handling Missing Values
Checked for missing data using .isnull().sum()

Focused on the Income column, where missing values were present

Imputed missing Income values using the median, as it is robust to outliers

### Removing Duplicates
Checked for duplicates using .duplicated()

Removed them using .drop_duplicates()

### Standardizing Text
Standardized categorical variables:

Education: Unified inconsistent labels like "2n Cycle" to "2nd Cycle"

Marital_Status: Mapped unusual labels ("YOLO", "Absurd", "Alone") consistently

Used .replace() with dictionary mapping for uniformity

### Converting Date Formats
Converted Dt_Customer from string ('%d-%m-%Y') to datetime64 using pd.to_datetime()

Handled errors with errors='coerce' to replace invalid formats with NaT

### Renaming Columns
Cleaned column headers to make them analysis-friendly:

Converted to lowercase

Replaced spaces with underscores

### Fixing Data Types
Ensured consistent and appropriate data types:

Year_Birth converted to integer

Income to float

Dt_Customer to datetime



## Result:
A fully cleaned dataset with:
- No missing values
- No duplicate records
- Uniform and standardized text entries
- Consistent date format
- Clean, readable column names
- Correct and consistent data types
