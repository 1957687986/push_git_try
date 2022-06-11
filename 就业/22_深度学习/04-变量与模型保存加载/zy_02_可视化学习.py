import tensorflow as tf
import tensorboard
# 去除警告
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 变量op

# 1、变量op能够持久化保存，普通张量op不可以
# 2、当定义一个变量op后，一定要在会话中去运行初始化
# 3、name参数，tensorboard使用时显示名字，可以让相同的op名字进行区分

# 常量
a = tf.constant(3.0, name="a")

b = tf.constant(4.0, name="b")

c = tf.add(a.b, name="add")

# 变量创建
var = tf.Variable(tf.random_normal([2, 3], mean=0.0, stddev=1.0),name="var")

print(a, var)

# 必须做一步显示的初始化
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    # 必须运行初始化op
    sess.run(init_op)

    # 把程序的图结构写入事件文件  graph  把指定的图写入事件文件当中
    fileWriter = tf.summary.FileWriter("../tmp/",graph=sess.graph)

    # 开启文件
    # --logdir = "../tmp/"

    print(sess.run([a, var]))