import cherrypy
import os
from cherrypy.lib import httpauth
from pprint import pprint

class HelloWorld:
	def index(self):
		return "Hello World!"
	index.exposed = True

class MyServer:
	exposed = True
	def __call__(self, *args, **params):
		raise cherrypy.HTTPError(403, "Request Forbidden -- You are not allowed.")

	def GET(self, *args, **params):
		if len(args[0]) > 0:
			raise cherrypy.HTTPError(403, "Request Forbidden -- You are not allowed.")
		page = "MyServer GET ... </BR>\n"
		page += str(args) +"</BR>\n"
		page += str(params) + "</BR>\n"
		return page

if __name__ == '__main__':
	
	hwserver = HelloWorld()
	
	cherrypy.tree.mount(hwserver)
	cherrypy.server.unsubscribe()
	
	server = cherrypy._cpserver.Server()
	server.socket_port=8080
	server._socket_host="0.0.0.0"
	server.thread_poll=100
	server.subscribe()
	
	cherrypy.engine.start()
	cherrypy.engine.block()
	
