#!/bin/bash
SRC_FILE=$1
LIB_FILE="${SRC_FILE/\.c/.so}"
TGT_FILE="/usr/local/bin/${LIB_FILE}"
gcc -fPIC -shared -o ${LIB_FILE} ${SRC_FILE} cJSON.c -O3 -I. -lcjson
sudo cp ${LIB_FILE} ${TGT_FILE}
