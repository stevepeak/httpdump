import os
import tornado.web
import tornado.ioloop
from json import dumps


class MainHandler(tornado.web.RequestHandler):
    def get(self, url):
        self.all(url)

    def post(self, url):
        self.all(url)

    def patch(self, url):
        self.all(url)

    def delete(self, url):
        self.all(url)

    def options(self, url):
        self.all(url)

    def all(self, url):
        res = dict(headers=self.request.headers,
                   body=self.request.body,
                   url=url,
                   query=self.request.arguments)
        print dumps(res, indent=True)
        self.finish(res)

application = tornado.web.Application([(r"/(.*)", MainHandler)])

if __name__ == "__main__":
    application.listen(os.getenv('PORT', 9999))
    tornado.ioloop.IOLoop.instance().start()
