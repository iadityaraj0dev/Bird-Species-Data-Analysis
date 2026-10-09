import pandas as pd
#GRASSLAND
# Specify the file path
file_path = "Bird_Monitoring_Data_GRASSLAND.XLSX"

# Read the Excel file with multiple sheets
excel_data = pd.ExcelFile(file_path)

# Get all sheet names
sheet_names = excel_data.sheet_names

# Read data from all sheets into a dictionary
sheets_dict = {sheet: excel_data.parse(sheet) for sheet in sheet_names}

# Combine all sheets into a single DataFrame, filtering out completely empty sheets
grassland_combined_df = pd.concat(
    [
        df.assign(Sheet=sheet_name)
        for sheet_name, df in sheets_dict.items()
        if not df.dropna(how="all").empty
    ],
    ignore_index=True
)

#FOREST 
file_path = "Bird_Monitoring_Data_FOREST(1).XLSX"

# Read the Excel file with multiple sheets
excel_data = pd.ExcelFile(file_path)

# Get all sheet names
sheet_names = excel_data.sheet_names

# Read data from all sheets into a dictionary
sheets_dict = {sheet: excel_data.parse(sheet) for sheet in sheet_names}

# Combine all sheets into a single DataFrame, filtering out completely empty sheets
forest_combined_df = pd.concat(
    [
        df.assign(Sheet=sheet_name)
        for sheet_name, df in sheets_dict.items()
        if not df.dropna(how="all").empty
    ],
    ignore_index=True
)

#Final df 
final_df= pd.concat([grassland_combined_df,forest_combined_df])
if __name__ == "__main__":
 print(final_df.shape)
 print(final_df.isnull().sum())


