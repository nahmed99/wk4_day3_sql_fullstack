from flask import Flask, render_template

# from the controllers directory (a package), file (a module) tasks_controller import tasks_blueprint (a route)
from controllers.tasks_controller import tasks_blueprint


app = Flask(__name__)


# 'bring' the blueprint route into this module
app.register_blueprint(tasks_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
