import pandas as pd

from openpyxl import load_workbook


sheet_list = load_workbook("template_upload.xlsx", read_only=True).sheetnames
print(sheet_list)

for sht in sheet_list:
    print(sht)
    df = pd.read_excel('template_upload.xlsx',sht)
    print(df)