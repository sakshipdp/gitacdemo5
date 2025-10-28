import requests
import pandas as pd 

import os

token = os.getenv("API_TOKEN")
print(f"Token : {token}")
if token == "1234abcd":
   print("correct")
else:
    print("incorrect")

#esponse = requests.get("https://jsonplaceholder.typicode.com/users")
#ata = response.json()
#f = pd.DataFrame(data)
#f = df [["id", "name"]]
#rint(df)
