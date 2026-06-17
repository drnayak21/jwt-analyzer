import base64
import argparse
import json

parser = argparse.ArgumentParser(description="JWT TOKEN DECODER")
parser.add_argument("-t", "--token", required = True, help= "The full JWT token to decode")
args = parser.parse_args()

token = args.token

parts = token.split(".")
for i in range(len(parts)):
    decoded_part = base64.b64decode(parts[i] + "==")
    if i < 2:

        json_data = json.loads(decoded_part)

        if i == 0:
            header_part = json_data

        print(f"parts[{i}]: {parts[i]} \n")
        print(f"DECODED {i} : {json_data} \n")
    else:
        print(f"parts[{i}]: {parts[i]} \n")
        print(f"DECODED {i} : {decoded_part} \n")


if header_part.get("alg") == "none":
    print("[VULNERABLE] Algorithm is none - no signature required")
elif header_part.get("alg") in ["HS256", "HS384", "HS512"]:
    print(f"[WARNING] {header_part.get('alg')} detected - may be vulnerable to brute force if weak secret used")  
else:
    print(f"[OK] Algorithm: {header_part.get('alg')}")
