import pandas as pd

df = pd.read_excel("EMP_WORKINFO.xlsx")

print("-------------------------------------------------------------------------------")
WFH = df["29-08-2023"].value_counts()["WFH"]
print(f"Today no of people in Work from home: {WFH}")
WFO = df["29-08-2023"].value_counts()["WFO"]
print(f"Today no of people in Work from office: {WFO}")
print("-------------------------------------------------------------------------------")

WFH = ["25-08-2023", "26-08-2023", "27-08-2023", "28-08-2023", "29-08-2023"]
countWFH = 0
countWFO = 0
#l = []
for i in WFH:
    WFH = df[i].value_counts()["WFH"]
    WFO = df[i].value_counts()["WFO"]
    #l.append(WFH)
    countWFH += WFH
    countWFO += WFO
    print(f"For this DATE:{i} No of employess are in Work from home:   {WFH}")
    print(f"For this DATE:{i} No of employess are in Work from Office: {WFO}")
    print("-------------------------------------------------------------------------------")

print(f"Total employees from past 5 days took Work from home are:   {countWFH}")
print(f"Total employees from past 5 days took Work from Office are: {countWFO}")
print("-------------------------------------------------------------------------------")

date_columns = df.columns[:]  #dates
incomplete_ids = []
for index, row in df.iterrows():  #generates pair of index and row , row by row
    if any(pd.isnull(row[date_columns])):
        incomplete_ids.append(row['Emp ID'])
incomplete_ids = set(incomplete_ids)
print(f"employee WFHo has not filledthe data: {incomplete_ids}")
print("-------------------------------------------------------------------------------")
print(f"The total WFO and WFH : {WFH + WFO}")





