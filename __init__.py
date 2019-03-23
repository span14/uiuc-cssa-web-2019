from flask import Flask, request, current_app, g, session
from flask_babel import Babel, refresh
from flask_login import LoginManager
from cssa.config import DevConfig
from cssa.authentication.forms import is_hidden_field

# need to read flask-security to add in more secure methods
# need to look up cookie setting in flask-login for security consideration 
# need to set up https credentials

babel = Babel()
login_manager = LoginManager()

def create_app(config_class=DevConfig):
    
    app = Flask(__name__)
    babel.init_app(app)
    login_manager.init_app(app)
    app.config.from_object(config_class)

    from cssa.main import bp as main
    app.register_blueprint(main)

    from cssa.authentication import bp as auth
    app.register_blueprint(auth, url_prefix='/auth')
    
    from cssa.service import bp as service
    app.register_blueprint(service, url_prefix="/service")

    # set jinja2 external function
    app.jinja_env.globals['bootstrap_is_hidden_field'] = is_hidden_field

    return app

@babel.localeselector
def get_locale():
    if 'language' in session:
        return session['language']
    return request.accept_languages.best_match(current_app.config['LANGUAGES'], default='en')