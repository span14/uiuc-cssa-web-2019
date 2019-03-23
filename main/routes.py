import os

from flask import render_template, request, current_app, url_for, flash, g, redirect, session
from flask_babel import _, get_locale, refresh, lazy_gettext as _l
from cssa.main import bp
from cssa.text import homeIntro

@bp.route('/')
@bp.route('/index')
def index():
    slides = []
    for fileA in os.listdir(current_app.config['HOME_CAROUSEL_FOLDER_LINK']):
        if fileA.endswith('.jpg'):
            slides.append((fileA.replace('.jpg', ''), 
                           url_for('static', filename='images/home/carousel/'+fileA)))
    
    return render_template('index.html', slides=slides, youtube=current_app.config['YOUTUBE'], info=homeIntro, title=_l("Home"))


@bp.route('/changelang', methods=['POST'])
def changelang():
    lang = request.form['changelang']
    if lang and lang in current_app.config['LANGUAGES']:
        session['language'] = lang
    return ("", 200)


@bp.before_request
def before_request():
    g.locale = str(get_locale())
