le defis c'est de creer un systeme de traduction instantané

genre un lecteur vidéo ou on selectionne la langue et la voix sort
en cette langue peu importe la langue originale de la video

# 1 : ALGORITHME

    1.creer une interface contenant une video et un Select contenant plusieur langue pour choisir une langue
    2.lorqu'on choisi une langue la video est envoyé côté backend et ainsi que la langue choisie
    3.côté backend je dois me demerder pour traduire cette vidéo dans la langue chosie et renvoyé la video chosie au frontend

# 1.1 details du point 3

    1.tranformer la video en texte
        -Extraire l'audio de la vidéo
        -Transcrire l'audio en texte
    2.traduire le texte
    3.transformer le texte en audio
    4.lier l'audio a la video
