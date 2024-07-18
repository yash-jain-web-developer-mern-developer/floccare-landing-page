import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")  # Assuming your main HTML file is named index.html

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), "dist")}),
        # Adjust "dist" to your actual build output directory
    ],template_path=os.path.join(os.path.dirname(__file__), "dist"))

if __name__ == "__main__":
    app = make_app()
    port = 8888  # Choose your desired port number
    app.listen(port)
    print("Server listening on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
