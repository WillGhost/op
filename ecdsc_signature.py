from ecdsa import SigningKey, VerifyingKey, SECP256k1, SECP112r2
from ecdsa.keys import BadSignatureError

private_key = SigningKey.generate(curve=SECP112r2)
print("Private Key:", private_key.to_string().hex())

public_key = private_key.verifying_key
public_key_hex = public_key.to_string().hex()
print("Public Key:", public_key_hex)

message = 'important data'
message = message.encode('utf-8')
signature = private_key.sign(message)
signature_hex = signature.hex()
print("Signature:", signature_hex)

# print(public_key.verify(signature, message))



#message = 'important data22'
#message = message.encode('utf-8')
vk = VerifyingKey.from_string(bytes.fromhex(public_key_hex), curve=SECP112r2)

try:
    rr = vk.verify(bytes.fromhex(signature_hex), message)
except BadSignatureError:
    rr = False
print('rrrrrrr', rr)
