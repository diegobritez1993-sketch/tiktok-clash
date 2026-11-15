"""TRIVIA LARGA (YouTube 16:9) — Héroes y mascotas. Domingo 15/11/2026 18:00.
Fuentes (consultadas el 15/11/2026):
- Pocket Gamer, "Clash of Clans gets all-new Barbarian King and Archer Queen hero units" (10/01/2013): versión 3.3 suma
  el Rey bárbaro y la Reina arquera y un recurso nuevo, el elixir oscuro, necesario para los héroes.
- Supercell, "Full patch notes: TH14 update" (11/04/2021): el Ayuntamiento 14 desbloquea la Casa de mascotas; 4 mascotas
  al lanzamiento (niveles 1 a 4 de la casa); las Cabañas del constructor mejoradas tienen una torreta que dispara.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from trivia_larga import TriviaLarga, main

K = "capturas/kit_creador/"
PG = "Pocket Gamer, 10/01/2013 (actualización 3.3)"
SC = "Supercell, notas del parche del TH14 (11/04/2021)"
EP = TriviaLarga(
    title="Trivia larga: Héroes y mascotas",
    intro=dict(kicker="SOLO EL 1% ACIERTA LAS 5", lines=[("¿CUÁNTO SABÉS", "w"), ("DE HÉROES", "w"), ("Y MASCOTAS?", "y")],
               vo="Trivia de Clash. Cinco preguntas sobre héroes y mascotas. Treinta segundos para cada una. ¿Te animás?",
               sticker=K + "estatua_rey_barbaro.png", bg=K + "arte_aniversario_fiesta.jpg"),
    preguntas=[
        dict(q="¿EN QUÉ AÑO LLEGARON EL REY BÁRBARO Y LA REINA ARQUERA?", options=["2012", "2013", "2015"], answer=1,
             vo="Pregunta uno. ¿En qué año llegaron el Rey bárbaro y la Reina arquera? ¿Dos mil doce, dos mil trece o dos mil quince?",
             dato="Llegaron juntos en enero de 2013, con la actualización 3.3",
             vo_dato="¡La be! Llegaron juntos en enero de dos mil trece.",
             source=PG, sticker=K + "estatua_rey_barbaro.png", bg=K + "arte_aniversario_paisaje.jpg"),
        dict(q="¿QUÉ RECURSO NUEVO LLEGÓ JUNTO CON ESOS HÉROES?", options=["GEMAS", "ELIXIR OSCURO", "MINERAL"], answer=1,
             vo="Pregunta dos. ¿Qué recurso nuevo llegó junto con esos héroes? ¿Gemas, elixir oscuro o mineral?",
             dato="El elixir oscuro llegó en esa misma actualización para pagar a los héroes",
             vo_dato="¡La be! El elixir oscuro llegó con ellos, para los héroes.",
             source=PG, sticker=K + "hechizo_pocion_rosa_pulpo.png", bg=K + "arte_batalla_esqueletos_bruja.jpg"),
        dict(q="¿CON QUÉ AYUNTAMIENTO LLEGARON LAS MASCOTAS?", options=["AYUNTAMIENTO 12", "AYUNTAMIENTO 13", "AYUNTAMIENTO 14"], answer=2,
             vo="Pregunta tres. ¿Con qué ayuntamiento llegaron las mascotas de los héroes? ¿El doce, el trece o el catorce?",
             dato="La Casa de mascotas llegó con el Ayuntamiento 14, en abril de 2021",
             vo_dato="¡La ce! Llegaron con el Ayuntamiento catorce, en abril de dos mil veintiuno.",
             source=SC, sticker=K + "oso_marron_azul.png", bg=K + "arte_coliseo_en_las_nubes.jpg"),
        dict(q="¿CUÁNTAS MASCOTAS HABÍA CUANDO SE ESTRENARON?", options=["2", "4", "8"], answer=1,
             vo="Pregunta cuatro. ¿Cuántas mascotas había cuando se estrenaron? ¿Dos, cuatro u ocho?",
             dato="Eran 4: una nueva por cada nivel de la Casa de mascotas",
             vo_dato="¡La be! Eran cuatro, una por cada nivel de la casa.",
             source=SC, sticker=K + "dragon_gris_volando.png", bg=K + "humor_mago_bana_bebe_dragon.jpg"),
        dict(q="¿QUÉ EDIFICIO EMPEZÓ A DISPARAR CON EL AYUNTAMIENTO 14?",
             options=["CABAÑA DEL CONSTRUCTOR", "CASTILLO DEL CLAN", "LABORATORIO"], answer=0,
             vo="Pregunta cinco, la última. ¿Qué edificio empezó a disparar con el Ayuntamiento catorce? ¿La cabaña del constructor, el castillo del clan o el laboratorio?",
             dato="Las cabañas mejoradas suman una torreta y el constructor repara defensas",
             vo_dato="¡La a! La cabaña del constructor: ahora tiene torreta y el constructor repara defensas.",
             source=SC, sticker=K + "estatua_constructor_martillo.png", bg=K + "arte_aniversario_fiesta.jpg"),
    ],
    thumb=dict(lines=[("¿ACERTÁS", "w"), ("LAS 5?", "y")], sticker=K + "estatua_rey_barbaro.png",
               bg=K + "arte_coliseo_en_las_nubes.jpg"),
)

if __name__ == "__main__":
    main(EP)
