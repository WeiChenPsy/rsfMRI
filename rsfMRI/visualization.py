import matplotlib.pyplot as plt
import seaborn as sns

def plot_matrix(matrix, labels=None, title="Functional Connectivity"):
    """
    使用 heatmap 畫相關矩陣。
    """
    plt.figure(figsize=(8, 6))
    sns.heatmap(matrix, xticklabels=labels, yticklabels=labels,
                cmap="coolwarm", center=0, square=True)
    plt.title(title)
    plt.show()
