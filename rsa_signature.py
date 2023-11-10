from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64

# openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:1024
# openssl rsa -in private_key.pem -out rsa_private_key.pem
# openssl rsa -pubout -in private_key.pem -out public_key.pem

signature_base64 = 'ZCg4WUnNob4r+6xtbE7bz7WxS14funebGjmqGBF+dkJs2qdPFTokmVzOvAO/VBPVhu4hU941XCmGCbOK1vFaeNwElr3lran8CYKtOzSm9K3SgNE/4ZPdG1OQrKQlU7eKKa60RrWC6P9DUDX2jGaQ0tPyjoIJVvfkUjGe96XJ0qU='
public_key_pem = '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDYRd9xBQPuduEXWNSMRrGkNaUs
fawnem1qMuIvFB+AprwT72/LhF5jy1gjEUsHQWKTV8HHVQDMfo9Argr1rbRTs9u+
FBcLcTpcGsILLt9LtMLC4WVHJ4ouTsnWe4JFNOJt4LoOW3hbS2yTJXP6BiE5flxp
kSwp7u0L1r+qu3r+OwIDAQAB
-----END PUBLIC KEY-----'''
private_key_string = '''-----BEGIN RSA PRIVATE KEY-----
MIICXgIBAAKBgQDYRd9xBQPuduEXWNSMRrGkNaUsfawnem1qMuIvFB+AprwT72/L
hF5jy1gjEUsHQWKTV8HHVQDMfo9Argr1rbRTs9u+FBcLcTpcGsILLt9LtMLC4WVH
J4ouTsnWe4JFNOJt4LoOW3hbS2yTJXP6BiE5flxpkSwp7u0L1r+qu3r+OwIDAQAB
AoGBAM5rSktd5RW6QzZ8Y0mLw8seJItlW2XGtR2yeS1EAJlTCpngYwyVR13qXDIE
NF81afeFv/8Xw45qkSHDu9QnOb8U6nJNBX7X+2+UI7XJkGHZBEJK1mL1Vk39suFa
2ep4+3Ms2YbvHVqa2ujV3FjJqu0A8xElVF+mVH0lWudhWe+ZAkEA7rbCuEC/Cofq
UU/eKUmh6w76up+qj4F7D4I0X9doq+gqA/4PiQqDxf9CU0UhF2atKJrzTliAa8TZ
y6i7vCOcPQJBAOfvGu6DyXAroDhJTYIbck9s6HEwqP/3TQqJyWpDA1JWOPEZxG73
0q7NPJVxbaCD2eMnGlBPW9r125+TP81HU9cCQQCeVEHai7cqePOFcv/bSqdGjOzo
EzbBcBP7OVUbrHgUbSxQ8ZXEQ2EbVi7bpCJKryNypzNxZ2nmEO6UEhpSsxvRAkBX
4UFTHpw05FLRAPVdVwj5D0sDmGxwkEOgupSWrs2TZRguQpUrdrtdgGZ0OYZQS6VD
bI2L4IXtcTrGPATwwxYBAkEAg+aSqtD46PwzlQPxLfdOepk37FyvWfo9wOeCQCbl
lLs2QHI5/guoMOfNMKPaIoum+V78hl1wXNCMZ4YnHKCYGg==
-----END RSA PRIVATE KEY-----'''


def verify_signature(signature_base64, message):
    signature = base64.b64decode(signature_base64)
    public_key = RSA.import_key(public_key_pem)
    message = message.encode('utf-8')
    hash = SHA256.new(message)
    try:
        pkcs1_15.new(public_key).verify(hash, signature)
        validation_result = True
    except (ValueError, TypeError):
        validation_result = False
    return validation_result


def make_signature(private_key_string, message):
    private_key = RSA.import_key(private_key_string)
    #public_key = key.publickey().export_key()
    message = message.encode('utf-8')
    hash = SHA256.new(message)
    signature = pkcs1_15.new(private_key).sign(hash)
    return base64.b64encode(signature).decode()

#rr = make_signature(private_key_string, 'test_message')
rr = verify_signature(signature_base64, 'test_message')
print(rr)

