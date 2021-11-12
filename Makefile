run:
	python ChicagoCrime.py
format:
	black .
setup:
	python -m pip install -r requirements.txt
web:
	python visualize.py