ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

SRC_FOLDER=$(ROOT_DIR)/src
BIN_FOLDER=$(ROOT_DIR)/bin
TEST_FOLDER=$(ROOT_DIR)/test-dir

TEST_NAME="Project_Test"
TEST_LANG="cpp"
TEST_OPT=
TEST_ARGS=$(TEST_LANG) $(TEST_NAME) $(TEST_OPT)


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
	python $(SRC_FOLDER)/new-project.py $(TEST_ARGS)
	cd $(ROOT_DIR)


#print number of lines
.phony: line_count
line_count:
	find $(SRC_FOLDER) -name '*.c' -o -name '*.h' -o -name '*.py' -o -name 'Makefile' | xargs wc -l

