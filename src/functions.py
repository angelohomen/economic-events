import warnings
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import dendrogram, linkage
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import StandardScaler
warnings.filterwarnings('ignore')
plt.rcParams['figure.figsize'] = 12,40

class CorrClass():
    def __init__(self):
        pass

    def cleanMatrix(self,retData) -> pd.DataFrame():
        m = len(retData.T)
        n = len(retData)
        lambda_p = (1+np.sqrt(m/n))**2
        corr = retData.corr()
        eig = np.linalg.eig(corr)
        eigva = eig[0]
        eigve = eig[1]
        cutoff = len(eigva[eigva > lambda_p])
        eigva[cutoff:] = sum(eigva[cutoff:])/len(eigva[cutoff:])
        corr = np.real(np.matmul(eigve, np.matmul(np.diag(eigva),eigve.T)))
        return pd.DataFrame(corr, index=retData.columns, columns=retData.columns)
 
    def cov2corr(self,cov):
        std=np.sqrt(np.diag(cov))
        corr=cov/np.outer(std,std)
        corr[corr<-1],corr[corr>1]=-1,1
        return corr

    def detonMatrix(self,retData) -> pd.DataFrame():
        m = len(retData.T)
        n = len(retData)
        lambda_p = (1+np.sqrt(m/n))**2
        corr = retData.corr()
        eig = np.linalg.eig(corr)
        eigva = eig[0][1:]
        eigve = eig[1].T[1:].T
        corr = np.real(np.matmul(eigve, np.matmul(np.diag(eigva),eigve.T)))
        return pd.DataFrame(corr, index=retData.columns, columns=retData.columns)

    def plot_heatmap_dendogram(self,df,fig_name):
        heatmap = sns.clustermap(df.corr(),figsize=(12,12))
        plt.show();
        row_linkage = heatmap.dendrogram_row.linkage
        plt.figure(figsize=(12, 40), dpi=80)
        dn = dendrogram(row_linkage, labels = df.columns, orientation='right', leaf_font_size=8)
        plt.savefig(f'{fig_name}.png',figsize=(12, 40))
        return dn
    
    def vif(self,X):
        scaler = StandardScaler()
        xs = scaler.fit_transform(X)
        vif = pd.DataFrame()
        vif["Features"] = X.columns
        vif["VIF Factor"] = [variance_inflation_factor(xs, i) for i in range(xs.shape[1])]
        return vif