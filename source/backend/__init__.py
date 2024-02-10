# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# ----- Libraries
# ----------------------------------------------------------------------------------------
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

import re
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
    with open('database/colors.json', 'r') as json_file:          # todo path
        recipes_data = json.load(json_file)
        return recipes_data


def define_routes(app):
    @app.route("/")
    def index():
        import_data = retrieve_data_json()
        return render_template('index.html')

    @app.route("/colors")
    def json():
        import_data = retrieve_data_json()
        return render_template('colors.html', data=import_data)


    @app.template_filter('get_type_name')
    def get_type_name(obj):
        return type(obj).__name__
    
    @app.template_filter('hex_to_rgb')
    def hex_to_rgb(value):
        value = value.lstrip('#')
        rgb_values = [int(value[i:i+2], 16) for i in (0, 2, 4)]
        return ', '.join(map(str, rgb_values))





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
