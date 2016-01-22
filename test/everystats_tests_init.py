#! /usr/bin/python
# -*- coding: utf-8-unix; -*- 

################################## En-Tête ##################################
# Description du rôle du programme
"""
Environnement de test pour 'everystats': phase d'initialisation préalable
à l'ensemble des tests.
"""
#
# Auteurs et Licence: Voir fichier "AUTHORS"
#
#############################################################################

############################ Import des modules #############################
import sys, os

########################### Fonctions du programme ##########################

    
######################## Corps principal du programme #######################

# Définit comme prioritaires les chemins vers les modules utilisés par le
# projet
sys.path.insert(1, os.path.join(sys.path[0], "../external/lib/CherryPy-4.0.0"))
sys.path.insert(1, os.path.join(sys.path[0], "../lib/"))
sys.path.insert(1, os.path.join(sys.path[0], "../bin/"))

print "Chemins 'sys.path' initalisés à:\n{}\n".format(sys.path)
