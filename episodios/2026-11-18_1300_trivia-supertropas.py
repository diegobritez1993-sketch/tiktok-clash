"""TikTok (trivia, miércoles 13:00): 3 preguntas sobre las supertropas.
Datos: Supercell, blog oficial "Coming Soon: The Super Troops" (24/03/2020): se activan desde Ayuntamiento 11;
llegaron con la actualización de primavera 2020 (Clash Ninja, "Spring 2020 Update Is Life", 04/04/2020).
Hoy se pueden tener 2 supertropas activas a la vez (Sportskeeda y Mobile Matters, guías de supertropas;
al lanzarse en 2020 era solo 1).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
EP = Episode([
    dict(type="hook", kicker="TRIVIA DE SUPERTROPAS", lines=[("¿SABÉS TODO", "w"), ("DE LAS", "w"), ("SUPERTROPAS?", "y")],
         sizes=(130, 130, 150), card="capturas/tropa_supermontapuercos.jpg", card_y=1400, dur=3.5, color=4,
         sticker=K + "hechizo_pocion_rosa_pulpo.png", sticker_h=300, sticker_x=870, sticker_y=1660, sticker_t=1.0,
         vo="Trivia de supertropas. Solo el uno por ciento acierta las tres."),
    dict(type="trivia", q=["¿DESDE QUÉ", "AYUNTAMIENTO PODÉS", "ACTIVAR SUPERTROPAS?"],
         options=["A) AYUNTAMIENTO 9", "B) AYUNTAMIENTO 11", "C) AYUNTAMIENTO 13"], answer=1,
         source="Supercell, blog oficial (24/03/2020)", dur=6.5, color=2,
         sticker=K + "boton_escudo_dorado.png", sticker_h=200, sticker_x=870, sticker_y=1770, sticker_t=1.0,
         vo="¿Desde qué Ayuntamiento podés activar supertropas?"),
    dict(type="trivia", q=["¿EN QUÉ AÑO", "LLEGARON LAS", "SUPERTROPAS?"],
         options=["A) 2018", "B) 2020", "C) 2022"], answer=1,
         source="Supercell (marzo 2020); Clash Ninja (abril 2020)", dur=6.5, color=1,
         sticker=K + "estatua_barbaro_estrella.png", sticker_h=260, sticker_x=870, sticker_y=1740, sticker_t=1.0,
         vo="¿En qué año llegaron las supertropas al juego?"),
    dict(type="trivia", q=["HOY, ¿CUÁNTAS", "SUPERTROPAS PODÉS", "TENER ACTIVAS A LA VEZ?"],
         options=["A) 1", "B) 2", "C) 4"], answer=1,
         source="Sportskeeda y Mobile Matters, guías de supertropas", dur=6.5, color=3,
         sticker=K + "duende_con_bolsa.png", sticker_h=260, sticker_x=870, sticker_y=1740, sticker_t=1.0,
         vo="Hoy, ¿cuántas supertropas podés tener activas a la vez?"),
    dict(type="outro", dur=3.0, color=5, vo="¿Cuántas acertaste? ¡Seguime para más de Clash!"),
], title="Trivia: supertropas", bg_pool=["capturas/tropa_supermontapuercos.jpg", K + "arte_coliseo_en_las_nubes.jpg",
                                         "capturas/aldea_nueva_interfaz.jpg", K + "arte_aniversario_paisaje.jpg"])

if __name__ == "__main__":
    main(EP)
