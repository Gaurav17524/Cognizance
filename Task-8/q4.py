import pandas as pd
stri = input("Enter the string")
li = list(stri.split(" "))
print(li)
series = pd.Series(li)
newSeries = series.map(lambda x: x[0].upper() + x[1:-1] + x[-1].lower())
print(newSeries)

  


