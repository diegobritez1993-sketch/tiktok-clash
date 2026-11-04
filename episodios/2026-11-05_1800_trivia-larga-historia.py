"""TRIVIA LARGA (YouTube 16:9) — historia de Clash of Clans. Jueves 5/11/2026 18:00.
Fuente de todos los datos: Wikipedia, "Clash of Clans" (consultada el 04/11/2026):
iOS 2/8/2012; anuncio del Super Bowl XLIX (feb 2015) con Liam Neeson; Base del constructor: actualización del 22/5/2017;
Juegos del clan dic 2017, Liga de guerras de clanes oct 2018, Equipamiento de héroes dic 2023; "Clash With Haaland" mayo 2024.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from trivia_larga import TriviaLarga, main

K = "capturas/kit_creador/"
EP = TriviaLarga(
    title="Trivia larga: historia de Clash",
    intro=dict(kicker="SOLO EL 1% ACIERTA LAS 5", lines=[("¿CUÁNTO SABÉS", "w"), ("DE LA HISTORIA", "w"), ("DE CLASH?", "y")],
               vo="Trivia de Clash. Cinco preguntas sobre la historia del juego, con treinta segundos para cada una. ¿Te animás?",
               sticker=K + "jinete_elefante_mangual.png", bg=K + "arte_aniversario_fiesta.jpg"),
    preguntas=[
        dict(q="¿EN QUÉ AÑO SALIÓ CLASH OF CLANS EN IPHONE?", options=["2010", "2012", "2014"], answer=1,
             vo="Pregunta uno. ¿En qué año salió Clash of Clans en iPhone? ¿Dos mil diez, dos mil doce o dos mil catorce?",
             dato="Salió el 2 de agosto de 2012 (en Android llegó en 2013)",
             vo_dato="¡La be! Salió el dos de agosto de dos mil doce.",
             source="Wikipedia, \"Clash of Clans\"", sticker=K + "torta_aniversario_14.png", bg=K + "arte_aniversario_paisaje.jpg"),
        dict(q="¿QUÉ ACTOR PROTAGONIZÓ EL COMERCIAL DE CLASH EN EL SUPER BOWL 2015?",
             options=["LIAM NEESON", "DWAYNE JOHNSON", "KEANU REEVES"], answer=0,
             vo="Pregunta dos. ¿Qué actor protagonizó el comercial de Clash en el Super Bowl dos mil quince?",
             dato="Liam Neeson, parodiando su papel en la película \"Búsqueda implacable\"",
             vo_dato="¡La a! Fue Liam Neeson, en un comercial que se hizo viral.",
             source="Wikipedia, \"Clash of Clans\"", sticker=K + "estatua_rey_barbaro.png", bg=K + "humor_barbaro_cine_palomitas.jpg"),
        dict(q="¿EN QUÉ AÑO LLEGÓ LA BASE DEL CONSTRUCTOR?", options=["2015", "2017", "2019"], answer=1,
             vo="Pregunta tres. ¿En qué año llegó la base del constructor? ¿Dos mil quince, dos mil diecisiete o dos mil diecinueve?",
             dato="Llegó con la actualización del 22 de mayo de 2017",
             vo_dato="¡La be! Llegó en mayo de dos mil diecisiete.",
             source="Wikipedia, \"Clash of Clans\"", sticker=K + "edificio_cabana_constructor_dorada.png", bg=K + "arte_coliseo_en_las_nubes.jpg"),
        dict(q="¿CUÁL DE ESTAS TRES LLEGÓ PRIMERO AL JUEGO?",
             options=["JUEGOS DEL CLAN", "LIGA DE GUERRAS DE CLANES", "EQUIPAMIENTO DE HÉROES"], answer=0,
             vo="Pregunta cuatro. ¿Cuál de estas tres llegó primero al juego? ¿Juegos del clan, Liga de guerras de clanes, o Equipamiento de héroes?",
             dato="Juegos del clan: diciembre de 2017. Liga de guerras: 2018. Equipamiento: 2023",
             vo_dato="¡La a! Los Juegos del clan llegaron en diciembre de dos mil diecisiete.",
             source="Wikipedia, \"Clash of Clans\"", sticker=K + "medalla_dorada_rombo.png", bg=K + "arte_batalla_esqueletos_bruja.jpg"),
        dict(q="¿CON QUÉ FUTBOLISTA HIZO CLASH UNA COLABORACIÓN EN 2024?",
             options=["LIONEL MESSI", "ERLING HAALAND", "CRISTIANO RONALDO"], answer=1,
             vo="Pregunta cinco, la última. ¿Con qué futbolista hizo Clash una colaboración en dos mil veinticuatro?",
             dato="\"Clash With Haaland\": un evento de un mes desde el 1 de mayo de 2024",
             vo_dato="¡La be! Fue con Erling Haaland, en mayo de dos mil veinticuatro.",
             source="Wikipedia, \"Clash of Clans\"", sticker=K + "estatua_barbaro_estrella.png", bg=K + "arte_aniversario_fiesta.jpg"),
    ],
    thumb=dict(lines=[("¿ACERTÁS", "w"), ("LAS 5?", "y")], sticker=K + "jinete_elefante_mangual.png", bg=K + "arte_aniversario_fiesta.jpg"),
)

if __name__ == "__main__":
    main(EP)
