#! /usr/bin python
# -*- coding: utf-8-unix; -*-

import cherrypy
import os, sys
import everystats

CHEMIN_DONNEES_DEMO=os.path.abspath(os.path.dirname(__file__))
CHEMIN_SITE_DEMO=os.path.join(CHEMIN_DONNEES_DEMO,'blog.html')	
CHEMIN_TEMPLATE_VISITES=os.path.join(CHEMIN_DONNEES_DEMO,'visites.html')
CHEMIN_TEMPLATE_VENTES=os.path.join(CHEMIN_DONNEES_DEMO,'ventes.html')

class templateCherrypy(object):
    
    def __init__(self,statsRecues):
        self.stats=statsRecues
        return
        
    @cherrypy.expose
    def index(self):
        statsVisites=self.stats.listJeuxStats["statsVisites"]
        visites=statsVisites.getVal("visites")+1
        self.stats.updateVal("statsVisites","visites",visites)
        return self.stats.getContent()
		
    @cherrypy.expose
    def acheter(self):
        statsVentes=self.stats.listJeuxStats["statsVentes"]
        ventes=statsVentes.getVal("ventes")+1
        stocks=statsVentes.getVal("stock")-1
        self.stats.updateVal("statsVentes","ventes",ventes)
        self.stats.updateVal("statsVentes","stock",stocks)
        return self.stats.getContent()

def lancerDemo(contenuStats):
    cherrypy.quickstart(contenuStats)
			
