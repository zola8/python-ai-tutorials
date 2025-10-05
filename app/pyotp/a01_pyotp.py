import time

import pyotp

key = "mysupersecretkey"
totp = pyotp.TOTP(key)

print(totp.now())

# time.sleep(30)
# print(totp.now())

input_code = input("Enter code: ")

print(totp.verify(input_code))
