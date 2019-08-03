## App Utilities
import os
import env
from db import mongo
from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap

from libs.data_extractor import get_data
from models.collection import Collection

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['DEBUG'] = True

Bootstrap(app)
mongo.init_app(app)


## Main View
@app.route('/')
def dashboard():

    return render_template('dashboard.html')


@app.route('/candidates', methods=['GET', 'POST'])
def candidates():
    candidates_data, max_prize = get_data()
    # Upload candidates to MongoDB
    mongodb = Collection()
    data = {}
    data['candidates_data'] = candidates_data
    try:
        mongodb.insert_data(data)
    except Exception as e:
        pass

    data_dict = {'candidates_data': candidates_data, 'max_prize': max_prize}
    return jsonify(data_dict)


@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error500(error):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()

# Heroku
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port)
