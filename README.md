# Poketest

A toy API for demonstrating testing.

## Installation

Install all required libraries with `pip install -r requirements.txt`.

This project assumes you have an accessible local Postgres database called `pokemon` and that your name is `dan`; I'll generalise this later, but for now, edit your connection details in `pokefunctions.py`.

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

## Rationale

### Why do we test?

- Extensibility
- Saves time (less manual testing)
- Spot errors/bugs
- Maintainability
- Bus factor
  - Bus factor: the number of people who would need to be hit by a bus for the organisation to fail
- Industry standard
- Asked about it in interviews
- Forces you to write better code