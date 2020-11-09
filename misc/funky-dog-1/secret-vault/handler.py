def read_from_file(path):
    try:
        f = open(path)
        return f.read()
    finally:
        f.close()


u = read_from_file("/var/openfaas/secrets/secret-username").strip()
p = read_from_file("/var/openfaas/secrets/secret-password").strip()
flag = read_from_file("/var/openfaas/secrets/flag")


def handle(req):
    username, password = req.split(":")
    if username == u and password == p:
        return "My little secret: " + flag
    else:
        return "No you! Wrong password or username."
