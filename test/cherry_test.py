#! /usr/bin python
# -*- coding: utf-8-unix; -*-

import cherrypy
import os
		
	
class templateCherrypy(object):
	@cherrypy.expose
	def index(self):
		Fresult=open('../lib/everystats/blog.shtml')
		result=Fresult.read()
		return result
			
cherrypy.quickstart(templateCherrypy())


#~ resultat=\
	#~ """
		#~ <html lang="fr">
			#~ <head>
				#~ <meta charset="utf-8" />
			#~ </head>		
			#~ <body>
				#~ <h1>Nombre de visites sur votre site</h1>
				#~ <p>{0}</p>
			#~ </body>
		#~ </html>	
	#~ """
	
#~ MEDIA_DIR = os.path.join(os.path.abspath("../."), u"lib/everystats")
	#~ 
#~ class Utilisateur(object):
	#~ @cherrypy.expose
	#~ def index(self):
		#~ return open(os.path.join(MEDIA_DIR, u'visites.html'))
		#return page
	#~ 
	#~ @cherrypy.expose
	#~ def generer(self,select):	
		#~ return resultat.format(select)
#~ 
#~ cherrypy.quickstart(Utilisateur())
