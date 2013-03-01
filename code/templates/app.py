from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop

class Handler(RequestHandler):

    def get(self):
        self.render("template.htm")


app = Application([("/", Handler)])
app.listen(8888)
IOLoop.instance().start()
