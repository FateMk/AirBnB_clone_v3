#!/usr/bin/python3

from models import storage
from api.v1.views import app_views

# Flask Applcation variables
app = Flask(__name__)
app.register_blueprint(app_views)

# begin flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")
 #   print(app.url_map)
    app.run(host=host, port=port)
