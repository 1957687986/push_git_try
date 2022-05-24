from distutils.core import setup

setup(name="zy_message", # 包名
      version="1.0",    # 版本
      description="zy's 发送和接受模块",
      long_description="完整的发送和接受模块",
      author="zy",
      author_email="zy.com",
      url="www.zy.com",
      py_modules=["zy_message.send_message",
                  "zy_message.receive_message"]
      )
