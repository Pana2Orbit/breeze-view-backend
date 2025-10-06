# make venv
.PHONY: venv activate install ready run-local build run
venv:
	python3 -m venv .venv || python -m venv .venv
activate:
	@echo "Run: source .venv/bin/activate (or .venv\Scripts\activate.bat on Windows)"
install:
	@if [ -n "$$VIRTUAL_ENV" ]; then \
		poetry install || pip3 install -r requirements.txt || pip install -r requirements.txt; \
	else \
		echo "Virtual environment not activated. Run 'make activate' or 'source .venv/bin/activate' first."; \
	fi
ready:
	python3 -m venv .venv || python -m venv .venv && source .venv/bin/activate && poetry install || pip3 install -r requirements.txt || pip install -r requirements.txt
run-local:
	@if [ -n "$$VIRTUAL_ENV" ]; then \
		uvicorn app.main:app --reload --host 0.0.0.0 --port 8000; \
	else \
		echo "Virtual environment not activated. Run 'make activate' or 'source .venv/bin/activate' first."; \
	fi
build:
	docker build -t breeze-view-backend .
run:
	docker run -p 8000:8000 breeze-view-backend