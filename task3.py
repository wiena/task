import pandas as pd
import numpy as np


path = './10L Comb_Expenditure_over_Threshold_Report_August_17.csv'
data = pd.read_csv(path, thousands = ',', encoding = 'ISO-8859-1')

table = pd.pivot_table(data, values = 'AP Amount (£)', rows = 'Expense Type', cols = 'Expense area', aggfunc = 'sum')
table.index.name = None
total = data.groupby('Expense area')['AP Amount (£)'].sum()
temp = pd.DataFrame(total)
temp.columns = ["Expense Type"]
temp=pd.DataFrame(temp).T
finalTable = pd.concat([temp, table])
formating = lambda x: '£' + str(x)
finalTable = finalTable.applymap(formating)

''' Python 3.x is used in this case
firstly import data, then make cross table and calculate sum of amount.
Then add subtotal for each column and format cells to include £ ''''












