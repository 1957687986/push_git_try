import tensorflow as tf
# 去除警告
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 创建一张图,包含了op和tensor上下文环境
# op:只要使用了TensorFlow的API定义的函数都是OP
# tensor:就代指的是数据

g = tf.Graph()

print(g)

# 使用
with g.as_default():
    c = tf.constant(11.0)
    print(c.graph)

# 实现加法运算
a = tf.constant(5.0)
b = tf.constant(6.0)

sum1 = tf.add(a,b)

# 默认的这张图，相当于给程序分配一段内存
gragh = tf.get_default_graph()

print(gragh)

# sum2,不可在TensorFlow中的run运行  ---  不是op
# var1 = 2
# var2 = 3
# sum2 = var1 + var2

var1 = 2.0

# 可以在run中运行  重载机制  重载成op类型
sum2 = a + var1

print(sum2)

print(sum1)

# 开启会话，使用的是默认图结构，只能运行一个图
# 可以在会话中指定图运行 --- graph=
# 只要有会话的上下文环境，就可以方便地使用eval（）

# 训练模型
# 实时提供数据去进行训练

# placeholder是一个占位符   feed_dict  一个字典
# [None,3]  用None表示样本不固定
plt = tf.placeholder(tf.float32,[2,3])

with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
    # print(sess.run([a,b,sum1]))
    print(sess.run(plt,feed_dict={plt:[[1,2,3],[4,5,6]]}))
    # 下面三个与sess没有关系，在哪都可以打印，是系统定义的
    # c是定义在g下面的
    # 运行某个程序与sess有关系
    print(a.graph)
    print(sum1.graph)
    print(sess.graph)
