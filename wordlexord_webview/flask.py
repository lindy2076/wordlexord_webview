from flask import Flask, render_template, jsonify, request, Response

from . import __name__
from wordlexord_webview.utils import try_convert


flask_app = Flask(__name__)


@flask_app.route('/')
def main():
    return render_template("main.html")


@flask_app.route('/guide')
def guide():
    return render_template("guide.html")


@flask_app.route('/api/fast_convert/', methods=["POST"])
def fast_convert():
    req = request.form.get("data")
    print("wer:", req)
    success, result = try_convert(req)
    res = {"msg": result, "success": success}
    return jsonify(res)
