import redis

r = redis.Redis(password="123456", decode_responses=True)

#创建一个管道对象
#自己去查pipeline
pipe = r.pipeline()

try:
	#pipe.set("name", "goudan")
	#链式操作,在以后封装的sql语句，全部是链式操作
	pipe.set("name", "xiaofang").set("age",29).set("sex",1)
except Exception as e:
	print(e)
	#把管道清空
	pipe.reset()
else:
	#执行操作
	pipe.execute()