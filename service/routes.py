from hashlib import md5
from flask import redirect, render_template, current_app, request
from flask_login import login_required
from cssa.service import bp
from cssa.service.infoRequest import get_location

@bp.route("/index")
def index():
    link = "https://www.gravatar.com/avatar/{}?d=identicon&s={}".format(md5("123456".encode('utf-8')).hexdigest(), 36)
    
    locationInfo = get_location(request.remote_addr)
    if locationInfo[0] != 'Error':
        

    return render_template('service/index.html', link=link)