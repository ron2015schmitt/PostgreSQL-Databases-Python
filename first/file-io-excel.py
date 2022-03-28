
import pandas as pd
import numpy as np

# by default it assumes a header row to ignore
df = pd.read_excel('ledger.xlsx')
arr = df.values
print("arr=", arr)

print("hello")

# now write to excel file
df = pd.DataFrame(np.array([[0, "lucas", 100], [1, "tom", 20], [2, "maria", 45]]), columns=['ID', 'name', 'balance'])
df.to_excel('ledger2.xlsx')


df = pd.read_excel('ledger2.xlsx')
arr = df.values
print("arr=", arr)



