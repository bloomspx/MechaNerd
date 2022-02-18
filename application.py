import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/", methods=["GET", "POST"])
def index():
    # TODO: Display the homepage
    return render_template("index.html")


@app.route("/keyboards", methods=["GET"])
def keyboards():
    return render_template("keyboards.html")

@app.route("/switches", methods=["GET"])
def switches():
    return render_template("switches.html")

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")
