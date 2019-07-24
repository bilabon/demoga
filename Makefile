# -*- makefile -*-

# definitions
SHELL = /bin/bash
HOST          = 127.0.0.1
PORT          = 8089
CURRPATH      = $(shell pwd)

TEST_OPTIONS=--verbosity=3
PYTHONPATH=.:..

MANAGE=PYTHONPATH=$(PYTHONPATH) DJANGO_SETTINGS_MODULE=settings.localdev django-admin.py
MANAGE_TEST=PYTHONPATH=$(PYTHONPATH) DJANGO_SETTINGS_MODULE=settings.testing django-admin.py
manage:
ifndef CMD
	@echo Please, specify CMD argument to execute Django management command
else
	$(MAKE) clean
	$(MANAGE)  $(CMD)
endif

run:
	$(MAKE) clean
	$(MANAGE) runserver $(HOST):$(PORT) --verbosity=3

shell:
	$(MAKE) clean
	$(MANAGE) shell

clean:
	@echo Cleaning up *.pyc files
	-find . | grep '.pyc$$' | xargs -I {} rm {}

test:
	$(MAKE) clean
	TESTING=1 $(MANAGE_TEST) test $(TEST_OPTIONS)

m:
	$(MANAGE) makemessages --locale=ru --ignore=client/* --ignore=*.txt

c:
	$(MANAGE) compilemessages --locale=ru
