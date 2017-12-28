#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from datetime import datetime
import MySQLdb
from blog.models import *

def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Bienvenue sur mon blog !</h1>
              <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)

def accueil(request):
    """ Afficher tous les articles de notre blog"""
    articles = Article.objects.all()
    db = MySQLdb.connect(host="mysql-watersense.alwaysdata.net",  # your host, usually localhost
                         user="146622",  # your username
                         passwd="Android92",  # your password
                         db="watersense_db")  # name of the data base

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    # Use all the SQL you like
    cur.execute("SELECT * FROM eventLora")

    # print all the first cell of all the rows
    for row in cur.fetchall():
        print
        row[0]

    db.close()
    return render(request, 'blog/Untitled.html', {'date': row[0]})
    #return render(request, 'blog/accueil.html', {'derniers_articles': articles})

def lire(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'blog/lire.html', {'article': article})

def view_article(request, id_article):
    # Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
    if int(id_article) > 100:
        raise Http404

    return redirect(view_redirection)

def view_redirection(request):
    return HttpResponse("Vous avez été redirigé.")

def list_articles(request, year, month):
    # Il veut des articles ? Soyons fourbe et redirigeons-le vers djangoproject.com
    return redirect("https://www.djangoproject.com")

def date_actuelle(request):
    return render(request, 'blog/Date.html', {'date': datetime.now()})

def addition(request, nombre1, nombre2):
    total = int(nombre1) + int(nombre2)

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    #{"total": 8, "nombre1": 5, "nombre2": 3, "request": <WSGIRequest ...>}
    #clé du dictionnaire = total, nb1, nb2 ... & valeur des clés sont la valeur des variables
    return render(request, 'blog/addition.html', locals())