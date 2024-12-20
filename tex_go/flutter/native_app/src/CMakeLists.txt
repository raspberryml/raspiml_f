# The Flutter tooling requires that developers have CMake 3.10 or later
# installed. You should not increase this version, as doing so will cause
# the plugin to fail to compile for some customers of the plugin.
cmake_minimum_required(VERSION 3.10)

project(native_app_library VERSION 0.0.1 LANGUAGES C)

add_library(native_app SHARED
  "native_app.c"
)

set_target_properties(native_app PROPERTIES
  PUBLIC_HEADER native_app.h
  OUTPUT_NAME "native_app"
)

target_compile_definitions(native_app PUBLIC DART_SHARED_LIB)

if (ANDROID)
  # Support Android 15 16k page size
  target_link_options(native_app PRIVATE "-Wl,-z,max-page-size=16384")
endif()
