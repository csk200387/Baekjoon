import base64
print(base64.b32encode(input().encode('UTF-8')).decode('ascii'))