from io import StringIO

import requests
from requests_toolbelt import MultipartEncoder
import json
import pandas as pd
# BASE_URL= "http://127.0.0.1:5000"
BASE_URL = "http://10.55.1.153:5000"
# 模型上传
url = BASE_URL + '/model/upload'

payload='''
{
    "bins_info":{"LAD_NORM_PAY_CNT":[{"cut_off":[1,4,5],
                                  "score":[128,106,116,122]}],
             "LST2_OVERDUE_DAYS": [{"cut_off": [1, 3, 5],
                                   "score": [126, 132, 118, 77]}],
             "bh_rl_summary_remainingMaxOverdueStatus": [{"cut_off": ["-9999999", "1,2,3,4,5,6,7"],
                                   "score": [121, 35]}],
             "bh_nrl_D30_overdueLoanCount": [{"cut_off": [1],
                                   "score": [135, 54]}],
             "bh_agg_query_last_days_d90": [{"cut_off": [0, 12, 33],
                                   "score": [106, 134, 116, 103]}]},
    "categorical_vars":["bh_rl_summary_remainingMaxOverdueStatus"]
}
'''

headers = {'Content-Type': 'application/json'}
response = requests.request("POST", url, data=payload, headers = headers)
model_id = json.loads(response.content).get('model_id')
model_info = json.loads(response.content).get('model_info') # 此为接口返回分割点，可与上传分割点进行核对，确保无误。
print('model_id 为 {0}'.format(model_id))

# 模型检查 非必要
# 模型预测可重复使用分割点，仅需记住model_id

# model_id = ''
url = BASE_URL + '/model/query/{0}'.format(model_id)
payload={}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)
print(response.text) # mdoel_id 对应的 模型内容

# 模型预测

# model_id = '20201211171724588626'
# model_id = 'lhp_oldcustomer_longterm_model_v1.1_tag0620'
model_id = 'hyuk_coldstart_yxsp_tag210121_xgb'
# model_id = 'hyuk_coldstart_yxsp_model114_tag0120'

# url = BASE_URL + '/model/ScoreCard/predict/{0}'.format(model_id)
url = BASE_URL + '/model/predict/{0}'.format(model_id)

# file_name = '../data/SAMPLE_OOT.csv'  # 需要预测的数据，csv 格式
# file_name = r'../data/x_test49.csv'  # 需要预测的数据，csv 格式
file_name = 'data/x_test49.csv'
data = MultipartEncoder(
    fields={'file':('file_name', open(file_name, 'rb'), 'text/plain')}
)
# data = pd.read_csv('data/x_test49.csv')
# dict(data.iloc[1,:])
response = requests.post(url, data=data,headers={'Content-Type': data.content_type})
print(response.content.decode())
result = json.loads(response.content.decode())

model_id = result.get('model_id') # model_id
data_id = result.get('data_id') # data_id, 预测文件的唯一标识符，下载预测文件时需要
# 预测文件下载
url = BASE_URL + '/model/download/{0}/{1}'.format(model_id, data_id)
payload={}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)
text = response.text
score = pd.read_csv(StringIO(text), sep=',') # 已经转成dataframe格式
score.to_csv('score1229.csv', index=False, index_label=False) #自定义导出