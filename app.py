from tornado.options import define, options
import tornado.ioloop
import tornado.web
import tornado.httpserver


class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self._async_callback()

    def _async_callback(self):
        self.write("Hello, world!")
        self.finish()

app = tornado.web.Application([
    (r"/", MainHandler),
])

define("port", default="5555", help="Port to listen on")

if __name__ == "__main__":
    tornado.options.parse_command_line()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(options.port)
    # autodetect cpu cores and fork one process per core
    try:
        server.start(0)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()
