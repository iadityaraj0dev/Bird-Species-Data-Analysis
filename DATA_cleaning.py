import pandas as pd
from final_df import final_df

#Drop columns 
final_df.drop(["AcceptedTSN","NPSTaxonCode","TaxonCode"], axis=1, inplace=True)
final_df.drop("Sub_Unit_Code", axis=1,inplace=True)

#Handle missing values
# Fill categorical columns
cat_cols = ["Sex", "Distance", "ID_Method", "Site_Name"]
for col in cat_cols:
    final_df[col] = final_df[col].fillna("Unknown")
final_df["Previously_Obs"]=final_df["Previously_Obs"].fillna(False).astype(bool)

#Fix datatype
final_df["Start_Time"] = pd.to_datetime(final_df["Start_Time"], format="%H:%M:%S")
final_df["End_Time"] = pd.to_datetime(final_df["End_Time"],format="%H:%M:%S")
final_df["Date"] = pd.to_datetime(final_df["Date"], errors="coerce")

# Fill numerical columns
num_cols = ["Temperature", "Humidity"]
for col in num_cols:
    final_df[col] = final_df[col].fillna(final_df[col].median())

# Clean time columns before conversion
final_df["Start_Time"] = final_df["Start_Time"].astype(str).str.strip()
final_df["End_Time"] = final_df["End_Time"].astype(str).str.strip()

# Convert to datetime (keep datetime objects, not .dt.time, for proper arithmetic)
final_df["Start_Time"] = pd.to_datetime(final_df["Start_Time"], errors="coerce")
final_df["End_Time"] = pd.to_datetime(final_df["End_Time"], errors="coerce")

#Remove Duplicate
final_df = final_df.drop_duplicates().copy()

#Feature Engineering 
# Extract Month & Year
final_df["Year"] = final_df["Date"].dt.year
final_df["Month"] = final_df["Date"].dt.month

# Final Clean Dataset
# Save cleaned dataset
final_df.to_csv("cleaned_bird_data.csv", index=False)

print("Data Cleaning Completed")
# print(final_df.head())
# print(final_df.isnull().sum())
