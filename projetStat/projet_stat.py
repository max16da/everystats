#!/usr/bin/python2.7
#-*- coding:utf-8 -*-

import cherrypy

class Helloword(object):
	@cherrypy.expose
	def index(self):
		return "Hello worldd!"
		
cherrypy.quickstart(Helloword())
