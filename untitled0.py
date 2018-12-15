from datetime import date
import pandas as pd

data = [['2017-11-06', 'ID1'],
        ['2017-11-07', 'ID1'],
        ['2017-11-08', 'ID2'],
        ['2017-11-10', 'ID3']]

df = pd.DataFrame(data, columns=['StartDate', 'Subject ID'])


writer = pd.ExcelWriter(r'C:\Anupam\summary.xls', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)

workbook = writer.book
worksheet = writer.sheets['Sheet1']

my_formats = {'"ID1"': '#FF0000',
              '"ID2"': '#00FF00',
              '"ID3"': '#0000FF'}

for val, color in my_formats.items():
    fmt = workbook.add_format({'font_color': color})
    worksheet.conditional_format('B2:B5', {'type': 'cell',
                                           'criteria': '=',
                                           'value': val,
                                           'format': fmt})
print(df)