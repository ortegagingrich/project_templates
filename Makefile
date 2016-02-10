ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

SRC_FOLDER=$(ROOT_DIR)/src
BIN_FOLDER=$(ROOT_DIR)/bin
TEST_FOLDER=$(ROOT_DIR)/test-dir

TEST_NAME="Project_Test"
TEST_LANG="C"


.phony: clobber
clobber:
	find $(TEST_FOLDER)/* -type d -not -iname '.gitignore' | xargs rm -r


.phony: test
test:
	cd $(TEST_FOLDER); \
	python $(SRC_FOLDER)/new-project.py $(TEST_LANG) $(TEST_NAME)
	cd $(ROOT_DIR)


#print number of lines
.phony: line_count
line_count:
	find $(SRC_FOLDER) -name '*.c' -o -name '*.h' -o -name '*.py' -o -name 'Makefile' | xargs wc -l

