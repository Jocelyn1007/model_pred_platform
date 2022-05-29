import json
from io import StringIO
import os
import pandas as pd
import requests
from requests_toolbelt import MultipartEncoder

BASE_URL = "http://10.55.1.153:8088"
# BASE_URL = "http://127.0.0.1:8088"
# BASE_URL = "http://10.55.1.153:5000"


def exec_all_in_one(input_data_path, output_data_path,model_id=None, model_info=None, model_type = 'ScoreCard'):
    # 检查服务器端口是否正常
    test_url = BASE_URL + '/model/check'
    response = requests.request("GET", test_url)
    status_code = response.status_code
    if status_code == 200:
        if model_info:
            try:
                upload_model_url = BASE_URL + '/model/upload'
                headers = {'Content-Type': 'application/json'}
                response = requests.request("POST", upload_model_url, data=model_info, headers=headers)
                model_id = json.loads(response.content).get('model_id')
            except:
                return "模型上传出错，请检查model_info格式是否正确"
                # 上传数据
        upload_data_url = BASE_URL + '/model/predict/{0}'.format(model_id)
        file_name = input_data_path  # 需要预测的数据，csv 格式

        data = MultipartEncoder(
            fields={'file': ('file_name', open(file_name, 'rb'), 'text/plain')}
        )
        response = requests.post(upload_data_url, data=data, headers={'Content-Type': data.content_type})
        try:
            result = json.loads(response.content.decode())
            data_id = result.get('data_id')  # data_id, 预测文件的唯一标识符，下载预测文件时需要
        except:
            return "数据上传出错:::{0}".format(response.content.decode())

        # 预测文件下载
        download_data_url = BASE_URL + '/model/download/{0}/{1}'.format(model_id, data_id)
        payload = {}
        headers = {}
        response = requests.request("GET", download_data_url, headers=headers, data=payload)
        text = response.text
        score = pd.read_csv(StringIO(text), sep=',')  # 转成dataframe格式
        score.to_csv(output_data_path, index=False, index_label=False)  # 自定义导出

        poison_url = BASE_URL + '/posion'
        response = requests.request("GET", poison_url, headers=headers, data=payload)

        return '{1}\n\n数据导出成功\n可使用:::\n {0} \n进行重复调用预测结果数据'.format(download_data_url, response.text)

    else:
        return "服务器报错"
    # 上传model

if __name__ == '__main__':
    # 无model_info
    # model_id = 'lhp_oldcustomer_longterm_model_v1.1_tag0620'
    # input_data_path = '../data/SAMPLE_OOT.csv'
    # output_data_path = 'output1229.csv'
    # result = exec_all_in_one(model_id=model_id, input_data_path=input_data_path, output_data_path=output_data_path)
    # print(result)

    # 有model_info
    model_info = {
        "bins_info": {"LAD_NORM_PAY_CNT": [{"cut_off": [1, 4, 5],
                                            "score": [128, 106, 116, 122]}],
                      "LST2_OVERDUE_DAYS": [{"cut_off": [1, 3, 5],
                                             "score": [126, 132, 118, 77]}],
                      "bh_rl_summary_remainingMaxOverdueStatus": [{"cut_off": ["-9999999", "1,2,3,4,5,6,7"],
                                                                   "score": [121, 35]}],
                      "bh_nrl_D30_overdueLoanCount": [{"cut_off": [1],
                                                       "score": [135, 54]}],
                      "bh_agg_query_last_days_d90": [{"cut_off": [0, 12, 33],
                                                      "score": [106, 134, 116, 103]}]},
        "categorical_vars": ["bh_rl_summary_remainingMaxOverdueStatus"]
    }
    input_data_path = '../data/20201210.csv'
    output_data_path = 'output1230.csv'
    result = exec_all_in_one(model_info=json.dumps(model_info), input_data_path=input_data_path, output_data_path=output_data_path)
    print(result)
