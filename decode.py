# -*- coding: utf-8 -*-

import sys

if len(sys.argv) < 4:
    print( "Usage: " + sys.argv[0] + " secret audience token")
    print( "Verifies token is attached to the specified audience" )
    exit(-1)

secret = sys.argv[1]
audience = sys.argv[2]
token = sys.argv[3]

import jwt

token = jwt.decode(token, secret,verify=True, audience=audience)
print(token['sub'])
