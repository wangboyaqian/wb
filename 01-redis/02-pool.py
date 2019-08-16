import redis

#创建连接池
pool = redis.ConnectionPool(password="123456", decode_responses=True)

#使用连接池对象去链接redis
r = redis.Redis(connection_pool=pool)

print(r.get("xxx"))
