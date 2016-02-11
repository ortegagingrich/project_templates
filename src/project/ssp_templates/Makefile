ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

SRC_FOLDER=$(ROOT_DIR)/src
BIN_FOLDER=$(ROOT_DIR)/bin
TEST_FOLDER=$(ROOT_DIR)/test-dir

TEST_ARGS={}


.phony: install
install:
	python setup.py install


.phony: uninstall
uninstall:
	python setup.py uninstall


.phony: clobber
clobber:
	rm -rf *.pyc
	find $(TEST_FOLDER)/* -type d -not -iname '.gitignore' | xargs rm -r

.phony: test
test:
	cd $(TEST_FOLDER); \
	python $(SRC_FOLDER)/main.py $(TEST_ARGS)
	cd $(ROOT_DIR)


