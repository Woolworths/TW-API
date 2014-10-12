# github.com/woolworths
# see licence
from mechanize import Browser

class TW (object):
    def __init__(self, username, password, *args, **kwargs):
        self.username = username
        self.password = password
        self.world = kwargs.get('world', 77)
        self.server = kwargs.get('server', 'net') # net = .net, us = .us

        self.url = "http://www.tribalwars." + self.server

        self.br = Browser()
        self.br.open(self.url)
        self.br.select_form(name='login_form')

        for form in br.forms():
            print("Form name:" + form.name)
            print(form)

if __name__ == "__main__":
    tw = TW('s', 's', 13, server="net")
