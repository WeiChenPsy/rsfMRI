import nibabel as nib
import pandas as pd

def load_nifti(path):
    """
    讀取 NIfTI 影像並回傳為 numpy array。
    """
    img = nib.load(path)
    return img.get_fdata(), img.affine, img.header

def load_confounds(path):
    """
    讀取 fmriprep 的 confounds tsv 檔案。
    """
    return pd.read_csv(path, sep='\t')
