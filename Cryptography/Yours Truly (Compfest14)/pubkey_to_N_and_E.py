from Crypto.PublicKey import RSA
key_encoded='''-----BEGIN PUBLIC KEY-----
MIIBHzANBgkqhkiG9w0BAQEFAAOCAQwAMIIBBwKB/wEtcArErCGnnmBPHi777bWX
iRHb969U78LdmQk/AQ58FiVA6LilGoKvxpkNRtGujjvTJDjCz7wCGRe2K9tp1OQ3
c0Trwws0QUXLsySUx6DRyjc6anhA3PmpAsLL193vzhJLzN/t7om+btjbIyVRe6yA
u4VVP2mSixufIi+zwV8T3M7yHZUITykk0fO+t562dyiLS9F72772KyaI3bPKpGdp
vcXtUMJhi0bcH7WOCV07+RBGp5cml2znpHn7/pMbUxeO3wi8eSptEjU1ZwqiiViE
mkIYxr8tiXauNFDnMCMENj6A9ijq9d9ADLt9d+jWcyzrEp9p54PZoksqJO/6VQID
AQAB
-----END PUBLIC KEY-----'''


pubkey = RSA.importKey(key_encoded)
print(pubkey.n)
print(pubkey.e)
