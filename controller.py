from numpy import NaN
from request import get_fxusdcad_from_boc, get_avgintwo_from_boc, cal_correlation

## Controller generates all the final result as a dictionary
def generator(start_date, end_date):
    result_fx = get_fxusdcad_from_boc(start_date,end_date)[0]
    result_avg = get_avgintwo_from_boc(start_date,end_date)[0]


    fx_list = get_fxusdcad_from_boc(start_date,end_date)[1]
    avg_list = get_avgintwo_from_boc(start_date,end_date)[1]
    result_avg.update(result_fx)

    error = ''
    if len(fx_list) > len(avg_list):
        error = "Could not Calculalte correlation since CORR lack of the data."
        result_avg['error'] = error
        return result_avg
    if len(fx_list) < len(avg_list):
        error = "Could not Calculalte correlation since USD/CAD lack of the data."
        result_avg['error'] = error
        return result_avg
    correlation = cal_correlation(fx_list, avg_list)
    if correlation is NaN:
        error = "Cannot calculate correlation by given results, please check."
        result_avg['error'] = error
        return result_avg

    result_avg['Correlation b/w USD/CAD and CORRA'] = correlation
    result_avg['error'] = error
    return result_avg