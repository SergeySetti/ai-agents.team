from flask import Flask, request, redirect

def create_app():
    app = Flask(__name__)

    @app.before_request
    def before_request():
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            return redirect(url, code=301)

    from . import main
    app.register_blueprint(main.bp)

    return app