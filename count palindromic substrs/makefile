.PHONY: runnable clean tests test

runnable:
	chmod +x hw3.py
	chmod +x run_tests.py

clean:
	rm -rf tests
	rm -rf *.pyc

tests: clean runnable
	python testgen.py

test:
	./run_tests.py
