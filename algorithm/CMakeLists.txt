cmake_minimum_required(VERSION 2.8)

include_directories(./include)

add_executable(util-test test/util-test.cpp)
add_executable(search-test test/search-test.cpp)
add_executable(sort-test test/sort-test.cpp)
add_executable(hello test/hello.cpp)