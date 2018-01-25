#
#
#

import sys

if len(sys.argv) < 4:
    print( "Usage: " + sys.argv[0] + " secret audience subject")
    print( "Produces a token with an audience claim" )
    exit(0)

secret = sys.argv[1]
audience = sys.argv[2]
subject = sys.argv[3]

import jwt

token = jwt.encode({'aud': audience, 'sub': subject}, secret, algorithm='HS256')
print(token)
