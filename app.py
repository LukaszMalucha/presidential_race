## App Utilities
import os
import env
import datetime
from db import mongo
from twitter import twitter_api
from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from bson.json_util import dumps



app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['DEBUG'] = True

Bootstrap(app)
mongo.init_app(app)


trends_list = [["Mother's Day", "1124741"], ["MothersDay", "591302"], ["Moms", "536456"], ["Happy Mothers", "276271"],
            ["IPL2019Final", "126930"], ["HappyMothersDay2019", "111327"], ["Porzingis", "112398"],
            ["Doris Day", "108480"], ["lotteryseatupgrade", "33000"], ["Brault", "15000"]]

## Main View
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

app.route('/trends', methods=['GET', 'POST'])
def trends():
    try:





        trends = {'top_ten_trends': trends_list}
    except:
        trends = {}
    return jsonify(trends)


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