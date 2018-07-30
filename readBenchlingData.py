import pandas as pd
from os import path
from os import listdir
from os.path import isfile, join

# mypath = './Inventory/'
# allChemicals = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#
# allCASNum = []
# notFound = []
# for chemical in allChemicals:
#     try:
#         print()
#         df = pd.read_csv(path.join(mypath, chemical), sep=":", index_col=None)
#         casNum = str.strip(df.loc['CAS #'][df.columns[0]])
#         if casNum == 'None' or casNum == '':
#             notFound.append(chemical)
#         else:
#             allCASNum.append(casNum)
#     except:
#         notFound.append(chemical)
#         continue
#
# print(allCASNum)

df = pd.read_csv('20180110_BenchlingChemicalDatabase.csv')
df.dropna(subset=['CAS #'], inplace=True)
df['CAS #'] = df['CAS #'].str.strip()
df['CAS #'].to_csv('CAS-list.txt', sep='\r', index=False)


# with open('CAS-list.txt', 'w') as casFile:
#     print("Writing Data to %s : " % 'CAS-list.txt')
#     for casNum in allCASNum:
#         casFile.write("%s\n" % casNum)
#
# with open('CAS_notFound.txt', 'w') as casFileNotFound:
#     for c in notFound:
#         casFileNotFound.write("%s\n" % c)
