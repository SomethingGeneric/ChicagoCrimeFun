run:
	python3 ChicagoCrimeFun.py
format:
	black .
setup:
	python3 -m pip install -r requirements.txt
web:
	python3 web.py
test:
	python3 TestAVLTree.py
