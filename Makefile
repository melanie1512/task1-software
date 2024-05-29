test: ## Run tests
	pytest test_structural.py

coverage: ## Run tests with coverage
	pytest --cov=example test_structural.py