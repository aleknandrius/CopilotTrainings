.PHONY: run

run:
	@echo "Please provide a valid example number. Usage: make run N"

run-%:
	@EXAMPLE_DIR=$$(find . -type d -name "$* Example*" | head -n 1); \
	if [ -n "$$EXAMPLE_DIR" ]; then \
		SCRIPT=$$(find "$$EXAMPLE_DIR" -maxdepth 1 -name "*.py" | head -n 1); \
		if [ -n "$$SCRIPT" ]; then \
			python3 "$$SCRIPT"; \
		else \
			echo "No Python script found in $$EXAMPLE_DIR"; \
		fi \
	else \
		echo "Folder for example $* not found"; \
	fi
