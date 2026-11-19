"""TRIVIA LARGA (YouTube 16:9) — Defensas. Jueves 19/11/2026 18:00.
Fuentes (consultadas el 19/11/2026):
- Supercell, blog oficial en español "Nuevas defensas": "Vamos a introducir dos nuevas defensas en el Ayuntamiento 15"
  (Torre de hechizos y Monolito). Clash Ninja, "Town Hall 15 is now live" (16/10/2022).
- Pocket Gamer, "Clash of Clans 101 - The complete guide to December's Town Hall 11 update" (dic. 2015): el Águila de
  artillería llega con el TH11 y "will only engage once 50% of an attackers troops are deployed".
- Pocket Gamer, "X-Bow - Clash of Clans complete guide to defenses": se desbloquea en el TH9; apunta a tierra y aire
  (11 casillas) o solo a tierra (14 casillas).
- Pocket Gamer, "Mortar - Clash of Clans complete guide to defenses" / Clash of Clans Wiki "Mortar": solo tropas terrestres.
- Nombres en español ("Águila de artillería", "Ballesta", "Torre infernal", "Torre de arqueras") según el blog oficial
  en español "Ajustes de equilibrio de junio".
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from trivia_larga import TriviaLarga, main

K = "capturas/kit_creador/"
PG11 = "Pocket Gamer, guía de la actualización del TH11 (dic. 2015)"
EP = TriviaLarga(
    title="Trivia larga: Defensas",
    intro=dict(kicker="SOLO EL 1% ACIERTA LAS 5", lines=[("¿CUÁNTO SABÉS", "w"), ("DE LAS", "w"), ("DEFENSAS?", "y")],
               vo="Trivia de Clash. Cinco preguntas sobre las defensas. Treinta segundos para cada una. ¿Te animás?",
               sticker=K + "defensa_tarta_dorada_chispas.png", bg=K + "arte_batalla_esqueletos_bruja.jpg"),
    preguntas=[
        dict(q="¿QUÉ DEFENSA NUEVA TRAJO EL AYUNTAMIENTO 15?",
             options=["ÁGUILA DE ARTILLERÍA", "MONOLITO", "BALLESTA"], answer=1,
             vo="Pregunta uno. ¿Qué defensa nueva trajo el Ayuntamiento quince? ¿El Águila de artillería, el Monolito o la Ballesta?",
             dato="El Monolito llegó con el TH15 (oct. 2022), junto a la Torre de hechizos",
             vo_dato="¡La be! El Monolito, en octubre de dos mil veintidós, junto con la Torre de hechizos.",
             source="Supercell, blog oficial \"Nuevas defensas\"; Clash Ninja (16/10/2022)",
             sticker=K + "roca_cabeza_ojos_azules.png", bg=K + "arte_coliseo_en_las_nubes.jpg"),
        dict(q="¿CON QUÉ AYUNTAMIENTO LLEGÓ EL ÁGUILA DE ARTILLERÍA?",
             options=["AYUNTAMIENTO 9", "AYUNTAMIENTO 11", "AYUNTAMIENTO 13"], answer=1,
             vo="Pregunta dos. ¿Con qué ayuntamiento llegó el Águila de artillería? ¿El nueve, el once o el trece?",
             dato="Llegó con el Ayuntamiento 11, en diciembre de 2015",
             vo_dato="¡La be! Llegó con el Ayuntamiento once, en diciembre de dos mil quince.",
             source=PG11, sticker=K + "dragon_gris_volando.png", bg=K + "arte_aniversario_paisaje.jpg"),
        dict(q="CUANDO SALIÓ, ¿CUÁNDO EMPEZABA A DISPARAR EL ÁGUILA?",
             options=["AL INSTANTE", "AL MINUTO", "MITAD DEL EJÉRCITO"], answer=2,
             vo="Pregunta tres. Cuando salió, ¿cuándo empezaba a disparar el Águila? ¿Al instante, al minuto, o cuando soltabas la mitad de tus tropas?",
             dato="En 2015 se activaba recién cuando soltabas el 50% de tus tropas",
             vo_dato="¡La ce! Se despertaba cuando soltabas la mitad de tus tropas.",
             source=PG11, sticker=K + "esqueleto_casco_aviador.png",
             bg=K + "humor_barbaro_rey_asustados.jpg"),
        dict(q="¿QUÉ DEFENSA PODÉS PONER SOLO A TIERRA O A TIERRA Y AIRE?",
             options=["BALLESTA", "MORTERO", "CAÑÓN"], answer=0,
             vo="Pregunta cuatro. ¿Qué defensa podés poner a disparar solo a tierra, o a tierra y aire? ¿La Ballesta, el Mortero o el Cañón?",
             dato="La Ballesta (desde el TH9): solo a tierra llega a 14 casillas; a tierra y aire, 11",
             vo_dato="¡La a! La Ballesta. Y si la ponés solo a tierra, llega más lejos.",
             source="Pocket Gamer, guía de la Ballesta (X-Bow)",
             sticker=K + "globo_calavera.png", bg=K + "arte_aniversario_fiesta.jpg"),
        dict(q="¿CUÁL DE ESTAS DEFENSAS NO LE PEGA A LAS TROPAS VOLADORAS?",
             options=["TORRE DE ARQUERAS", "MORTERO", "TORRE INFERNAL"], answer=1,
             vo="Pregunta cinco, la última. ¿Cuál de estas defensas no le pega a las tropas voladoras? ¿La Torre de arqueras, el Mortero o la Torre infernal?",
             dato="El Mortero solo ataca tropas terrestres: los dragones y globos pasan tranquilos",
             vo_dato="¡La be! El Mortero solo le pega a las tropas de tierra.",
             source="Pocket Gamer, guía del Mortero; Clash of Clans Wiki",
             sticker=K + "maquina_dirigible_barril_rojo.png", bg=K + "arte_coliseo_en_las_nubes.jpg"),
    ],
    thumb=dict(lines=[("¿ACERTÁS", "w"), ("LAS 5?", "y")], sticker=K + "defensa_tarta_dorada_chispas.png",
               bg=K + "arte_batalla_esqueletos_bruja.jpg"),
)

if __name__ == "__main__":
    main(EP)
