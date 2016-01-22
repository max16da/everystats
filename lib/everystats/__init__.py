#! /usr/bin python
# -*- coding: utf-8-unix; -*-

################################## En-Tête ##################################
# Description du rôle du module
"""
Module à la création du modèle d'affichage (template)
"""
#
# Auteurs et Licence: Voir fichier "Authors"
#############################################################################
import site_demo_everystats
import os
import string
import cgi
############################# Classe du module #############################

class EveryStats(object):
    def __init__(self,refStat,fileTemplate):
        FTemplate=open(fileTemplate)
        self.template=string.Template(FTemplate.read())
        #~ self.template=string.Template('<html><body><p>Visites : $statsVisites</p></body></html>')
        self.listJeuxStats={} 
        return
	
    def addJeuStats(self,jeuStats):
        self.listJeuxStats[jeuStats.nom]=jeuStats
        return
		
    def getContent(self):
        #d={'statsVisites':'Mon bloc Visites'}
        content=self.template.substitute(self.listJeuxStats)
        #content="<html><body><p>Dico: {}</p></body></html>".format(cgi.escape(str(self.listJeuxStats)))
        return content
        
    def updateVal(self,jeuStats,nomStat,valStat):
        stats=self.listJeuxStats[jeuStats]
        stats.updateVal(nomStat,valStat)
        return
    
class JeuStats(object):
    def __init__(self,nomJeuStats):
        self.nom=nomJeuStats
        self.listStatsType={}
        self.listStats={}
        self.template=None
        return 

    def addStat(self,nomStat,typeStat,valInit):
        valeur=valInit
        self.listStatsType[nomStat]=typeStat
        self.listStats[nomStat]=valeur
        return
    
    def getVal(self,nomStat):
        return self.listStatsType[nomStat](self.listStats[nomStat])
    
    def updateVal(self,nomStat,valStat):
        self.listStats[nomStat]=self.listStatsType[nomStat](valStat)
        return
        
    def setTemplate(self,fileTemplate):
        FTemplate=open(fileTemplate)
        self.template=string.Template(FTemplate.read())
        return
    
    def getContent(self):
        #content="contenu de {}".format(self.nom)
        content=None
        if self.template:
            content=self.template.substitute(self.listStats)
        return content
        
    def __str__(self):
        str_repr=self.getContent()
        if str_repr is not None:
            return str_repr
        else:
            return cgi.escape(repr(self))
