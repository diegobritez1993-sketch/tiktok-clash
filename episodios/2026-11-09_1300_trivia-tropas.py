"""TikTok (trivia, lunes 13:00): 3 preguntas sobre tropas clásicas.
Datos: Clash of Clans Wiki (Fandom) "Hog Rider": salta muros de cualquier nivel; "Wall Breaker": 40x de daño a muros;
Sportskeeda "Best ways to use Healer": "She only heals ground troops and ignores air-bourne troops".
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
EP = Episode([
    dict(type="hook", kicker="TRIVIA DE TROPAS", lines=[("SOLO EL 1%", "y"), ("ACIERTA", "w"), ("LA ÚLTIMA", "r")],
         sizes=(160, 140, 150), card="capturas/tropa_supermontapuercos.jpg", card_y=1400, dur=3.5, color=2,
         sticker=K + "aldeana_pelirroja_sorprendida.png", sticker_h=360, sticker_x=880, sticker_y=1680, sticker_t=1.2,
         vo="Trivia de tropas. Solo el uno por ciento acierta la última."),
    dict(type="trivia", q=["¿QUÉ TROPA SALTA LOS", "MUROS SIN HECHIZO?"],
         options=["A) GIGANTE", "B) MONTAPUERCOS", "C) VALQUIRIA"], answer=1,
         source="Clash of Clans Wiki, Montapuercos", dur=6.5, color=4,
         vo="¿Qué tropa salta los muros sin ningún hechizo?"),
    dict(type="trivia", q=["¿CUÁNTO DAÑO EXTRA", "LE HACE UN ROMPEMUROS", "A LOS MUROS?"],
         options=["A) x10", "B) x20", "C) x40"], answer=2,
         source="Clash of Clans Wiki, Rompemuros", dur=6.5, color=1,
         sticker=K + "maquina_taladro_calavera.png", sticker_h=230, sticker_x=880, sticker_y=1770, sticker_t=1.0,
         vo="¿Cuánto daño extra le hace un rompemuros a los muros?"),
    dict(type="trivia", q=["¿A QUIÉN NO", "PUEDE CURAR", "LA CURANDERA?"],
         options=["A) BÁRBAROS", "B) GIGANTES", "C) DRAGONES"], answer=2,
         source="Sportskeeda: solo cura tropas terrestres", dur=6.5, color=3,
         sticker=K + "dragon_gris_volando.png", sticker_h=230, sticker_x=870, sticker_y=1770, sticker_t=1.0,
         vo="¿A quién no puede curar la curandera?"),
    dict(type="outro", dur=3.0, color=0, vo="¿Cuántas acertaste? ¡Seguime para más de Clash!"),
], title="Trivia: tropas", bg_pool=["capturas/tropa_golem_meteorico.jpg", K + "arte_batalla_esqueletos_bruja.jpg",
                                    "capturas/tropa_supermontapuercos.jpg", K + "arte_aniversario_paisaje.jpg"])

if __name__ == "__main__":
    main(EP)
