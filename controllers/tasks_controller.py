from flask import Flask, render_template, Blueprint
from repositories import task_repository
import repositories.user_repository as user_repository


tasks_blueprint = Blueprint("tasks", __name__)

# using blueprint instead of route directly. This will be taken by app.py to attach to the app (flask) object in app.py. We are keeping app.py small and clean by moving most of the routes into this file.
@tasks_blueprint.route("/tasks")
def tasks():
    # retrieve data from a database...
    tasks = task_repository.select_all()

    # pass the data from line above to the route in the render_tamplate
    return render_template("tasks/index.html", all_tasks=tasks)


# NEW
# GET '/tasks/new' ==> show html form to create a new task
# We added the methods variable to be SPECIFIC that only want GET requests here.
@tasks_blueprint.route("/tasks/new", methods=["GET"])
def new_task():
    users = user_repository.select_all()
    # return render_template("tasks/new.html", all_users=['Colin', 'Niall', 'Peter'])
    return render_template("tasks/new.html", all_users=users)

# CREATE
# POST '/tasks' ==> handle the POST from the new form
# Note: This will be the same route as the on defined before the tasks() function
@tasks_blueprint.route("/tasks", methods=["POST"])
def create_task():
    print("post was called")

# SHOW
# GET '/tasks/<id>' ==> Show some html for a specific task

# EDIT
# GET '/tasks/<id>/edit' ==> Show some html form to edit a specific task

# UPDATE
# PUT '/tasks/<id>' ==> handle the PUT from the edit form

# DELETE
# DELETE '/tasks/<id>' ==> Handle the delete - to delete a specific task