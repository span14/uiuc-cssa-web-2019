from cssa import create_app
from cssa.cli import register

app = create_app()
register(app)