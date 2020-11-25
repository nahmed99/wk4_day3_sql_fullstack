from flask import Flask, render_template, Blueprint

tasks_blueprint = Blueprint("tasks", __name__)

# using blueprint instead of route directly. This will be taken by app.py to attach to the app (flask) object in app.py. We are keeping app.py small and clean by moving most of the routes into this file.
@tasks_blueprint.route("/tasks")
def tasks():
    return render_template("tasks/index.html")