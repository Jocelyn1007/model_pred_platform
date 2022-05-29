import datetime
import numpy as np
from utility.writelog import log
import math
import decimal as dc
from decimal import Decimal as Dc
logger = log()


def generate_model_id():
    return '{}'.format(datetime.datetime.now().strftime("%Y%m%d%H%M%S%f"))

def compute_score(value, bin_info, is_closed=False, is_categorical=False):
    '''
    通过分割点确定value对应的score
    :param value: 需要确定的value
    :param bin_info: 分箱信息，含有cut_off与score
    :param is_closed: 对于数值型变量，分割点两端是否为闭区间
    :param is_categorical: 是否为分类变量
    :return: list 返回value对应的score
    '''
    cut_off = bin_info[0].get('cut_off')
    score = bin_info[0].get('score')
    list = []
    if is_categorical:
        for v in value:
            v = str(v)
            for c in cut_off:
                if v in c:
                    s = score[cut_off.index(c)]
                    list.append(s)
                    continue
    else:
        if is_closed:
            cut_off[0] = np.nan_to_num(-np.inf)
            cut_off[-1] = np.nan_to_num(np.inf)
        else:
            cut_off.insert(0, np.nan_to_num(-np.inf))
            cut_off.insert(len(cut_off), np.nan_to_num(np.inf))
        i = 0
        while i < len(value):
            v = value[i]
            if math.isnan(v):
                m = 0
            else:
                # logger.info("现在测试的数据为:::{0}".format(v))
                j = len(cut_off) - 2
                if len(cut_off) - 1 == len(score):
                    m = len(cut_off) - 2
                else:
                    m = len(cut_off) - 1
                while j >= 0:
                    if v >= cut_off[j]:
                        j = -1
                    else:
                        j -= 1
                        m -= 1
            list.append(score[m])
            logger.info('''{0}--->{1}'''.format(v, score[m]))
            i += 1
    return list

# def compute_degree(score):
#     if score >= 623:
#         degree = 'D'
#     elif score >= 606:
#         degree = 'C'
#     elif score >= 554:
#         degree = 'B'
#     else:
#         degree = 'A'
#     return degree


def compute_final_score(data, model_info):
    categorical_vars = model_info.get('categorical_vars')
    for var in model_info.get('bins_info').keys():
        new_col = var + '_map'
        logger.info('#' * 20 + var + '#' * 20)
        # logger.info('正在运行{0}'.format(var))
        if var in categorical_vars:
            is_categorical = True
        else:
            is_categorical = False
        data[new_col] = compute_score(data[var], bin_info=model_info.get('bins_info').get(var), is_closed=False,
                                      is_categorical=is_categorical)

    map_score = [var for var in data.columns.values if 'map' in var]

    data['score'] = data[map_score].apply(lambda x: Dc(str(round(x.sum(),10))).quantize(Dc('0'), rounding=dc.ROUND_HALF_UP), axis=1)
    return data



if __name__ == '__main__':
    import pandas as pd
    # print(generate_model_id())
    '''
    如果分箱有空值，np.nan，则将nan对应的分值放在score[0]
    '''
    model_info = {
	"bins_info": {
		"l15m_overdue_days": [
			{
				"cut_off": [
					1
				],
				"score": [
					62,
					45
				]
			}
		],
		"l18m_lst_prepay_gt0_time": [
			{
				"cut_off": [
					35
				],
				"score": [
					79,
					53
				]
			}
		],
		"td_idcard_loan_muti_platform_d30_plat_num": [
			{
				"cut_off": [
					7,
					11
				],
				"score": [
					68,
					58,
					35
				]
			}
		],
		"xy_behavior2_B22170036": [
			{
				"cut_off": [
					0,
					2,
					5
				],
				"score": [
					41,
					69,
					51,
					34
				]
			}
		],
		"xy_behavior2_B22170052": [
			{
				"cut_off": [
					20,
					26
				],
				"score": [
					48,
					63,
					88
				]
			}
		],
		"xy_yzas_apply_score": [
			{
				"cut_off": [
					593,610
				],
				"score": [
					56,
					61,
					71
				]
			}
		],
		"bh_agg_query_early_days_d360": [
			{
				"cut_off": [
					1,243,295
				],
				"score": [
					71,
					54,
					59,
					66
				]
			}
		],
		"br_als_m1_cell_pdl_allnum": [
			{
				"cut_off": [
					1,
					3
				],
				"score": [
					68,
					63,
					48
				]
			}
		],
		"br_als_m3_id_af_orgnum": [
			{
				"cut_off": [
					1
				],
				"score": [
					63,
					34
				]
			}
		],
		"br_als_m6_id_nbank_p2p_orgnum": [
			{
				"cut_off": [
					1,
					2
				],
				"score": [
					75,

					57,
					41
				]
			}
		],
		"br_als_fst_id_nbank_inteday": [
			{
				"cut_off": [
					343
				],
				"score": [
					53,
					65
				]
			}
		]
	},
	"categorical_vars": []
}
    data = pd.read_csv(r'/home/datamining/pyprojects/modeltest/test0126/models/hyuk/coldstart/oldcustomer/tag210126/data/20210126145212465339.csv')
    result = compute_final_score(data, model_info)

    print(result)

