from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
from sklearn.metrics import  silhouette_score

prior = pd.read_csv("./order_products__prior.csv")
products = pd.read_csv("./products.csv")
orders = pd.read_csv("./orders.csv")
aisles = pd.read_csv("./aisles.csv")

_mg = pd.merge(prior,products,on=["product_id","product_id"])
_mg = pd.merge(_mg,orders,on=["order_id","order_id"])
mt = pd.merge(_mg,aisles,on=["aisle_id","aisle_id"])

print(mt.head(10))

cross = pd.crosstab(mt["user_id"],mt["aisle"])

print(cross.head(10))

# 主成分分析
pca = PCA(n_components=0.9)

data = pca.fit_transform(cross)

# 把样本数量减少
x = data[:500]
print(x.shape)

# 假设有四个类别
km = KMeans(n_clusters=4)

km.fit(x)

predict = km.predict(x)
print(predict)

plt.figure(figsize=(20,8),dpi=80)

# 建立四个颜色列表
colored = ["orange","green","blue","purple"]

color = [colored[i] for i in predict]

plt.scatter(x[:,5],x[:,20],color=color)

plt.xlabel("1")
plt.ylabel("20")

plt.show()

# 聚类评估
print(silhouette_score(x,predict))
