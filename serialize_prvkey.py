from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import base64

with open(r"D:\cert\rsa_private_key.p8", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

private_key_der = private_key.private_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
private_key_b64 = base64.b64encode(private_key_der).decode('utf-8')
print(private_key_b64)
