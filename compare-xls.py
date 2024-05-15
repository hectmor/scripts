import pandas as pd

def compare_excel_sheets(file1, file2):
    sheets1_raw = pd.read_excel(file1, sheet_name=None)
    sheets2_raw = pd.read_excel(file2, sheet_name=None)

    sheets1 = {sheet_name: df.sort_values(by=df.columns[0])\
                for sheet_name, df in sheets1_raw.items()}
    sheets2 = {sheet_name: df.sort_values(by=df.columns[0])\
                for sheet_name, df in sheets2_raw.items()}
   
    if len(sheets1) != len(sheets2):
        print("The number of sheets in the two Excel files is different.")
        return

    for sheet_name in sheets1.keys():
        if sheet_name not in sheets2:
            print(f"Sheet '{sheet_name}' is missing in the second Excel file.")
            continue

        df1 = sheets1[sheet_name].reset_index(drop=True)
        df2 = sheets2[sheet_name].reset_index(drop=True)
        
        if not df1.equals(df2):
            print(f"Different sheet: {sheet_name}.")
        else:
            print(f"Non different sheet: {sheet_name}.")

if __name__ == "__main__":
    file1 = "file_1.xlsx"  
    file1 = "file_2.xlsx"  

    compare_excel_sheets(file1, file2)

