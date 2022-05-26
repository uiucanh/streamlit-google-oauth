VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
STREAMLIT = $(VENV)/bin/streamlit
run: $(VENV)/bin/activate
	$(STREAMLIT) run app.py --server.port 8080


$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt


clean:
	rm -rf __pycache__
	rm -rf $(VENV)