# Timing attack with statistical analysis.
# The signature is calculated as s = HMAC(name||grade, k), where || indicates concatenation, k is the secret key.
# Signature is truncated to 10 bytes(20 hex digits).
# The function chrmp takes a lot of time. Takes longer time if the one char is correct.

# Program should take name and grade as parameters and should output a valid signature, 20 chars.

# Prova alla möjligheter för varje char, och om det tar märkbart längre tid innebär det att vi har en match.

import requests
import time
import urllib3

# Turns off annoying warnings about certificates.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def http_request_time(URL, params):
    # Disables SSL verification since we don't have a valid certificate.
    r = requests.get(URL, params, verify=False)
    time = r.elapsed.total_seconds()
    return time


def generate_chars():
    chars = []
    for i in range(16):
        char = hex(i)[2:]
        chars.append(char)
    return chars


def generate_signature(name, grade, URL):
    signature = ""
    possible_chars = generate_chars()
    params = {'name': name, 'grade': grade, 'signature': signature}
    iterations = 20
    for i in range(20):  # Signature is 20 chars long.
        max_time = 0.0
        subject_char = ''
        for char in possible_chars:
            temp = signature + char
            params['signature'] = temp

            request_times = []
            for i in range(iterations):
                request_times.append(http_request_time(URL, params))
            current_time = min(request_times)

            if current_time > max_time:
                max_time = current_time
                subject_char = char

        signature += subject_char
        print("Working...")
    print("The signature is: " + signature)


def main():
    name = input(str("Input the name: "))
    grade = input("Input the grade: ")
    URL = "https://eitn41.eit.lth.se:3119/ha4/addgrade.php"

    generate_signature(name, grade, URL)


main()
