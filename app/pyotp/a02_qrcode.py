import pyotp
import qrcode

from a01_pyotp import totp

key = "mysupersecretkey"

uri = pyotp.totp.TOTP(key).provisioning_uri(name="user123", issuer_name="My Python App")

print(uri)

qrcode.make(uri).save("qrcode.jpg")

while True:
    print(totp.verify(input("Enter code: ")))
