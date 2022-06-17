import tensorflow as tf

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string("job_name"," ","启动服务类型是ps还是worker")
tf.app.flags.DEFINE_string("task_index",0,"指定ps或worker当中的哪一台服务器为task:0 or task:1")

def main(argv):
    # 定义全局计数op，给钩子列表当中的训练步数使用
    global_step = tf.contrib.framework.get_or_create_global_step()
    # 指定集群描述对象
    cluster = tf.train.ClusterSpec({
        "ps":["10.211.55.3:2223"],
        "worker":["10.24.154.116:2222"]
    })

    # 指定创建不同的服务
    server = tf.train.Server(cluster, job_name=FLAGS.job_name,task_index=FLAGS.task_index)

    # 根据不同的服务做不同的事情 ps 更新，保存参数 worker：指定设备去运行模型计算
    if FLAGS.job_name == "ps":
        # 参数服务器什么都不干，只需要等待worker传递参数
        server.join()
    else:
        worker_device = "/job:worker/task:0/cpu:0"
        # 可以指定设备去运行
        with tf.device(tf.train.replica_device_setter(
            worker_device= worker_device,
            cluster=cluster
        )):
            # 矩阵乘法运算
            x = tf.Variable([[1,2,3,4]])
            w = tf.Variable([[2],[2],[2],[2]])

            mat = tf.matmul(x,w)

        # 创建分布式会话
        with tf.train.MonitoredTrainingSession(
            master="grpc://10.24.154.116:2222", # 指定主worker
            is_chief= (FLAGS.task_index == 0), # 判断是否是主worker
            config=tf.ConfigProto(log_device_placement=True), # 打印设备信息
            hooks=[tf.train.StopAtStepHook(last_step=200)]
        ) as mon_sess:
            while not mon_sess.should_stop():
                print(mon_sess.run(mat))


if __name__ == '__main__':
    tf.app.run()