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


############################# Classe du module #############################
import cherrypy
import os

class everystats_visite(object):

	@cherrypy.expose
	def setTemplate(self):
		template_statsVisite=\
		"""
			<html lang="fr">
				<head>
					<meta charset="utf-8" />
				</head>		
				<body>
					<h1>Nombre de visites</h1>
					<p>{statsVisite}</p>
				</body>
			</html>	
		"""
		return template_statsVisite
		
