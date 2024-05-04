import os
import sys

import msgpack
import sourcedefender  # pylint: disable=unused-import
import tgcrypto

# Save the original function references
original_ctr256_decrypt = tgcrypto.ctr256_decrypt

SOURCE_CODE = ""


# Define wrapper function with print behavior
def wrap_ctr256_decrypt(data: bytes, key: bytes, iv: bytes, state: bytes):
    global SOURCE_CODE
    result = original_ctr256_decrypt(data, key, iv, state)
    unpacked = msgpack.loads(result)
    SOURCE_CODE = unpacked.get("code")
    print(SOURCE_CODE)

    # Disable potentially dangerous code and return timestamp = 2999-01-01
    dummy_data = msgpack.dumps({"code": "", "eol_timestamp": 32472144000})
    return dummy_data


# Replace the original function with the wrapper in the tgcrypto module
tgcrypto.ctr256_decrypt = wrap_ctr256_decrypt


filename = os.path.splitext(sys.argv[1])[0]
__import__(filename)
