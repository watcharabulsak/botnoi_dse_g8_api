#!/usr/bin/python

import dseg8.team as team
import time
import os
from flask import Flask, abort, redirect, send_from_directory, Blueprint, Response, render_template  # , jsonify
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


@app.route('/')  # เมื่อเข้ามาที่ root
def index():
    return redirect("/web/index.html", code=302)


@app.route("/web", strict_slashes=False)  # เผื่อมีใครพิมพ์ /web เข้ามาตรงๆ
def home_page():
    return redirect("/web/index.html", code=302)


# @app.route("/test")
# def test_route():
#     return jsonify(team.get_team_df().values.tolist())


@app.route('/web/<path:filename>')  # ใช้ static html จาก folder static
def static_files(filename):
    file_name = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),  "templates", filename)

    if os.path.exists(file_name):
        return render_template(filename, team=team.get_team_df().values.tolist())
    else:
        # Return not found http status code 404 and use browser default 404 page
        return abort(404)


# Start flask
if __name__ == '__main__':
    app.run(threaded=True)
