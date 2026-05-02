# CodeCompass Makefile
# IBM Bob Dev Day Hackathon | Powered by IBM watsonx.ai

.PHONY: install run test lint docker-build docker-run clean

install:
	pip install -r requirements.txt

run:
	uvicorn main:app --host 0.0.0.0 --port 8000 --reload

test:
	pytest --tb=short -v --cov=. --cov-report=term-missing

lint:
	python -m py_compile main.py analyzer.py && echo "Syntax OK"

docker-build:
	docker build -t codecompass .

docker-run:
	docker run -p 8000:8000 --env-file .env codecompass

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
