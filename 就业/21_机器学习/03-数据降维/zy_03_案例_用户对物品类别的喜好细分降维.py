import pandas as pd
from sklearn.decomposition import PCA

# 读取文件
file_path1 = "./order_products__prior.csv"
file_path2 = "./products.csv"
file_path3 = "./orders.csv"
file_path4 = "./aisles.csv"

prior = pd.read_csv(file_path1)
product = pd.read_csv(file_path2)
order = pd.read_csv(file_path3)
aisle = pd.read_csv(file_path4)

# 合并各张表到一张表
_mg = pd.merge(prior,product,on=["product_id","product_id"])
_mg = pd.merge(_mg,order,on=["order_id","order_id"])
mt = pd.merge(_mg,aisle,on=["aisle_id","aisle_id"])

# print(mt.head(5))
# print(mt.info())

# 建立一个类似行，列数据  （交叉表）
cross = pd.crosstab(mt["user_id"],mt["aisle"])

# print(cross.head(5))
# print(cross.info())

# 进行主成分分析
pca = PCA(n_components=0.9)
data = pca.fit_transform(cross)
print(data)
