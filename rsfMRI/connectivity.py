import numpy as np

def compute_correlation(timeseries):
    """
    回傳 ROI × ROI 的皮爾森相關矩陣。
    """
    return np.corrcoef(timeseries.T)

def fisher_z(corr_matrix):
    """
    對相關矩陣進行 Fisher Z 轉換。
    """
    return np.arctanh(corr_matrix)
