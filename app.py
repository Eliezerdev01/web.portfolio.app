import logic.links as links
from engine import app, db
import utils.models as mods

with app.app_context():
    db.create_all()

app.run(debug=True, host="0.0.0.0")