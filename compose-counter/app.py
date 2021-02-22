from flask import Flask
import redis

redis = redis.from_url("redis://redis:6379")
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World! "+str(redis.incr("counter"))

if __name__ == '__main__':
    if not redis.exists("counter"):
        redis.set("counter", 0)
    app.run()
