import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_integer("is_train",0,"指定程序是预测还是训练")


def full_connect():
    # 获取真实数据   "./data/mnist/input_data/"此文件路径为TensorFlow中自带的路径
    mnist = input_data.read_data_sets("./data/mnist/input_data/", one_hot=True)

    # 1、建立数据占位符  ---->   想实时运行时提供数据    x[None,784]  y_true [None,10]
    # with tf.variable_scope  此函数为建立一个作用域
    with tf.variable_scope("data"):
        x = tf.placeholder(tf.float32, [None,784])

        y_true = tf.placeholder(tf.int32,[None, 10])

    # 2、建立全连接层的神经网络   w[784,10] b[10]
    with tf.variable_scope("fc_model"):
        # 随机初始化权重和偏置
        weight = tf.Variable(tf.random_normal([784,10],mean=0.0,stddev=1.0),name="w")

        # tf.constant  此函数为创建常量
        bias = tf.Variable(tf.constant(0.0,shape = [10]))

        # 预测None个样本的输出结果   matrix[None,784]*[784,10] = [None,10]
        # w1*x1+w2*x2+....+b
        y_predict = tf.matmul(x,weight) + bias

    # 3、求出所有样本的损失，然后求平均值
    with tf.variable_scope("sotf_cross"):

        # 求平均交叉熵损失
        loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_true,logits=y_predict))

    # 4、梯度下降求出损失
    with tf.variable_scope("optimizer"):

        train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

    # 5、计算准确率
    with tf.variable_scope("acc"):

        equal_list = tf.equal(tf.argmax(y_true,1),tf.argmax(y_predict,1))

        # 转换为float类型  equal_list有None个样本
        accuracy = tf.reduce_mean(tf.cast(equal_list,tf.float32))

    # 收集变量，单个数字值收集
    tf.summary.scalar("losses",loss)
    tf.summary.scalar("acc",accuracy)

    # 高纬度变量收集
    tf.summary.histogram("weightes",weight)
    tf.summary.histogram("biases",bias)

    # 初始化变量op
    init_op = tf.global_variables_initializer()

    # 定义合并变量op
    merged = tf.summary.merge_all()

    # 创建一个saver
    saver = tf.train.Saver()

        # 开启会话训练
    with tf.Session() as sess:
        # 初始化变量
        sess.run(init_op)

        # 建立events文件写入
        filewriter = tf.summary.FileWriter("../tmp/",graph=sess.graph)

        if FLAGS.is_train == True:

            # 迭代步数去训练，更新参数去预测
            for i in range(2000):

                # 取出真实存在的特征值和目标值
                minst_x,minst_y = mnist.train.next_batch(50)

                # 运行train_op训练
                sess.run(train_op, feed_dict={x: minst_x, y_true:minst_y})

                # 写入每步训练的值
                summary = sess.run(merged,feed_dict={x: minst_x, y_true:minst_y})

                filewriter.add_summary(summary,i)

                print("训练第%d步，准确率为%f,损失值为%f" %(i,
                                               sess.run(accuracy,feed_dict={x: minst_x, y_true:minst_y}),
                                               sess.run(loss,feed_dict={x: minst_x, y_true:minst_y})))


            # 保存模型
            saver.save(sess,"../ckpt/fc_model")
        else:

            # 加载模型
            saver.restore(sess,"../ckpt/fc_model")

            # 如果是0，做出预测
            for i in range(100):

                # 每次测试一张图片
                x_text,y_text = mnist.test.next_batch(1)

                #
                print("第%d张图片，手写数字目标是%d，预测结果是%d" %(
                    i,
                    tf.argmax(y_text,1).eval(),
                    tf.argmax(sess.run(y_predict,feed_dict={x: x_text, y_true:y_text}),1).eval()
                ))

    return None

if __name__ == '__main__':
    full_connect()