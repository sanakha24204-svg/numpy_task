import pandas as pd

data = pd.read_csv("C:/Users/Anakha/OneDrive/Desktop/EDA/pandas work/employee_works.py/sample (1).csv")
# read the data from the csv file 
df = pd.DataFrame(data)
#convert into data structure
print(df)

print(df.describe()) # it return statistical data