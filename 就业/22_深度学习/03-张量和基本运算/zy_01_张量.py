import tensorflow as tf
# 去除警告
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 创建一张图,包含了op和tensor上下文环境
# op:只要使用了TensorFlow的API定义的函数都是OP
# tensor:就代指的是数据

# g = tf.Graph()
#
# print(g)
#
# # 使用
# with g.as_default():
#     c = tf.constant(11.0)
#     print(c.graph)
#
# # 实现加法运算
# tf.constant创建常量
# a = tf.constant(5.0)
# b = tf.constant(6.0)
#
# sum1 = tf.add(a,b)
#
# # 默认的这张图，相当于给程序分配一段内存
# gragh = tf.get_default_graph()
#
# print(gragh)
#
# # sum2,不可在TensorFlow中的run运行  ---  不是op
# # var1 = 2
# # var2 = 3
# # sum2 = var1 + var2
#
# var1 = 2.0
#
# # 可以在run中运行  重载机制  重载成op类型
# sum2 = a + var1
#
# print(sum2)
#
# print(sum1)
#
# # 开启会话，使用的是默认图结构，只能运行一个图
# # 可以在会话中指定图运行 --- graph=
# # 只要有会话的上下文环境，就可以方便地使用eval（）
#
# # 训练模型
# # 实时提供数据去进行训练
#
# # placeholder是一个占位符   feed_dict  一个字典
# # [None,3]  用None表示样本不固定
# plt = tf.placeholder(tf.float32,[2,3])
#
# with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
#     # print(sess.run([a,b,sum1]))
#     print(sess.run(plt,feed_dict={plt:[[1,2,3],[4,5,6]]}))
#     # 下面三个与sess没有关系，在哪都可以打印，是系统定义的
#     # c是定义在g下面的
#     # 运行某个程序与sess有关系
#     print(a.graph)
#     print("-" * 50)
#     print(a.shape)
#     print(plt.shape)
#     print("-"*50)
#     print(a.name)
#     print("-"*50)
#     print(a.op)

# 打印出来的形状表示
# 0维:()  1维:(5)   2维:(5,6)   3维:(2,3,4)


# 形状改变
# 静态形状和动态形状
# placeholder  为一个占位符
plt = tf.placeholder(tf.float32,[None,2])

print(plt)

# 不固定的时候才可以改，固定的值不可改
plt.set_shape([3,2])

print(plt)

# 对于静态形状来说，一旦张量形状固定后就不可再次设置静态形状，也不可跨纬度进行修改，2维到3维不可
# 动态形状可以去创建一个新的张量，一定要注意元素的数量要匹配，可跨维
# plt.set_shape([4,2])
#
# print(plt)

plt_reshape = tf.reshape(plt,[2,3])

print(plt_reshape)

with tf.Session() as sess:
    pass
