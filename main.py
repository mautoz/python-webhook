# Code from: https://blog.bearer.sh/consume-webhooks-with-python/
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/', methods=['POST'])
def respond():
    print(request.json)
    return Response(status=200)

if __name__ == "__main__":
    respond()