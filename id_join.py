import chardet
import time
import csv
import ast
import requests
import json
import pandas as pd

start= time.time()
print("Clock started")

with open("spmooddata.csv", 'rb') as rawdata:
    result = chardet.detect(rawdata.read(100000))
result
#{'encoding': 'Windows-1252', 'confidence': 0.73, 'language': ''}
df= pd.read_csv(r"spmooddata.csv", encoding= "Windows-1252")
df= pd.DataFrame(df, columns=["Song ID"])
songidcol= df.to_json()
songidcol2= ast.literal_eval(songidcol)
#songidcol2= json.dumps(songidcol)
songidparsed= songidcol2["Song ID"]
    
k=0 
concatls=[] 
concatpre=[]

def get_concat_query(k, concatls, concatpre):
    for i in range (0, len(songidparsed)):
        if i<100+100*k:
            songidval= songidparsed.get(str(i))
            concatpre.append(songidval)
            joined= ",".join(concatpre)
            if i%100==99:
                concatls.append(joined)
                concatpre=[]
        k=k+1
get_concat_query(k,concatls,concatpre)

end=time.time()
print("Seconds: %.2f"
      % (end-start))
