# -*- coding: utf-8 -*-

from HuobiMarketService import generate_signature
import datetime
import requests
import json


AccessKey = "XXX"
SecretKey = "XXX"
timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
param = {
    "AccessKeyId": AccessKey,
    "SignatureMethod": "HmacSHA256",
    "SignatureVersion": "2",
    "Timestamp": timestamp
}
url = "https://api.btcgateway.pro/swap-api/v1/swap_matchresults"
sign = generate_signature(url, "POST", param, "/notification", SecretKey)

print(sign)

param['Signature'] = sign
headers = dict()
headers["Accept"] = "application/json"
headers["Content-type"] = "application/json"
res = requests.get("https://api.btcgateway.pro/api/v1/timestamp", params=param, headers=headers)
print(res.json())
data = {"contract_code": "BTC-USD", "trade_type": 0, "create_date": 30}
res = requests.post(url, data=json.dumps(data), params=param, headers=headers)
print(res.json())
