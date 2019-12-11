# Timing attack with statistical analysis.
# The signature is calculated as s = HMAC(name||grade, k), where || indicates concatenation, k is the secret key.
# Signature is truncated to 10 bytes(20 hex digits).
# The function chrmp takes a lot of time. Takes longer time if the one char is correct.

# Program should take name and grade as parameters and should output a valid signature, 20 chars.

# Prova alla möjligheter för varje char, och om det tar märkbart längre tid innebär det att vi har en match.

import requests
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # Turns off annoying warnings about certificates. 


def http_request_time(URL, params):
    # Disables SSL verification since we don't have a valid certificate.
    r = requests.get(URL, params, verify=False)
    return r.elapsed.total_seconds()


def generate_chars():
    chars = []
    for i in range(16):
        char = hex(i)[2:]
        chars.append(char)
    return chars


def generate_signature(name, grade):
    URL = "https://eitn41.eit.lth.se:3119/ha4/addgrade.php"
    signature = ""
    possible_chars = generate_chars()
    params = {'name': name, 'grade': grade, 'signature': signature}
    for i in range(20):  # Signature is 20 chars long.
        max_time = 0
        for char in possible_chars:
            temp = signature + char
            params[signature] = temp

            current_time = http_request_time(URL, params)

            if current_time > max_time:
                max_time = current_time
                signature += char
        print("Working...")
    print(len(signature))
    print(signature)

generate_signature("Kalle", "5")