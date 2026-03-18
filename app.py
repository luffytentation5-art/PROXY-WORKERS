from flask import Flask, request, Response
import requests

app = Flask(__name__)

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

@app.route("/fetch")
def fetch():
    url = request.args.get("url")

    if not url:
        return "No URL"

    try:
        r = requests.get(url, headers=HEADERS)
        return Response(r.content, content_type=r.headers.get("Content-Type"))
    except:
        return "Error"