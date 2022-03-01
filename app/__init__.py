"""A simple flask web app"""
from flask import Flask, render_template


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    @app.route("/")
    def index():
        name = "Prem Kumar's"
        return render_template('index.html', name=name)

    @app.route("/about")
    def about():
        name = "Prem Kumar's"
        return render_template('about.html', name=name)

    return app
