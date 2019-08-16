import redis

r = redis.Redis(password="123456", decode_responses=True)

r.set("xxx","yyy")

print(r.get("xxx"))