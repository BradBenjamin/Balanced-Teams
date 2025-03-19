import pandas as pd

# Read the Excel file into a pandas DataFrame
df = pd.read_excel("Echipe.xlsx")

# Sort the DataFrame by gender, age, and height
df.sort_values(by=["Gender", "Age", "Height"], inplace=True)  # Adjust column names as per your Excel file

# Calculate the number of boys and girls
num_boys = df[df["Gender"] == "Boy"].shape[0]  # Adjust column name for gender
num_girls = df[df["Gender"] == "Girl"].shape[0]  # Adjust column name for gender

# Calculate the number of boys and girls per team
boys_per_team = num_boys // 4
girls_per_team = num_girls // 4

# Assign team numbers
num_children = df.shape[0]
df["Team"] = (df.reset_index().index // (num_children // 4)) + 1

print(df.head())
# Write the updated DataFrame back to an Excel file
df.to_excel("team_assignments.xlsx")