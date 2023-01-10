import argparse
import ctypes
import json
import os

python_json = """
[
    {
        "name": "ABC",
        "greeting": "Hello"
    },
    {
        "name": "XYZ",
        "greeting": "Hi"
    }
]
"""


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--edr', type=str, default='qradar',
                        help='Type of EDR')
    args = parser.parse_args()
    so_file = os.path.join(os.sep, 'usr', 'local', 'bin',
                           f'{args.edr}_kestrel.so')
    json_functions = ctypes.CDLL(so_file)
    json_functions.transform_json.argtypes = [ctypes.c_char_p]
    json_functions.transform_json.restype = ctypes.c_char_p
    res_bytes = json_functions.transform_json(bytes(python_json, 'UTF-8'))
    res_str = res_bytes.decode('UTF-8')
    res_json = json.loads(res_str)
    print(json.dumps(res_json, indent=2))
