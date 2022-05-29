from all_in_one import exec_all_in_one

# 已有模型，由模型同事提供 model_id
'''
model_id : 模型Id
# 模型命名规则 项目名称_新老客（new/old customer）_期限（short/long term）_tag(模型上线时间 yymmdd)_模型所用算法(xgb,scorecard)
input_data_path :要预测数据存放目录
output_data_path:导出数据存放目录
'''

# 已有模型测试
# model_id = 'hyuk_coldstart_yxsp_tag210121_xgb' # 惠域U卡冷启动模型 营销审批模型 49个字段 使用量化派数据建模 示例数据 data/x_test49.csv
# model_id = 'hyuk_coldstart_yxsp_tag210122_xgb' # 惠域U卡冷启动模型 营销审批模型 114个字段
# model_id = 'lhp_oldcustomer_longterm_tag201201_scorecard' # 量化派老客长期限模型
# model_id = '20210107180115263245' # 自定义上传模型，可咨询模型组具体上传方法
# model_id = '360_all_3rd_tag210126_scorecard' # 分期乐冷启动模型，使用360小贷数据建模 示例数据  data/360小贷样本打分0126.csv
# model_id = '360_all_3rd_tag210603_scorecard' # 分期乐冷启动模型，使用360小贷数据建模 示例数据  data/360小贷样本打分20210602.csv
# model_id = 'hyuk_coldstart_oldcustomer_tag210126_scorecard' #惠域U卡冷启动模型 使用量化派数据建模 U卡做OOT 示例数据 data/SCORE.csv
# model_id = 'lhp_oldcustomer_shortterm_tag210204_scorecard' # 惠域U卡冷启动模型 使用量化派数据建模 量化派做OOT
# model_id = '360_hr_v4_tag210818_scorecard' # 惠域U卡冷启动模型 使用量化派数据建模 量化派做OOT
model_id = '360_lr_v2_tag220228_scorecard' # 360小贷低定价模型v2(去掉腾讯反欺诈分）
input_data_path = 'E:\\工作文件\\模型监控\\data\\all_data20220228new1.csv'
output_data_path = 'E:\\工作文件\\模型监控\\data\\all_data20220228new_score20220228newnew.csv'
result = exec_all_in_one(model_id=model_id, input_data_path=input_data_path, output_data_path=output_data_path)
print(result)


























# # 自定义模型分割点与分数，自主上传模型
# '''
# model_info 格式：
# {
#     "bins_info":{"LAD_NORM_PAY_CNT":[{"cut_off":[1,4,5],
#                                   "score":[128,106,116,122]}],
#              "LST2_OVERDUE_DAYS": [{"cut_off": [1, 3, 5],
#                                    "score": [126, 132, 118, 77]}],
#              "bh_rl_summary_remainingMaxOverdueStatus": [{"cut_off": ["-9999999", "1,2,3,4,5,6,7"],
#                                    "score": [121, 35]}],
#              "bh_nrl_D30_overdueLoanCount": [{"cut_off": [1],
#                                    "score": [135, 54]}],
#              "bh_agg_query_last_days_d90": [{"cut_off": [0, 12, 33],
#                                    "score": [106, 134, 116, 103]}]},
#     "categorical_vars":["bh_rl_summary_remainingMaxOverdueStatus"]
# }
#
# 其中分割点不包含数据断点，
# 例："LAD_NORM_PAY_CNT":[{"cut_off":[1,4,5], "score":[128,106,116,122]}]
# 即  case when LAD_NORM_PAY_CNT < 1     then 128
#          when 1<= LAD_NORM_PAY_CNT < 4 then 106
#          when 4<= LAD_NORM_PAY_CNT < 5 then 116
#          when 5<= LAD_NORM_PAY_CNT     then 122
# 分类型分组，分组与 分数一一对应。
# categorical_vars 记录分组变量变量名
# '''
# model_info = {
#     "bins_info": {"LAD_NORM_PAY_CNT": [{"cut_off": [1, 4, 5],
#                                         "score": [128, 106, 116, 122]}],
#                   "LST2_OVERDUE_DAYS": [{"cut_off": [1, 3, 5],
#                                          "score": [126, 132, 118, 77]}],
#                   "bh_rl_summary_remainingMaxOverdueStatus": [{"cut_off": ["-9999999", "1,2,3,4,5,6,7"],
#                                                                "score": [121, 35]}],
#                   "bh_nrl_D30_overdueLoanCount": [{"cut_off": [1],
#                                                    "score": [135, 54]}],
#                   "bh_agg_query_last_days_d90": [{"cut_off": [0, 12, 33],
#                                                   "score": [106, 134, 116, 103]}]},
#     "categorical_vars": ["bh_rl_summary_remainingMaxOverdueStatus"]
# }
# input_data_path = '../data/20201210.csv'
# output_data_path = 'output1230.csv'
# result = exec_all_in_one(model_info=json.dumps(model_info), input_data_path=input_data_path,
#                          output_data_path=output_data_path)
# print(result)