package main

import (
	"crypto"
	"crypto/rand"
	"crypto/rsa"
	"crypto/sha256"
	"crypto/x509"
	"encoding/base64"
	"encoding/pem"
	"fmt"
)

//# openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:1024
//# openssl rsa -in private_key.pem -out rsa_private_key.pem
//# openssl rsa -pubout -in private_key.pem -out public_key.pem

func main() {
	privateKeyPEM := `-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----`
	//signature_base64 := "ZCg4WUnNob4r+6xtbE7bz7WxS14funebGjmqGBF+dkJs2qdPFTokmVzOvAO/VBPVhu4hU941XCmGCbOK1vFaeNwElr3lran8CYKtOzSm9K3SgNE/4ZPdG1OQrKQlU7eKKa60RrWC6P9DUDX2jGaQ0tPyjoIJVvfkUjGe96XJ0qU="
	//	public_key_pem := `-----BEGIN PUBLIC KEY-----
	//MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDYRd9xBQPuduEXWNSMRrGkNaUs
	//fawnem1qMuIvFB+AprwT72/LhF5jy1gjEUsHQWKTV8HHVQDMfo9Argr1rbRTs9u+
	//FBcLcTpcGsILLt9LtMLC4WVHJ4ouTsnWe4JFNOJt4LoOW3hbS2yTJXP6BiE5flxp
	//kSwp7u0L1r+qu3r+OwIDAQAB
	//-----END PUBLIC KEY-----`

	//rr := VerifySignature(public_key_pem, signature_base64, "test_message")
	rr, err := MakeSignature(privateKeyPEM, "test_message")
	fmt.Println(rr, err)
}

func MakeSignature(privateKeyPem, message string) (string, error) {
	block, _ := pem.Decode([]byte(privateKeyPem))
	if block == nil || block.Type != "RSA PRIVATE KEY" {
		err := fmt.Errorf("Failed to decode PEM block containing private key")
		return "", err
	}
	privateKey, err := x509.ParsePKCS1PrivateKey(block.Bytes)
	if err != nil {
		fmt.Println("Failed to parse RSA private key: ", err)
		return "", err
	}
	hashed := sha256.Sum256([]byte(message))
	signature, err := rsa.SignPKCS1v15(rand.Reader, privateKey, crypto.SHA256, hashed[:])
	if err != nil {
		fmt.Printf("Error from signing: %s\n", err)
		return "", err
	}
	signatureBase64 := base64.StdEncoding.EncodeToString(signature)
	return signatureBase64, nil
}

func VerifySignature(publicKey, signatureBase64, message string) bool {
	// Decode the public key
	block, _ := pem.Decode([]byte(publicKey))
	if block == nil {
		return false
	}
	pub, err := x509.ParsePKIXPublicKey(block.Bytes)
	if err != nil {
		return false
	}
	rsaPub, ok := pub.(*rsa.PublicKey)
	if !ok {
		return false
	}

	signature, err := base64.StdEncoding.DecodeString(signatureBase64)
	if err != nil {
		return false
	}

	hashed := sha256.Sum256([]byte(message))
	err = rsa.VerifyPKCS1v15(rsaPub, crypto.SHA256, hashed[:], signature)
	if err != nil {
		return false
	} else {
		return true
	}
}

