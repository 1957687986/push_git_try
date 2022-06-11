import tensorflow as tf
# 去除警告
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 变量op

# 1、变量op能够持久化保存，普通张量op不可以
# 2、当定义一个变量op后，一定要在会话中去运行初始化

# 变量创建
a = tf.constant([1,2,3,4,5,6])

# 变量
var = tf.Variable(tf.random_normal([2,3],mean = 0.0 ,stddev=1.0))

print(a,var)

# 必须做一步显示的初始化
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    # 必须运行初始化op
    sess.run(init_op)

    print(sess.run([a,var]))