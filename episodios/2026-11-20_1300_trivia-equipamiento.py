"""TikTok (trivia, viernes 13:00): 3 preguntas sobre el equipamiento de héroes.
Datos: Supercell, blog oficial "Introducing Hero Equipment" (12/12/2023): cada héroe lleva DOS piezas a la vez;
se mejora en la Herrería, que se construye desde Ayuntamiento 8. Flecha congelada = equipamiento épico de la
Reina arquera (Mobile Matters, guía "Frozen Arrow", 09/02/2024). Término "herrería" verificado en el blog
oficial en español (17/11/2026).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
EP = Episode([
    dict(type="hook", kicker="TRIVIA DE EQUIPAMIENTO", lines=[("SOLO EL 1%", "y"), ("ACIERTA", "w"), ("LAS TRES", "w")],
         sizes=(160, 130, 140), card="capturas/equipo_flecha_congelada.jpg", card_y=1400, dur=3.5, color=1,
         sticker=K + "runa_naranja_brillante.png", sticker_h=260, sticker_x=880, sticker_y=1680, sticker_t=1.0,
         vo="Trivia de equipamiento de héroes. Solo el uno por ciento acierta las tres."),
    dict(type="trivia", q=["¿CUÁNTAS PIEZAS DE", "EQUIPAMIENTO LLEVA", "UN HÉROE A LA VEZ?"],
         options=["A) 1", "B) 3", "C) 2"], answer=2,
         source="Supercell, blog oficial (12/12/2023)", dur=6.5, color=4,
         sticker=K + "estatua_rey_barbaro.png", sticker_h=300, sticker_x=870, sticker_y=1720, sticker_t=1.0,
         vo="¿Cuántas piezas de equipamiento puede llevar un héroe a la vez?"),
    dict(type="trivia", q=["¿DE QUÉ HÉROE ES", "LA FLECHA", "CONGELADA?"],
         options=["A) REY BÁRBARO", "B) REINA ARQUERA", "C) GRAN CENTINELA"], answer=1,
         source="Mobile Matters, guía Flecha congelada (2024)", dur=6.5, color=2,
         sticker=K + "lanza_violeta_brillante.png", sticker_h=280, sticker_x=880, sticker_y=1720, sticker_t=1.0,
         vo="¿De qué héroe es la Flecha congelada?"),
    dict(type="trivia", q=["¿DESDE QUÉ", "AYUNTAMIENTO TENÉS", "LA HERRERÍA?"],
         options=["A) AYUNTAMIENTO 8", "B) AYUNTAMIENTO 10", "C) AYUNTAMIENTO 12"], answer=0,
         source="Supercell, blog oficial (12/12/2023)", dur=6.5, color=3,
         sticker=K + "edificio_taller_madera_oscura.png", sticker_h=280, sticker_x=870, sticker_y=1720, sticker_t=1.0,
         vo="¿Desde qué Ayuntamiento podés construir la Herrería?"),
    dict(type="outro", dur=3.0, color=5, vo="¿Cuántas acertaste? ¡Seguime para más de Clash!"),
], title="Trivia: equipamiento de héroes", bg_pool=["capturas/equipo_flecha_congelada.jpg", K + "arte_coliseo_en_las_nubes.jpg",
                                                    "capturas/heroe_reina_stats.jpg", K + "arte_aniversario_paisaje.jpg"])

if __name__ == "__main__":
    main(EP)
