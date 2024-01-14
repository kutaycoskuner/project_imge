# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# ----- Libraries
# ----------------------------------------------------------------------------------------
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

import json

# ----------------------------------------------------------------------------------------
# ----- Global States
# ----------------------------------------------------------------------------------------
app_state = {'is_edit_mode': False}

# ----------------------------------------------------------------------------------------
# ----- Main
# ----------------------------------------------------------------------------------------


def create_flask_app():
    app = Flask(
        __name__,
        static_folder='../frontend/static/',            # todo path
        template_folder='../frontend/templates/',         # todo path
    )
    app.config['SECRET_KEY'] = "rthrthaeradasdzdvzcvets"        # todo key
    return app


def retrieve_data_json():
    with open('database/recipes.json', 'r') as json_file:          # todo path
        recipes_data = json.load(json_file)
        return recipes_data




def define_routes(app):
    @app.route("/")
    def index():
        recipes_data = retrieve_data_json()
        return render_template('index.html')

    @app.route("/json")
    def json():
        return render_template('json.html')



# ----------------------------------------------------------------------------------------
# ----- Initialize
# ----------------------------------------------------------------------------------------


def start():
    # retrieve data
    recipes_data = retrieve_data_json()

    # create application
    app = create_flask_app()
    define_routes(app)
    app.run(debug=True)
