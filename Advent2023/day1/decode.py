import base64
import json

encoded_string = "WAAAAAAAAADgAAAMAAAAAAAAAAAAAAAAAABgAAAAAAA4AAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAYAAAAAAAAAAgAAAAAAAAACAAAAAAAAAAIAAAAAAAAAA=="
decoded_bytes = base64.b64decode(encoded_string)
decoded_string = decoded_bytes.decode('utf-8', errors='ignore')
gpu_preferences = json.loads(decoded_string)
print(gpu_preferences)


