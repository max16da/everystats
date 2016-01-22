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

class everystats_vente(object):
    def __init__(self):
        print "fonction initialisation"
        return

	@cherrypy.expose
	def setTemplate(self):
		template_statsVente=\
		"""
			<html lang="fr">
				<head>
					<meta charset="utf-8" />
				</head>		
				<body>
					<h1>Statistique des ventes/stock</h1>
					<ul>
						<li><b>Livres vendus : </b>{statsLivreVente}</li>
						<li><b>Livres en stock :</b>{statsLivreStock}</li>
						<li><b>CD vendus :</b>{statsCdVente}</li>
						<li><b>CD en stock :</b>{statsCdStock}</li>
					</ul>
				</body>
			</html>	
		"""
		return template_statsVente
		
