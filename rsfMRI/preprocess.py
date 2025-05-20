import numpy as np
from sklearn.linear_model import LinearRegression

def regress_confounds(timeseries, confounds):
    """
    使用線性回歸移除 confound 影響。
    """
    model = LinearRegression()
    model.fit(confounds, timeseries)
    predicted = model.predict(confounds)
    cleaned = timeseries - predicted
    return cleaned
