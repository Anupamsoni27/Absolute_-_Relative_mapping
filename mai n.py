from builtins import type, print

import pandas as pd


from datetime import datetime, timedelta
from pandas import ExcelWriter
# from zope.interface.ro import ro
import datetime
# current_datetime = datetime.now().date().strftime('%Y-%m-%d')
current_datetime = "01-06-2018"
FMT = '%d-%m-%Y'
current_datetime = datetime.datetime.strptime(current_datetime, FMT)
df = pd.read_excel(r"C:\Users\anupam.soni\PycharmProjects\Absolute_&_Relative_mapping\ALI_DHUB1.xlsx",sheet_name='rollover',index_col=None,header=[0])
print(current_datetime)
# print(df)
df = df.sort_values(df.columns[0])
list1 = list(df.columns[1])
rollover_range = len(list1)
# print(df)
for index, row in df.iterrows():
    temp_date = row[1]
    FMT = '%d-%m-%Y'
    temp_date = str(temp_date)
    temp_date = datetime.datetime.strptime(temp_date, FMT)
    import datetime

    if temp_date > current_datetime:
        print(temp_date)
        current_period_month = temp_date
        current_period_code = row[0]
        FMT = '%d-%m-%Y'
        from datetime import datetime, time, timedelta

        current_year = current_datetime.year
        current_month = current_datetime.month

        rollover_year  = temp_date.year
        rollover_month = temp_date.month

        year_diff = rollover_year - current_year
        month_diff = rollover_month - rollover_month

        print(year_diff, month_diff)
        shift = year_diff * 12 + month_diff
        global period_list
        period_list = []
        global period_df
        if shift == 0:


            for x in range(0,rollover_range):

                if len(str(x)) == 1:
                    temp_period = "M0" + str(x)
                elif len(str(x)) == 2 :
                    temp_period = "M" + str(x)
                period_list.append(temp_period)

            period_df = pd.DataFrame(period_list,columns=["Relative_code"])
            df["Relative_code"] = period_df
            print(df)
            df.to_csv("output.csv",index= False)
            relPeriod = "M0"
        elif shift > 0:


            for x in range(1, rollover_range+1):

                if len(str(x)) == 1:
                    temp_period = "M0" + str(x)
                elif len(str(x)) == 2:
                    temp_period = "M" + str(x)
                period_list.append(temp_period)

            period_df = pd.DataFrame(period_list, columns=["Relative_code"])
            df["Relative_code"] = period_df
            print(df)
            df.to_csv("output.csv", index=False)
            relPeriod = "M0"

        # tdelta = datetime.strptime(temp_date, FMT) - datetime.strptime(current_datetime, FMT)
        # print((tdelta))
    try:
     print(current_period_month, current_period_code)
     # delta = temp_date - current_datetime
     # print(delta)
     # current_period_code = row[0]
     # print(current_period_code)
     break
    except:
        pass
