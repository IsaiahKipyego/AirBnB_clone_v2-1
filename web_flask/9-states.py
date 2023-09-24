#!/usr/bin/python3
"""
Starts a flask web application for the airbnb template
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False, defaults={'id': None})
@app.route('/states/<id>', strict_slashes=False)
def states(id):
    """
    displays the states in the database
    """
    states = storage.all(State).values()
    if id is None:
        return render_template('9-states.html', states=states, city=False)
    else:
        for state in states:
            if state.id == id:
                return render_template('9-states.html', state=state, city=True)
        return render_template('9-states.html', city=False, not_found=True)


@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
