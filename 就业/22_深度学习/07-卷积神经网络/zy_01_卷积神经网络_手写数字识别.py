import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


# 定义初始化权重的函数
def weight_variables(shape):
    w = tf.Variable(tf.random_normal(shape=shape,mean=0.0,stddev=1.0))
    return w

def bais_variables(shape):
    b = tf.Variable(tf.constant(0.0,shape=shape))
    return b


def model():
    """
    自定义卷积模型
    :return: None
    """
    # 1、建立数据占位符  ---->   想实时运行时提供数据    x[None,784]  y_true [None,10]
    # with tf.variable_scope  此函数为建立一个作用域
    with tf.variable_scope("data"):
        x = tf.placeholder(tf.float32, [None, 784])

        y_true = tf.placeholder(tf.int32, [None, 10])

    # 2、一卷积层  卷积：5*5*1,32个filter，strides=1，激活: tf.nn.relu，池化
    with tf.variable_scope("conv1"):
        # 随机初始化权重，偏置[32]
        w_conv1 = weight_variables([5,5,1,32])

        b_conv1 = bais_variables([32])

        # 对x进行形状的改变[None,784] --->[None,28,28,1]
        x_reshape = tf.reshape(x,[-1,28,28,1])

        # 卷积计算结果[None,28,28,1]--->[None,28,28,32]
        x_relu1 = tf.nn.relu(tf.nn.conv2d(x_reshape,w_conv1,strides=[1,1,1,1],padding="SAME") + b_conv1)

        # 池化  2*2，strides2, [None,28,28,32]---->[None,14,14,32]
        x_pool1 = tf.nn.max_pool(x_relu1,ksize=[1,2,2,1],strides=[1,2,2,1],padding="SAME")

    # 3、二卷积层  卷积：5*5*32,64个filter，strides=1，激活: tf.nn.relu，池化
    with tf.variable_scope("conv2"):
        # 随机初始化权重，偏置[64]
        w_conv2 = weight_variables([5, 5, 32, 64])

        b_conv2 = bais_variables([64])

        # 卷积，激活，池化运算
        # [None,14,14,32]--->[None,14,14,64]
        x_relu2 = tf.nn.relu(tf.nn.conv2d(x_pool1, w_conv2, strides=[1, 1, 1, 1], padding="SAME") + b_conv2)

        # 池化  2*2，strides2, [None,14,14,64]---->[None,7,7,64]
        x_pool2 = tf.nn.max_pool(x_relu2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")

    # 4、全连接层  [None,7,7,64] ---->[None,7*7*64]*[7*7*64,10] + [10]=[None,10]
    with tf.variable_scope("fc"):
        # 随机初始化权重和偏置
        w_fc = weight_variables([7*7*64, 10])

        b_fc = bais_variables([10])

        # 修改形状 [None,7,7,64]--->[None,7*7*64]
        x_fc_reshape = tf.reshape(x_pool2,[-1,7*7*64])

        # 矩阵运算得出每个样本的10个结果
        y_predict = tf.matmul(x_fc_reshape,w_fc) + b_fc

    return x,y_true,y_predict


def conv_fc():
    # 获取真实数据   "./data/mnist/input_data/"此文件路径为TensorFlow中自带的路径
    mnist = input_data.read_data_sets("./data/mnist/input_data/", one_hot=True)

    # 定义模型，得出输出
    x,y_true,y_predict = model()

    # 进行交叉熵损失计算
    # 3、求出所有样本的损失，然后求平均值
    with tf.variable_scope("sotf_cross"):
        # 求平均交叉熵损失
        loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_true, logits=y_predict))

    # 4、梯度下降求出损失
    with tf.variable_scope("optimizer"):
        train_op = tf.train.GradientDescentOptimizer(0.0001).minimize(loss)

    # 5、计算准确率
    with tf.variable_scope("acc"):
        equal_list = tf.equal(tf.argmax(y_true, 1), tf.argmax(y_predict, 1))

        # 转换为float类型  equal_list有None个样本
        accuracy = tf.reduce_mean(tf.cast(equal_list, tf.float32))

    # 定义初始化变量op
    init_op = tf.global_variables_initializer()

    # 开启会话运行
    with tf.Session() as sess:
        sess.run(init_op)

        # 循环去训练
        for i in range(1000):
            # 取出真实存在的特征值和目标值
            mnist_x, mnist_y = mnist.train.next_batch(50)

            # 运行train_op训练
            sess.run(train_op, feed_dict={x: mnist_x, y_true: mnist_y})

            print("训练第%d步，准确率为%f,损失值为%f" % (i,
                                            sess.run(accuracy, feed_dict={x: mnist_x, y_true: mnist_y}),
                                            sess.run(loss, feed_dict={x: mnist_x, y_true: mnist_y})))

    return None

if __name__ == '__main__':
    conv_fc()