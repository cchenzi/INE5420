.RECIPEPREFIX = >

.PHONY: app
app: 
> poetry run python3 app/main.py

.PHONY: test
test:
> poetry run pytest

.PHONY: convert
convert: 
> poetry run pyuic5 $(ui_file) -o $(py_file)

.PHONY: format
format:
> poetry run black ./app
> poetry run black ./tests