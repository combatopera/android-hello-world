VENV_PATH = build/venv

.PHONY: test
test:
	python3 -m venv '$(VENV_PATH)'
	'$(VENV_PATH)'/bin/pip install --upgrade pip # Suppress warning.
	'$(VENV_PATH)'/bin/pip install wheel # Allow binary installs.
	'$(VENV_PATH)'/bin/pip install Cython # Needed to make setup.py runnable.
	'$(VENV_PATH)'/bin/pip install -e .
	'$(VENV_PATH)'/bin/android-hello
