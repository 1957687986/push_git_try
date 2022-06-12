import tensorflow as tf

# 模拟一下异步子线程存入样本，主线程 读取样本

# 1、定义一个队列， 1000
Q = tf.FIFOQueue(1000,tf.float32)

# 2、定义子线程要做的事  值 + 1 放入队列当中
var = tf.Variable(0.0, tf.float32)

# 实现自增
data = tf.assign_add(var,tf.constant(1.0))

en_q = Q.enqueue(data)

# 3、定义队列管理器op， 指定多少个子线程及其该做的事
qr = tf.train.QueueRunner(Q, enqueue_ops=[en_q] * 2)

# 初始化变量op
init_op = tf.global_variables_initializer()


with tf.Session() as sess:
    # 初始化变量
    sess.run(init_op)

    # 开启线程管理器
    coord = tf.train.Coordinator()

    # 真正开启子线程
    threads = qr.create_threads(sess,coord=coord, start=True)

    # 主线程，不断地读取训练数据
    for i in range(300):
        print(sess.run(Q.dequeue()))

    # 主线程结束，意味着session关闭，意味着资源释放
    # 回收线程
    coord.request_stop()
    coord.join(threads)
