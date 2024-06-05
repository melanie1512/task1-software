coverage: ## Run tests with coverage
	pytest --cov=main test_structural.py

test: ## Run tests
	pytest test_structural.py