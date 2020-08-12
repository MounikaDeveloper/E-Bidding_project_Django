import time
import requests
amt = 1

while True:
    if amt >= 5:
        break
    else:
        res = requests.get("http://127.0.0.1:8000/index/product/")
        print(res.json())
        amt+=1
        time.sleep(2)

