import pandas
from bs4 import BeautifulSoup
import requests
#creating dataframe by Passing list
df1=pandas.DataFrame([[1,2,3],[4,5,6]],columns=["A","B","C"],index=["A","B"])
#Creating data frame by passing dictionary
df2=pandas.DataFrame([{"A":1,"B":2,"C":3},{"A":11,"B":12,"C":13}],index=["A","B"])
#OR
df3=pandas.DataFrame([{"A":11,"B":2,"C":3},{"A":11,"B":12,"C":13}])
print (type(df3))
#<class 'pandas.core.frame.DataFrame'>
print (type(df3.mean()))
#<class 'pandas.core.series.Series'>
print (type(df3.mean().mean()))

#<class 'float'>
