run:
	python ChicagoCrime.py small_dataset.csv
format:
	black .
setup:
	python -m pip install -r requirements.txt
web:
	python web.py
test:
	python test_adt.py