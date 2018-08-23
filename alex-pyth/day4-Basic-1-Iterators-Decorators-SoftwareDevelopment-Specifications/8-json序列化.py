

#
# info = {
#     'name':'gsy',
#     'age':22
# }
#
# f  = open("test.yaml.txt","w")
# f.write(str(info))
#
# f.close()
#
# #序列化就是把内存的数据对象变成字符串，存到了硬盘上面，


# import json
#
# info = {
#     'name':'gsy',
#     'age':22
# }
#
# f  = open("test.yaml.txt","w")
# f.write(json.dumps(info))   #直接读取info，write是不支持字典的，通过json.dump转换为字符串，
#
# f.close()
#
# #序列化就是把内存的数据对象变成字符串，存到了硬盘上面，



import pickle


def sayhi(name):
    print('helo',name)



info = {
    'name':'gsy',
    'age':22,
    'func':sayhi
}

f  = open("test.yaml.txt","wb")
print()
f.write(pickle.dumps(info))  #直接读取info，write是不支持字典的，通过json.dump转换为字符串，

f.close()

'''
�}q (X   nameqX   gsyqX   ageqKu.
此时在txt文本中写入的内容是二进制文件，所以不能正常显示，他其实和json一样，
'''
#序列化就是把内存的数据对象变成字符串，存到了硬盘上面，
