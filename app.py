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


# 🔥 CAPTURA TODO (ESTO ARREGLA EL 404)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return "Ruta no válida en proxy"
def rewrite_html(content, base_url):
    content = content.replace('href="/', f'href="/proxy?url={base_url}/')
    content = content.replace('src="/', f'src="/proxy?url={base_url}/')
    return content