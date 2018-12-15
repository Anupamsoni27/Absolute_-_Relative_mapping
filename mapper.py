from builtins import type, print, complex
import pandas as pd
from datetime import datetime, timedelta
from pandas import ExcelWriter
# from zope.interface.ro import ro
import datetime
# current_datetime = datetime.now().date().strftime('%Y-%m-%d')
# current_datetime = "29-12-2015"
# FMT = '%d-%m-%Y'
# current_datetime = datetime.datetime.strptime(current_datetime, FMT)
# from sympy import primenu


# model_list = list(model_list)
# model_list = model_list.sort()
# print(model_list)
global obeservation_list
obeservation_list = []
class main():
    def __init__(self, name):
        self.name = name

    def method2(self, temp_date, temp_model, temp_relative_model_code):
        df2 = pd.read_excel(
            r"C:\Users\anupam.soni\PycharmProjects\Absolute_&_Relative_mapping\ALI_DHUB1_2.xlsx",
            sheet_name='data', index_col=None, header=[0])
        rel_model_list = df2.columns
        for t_model in rel_model_list:

            if "Date" not in t_model and str(t_model.split("/")[-3]).split(".")[-1] == temp_relative_model_code:
                df3 = df2[[df2.columns[0], temp_model, t_model]]
                df3.columns.values[0] = "Date"
                df3 = df3[df3["Date"] == temp_date]

                df3["observation_list"]= list(df3[temp_model] == df3[t_model])

                observation_list = list(df3["observation_list"])
                for a in observation_list:
                    if "False" ==str(a):
                     absolute_value = float(df3.ix[1,temp_model])
                     relative_value = float(df3.ix[1, t_model])
                     # print( df3)
                     temp_row = temp_date.strftime('%d-%m-%Y'), temp_model, t_model, absolute_value,relative_value,bool(absolute_value== relative_value)
                     print(temp_row)
                     obeservation_list.append(temp_row)
    #             df3.to_csv("file"+str(temp_relative_model_code)+".csv")
    # df1 = df[df["Date"]== temp_date]

    def method_1(self, model, df):

        if "Date" not in model and len(str(model.split("/")[-3]).split(".")[-1]) > 4:
            if int(df.loc[:, model].sum()) > 0:
                small_df = df[[df.columns[0], model]]
                # print(small_df.head())
                for index, row in small_df.iterrows():
                    temp_value = row[1]

                    if int(temp_value) > 0:

                        contract = str(model.split("/")[-3]).split(".")[-1]
                        if "M" in contract:
                            contract_year = contract.split("M")[0]
                            contract_period = contract.split("M")[1]
                        elif "Q" in contract:
                            contract_year = contract.split("Q")[0]
                            contract_period = contract.split("Q")[1]
                        elif "Y" in contract:
                            contract_year = contract.split("Y")[0]

                        temp_date = row[0]
                        temp_model = model
                        #                       print(type(temp_date))
                        temp_date = str(temp_date).split(" ")[0]
                        FMT = '%Y-%m-%d'
                        temp_date = datetime.datetime.strptime(temp_date, FMT)
                        #                       print(type(temp_date))

                        temp_date_year = str(temp_date)
                        temp_date_year = str(temp_date_year.split(" ")[0]).split("-")[0]
                        temp_date_month = str(str(temp_date).split(" ")).split("-")[1]
                        # print(contract_year,temp_date_year)
                        if int(contract_year) - int(temp_date_year) == 0:

                            temp_relative_model_code = int(contract_period) - int(temp_date_month)

                            # print(model, index)
                            # print(int(contract_period), int(temp_date_month))

                            if len(str(temp_relative_model_code)) == 1:
                                temp_relative_model_code = "M0" + str(temp_relative_model_code)
                            elif len(str(temp_relative_model_code)) == 2:
                                temp_relative_model_code = "M" + str(temp_relative_model_code)

                            # print(temp_relative_model_code)
                        elif int(contract_year) - int(temp_date_year) > 0:
                            contract_period = int(contract_period) + 12

                            temp_relative_model_code = int(contract_period) - int(temp_date_month)

                            if len(str(temp_relative_model_code)) == 1:
                                temp_relative_model_code = "M0" + str(temp_relative_model_code)
                            elif len(str(temp_relative_model_code)) == 2:
                                temp_relative_model_code = "M" + str(temp_relative_model_code)
                            # print(model, index)
                            # print(int(contract_period), int(temp_date_month))
                            # print(temp_relative_model_code)

                        dbObj.method2(temp_date, temp_model, temp_relative_model_code)


dbObj = main("Connect MS SQL")
global df
xl = pd.ExcelFile(r"C:\Users\anupam.soni\PycharmProjects\Absolute_&_Relative_mapping\ALI_DHUB1_2.xlsx")

print(xl.sheet_names)
df_rollover = pd.read_excel(r"C:\Users\anupam.soni\PycharmProjects\Absolute_&_Relative_mapping\ALI_DHUB1_2.xlsx",
                   sheet_name=xl.sheet_names[1], index_col=None, header=[0])

df = pd.read_excel(r"C:\Users\anupam.soni\PycharmProjects\Absolute_&_Relative_mapping\ALI_DHUB1_2.xlsx",
                   sheet_name=xl.sheet_names[0], index_col=None, header=[0])
df.columns.values[0] = "Date"
global model_list
model_list = df.columns
for model in model_list:
    if "Date" not in model and len(str(model.split("/")[-3]).split(".")[-1]) > 4:
        dbObj.method_1(model, df)
obeservation_df = pd.DataFrame(obeservation_list, columns=["Date Index", "Absolute Model Code", "Relative model Code", "Absolute Value", "Relative Value", "Observation"])
obeservation_df.to_csv("obeservation_file.csv",index=False)
writer = ExcelWriter('output.xlsx')
df.to_excel(writer, 'Data Checked', index=False)
df_rollover.to_excel(writer, 'Sheet2', index=False)
obeservation_df.to_excel(writer, 'Validation Report', index=False)

writer.save()

