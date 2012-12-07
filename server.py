import cherrypy
import os
from cherrypy.lib import httpauth
from pprint import pprint

class HelloWorld:
	def index(self):
		return "Hello World!"
	index.exposed = True

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
	
