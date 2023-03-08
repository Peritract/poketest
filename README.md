# Poketest

A toy API for demonstrating testing.

## Installation

Install all required libraries with `pip install -r requirements.txt`.

## Development

Run the program with `python api.py`.

If you're feeling fancy, you could do the following instead:

```sh
export FLASK_APP=api
export FLASK_DEBUG=true
export FLASK_RUN_PORT=8080
flask run
```

Or even

```sh
flask --app api run --port 8080 --debug
```

Pick your favourite; they all do basically the same thing.

## Testing

- Run all tests with `pytest`
- Check test coverage with `pytest --cov --cov-report=term-missing`

## Linting

Run `pylint *.py` to assess code quality.
