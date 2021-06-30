


def encrypt_RSA(message):
    with open(SINA_PUB_FILE) as f:
        key = f.read()
    pubkey = str(key).encode('utf8')
    bio = BIO.MemoryBuffer(pubkey)
    rsa = RSA.load_pub_key_bio(bio)
    encrypted = rsa.public_encrypt(message, RSA.pkcs1_padding)
    return encrypted.encode('base64').strip()

def decrypt_RSA(package):
    with open(RSA_PRI_FILE) as f:
        key = f.read()
    priv_key = BIO.MemoryBuffer(key.encode('utf-8'))
    key = RSA.load_key_bio(priv_key)
    decrypted = key.private_decrypt(b64decode(package), RSA.pkcs1_padding)
    return decrypted

def make_rsa_sum(text):
    m = EVP.MessageDigest("sha1")
    m.update(text)
    digest = m.final()
    key = RSA.load_key(SIGN_PRI_FILE)
    return base64.b64encode(key.sign(digest, 'sha1'))

def verify_sign(text, signature):
    ''' pub_key & text & sign 三者验签 '''
    m = EVP.MessageDigest("sha1")
    m.update(text)
    digest = m.final()
    k = RSA.load_pub_key(SINA_SIGN_PUB_FILE)
    return k.verify(digest, base64.b64decode(signature), 'sha1')

