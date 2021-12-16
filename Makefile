run:
	python ChicagoCrimeFun.py
format:
	black .
setup:
	python -m pip install -r requirements.txt
web:
	python web.py
test:
	python TestAVLTree.py