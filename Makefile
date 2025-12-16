.PHONY: run test docker

run:
	uvicorn app.main:app --reload

test:
	pytest -q

docker:
	docker compose up --build