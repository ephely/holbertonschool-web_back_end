#!/usr/bin/env python3
""" Force locale with URL parameter """
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """ Configuration for Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()


def get_locale():
    """ Determine the best match with our supported languages """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ Retrieve user from mock database """
    login_as = request.args.get('login_as')
    if login_as:
        return users.get(int(login_as))
    return None


@app.before_request
def before_request():
    """ Detect user before request """
    g.user = get_user()


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """ Basic route """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
