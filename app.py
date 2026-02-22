import logic.links as links
from engine import app, db
import utils.models as mods
from a2wsgi import ASGIMiddleware as production

with app.app_context():
    db.create_all()

app = production(app)                                 