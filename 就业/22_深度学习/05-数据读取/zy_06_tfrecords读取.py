import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 定义cifar的数据等命令行参数
FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string("cifar_dir", "../data/cifar/cifar-10-batches-bin/","文件目录")
tf.app.flags.DEFINE_string("cifar_tfrecords", "../tmp/cifar.tfrecords","存进tfrecords中的文件")



class CifarRead(object):
    """
    完成读取二进制文件，写进tfrecords,读取tfrecords
    """
    def __init__(self,filelist):
        # 文件列表
        self.file_list = filelist

        # 定义读取图片的一些属性
        self.height = 32
        self.width = 32
        self.channel = 3
        # 二进制文件每张图片的字节
        self.label_bytes = 1
        self.image_bites = self.height * self.width * self.channel

        self.bytes = self.image_bites + self.label_bytes


    def read_and_decode(self):

        # 1、构造文件队列
        file_queue = tf.train.string_input_producer(self.file_list)

        # 2、构造二进制文件读取器,读取内容，每个样本字节数
        reader = tf.FixedLengthRecordReader(self.bytes)

        key, value = reader.read((file_queue))
        print(value)

        # 3、解码,二进制文件
        label_image = tf.decode_raw(value,tf.uint8)

        print(label_image)

        # 4、分割处理出图片与标签数据，切出特征值与目标值
        # label = tf.slice(label_image,[0],[self.label_bytes])

        label = tf.cast(tf.slice(label_image,[0],[self.label_bytes]),tf.int32)

        image = tf.slice(label_image,[self.label_bytes],[self.image_bites])

        print(label,image)

        # 5、可以对图片的特征数据进行形状的改变  [3072]  --->   [32,32,3]
        image_reshape = tf.reshape(image,[self.height,self.width,self.channel])

        print(label,image_reshape)

        # 6、批处理
        image_batch,label_batch = tf.train.batch([image_reshape,label], batch_size=10,num_threads=1,capacity=10)

        print(image_batch,label_batch)

        return image_batch,label_batch


    def write_ro_tfrecords(self, image_batch, label_batch):
        """
        将图片的目标值和特征值存进tfrecords
        :param image_batch: 100张图片的特征值
        :param label_batch: 100张图片的目标值
        :return: None
        """
        # 1、建立一个tfrecords文件存储器
        writer = tf.python_io.TFRecordWriter(FLAGS.cifar_tfrecords)

        # 2、循环的将所有样本都写入文件，每张图片样本都要构造example协议
        for i in range(10):
            # 去除第i个图片数据的特征值和目标值
            image = image_batch[i].eval().tostring()

            label = int(label_batch[i].eval()[0])

            # 构造一个样本的example
            example = tf.train.Example(features=tf.train.Features(feature={
                "image":tf.train.Feature(bytes_list=tf.train.BytesList(value=[image])),
                "label":tf.train.Feature(int64_list=tf.train.Int64List(value=[label])),
            }))

            # 写入单独的样本
            writer.write(example.SerializeToString())

        # 关闭
        writer.close()

        return None


    def read_from_tfrecords(self):

        # 1、构造文件队列
        file_queue = tf.train.string_input_producer([FLAGS.cifar_tfrecords])

        # 2、构造文件阅读器，读取内容example   value = 一个样本的序列化example
        reader = tf.TFRecordReader()

        key, value = reader.read(file_queue)

        # 3、解析example
        features = tf.parse_single_example(value, features={
            "image":tf.FixedLenFeature([],tf.string),
            "label":tf.FixedLenFeature([],tf.int64),
        })

        print(features["image"],features["label"])

        # 4、解码内容,如果读取的内容格式是string需要解码，如果是int64，float32不需要解码
        image = tf.decode_raw(features["image"],tf.uint8)

        label = features["label"]

        # print(image,label)

        # 固定图片形状，方便批处理
        image_reshape = tf.reshape(image,[self.height,self.width,self.channel])

        print(image_reshape,label)

        # 进行批处理
        image_batch, label_batch = tf.train.batch([image_reshape,label],batch_size=10,num_threads=1,capacity=10)

        return image_batch,label_batch


if __name__ == '__main__':
    # 1、找到文件放入列表   路径＋名字  -->列表当中
    file_name = os.listdir(FLAGS.cifar_dir)

    filelist = [os.path.join(FLAGS.cifar_dir, file) for file in file_name if file[-3:] == "bin"]

    # print(file_name)
    print(filelist)

    # image_resize = picread(filelist)
    cf = CifarRead(filelist)

    # 在读取tfrocords文件时注释下面
    image_batch,label_batch  = cf.read_and_decode()

    # 开启会话运行结果
    with tf.Session() as sess:
        # 定义一个线程协调器
        coord = tf.train.Coordinator()

        # 开启读文件的线程
        threads = tf.train.start_queue_runners(sess, coord=coord)

        cf.read_from_tfrecords()

        # 存进tfrecords文件
        # print("开始存储...")
        #
        # cf.write_ro_tfrecords(image_batch,label_batch)
        #
        # print("结束存储...")

        # 打印读取内容
        print(sess.run([image_batch,label_batch]))

        # 不要忘记回收子线程
        coord.request_stop()

        coord.join(threads)