# ensure your python env is target env
# ensure configurated your ~/.pypirc file
python3 -m build
python3 -m twine upload --repository pypi dist/*