from flask import Flask, render_template, Blueprint, redirect, request
from repositories import task_repository
import repositories.user_repository as user_repository
from models.task import Task


tasks_blueprint = Blueprint("tasks", __name__)

# using blueprint instead of route directly. This will be taken by app.py to attach to the app (flask) object in app.py. We are keeping app.py small and clean by moving most of the routes into this file.
@tasks_blueprint.route("/tasks")
def tasks():
    # retrieve data from a database...
    tasks = task_repository.select_all()

    # pass the data from line above to the route in the render_tamplate
    return render_template("tasks/index.html", all_tasks=tasks)


# NEW
# GET '/tasks/new' -> show html form to create a new task
# We added the methods variable to be SPECIFIC that only want GET requests here.
@tasks_blueprint.route("/tasks/new", methods=["GET"])
def new_task():
    users = user_repository.select_all()
    # return render_template("tasks/new.html", all_users=['Colin', 'Niall', 'Peter'])
    # We are passing the list of user in  so that they can be added to a
    # drop-down list (for user to choose from - see new.html file)
    return render_template("tasks/new.html", all_users=users)

# CREATE
# POST '/tasks' -> handle the POST from the new form
# Note: This will be the same route as the one defined before the tasks() function
@tasks_blueprint.route("/tasks", methods=["POST"])
def create_task():
    # grab the form data for the description, user_id, duration and completed
    description = request.form['description']
    user_id = request.form['user_id']
    duration = request.form['duration']
    completed = request.form['completed']
    
    # select the user using the repository
    user = user_repository.select(user_id)
    
    # create a new task object
    task = Task(description, user, duration, completed)

    # save that new task object back to the database with the save method
    task_repository.save(task)

    return redirect('/tasks')


# SHOW
# GET '/tasks/<id>' -> Show some html for a specific task
@tasks_blueprint.route('/tasks/<id>')
def show_task(id):
    task = task_repository.select(id)
    return render_template("tasks/show.html", task=task)


# EDIT
# GET '/tasks/<id>/edit' -> Show some html form to edit a specific task


# UPDATE
# PUT '/tasks/<id>' -> handle the PUT from the edit form


# DELETE
# DELETE '/tasks/<id>' -> Handle the delete - to delete a specific task
# We can't use HTTP DELETE because HTML forms don't fo DELETE...so...we
# will use this unsecure method - this could be open to hacker attacks,
# by injecting dodgy html to potentially being able to delete many users...
@tasks_blueprint.route("/tasks/<id>/delete", methods=["POST"])
def delete_task(id):
    task_repository.delete(id)
    return redirect('/tasks')