import yagmail
from nameko.rpc import rpc


class Mail(object):
    name = "email"

    @rpc
    def send(self, to, subject, contents):
        yag = yagmail.SMTP('some@email.com', 'somepass')
        yag.send(to=to.encode('utf-8'),
                 subject=subject.encode('utf-8'),
                 contents=[contents.encode('utf-8')])
