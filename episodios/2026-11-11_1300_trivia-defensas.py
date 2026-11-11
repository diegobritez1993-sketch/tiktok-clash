"""TikTok (trivia, miércoles 13:00): 3 preguntas sobre defensas de la aldea.
Datos: Pocket Gamer, "Inferno Tower - complete guide to defenses": desbloqueo con Ayuntamiento 10, ataca tierra y aire.
Clash of Clans Wiki (Fandom), "Mortar": punto ciego de 4 casillas (alcance 4-11), no ataca tropas aéreas.
Pocket Gamer, "Air Defense - complete guide to defenses": solo ataca tropas aéreas, indefensa contra tropas terrestres.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
EP = Episode([
    dict(type="hook", kicker="TRIVIA DE DEFENSAS", lines=[("¿CONOCÉS", "w"), ("TU ALDEA?", "y"), ("SOLO EL 1% SÍ", "r")],
         sizes=(140, 150, 120), card="capturas/base_guerra_th18_armada.jpg", card_y=1400, dur=3.5, color=1,
         sticker=K + "barbaro_realista_espada.png", sticker_h=380, sticker_x=870, sticker_y=1690, sticker_t=1.2,
         vo="Trivia de defensas. ¿Conocés tu aldea? Solo el uno por ciento acierta las tres."),
    dict(type="trivia", q=["¿CON QUÉ AYUNTAMIENTO", "SE DESBLOQUEA LA", "TORRE INFERNAL?"],
         options=["A) AYUNTAMIENTO 8", "B) AYUNTAMIENTO 10", "C) AYUNTAMIENTO 12"], answer=1,
         source="Pocket Gamer, guía de la Torre infernal", dur=6.5, color=0,
         vo="¿Con qué Ayuntamiento se desbloquea la Torre infernal?"),
    dict(type="trivia", q=["¿CUÁNTAS CASILLAS", "DE PUNTO CIEGO", "TIENE EL MORTERO?"],
         options=["A) 2 CASILLAS", "B) 4 CASILLAS", "C) 6 CASILLAS"], answer=1,
         source="Clash of Clans Wiki, Mortero (alcance 4-11)", dur=6.5, color=4,
         sticker=K + "estatua_constructor_martillo.png", sticker_h=230, sticker_x=880, sticker_y=1770, sticker_t=1.0,
         vo="¿Cuántas casillas de punto ciego tiene el mortero?"),
    dict(type="trivia", q=["¿A QUÉ TROPA NO", "LE PUEDE PEGAR LA", "DEFENSA AÉREA?"],
         options=["A) GLOBO", "B) ESBIRRO", "C) MONTAPUERCOS"], answer=2,
         source="Pocket Gamer: solo ataca tropas aéreas", dur=6.5, color=2,
         sticker=K + "globo_calavera.png", sticker_h=230, sticker_x=870, sticker_y=1770, sticker_t=1.0,
         vo="¿A qué tropa no le puede pegar la defensa aérea?"),
    dict(type="outro", dur=3.0, color=5, vo="¿Cuántas acertaste? ¡Seguime para más de Clash!"),
], title="Trivia: defensas", bg_pool=["capturas/base_guerra_th17_armada.jpg", K + "arte_coliseo_en_las_nubes.jpg",
                                      "capturas/base_th18_antidos_2.jpg", "capturas/aldea_nueva_interfaz.jpg"])

if __name__ == "__main__":
    main(EP)
