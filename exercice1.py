# Exercice 1
#declaration de la chaine de caractére
words = "Le blog 'ledatascientist' est le blog français de référence en Data Science."
#La méthode split() décompose les grandes chaînes en plus petites.
#Par conséquent, le comptage des mots dans le tableau de chaînes sera basé non pas exactement sur les mots mais sur la façon dont le séparateur de fractionnement est défini.
words = words.split('.''')
words = [sentence.split() for sentence in words]
#La méthode sum() additionne les éléments de gauche à droite et renvoie la somme.
#La fonction len() renvoie le nombre des éléments (ou la longueur) dans un objet.
average = sum(len(word) for word in words)/len(words)
# print() affiche l'argument qu'on lui passe
print("la longueur moyenne des mots de notre texte est " + str(average) + " mots.")


