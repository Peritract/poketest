"""An API for interacting with the pokemon database."""

from flask import Flask, request, jsonify

import pokefunctions

api = Flask(__name__)


@api.route('/pokemon', methods = ['GET', 'POST'])
def pokemon() -> list | dict:
    """Returns a list of pokemon, or adds a new one and returns it."""
    if request.method == 'GET':
        try:
            data = pokefunctions.get_all()
            return data
        except Exception as err:
            print(err)
            return jsonify({"error": True,
                            "Message": "Unable to retrieve pokemon"}), 500

    else:
        data = request.json
        new_pokemon = pokefunctions.add_one(data)
        return jsonify(new_pokemon), 201


if __name__ == "__main__":
    api.run(debug=True, port=8080)
