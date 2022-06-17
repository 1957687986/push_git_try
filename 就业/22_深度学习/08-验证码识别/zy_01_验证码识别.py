import tensorflow as tf

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string("captcha_dir","../data/tfrecords/captcha.tfrecords","验证码数据路径")
tf.app.flags.DEFINE_integer("batch_size",100,"每批次训练的样本数")
tf.app.flags.DEFINE_integer("label_num",4,"每个样本的目标值数量")
tf.app.flags.DEFINE_integer("letter_num",26,"每个目标值取得可能性个数")


# 定义初始化权重的函数
def weight_variables(shape):
    w = tf.Variable(tf.random_normal(shape=shape,mean=0.0,stddev=1.0))
    return w

def bais_variables(shape):
    b = tf.Variable(tf.constant(0.0,shape=shape))
    return b


def read_and_decode():
    """
    读取验证码数据API
    :return: image_batch,label_batch
    """
    # 1、构建文件队列
    file_queue = tf.train.string_input_producer([FLAGS.captcha_dir])

    # 2、构建读取阅读器，读取文件内容，默认一个样本
    reader = tf.TFRecordReader()

    # 3、读取内容
    key, value = reader.read(file_queue)

    # tfrecords格式example，需要解析
    features = tf.parse_single_example(value, features={
        "image":tf.FixedLenFeature([],tf.string),
        "label":tf.FixedLenFeature([],tf.string),
    })

    # 解码内容,字符串内容
    # 1、先解析图片特征值
    image = tf.decode_raw(features["image"],tf.uint8)

    # 2、解析图片目标值
    label = tf.decode_raw(features["label"],tf.uint8)

    print(image,label)

    # 改变形状
    image_reshape = tf.reshape(image,[20,80,3])

    label_reshape = tf.reshape(label,[4])

    print(image_reshape,label_reshape)

    # 进行批处理,每批次·读取的样本数，也就是每次训练的样本数
    image_batch,label_batch = tf.train.batch([image_reshape,label_reshape],batch_size=FLAGS.batch_size,num_threads=1,capacity=FLAGS.batch_size)

    print(image_batch,label_batch)

    return image_batch,label_batch


def fc_model(image):
    """
    进行预测结果
    :param image: 100图片特征值 [100,20,80,3]
    :return: y_predict
    """
    with tf.variable_scope("model"):
        # 将图片数据形状转换成二维
        image_reshape = tf.reshape(image,[-1,20*80*3])

        # 1、随机初始化权重，偏置
        # matrix  [100,20*80*3] * [20*80*3,4*26] + [104]
        weights = weight_variables([20*80*3,4*26])
        bias = bais_variables([4*26])

        # 进行全连接层计算[100,4*26]
        y_predict = tf.matmul(tf.cast(image_reshape,tf.float32),weights) +bias

    return y_predict

def predict_to_onehot(label):
    """
    将读取文件中的目标值转换成one-hot编码
    :param label: [100,4]  [[1,2,3,4],[]....]
    :return: one-hot
    """
    # 进行one_hot转换，提供给交叉熵损失计算，准确率计算[100,4,26]
    label_one_hot = tf.one_hot(label, depth=FLAGS.letter_num,on_value=1.0,axis=2)

    print(label_one_hot)

    return label_one_hot


def captcharec():
    """
    验证码识别程序
    :return: None
    """
    # 1、读取验证码数据文件  label_batch  [100,4]
    image_batch,label_batch = read_and_decode()

    # 2、输入图片特征数据，建立模型，得出预测结果
    # 一层全连接神经网络进行预测
    # matrix  [100,20*80*3] * [20*80*3,4*26] + [104]
    y_predict = fc_model(image_batch)

    # [100,4*26]
    print(y_predict)

    # 3、先把目标值转换成one-hot编码
    y_true = predict_to_onehot(label_batch)

    # 4、softmax计算，交叉熵损失计算[100,4,26]
    with tf.variable_scope("sotf_cross"):

        # 求平均交叉熵损失  y_true  [100,4,26]  ----->[100,4*26]
        loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
            labels=tf.reshape(y_true,[FLAGS.batch_size,FLAGS.letter_num*FLAGS.label_num]),
            logits=y_predict))

    # 5、梯度下降优化损失
    with tf.variable_scope("optimizer"):
        train_op = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

    # 6、计算每批次准确率   三维比较
    with tf.variable_scope("acc"):
        # 比较每个样本预测值与目标值是否位置（4个）一样
        # tf.argmax(y_true, 2)此2为
        #   0  1  2
        # [100,4,26]
        # tf.argmax(预测值,2)
        # y_predict  [100,4*26]转换成[100,4,26]
        equal_list = tf.equal(tf.argmax(y_true, 2), tf.argmax(tf.reshape(y_predict,[FLAGS.batch_size,FLAGS.label_num,FLAGS.letter_num]), 2))

        # 转换为float类型  equal_list有None个样本
        accuracy = tf.reduce_mean(tf.cast(equal_list, tf.float32))

    # 初始化变量op
    init_op = tf.global_variables_initializer()

    # 开启会话
    with tf.Session() as sess:
        sess.run(init_op)


        # 开启线程协调器和开启线程（有数据在文件中读取提供给模型）
        coord = tf.train.Coordinator()

        # 开启线程去运行读取文件操作
        threads = tf.train.start_queue_runners(sess,coord=coord)

        #训练识别程序
        for i in range(5000):
            # train_op代表着优化训练后的结果，代表着一个批次的结束
            sess.run(train_op)

            print("第%d批次的准确率为：%f" % (i,accuracy.eval()))

        # 回收线程
        coord.request_stop()

        coord.join(threads)

    return None


if __name__ == '__main__':
    captcharec()