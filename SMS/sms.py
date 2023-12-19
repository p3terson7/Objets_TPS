# -*- coding: utf-8 -*-
# Ce script permet d'envoyer un courriel à partir de votre compte gMail
# Vous devez obtenir un mot de passe d'application de 16 caractères: AAAA BBBB CCCC DDDD
# Affectez ce mot de passe à la variable gmail_app_motPasse
# =============================================================================
#!/usr/bin/python3
import smtplib # si manquant -> pip install secure-smtplib

USER = 'videopoi.dofuus@gmail.com'
PASS = 'drtk incm kpog idnn'

gmail_utilisateur = USER
gmail_app_motPasse = PASS  # obtenu de Google
de = gmail_utilisateur
vers = gmail_utilisateur
sujet = "URGENT"
try:
    corps = "Bonjour!\n\nUne image suspecte a été prise par votre Raspberry PI!"
    leCourriel = """\
From: %s
To: %s
Subject: %s

%s
""" % (de, vers, sujet, corps)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_utilisateur, gmail_app_motPasse)
    server.sendmail(de, vers, leCourriel.encode('utf-8')) # latin pour Outlook
    server.close()
    print('Courriel envoyé!')
except Exception as exception:
    print("Erreur: %s!\n\n" % exception)