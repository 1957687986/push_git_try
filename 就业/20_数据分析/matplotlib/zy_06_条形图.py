from matplotlib import pyplot as plt
from matplotlib import font_manager
import matplotlib

matplotlib.rc("font",family = "KaiTi")

a = ["战狼2","速度与激情8","功夫瑜伽","西游伏魔篇","变形金刚5","最后的骑士","摔跤吧！爸爸","加勒比海盗5",
     "死无对证","金刚：骷髅岛","极限特工：\n终极回归","生化危机\n6：终章","乘风破浪","神偷奶爸3","智取威虎山",
     "大闹天竺金","金刚狼3：\n殊死一战","蜘蛛侠：\n英雄归来","悟空传","银河护卫队2"]
b = [56.01,26.94,17.52,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,
     6.99,6.88,6.86,6.58,6.23]

# 设置大小
plt.figure(figsize=(20,8),dpi=80)

# 先绘制图形x,y轴由系统自己定义
plt.bar(range(len(a)),b)

# 对系统自己定义的x,y轴进行修改
plt.xticks(range(len(a)),a,rotation = 45)

plt.show()