#!/usr/bin/env python

import tornado.ioloop
import tornado.web

import psycopg2

class MainHandler(tornado.web.RequestHandler):
    def get(self):

	    conn = psycopg2.connect(database='alvin_generator')
	    cur = conn.cursor()
	    cur.execute('select * from alvin;')
	    db_data = cur.fetchone()
	    cur.close()

	    self.write("<h1>Hello, world ... %s</h1><img src='https://media.licdn.com/media/p/6/005/052/091/2826828.jpg' />" % db_data)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8001)
    tornado.ioloop.IOLoop.current().start()