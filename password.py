import hashlib
sha512 = hashlib.sha512()
sha384 = hashlib.sha384()
sha224 = hashlib.sha224()
sha512.update('cc123'.encode("utf-8"))
a = sha512.hexdigest()
a = a[::2]
sha384.update(str(a).encode("utf-8"))
a = sha384.hexdigest()
a = a[::2]
sha224.update(str(a).encode("utf-8"))
a = sha224.hexdigest()
a = a[::2]
sha512 = hashlib.sha512()
sha512.update(str(a).encode("utf-8"))
a = sha512.hexdigest()
a = a[::2]
print(a)
while True:
    sha512 = hashlib.sha512()
    sha384 = hashlib.sha384()
    sha224 = hashlib.sha224()
    sha512.update(str(input("passwd:")).encode("utf-8"))
    b = sha512.hexdigest()
    b = b[::2]
    sha384.update(str(b).encode("utf-8"))
    b = sha384.hexdigest()
    b = b[::2]
    sha224.update(str(b).encode("utf-8"))
    b = sha224.hexdigest()
    b = b[::2]
    sha512 = hashlib.sha512()
    sha512.update(str(b).encode("utf-8"))
    b = sha512.hexdigest()
    b = b[::2]
    if a == b:
        break
    else:
        print("密码错误")
