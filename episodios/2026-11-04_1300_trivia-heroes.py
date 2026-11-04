"""TikTok (trivia, miércoles 13:00): 3 preguntas sobre los héroes de la aldea principal.
Datos: el Gran centinela llegó con la actualización del Ayuntamiento 11 (diciembre 2015; TouchArcade 09/12/2015,
PocketGamer "December's Town Hall 11 update"); la Campeona real llegó con el Ayuntamiento 13 (Clash Ninja,
"December 2019 brings TH13"); hoy la aldea tiene 6 héroes: Reina arquera, Rey bárbaro, Duque dragón, Gran centinela,
Príncipe de los esbirros y Campeona real (Wikipedia "Clash of Clans").
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
EP = Episode([
    dict(type="hook", kicker="TRIVIA DE HÉROES", lines=[("¿SABÉS", "w"), ("DE HÉROES?", "y"), ("3 PREGUNTAS", "w")],
         sizes=(140, 150, 120), card="capturas/heroe_reina_stats.jpg", card_y=1380, dur=3.5, color=2,
         sticker=K + "estatua_rey_barbaro.png", sticker_h=360, sticker_x=870, sticker_y=1650, sticker_t=1.2,
         vo="¿Cuánto sabés de héroes? Tres preguntas, a ver."),
    dict(type="trivia", q=["¿QUÉ HÉROE LLEGÓ", "CON EL TH11?"],
         options=["A) REY BÁRBARO", "B) GRAN CENTINELA", "C) CAMPEONA REAL"], answer=1,
         source="TouchArcade, update del TH11 (dic. 2015)", dur=6.5, color=1,
         vo="¿Qué héroe llegó con el Ayuntamiento once?"),
    dict(type="trivia", q=["¿CON QUÉ AYUNTAMIENTO", "LLEGÓ LA CAMPEONA REAL?"],
         options=["A) TH12", "B) TH13", "C) TH14"], answer=1,
         source="Clash Ninja, \"December 2019 brings TH13\"", dur=6.5, color=4,
         vo="¿Con qué Ayuntamiento llegó la Campeona real?"),
    dict(type="trivia", q=["¿CUÁNTOS HÉROES TIENE", "HOY LA ALDEA?"],
         options=["A) 4", "B) 5", "C) 6"], answer=2,
         source="Wikipedia, \"Clash of Clans\"", dur=6.5, color=3,
         sticker=K + "medalla_dorada_rombo.png", sticker_h=240, sticker_x=900, sticker_y=1740, sticker_t=1.0,
         vo="¿Cuántos héroes tiene hoy la aldea principal?"),
    dict(type="outro", dur=3.0, color=0, vo="¿Cuántas acertaste? ¡Seguime para más de Clash!"),
], title="Trivia: héroes", bg_pool=["capturas/heroe_reina_stats.jpg", K + "arte_batalla_esqueletos_bruja.jpg",
                                     "capturas/aldea_nueva_interfaz.jpg", K + "arte_coliseo_en_las_nubes.jpg"])

if __name__ == "__main__":
    main(EP)
