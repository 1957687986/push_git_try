import tensorflow as tf
import tensorboard
# 去除警告
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 1、训练参数问题: trainable参数
# 学习率和步数的设置

# 2、添加一些权重参数，损失值等在tensorboard观察情况
#     1、收集变量 tensor
#     2、合并变量写入事件文件


def myregression():
    """
    自实现一个线性回归预测
    :return: None
    """
    with tf.variable_scope("data"):

        # 1、准备数据  x 特征值  [100,1]   y 目标值[100]
        x = tf.random_normal([100,1],mean=1.75, stddev=0.5,name="x_data")

        # 矩阵相乘必须是二维的
        y_true = tf.matmul(x,[[0.7]]) + 0.8

    with tf.variable_scope("model"):

        # 2、建立线性回归模型  1 个权重  1个偏值 y = x*w + b
        # 随机给一个权重和偏值 ，让他去计算损失，然后在当前状态下优化
        # 用变量定义才能优化
        # trainable参数：指定这个变量能跟着梯度下降一起优化
        weight = tf.Variable(tf.random_normal([1,1],mean=0.0,stddev=1.0),name="w")
        bias = tf.Variable(0.0,name="b")

        y_predict = tf.matmul(x, weight) + bias

    with tf.variable_scope("loss"):
        # 3、建立损失函数，均方误差
        loss = tf.reduce_mean(tf.square(y_true - y_predict))

    with tf.variable_scope("optimizer"):

        # 4、梯度下降优化损失 leaning_rate: 0~1,2,3,5,7,10
        train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

    # 1、收集tensor
    tf.summary.scalar("losses",loss)

    tf.summary.histogram("weightes",weight)

    # 定义合并tensor的op
    merged = tf.summary.merge_all()

    # 定义初始化变量op
    init_op = tf.global_variables_initializer()

    # 定义一个保存模型的实例
    saver = tf.train.Saver()

    # 通过会话运行程序
    with tf.Session() as sess:
        # 初始化变量
        sess.run(init_op)

        # 打印随机最先初始化的权重和偏置
        print("随机初始化的参数权重为：%f , 偏置为：%f" %(weight.eval(),bias.eval()))

        # 建立事件文件
        filewriter = tf.summary.FileWriter("../tmp/",graph=sess.graph)

        # 加载模型，覆盖模型当中随机定义的参数，从上次训练的参数开始
        if os.path.exists("../ckpt/checkpoint"):
            saver.restore(sess,"../ckpt/model")

        # 循环训练，运行优化
        for i in range(100):
            # 运行优化op
            sess.run(train_op)

            # 运行合并的tensor
            summary = sess.run(merged)

            # 合并变量写入事件文件
            filewriter.add_summary(summary,i)

            print("第%d次优化后参数权重为：%f , 偏置为：%f" %(i,weight.eval(),bias.eval()) )

        # 模型保存
        saver.save(sess,"../ckpt/model")

    return None

if __name__ == '__main__':
    myregression()