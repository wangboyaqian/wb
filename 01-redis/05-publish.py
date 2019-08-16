import redis

r = redis.Redis(password="123456", decode_responses=True)

while True:
	channel = input("请输入您要发布的频道: ")
	message = input("请输入您要发布的内容: ")
	#向指定的指定的频道发送指定的消息
	r.publish(channel, message)