from cryptography.hazmat.backends import default_backend
from cryptography.x509 import load_pem_x509_certificate

from service_identity.cryptography import extract_patterns


# Test certificates

PEM_DNS_ONLY = b"""\
-----BEGIN CERTIFICATE-----
MIIGbjCCBVagAwIBAgIDCesrMA0GCSqGSIb3DQEBBQUAMIGMMQswCQYDVQQGEwJJ
TDEWMBQGA1UEChMNU3RhcnRDb20gTHRkLjErMCkGA1UECxMiU2VjdXJlIERpZ2l0
YWwgQ2VydGlmaWNhdGUgU2lnbmluZzE4MDYGA1UEAxMvU3RhcnRDb20gQ2xhc3Mg
MSBQcmltYXJ5IEludGVybWVkaWF0ZSBTZXJ2ZXIgQ0EwHhcNMTMwNDEwMTk1ODA5
WhcNMTQwNDExMTkyODAwWjB1MRkwFwYDVQQNExBTN2xiQ3Q3TjJSNHQ5bzhKMQsw
CQYDVQQGEwJVUzEeMBwGA1UEAxMVd3d3LnR3aXN0ZWRtYXRyaXguY29tMSswKQYJ
KoZIhvcNAQkBFhxwb3N0bWFzdGVyQHR3aXN0ZWRtYXRyaXguY29tMIIBIjANBgkq
hkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxUH8iDxIEiDcMQb8kr/JTYXDGuE8ISQA
uw/gBqpvHIvCgPBkZpvjQLA23rnUZm1S3VG5MIq6gZVdtl9LFIfokMPGgY9EZng8
BaI+6Y36cMtubnzW53OZb7yLQQyg+rjuwjvJOY33ZulEthxhdB3km1Leb67iE9v7
dpyKeJ/8m2IWD37HCtXIEnp9ZqWOZkAPzlzDt6oNxj0s/l3z23+XqZdr+kmlh9U+
VWBTPppO4AJNwSqbBd0PgIozbYsp6urxSr40YQkIYFOOZQNs7HETJE71Ia7DQcUD
kUF1jZSYZnhVQwGPisqQLGodt9q9p2BhpSf0cUm02uKKzYi5A2h7UQIDAQABo4IC
7TCCAukwCQYDVR0TBAIwADALBgNVHQ8EBAMCA6gwEwYDVR0lBAwwCgYIKwYBBQUH
AwEwHQYDVR0OBBYEFGeuUvDrFHkl7Krl/+rlv1FsnsU6MB8GA1UdIwQYMBaAFOtC
NNCYsKuf9BtrCPfMZC7vDixFMDMGA1UdEQQsMCqCFXd3dy50d2lzdGVkbWF0cml4
LmNvbYIRdHdpc3RlZG1hdHJpeC5jb20wggFWBgNVHSAEggFNMIIBSTAIBgZngQwB
AgEwggE7BgsrBgEEAYG1NwECAzCCASowLgYIKwYBBQUHAgEWImh0dHA6Ly93d3cu
c3RhcnRzc2wuY29tL3BvbGljeS5wZGYwgfcGCCsGAQUFBwICMIHqMCcWIFN0YXJ0
Q29tIENlcnRpZmljYXRpb24gQXV0aG9yaXR5MAMCAQEagb5UaGlzIGNlcnRpZmlj
YXRlIHdhcyBpc3N1ZWQgYWNjb3JkaW5nIHRvIHRoZSBDbGFzcyAxIFZhbGlkYXRp
b24gcmVxdWlyZW1lbnRzIG9mIHRoZSBTdGFydENvbSBDQSBwb2xpY3ksIHJlbGlh
bmNlIG9ubHkgZm9yIHRoZSBpbnRlbmRlZCBwdXJwb3NlIGluIGNvbXBsaWFuY2Ug
b2YgdGhlIHJlbHlpbmcgcGFydHkgb2JsaWdhdGlvbnMuMDUGA1UdHwQuMCwwKqAo
oCaGJGh0dHA6Ly9jcmwuc3RhcnRzc2wuY29tL2NydDEtY3JsLmNybDCBjgYIKwYB
BQUHAQEEgYEwfzA5BggrBgEFBQcwAYYtaHR0cDovL29jc3Auc3RhcnRzc2wuY29t
L3N1Yi9jbGFzczEvc2VydmVyL2NhMEIGCCsGAQUFBzAChjZodHRwOi8vYWlhLnN0
YXJ0c3NsLmNvbS9jZXJ0cy9zdWIuY2xhc3MxLnNlcnZlci5jYS5jcnQwIwYDVR0S
BBwwGoYYaHR0cDovL3d3dy5zdGFydHNzbC5jb20vMA0GCSqGSIb3DQEBBQUAA4IB
AQCN85dUStYjHmWdXthpAqJcS3KD2JP6N9egOz7FTcToXLW8Kl5a2SUVaJv8Fzs+
wtbPJQSm0LyGtfdrR6iKFPf28Vm/VkYXPiOV08GD9B7yl1SjktXOsGMPlOHU8YQZ
DEsHOrRvaZBSA1VtBQjYnoO0pDVu9QwDLAPLFvFice2PN803HuMFIwcuQSIrh4nq
PqwitBZ6nPPHz7aSiAut/+txK3EZll0d+hl0H3Phd+ICeITYhNkLe90k7l1IFpET
fJiBDvG/iDAJISgkrR1heuX/e+yWfx7RvqGlMLIE35d+0MhWy92Jzejbl8fJdr4C
Kulh/pV07MWAUZxscUPtWmPo
-----END CERTIFICATE-----"""

DNS_IDS = extract_patterns(
    load_pem_x509_certificate(PEM_DNS_ONLY, default_backend())
)

PEM_CN_ONLY = b"""\
-----BEGIN CERTIFICATE-----
MIIDlzCCAn+gAwIBAgIUNS9qfJRgoLrr68mAfmhzBior0JAwDQYJKoZIhvcNAQEL
BQAwWzELMAkGA1UEBhMCQVUxEzARBgNVBAgMClNvbWUtU3RhdGUxITAfBgNVBAoM
GEludGVybmV0IFdpZGdpdHMgUHR5IEx0ZDEUMBIGA1UEAwwLZXhhbXBsZS5jb20w
HhcNMjMwNjA4MDkwNDAxWhcNNDkwMTI3MDkwNDAxWjBbMQswCQYDVQQGEwJBVTET
MBEGA1UECAwKU29tZS1TdGF0ZTEhMB8GA1UECgwYSW50ZXJuZXQgV2lkZ2l0cyBQ
dHkgTHRkMRQwEgYDVQQDDAtleGFtcGxlLmNvbTCCASIwDQYJKoZIhvcNAQEBBQAD
ggEPADCCAQoCggEBALltBNRAyeFczK2kdKTkW6E3/+rptXBcaw3SyltY/Ft8DPe3
lW/GWbbgAU7ceYC0LkYxOEnyQTlXhTyLHSk+PCQLi2ESgwWGnGY5Eusk1DRJ162q
hLUkmz25KdTILnh402fgoziF2RU6PnA7iIwAVntT5uh4S1yPW7TWkdPsE0tc1yBx
3SAHTXDkoahjKSot35Q87Jw92fxUd7WqVmDrgcLMvp8rXNjdg+HG4fQGoMcSQq2Z
nVPIoWSTOGdL6SzSs6Wvllz3n7YWShTqp9CmGctCGubt02fHF+8G/dMTTukntG4q
EjBtVfeDFx8yXUdOgN4egFxZGYATAUsLcyzNhQcCAwEAAaNTMFEwHQYDVR0OBBYE
FDkuqwU8KxIvwAwMqVpNFYlgd6WbMB8GA1UdIwQYMBaAFDkuqwU8KxIvwAwMqVpN
FYlgd6WbMA8GA1UdEwEB/wQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEBAJ9Nb/C0
2gkxhWm3S2/9onPMhFOxDLsYxBvZtJMeOvRRrJaxN2m0aXkm0Ww8Bq0qEegZE51m
0T57IOS256rQlxEnZNeAWT2tf8FEqQGjbI1c/prj420e6afn18x8CSQgiOG4PJ+S
YfufRjSHAYwiiNi+tiKBQ8jOuayFhih9/GsDJvAMW0HjaYZyG6jlA9p4bL1rSqD3
gE+upYhkpVN1lFRZAhxRZOVIqJV/ppHp9RAuawsUdSNKm+rnlaExJKoVys+tZL9+
djWWQVqnttYocQQ0umX4ydCTr1RM+7ziwWTR5kpOESA/gZePZQqeH9k+XrPEQtLn
6QBxk+Ft53ZPVso=
-----END CERTIFICATE-----
"""


PEM_OTHER_NAME = b"""\
-----BEGIN CERTIFICATE-----
MIID/DCCAuSgAwIBAgIJAIS0TSddIw6cMA0GCSqGSIb3DQEBBQUAMGwxFDASBgNV
BAMTC2V4YW1wbGUuY29tMSAwHgYJKoZIhvcNAQkBFhFib2d1c0BleGFtcGxlLmNv
bTEUMBIGA1UEChMLRXhhbXBsZSBJbmMxDzANBgNVBAcTBkJlcmxpbjELMAkGA1UE
BhMCREUwHhcNMTQwMzA2MTYyNTA5WhcNMTUwMzA2MTYyNTA5WjBsMRQwEgYDVQQD
EwtleGFtcGxlLmNvbTEgMB4GCSqGSIb3DQEJARYRYm9ndXNAZXhhbXBsZS5jb20x
FDASBgNVBAoTC0V4YW1wbGUgSW5jMQ8wDQYDVQQHEwZCZXJsaW4xCzAJBgNVBAYT
AkRFMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxGQUcOc8cAdzSJbk
0eCHA1qBY2XwRG8YQzihgQS8Ey+3j69Xf0mtWOlL6v23v8J1ilA7ERs87Y4nbV/9
GJVhC/jTMZmrC6ogwtVIl1wL8sTiHaQZ/4pbpx57YW3qCdefLQrZqAMUgAe20z0G
YVU97u5EGXHYahG4TnB3xN6Qd3BGKP7K69Lb7ZOES2Esq533AZxZShseYR4JNYAc
2anag2/DpHw6k8ZaxtWHR4SmxlkCoW5IPK0YypeUY91PFY+dxJQEewtisfALKltE
SYnOTWkc0K9YuLuYVogx0K285wX4/Yha2wyo6KSAm0txJayOhcrEP2/34aWCl62m
xOtPbQIDAQABo4GgMIGdMIGaBgNVHREEgZIwgY+CDSouZXhhbXBsZS5uZXSCC2V4
YW1wbGUuY29thwTAqAABhxAAEwAAAAAAAAAAAAAAAAAXhhNodHRwOi8vZXhhbXBs
ZS5jb20voCYGCCsGAQUFBwgHoBoWGF94bXBwLWNsaWVudC5leGFtcGxlLm5ldKAc
BggrBgEFBQcIBaAQDA5pbS5leGFtcGxlLmNvbTANBgkqhkiG9w0BAQUFAAOCAQEA
ACVQcgEKzXEw0M9mmVFFXL2SyDk/4oaDFZbnNfyUp+H7bnxdVBG2M3DzQQLw5yH5
k4GNPvHOKshBbaFcZWiG1sdrfQJy/UjIWnaC5410npfBv7kJWafKKxZzMq3gp4rd
jPO2LxuWcYVOnUtA3CBe12tRV7ynGU8KmKOsU9bOWhUKo8DJ4a6XHB+YwXeOTPyU
mG7XBpQebT01I3OijFJ+apKR2ubjwZE8l1+BAlTzHyUmmcTTWTQk8FTFcP3nZuIr
VyudDBMASs4yVGHzQxmMalYYzd7ZDzM1NrgfG1KyKWqZEA0MzUxiYdUbZN79xL52
EyKUOXPHw78G6zsVmAE1Aw==
-----END CERTIFICATE-----"""


PEM_EVERYTHING = b"""\
-----BEGIN CERTIFICATE-----
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
3HotzNMgpPpx8C2KKLKKaiIGRY0pg/WC6w==
-----END CERTIFICATE-----"""
