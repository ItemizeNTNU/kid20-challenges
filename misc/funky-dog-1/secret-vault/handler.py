def read_from_file(path):
    try:
        f = open(path)
        return f.read()
    finally:
        f.close()


username = read_from_file("/var/openfaas/secrets/secret-username")
password = read_from_file("/var/openfaas/secrets/secret-password")
flag = read_from_file("/var/openfaas/secrets/flag")


def handle(req):
    request_username, request_password = req.split(":")
    if request_password == password and request_username == username:
        return "My little secret: " + flag
    else:
        return "No you! Wrong password and username"
