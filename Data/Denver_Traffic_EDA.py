import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

base_path = os.path.dirname(__file__)
project_root = os.path.join(base_path, "..")
data_path = os.path.join(project_root, "Assets", "Denver_Traffic_Accidents.csv")
df = pd.read_csv(data_path)

# Check prints
print(df.info(), "\n")
print(df.head(), "\n")

# Drop unnecessary columns
df = df.drop(columns=["incident_id", "offense_id", "offense_code_extension", "first_occurrence_date", "last_occurrence_date",
                  "geo_x", "geo_y", "precinct_id", "ROAD_DESCRIPTION", "ROAD_CONTOUR", "TU1_VEHICLE_MOVEMENT",
                  "TU2_VEHICLE_MOVEMENT", "FATALITY_MODE_1", "TU1_PEDESTRIAN_ACTION", "TU2_PEDESTRIAN_ACTION",
                  "FATALITY_MODE_2", "SERIOUSLY_INJURED_MODE_1", "SERIOUSLY_INJURED_MODE_2", "POINT_X", "POINT_Y",
                  "x", "y"], errors="ignore")
print(df.head())

# Missing values heatmap
fig, ax, = plt.subplots(figsize=(15, 8))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis', ax=ax)
ax.set_title("Missing Values Heatmap")
ax.set_xlabel("Columns")
ax.set_ylabel("Rows")
plt.show()

# Check for duplicate rows
print("Duplicates: \n")
print(df[df.duplicated()])

# Save to new file
clean_data_path = os.path.join(project_root, "Data", "Denver_Traffic_Clean.csv")
df.to_csv(clean_data_path, index=False)