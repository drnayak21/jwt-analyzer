# jwt-analyzer

A CLI tool to decode and analyze JWT tokens for common vulnerabilities.

## Features
- Decodes header and payload
- Detects `alg: none` vulnerability
- Warns on weak HMAC algorithms (HS256/HS384/HS512)

## Installation
```bash
pip install requests
```

## Usage
```bash
python main.py -t <jwt_token>
```

## Example Output
```
DECODED 0 : {'alg': 'HS256', 'typ': 'JWT'}
DECODED 1 : {'sub': '1234567890', 'name': 'John Doe', 'iat': 1516239022}
[WARNING] HS256 detected - may be vulnerable to brute force if weak secret used
```