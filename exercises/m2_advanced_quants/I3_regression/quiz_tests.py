from collections import OrderedDict
import numpy as np
import pandas as pd
import scipy.stats as stats
from tests import project_test, generate_random_tickers, generate_random_dates, assert_output
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.tsa.arima_model import ARIMA

@project_test
def test_is_normal_ks(fn):

    sample_normal = stats.norm.rvs(loc=0.0, scale=1.0, size=(1000,))
    fn_inputs = {
        'sample': sample_normal}

    fn_correct_outputs = OrderedDict([
        ('normal',np.True_)
        ])

    assert_output(fn, fn_inputs, fn_correct_outputs)


    sample_not_normal = stats.lognorm.rvs(s=0.5, loc=0.0, scale=1.0, size=(1000,))
    fn_inputs = {
        'sample': sample_not_normal}

    fn_correct_outputs = OrderedDict([
        ('not_normal',np.False_)
        ])

    assert_output(fn, fn_inputs, fn_correct_outputs)


@project_test
def test_fit_arima(fn):
    np.random.seed(200)

    ar_params = np.array([1, -0.5])
    ma_params = np.array([1, -0.3])
    ret = ArmaProcess(ar_params, ma_params).generate_sample(nsample=5*252)

    ret = pd.Series(ret)
    drift = 100
    price = pd.Series(np.cumsum(ret)) + drift

    lret = np.log(price) - np.log(price.shift(1))
    lret = lret[1:]

    #TODO: choose autoregression lag of 1
    AR_lag_p = 1

    #TODO: choose moving average lag of 1
    MA_lag_q = 1

    #TODO: choose order of integration 1
    order_of_integration_d = 1

    #TODO: Create a tuple of p,d,q
    order = (AR_lag_p, order_of_integration_d, MA_lag_q)

    arima_model = ARIMA(lret.values, order=order)
    arima_result = arima_model.fit()

    fittedvalues = arima_result.fittedvalues
    arparams = arima_result.arparams
    maparams = arima_result.maparams

    fn_inputs = {
        'lret': lret
        }

    fn_correct_outputs = OrderedDict([
        ('fittedvalues',fittedvalues),
        ('arparams',arparams),
        ('maparams',maparams),
        ])

    assert_output(fn, fn_inputs, fn_correct_outputs)
