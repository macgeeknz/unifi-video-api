import ssl



class Handle:

    def __init__(self, apikey, server):
        self.apikey = apikey
        self.server = server

        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE
