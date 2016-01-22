#! /usr/bin python
# -*- coding: utf-8-unix; -*-

################################## En-Tête ##################################
# Description du rôle du programme
"""Lancement du gestionnaire des statistiques "everystats", intégrable dans toute application web pour gérer toutes sortes de statistiques, écrit en Python.

Il s'appuie sur la librairie CherryPy, un environnemet de développement web minimaliste pour Python.
"""
#
# Auteurs et Licence: Voir fichier "AUTHORS"
#
#############################################################################


############################ Import des modules #############################
import sys
import everystats
import site_demo_everystats as demo



########################### Classes du programme ##########################
class lanceurAppli(object):
    def __init__(self):
        demoStats=everystats.EveryStats("demoStats",
		                                demo.CHEMIN_SITE_DEMO)
        self.contentDemo=demo.templateCherrypy(demoStats)
        
        Stats_Visites_Site=everystats.JeuStats("statsVisites")
        Stats_Ventes_Site=everystats.JeuStats("statsVentes")		
		
        demoStats.addJeuStats(Stats_Visites_Site)
        demoStats.addJeuStats(Stats_Ventes_Site)
        
        Stats_Visites_Site.addStat("visites",int,0)
        Stats_Ventes_Site.addStat("ventes",int,0)
        Stats_Ventes_Site.addStat("stock",int,100)

        #~ Stats_Visites_Site.getContent()
        
        Stats_Visites_Site.setTemplate(demo.CHEMIN_TEMPLATE_VISITES)
        Stats_Ventes_Site.setTemplate(demo.CHEMIN_TEMPLATE_VENTES)
		
        return
        
		
    def lancer(self):
        """Lance le gestionnaire 'everystats'."""
        demo.lancerDemo(self.contentDemo)
        return 

########################### Fonctions du programme ##########################
def lancerAppli():
    lanceur=lanceurAppli()
    lanceur.lancer()
    
######################## Corps principal du programme #######################

if __name__ == "__main__":
    lancerAppli()

