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
# headers
host = "https://api.btcgateway.pro"

headers = dict()
headers["Accept"] = "application/json"
headers["Content-type"] = "application/json"

# 获取服务器时间戳
sign = generate_signature(host, "GET", param, "/swap-api/v1/timestamp", SecretKey)
# print(sign)
r_p_1 = param.copy()
r_p_1['Signature'] = sign
res = requests.get("https://api.btcgateway.pro/api/v1/timestamp", params=r_p_1, headers=headers)
print(res.json())


sign = generate_signature(host, "POST", param, "/swap-api/v1/swap_matchresults", SecretKey)
# print(sign)
r_p_2 = param.copy()
r_p_2['Signature'] = sign
data = {"contract_code": "BTC-USD", "trade_type": 0, "create_date": 30}
res = requests.post(host + "/swap-api/v1/swap_matchresults", data=json.dumps(data), params=r_p_2, headers=headers)
print(res.json())
