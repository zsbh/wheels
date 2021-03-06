# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.18

# Default target executed when no arguments are given to make.
default_target: all

.PHONY : default_target

# Allow only one "make -f Makefile2" at a time, but pass parallelism.
.NOTPARALLEL:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Users/baohong/Library/Homebrew/Cellar/cmake/3.18.2/bin/cmake

# The command to remove a file.
RM = /Users/baohong/Library/Homebrew/Cellar/cmake/3.18.2/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/baohong/Documents/code/wheels

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/baohong/Documents/code/wheels

#=============================================================================
# Targets provided globally by CMake.

# Special rule for the target rebuild_cache
rebuild_cache:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Running CMake to regenerate build system..."
	/Users/baohong/Library/Homebrew/Cellar/cmake/3.18.2/bin/cmake --regenerate-during-build -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR)
.PHONY : rebuild_cache

# Special rule for the target rebuild_cache
rebuild_cache/fast: rebuild_cache

.PHONY : rebuild_cache/fast

# Special rule for the target edit_cache
edit_cache:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Running CMake cache editor..."
	/Users/baohong/Library/Homebrew/Cellar/cmake/3.18.2/bin/ccmake -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR)
.PHONY : edit_cache

# Special rule for the target edit_cache
edit_cache/fast: edit_cache

.PHONY : edit_cache/fast

# The main all target
all: cmake_check_build_system
	$(CMAKE_COMMAND) -E cmake_progress_start /Users/baohong/Documents/code/wheels/CMakeFiles /Users/baohong/Documents/code/wheels//CMakeFiles/progress.marks
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 all
	$(CMAKE_COMMAND) -E cmake_progress_start /Users/baohong/Documents/code/wheels/CMakeFiles 0
.PHONY : all

# The main clean target
clean:
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 clean
.PHONY : clean

# The main clean target
clean/fast: clean

.PHONY : clean/fast

# Prepare targets for installation.
preinstall: all
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall

# Prepare targets for installation.
preinstall/fast:
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall/fast

# clear depends
depend:
	$(CMAKE_COMMAND) -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 1
.PHONY : depend

#=============================================================================
# Target rules for targets named util_test

# Build rule for target.
util_test: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 util_test
.PHONY : util_test

# fast build rule for target.
util_test/fast:
	$(MAKE) $(MAKESILENT) -f algorithm/CMakeFiles/util_test.dir/build.make algorithm/CMakeFiles/util_test.dir/build
.PHONY : util_test/fast

#=============================================================================
# Target rules for targets named search_test

# Build rule for target.
search_test: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 search_test
.PHONY : search_test

# fast build rule for target.
search_test/fast:
	$(MAKE) $(MAKESILENT) -f algorithm/CMakeFiles/search_test.dir/build.make algorithm/CMakeFiles/search_test.dir/build
.PHONY : search_test/fast

#=============================================================================
# Target rules for targets named sort_test

# Build rule for target.
sort_test: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 sort_test
.PHONY : sort_test

# fast build rule for target.
sort_test/fast:
	$(MAKE) $(MAKESILENT) -f algorithm/CMakeFiles/sort_test.dir/build.make algorithm/CMakeFiles/sort_test.dir/build
.PHONY : sort_test/fast

#=============================================================================
# Target rules for targets named list

# Build rule for target.
list: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 list
.PHONY : list

# fast build rule for target.
list/fast:
	$(MAKE) $(MAKESILENT) -f algorithm/CMakeFiles/list.dir/build.make algorithm/CMakeFiles/list.dir/build
.PHONY : list/fast

#=============================================================================
# Target rules for targets named prototype_main

# Build rule for target.
prototype_main: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 prototype_main
.PHONY : prototype_main

# fast build rule for target.
prototype_main/fast:
	$(MAKE) $(MAKESILENT) -f design_pattern/CMakeFiles/prototype_main.dir/build.make design_pattern/CMakeFiles/prototype_main.dir/build
.PHONY : prototype_main/fast

#=============================================================================
# Target rules for targets named singleton_main

# Build rule for target.
singleton_main: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 singleton_main
.PHONY : singleton_main

# fast build rule for target.
singleton_main/fast:
	$(MAKE) $(MAKESILENT) -f design_pattern/CMakeFiles/singleton_main.dir/build.make design_pattern/CMakeFiles/singleton_main.dir/build
.PHONY : singleton_main/fast

#=============================================================================
# Target rules for targets named abstract_factory_main

# Build rule for target.
abstract_factory_main: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 abstract_factory_main
.PHONY : abstract_factory_main

# fast build rule for target.
abstract_factory_main/fast:
	$(MAKE) $(MAKESILENT) -f design_pattern/CMakeFiles/abstract_factory_main.dir/build.make design_pattern/CMakeFiles/abstract_factory_main.dir/build
.PHONY : abstract_factory_main/fast

#=============================================================================
# Target rules for targets named factory_method_main

# Build rule for target.
factory_method_main: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 factory_method_main
.PHONY : factory_method_main

# fast build rule for target.
factory_method_main/fast:
	$(MAKE) $(MAKESILENT) -f design_pattern/CMakeFiles/factory_method_main.dir/build.make design_pattern/CMakeFiles/factory_method_main.dir/build
.PHONY : factory_method_main/fast

#=============================================================================
# Target rules for targets named builder_main

# Build rule for target.
builder_main: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 builder_main
.PHONY : builder_main

# fast build rule for target.
builder_main/fast:
	$(MAKE) $(MAKESILENT) -f design_pattern/CMakeFiles/builder_main.dir/build.make design_pattern/CMakeFiles/builder_main.dir/build
.PHONY : builder_main/fast

#=============================================================================
# Target rules for targets named simple_factory_main

# Build rule for target.
simple_factory_main: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 simple_factory_main
.PHONY : simple_factory_main

# fast build rule for target.
simple_factory_main/fast:
	$(MAKE) $(MAKESILENT) -f design_pattern/CMakeFiles/simple_factory_main.dir/build.make design_pattern/CMakeFiles/simple_factory_main.dir/build
.PHONY : simple_factory_main/fast

#=============================================================================
# Target rules for targets named shared_test

# Build rule for target.
shared_test: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 shared_test
.PHONY : shared_test

# fast build rule for target.
shared_test/fast:
	$(MAKE) $(MAKESILENT) -f libsptr/CMakeFiles/shared_test.dir/build.make libsptr/CMakeFiles/shared_test.dir/build
.PHONY : shared_test/fast

#=============================================================================
# Target rules for targets named scoped_test

# Build rule for target.
scoped_test: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 scoped_test
.PHONY : scoped_test

# fast build rule for target.
scoped_test/fast:
	$(MAKE) $(MAKESILENT) -f libsptr/CMakeFiles/scoped_test.dir/build.make libsptr/CMakeFiles/scoped_test.dir/build
.PHONY : scoped_test/fast

#=============================================================================
# Target rules for targets named json_example

# Build rule for target.
json_example: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 json_example
.PHONY : json_example

# fast build rule for target.
json_example/fast:
	$(MAKE) $(MAKESILENT) -f libjson/CMakeFiles/json_example.dir/build.make libjson/CMakeFiles/json_example.dir/build
.PHONY : json_example/fast

#=============================================================================
# Target rules for targets named libjson

# Build rule for target.
libjson: cmake_check_build_system
	$(MAKE) $(MAKESILENT) -f CMakeFiles/Makefile2 libjson
.PHONY : libjson

# fast build rule for target.
libjson/fast:
	$(MAKE) $(MAKESILENT) -f libjson/CMakeFiles/libjson.dir/build.make libjson/CMakeFiles/libjson.dir/build
.PHONY : libjson/fast

# Help Target
help:
	@echo "The following are some of the valid targets for this Makefile:"
	@echo "... all (the default if no target is provided)"
	@echo "... clean"
	@echo "... depend"
	@echo "... edit_cache"
	@echo "... rebuild_cache"
	@echo "... abstract_factory_main"
	@echo "... builder_main"
	@echo "... factory_method_main"
	@echo "... json_example"
	@echo "... libjson"
	@echo "... list"
	@echo "... prototype_main"
	@echo "... scoped_test"
	@echo "... search_test"
	@echo "... shared_test"
	@echo "... simple_factory_main"
	@echo "... singleton_main"
	@echo "... sort_test"
	@echo "... util_test"
.PHONY : help



#=============================================================================
# Special targets to cleanup operation of make.

# Special rule to run CMake to check the build system integrity.
# No rule that depends on this can have commands that come from listfiles
# because they might be regenerated.
cmake_check_build_system:
	$(CMAKE_COMMAND) -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 0
.PHONY : cmake_check_build_system

