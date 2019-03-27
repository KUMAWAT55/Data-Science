import pandas
import xlrd
#import os
#print(os.listdir("/home/rk/Desktop/Data Science/source"))
print("*************CSV**************")
df_csv=pandas.read_csv("/home/rk/Desktop/Data Science/source/supermarkets.csv")
print(df_csv)
print("*************JSON**************")
df_json=pandas.read_json("/home/rk/Desktop/Data Science/source/supermarkets.json")
print(df_json)
print("*************XLSX**************")
df_xlsx=pandas.read_excel("/home/rk/Desktop/Data Science/source/supermarkets.xlsx",sheet_name=0)
print(df_xlsx)
print("*************TEXT COMMA**************")
df_text_comma=pandas.read_csv("/home/rk/Desktop/Data Science/source/supermarkets-commas.txt")
print(df_text_comma)
print("*************TEXT SEMICOLON**************")
df_text_semi=pandas.read_csv("/home/rk/Desktop/Data Science/source/supermarkets-semi-colons.txt",sep=";")
print(df_text_semi)
print("*************NO HEADER TEXT**************")
df_text_comma_noheader=pandas.read_csv("/home/rk/Desktop/Data Science/source/supermarkets-commas_noheader.txt",header=None)
df_text_comma_noheader.columns=["ID","ADDRESS","CITY","STATE","COUNTRY","NAME","EMPLOYEES"]
print(df_text_comma_noheader)
df_text_comma_noheader.set_index("ID",inplace=True,drop=False)
df_text_comma_noheader.set_index("ADDRESS",inplace=True,drop=False)
print(df_text_comma_noheader)
