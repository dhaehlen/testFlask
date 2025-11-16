from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return """<p>Hello from Flask + Gunicorn + Nginx!</p>
        <p>Hosted on my homelab</p>"""
        
    return app