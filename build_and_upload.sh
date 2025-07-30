# ensure your python env is target env
# ensure edited pyproject.toml file
# ensure you have build and twine installed
# ensure configurated your ~/.pypirc file
python3 -m build
python3 -m twine upload --repository pypi dist/*