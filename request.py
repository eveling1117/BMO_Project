import requests 
from scipy.stats import pearsonr

## Request inlcude all the function that extract data from API
def get_fxusdcad_from_boc(start, end):
    website = f'https://www.bankofcanada.ca/valet/observations/FXUSDCAD'
    PARAMS = {'start_date':start, 'end_date':end}
    response = requests.get(url = website, params= PARAMS)
    data = response.json()

    result_list = []
    for i in data['observations']:
        each = float(i['FXUSDCAD']['v'])
        result_list.append(each)
    max_in_period, min_in_period = max(result_list), min(result_list)
    avg_in_period = sum(result_list) / len(result_list)

    result_dict = {'Max of USD/CAD': round(max_in_period, 4), "Min of USD/CAD": round(min_in_period, 4), "Avg of USD/CAD": round(avg_in_period, 4)}
    return result_dict, result_list

def get_avgintwo_from_boc(start, end):
    website = f'https://www.bankofcanada.ca/valet/observations/AVG.INTWO'
    PARAMS = {'start_date':start, 'end_date':end}
    response = requests.get(url = website, params= PARAMS)
    data = response.json()
    result_list = []
    for i in data['observations']:
        each = float(i['AVG.INTWO']['v'])
        result_list.append(each)
    max_in_period, min_in_period = max(result_list), min(result_list)
    avg_in_period = sum(result_list) / len(result_list)

    result_dict = {'Max of CORRA': round(max_in_period, 4), "Min of CORRA": round(min_in_period, 4), "Avg of CORRA": round(avg_in_period, 4)}
    return result_dict, result_list

def cal_correlation(fx, avg):
    corr, _ = pearsonr(fx, avg)
    return corr




