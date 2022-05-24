def print_line(char,num):

    print(char * num)

def print_Lines(char,num):
    """打印多行分隔符"""
    row = 0

    while row < 5 :
        print_line(char,num)

        row += 1

name = "程序员"