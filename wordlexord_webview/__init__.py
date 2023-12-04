import webview

from wordlexord_webview.flask import flask_app


def app():
    webview.create_window('Wordlexord + Flask', flask_app, width=1800, height=1000)  
    webview.start()
