# python-c-perf
Demo of python invoking C code.  Runs on Linux ubuntu.

### Install cJSON Package

1. Download the code: 
   ```
   git clone git@github.com:DaveGamble/cJSON.git
   ```
2. Install the pre-requisite build tools
   ```
   sudo apt update
   sudo apt install build-essential
   wget https://github.com/Kitware/CMake/releases/download/v3.25.1/cmake-3.25.1-linux-x86_64.sh
   sudo sh cmake-3.25.1-linux-x86_64.sh
   ```
3. Install cJSON:
   ```
   cd cJSON
   mkdir -p build
   cd build
   ${HOME}/cmake-3.25.1-linux-x86_64/bin/cmake ..
   make
   sudo make install
   ```

### C Code
The C code uses the cJSON package (https://github.com/DaveGamble/cJSON) to transform a JSON text from one format to another.

### Python Code
The Python code uses the `ctypes` package to invoke the C function that transforms the JSON string and retrieves the result of that function.

### To Run
1. Build the C library from the C code using the `build_lib.sh` script:
   ```
   ./build_lib.sh qradar_kestrel.c
   ```
2. Run the python code:
   ```
   python3 qradar_kestrel.py
   ```
