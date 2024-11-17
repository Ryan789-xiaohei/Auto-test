import os
# os.mkdir("testdir1")

# print(os.listdir("./"))
# os.removedirs("testdir")
# print(os.getcwd())
#
# print(os.path.exists("b"))
# if not os.path.exists("b"):
#    os.mkdir("b")
# if not os.path.exists("b/test1.txt"):
#    f =open("b/test1.txt","w")
#    f.write("小黑你好啊，加油哦")
#    f.close()

# import time
#
# # print(time.asctime())
# # print(time.time())
# # print(time.localtime())
# # print(time.strftime("%Y年%m月%d日 %H:%M:%S", time.localtime()))
#
# # 获取两天前的时间
# now_timestamp=time.time()
# two_day_before=now_timestamp-60*60*24*2
# time_tuple=time.localtime(two_day_before)
# print(time.strftime("%Y年%m月%d日 %H:%M:%S", time_tuple))

# import urllib.request
#
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.status)
# print(response.read())
# print(response.headers())
#
# import math
#
# print(math.ceil(8.9))
# print(math.floor(9.9))
# print(math.sqrt(48))
