import os
import click

def register(app):

    @app.cli.group()
    def translate():
        pass
    
    @translate.command()
    def update():
        if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
            raise RuntimeError("extract command failed")
        if os.system('pybabel update -i messages.pot -d translations'):
            raise RuntimeError("update command failed")
        os.remove('messages.pot')
    
    @translate.command()
    def compile():
        if os.system('pybabel compile -d translations'):
            raise RuntimeError("compile command failed")
    
    @translate.command()
    @click.argument('lang')
    def init(lang):
        if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
            raise RuntimeError("extract command failed")
        if os.system('pybabel init -i messages.pot -d translations -l {}'.format(lang)):
            raise RuntimeError("init command failed")
        os.remove('messages.pot')