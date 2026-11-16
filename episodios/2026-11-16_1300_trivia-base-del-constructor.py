"""TikTok (trivia, lunes 13:00): 3 preguntas sobre la Base del constructor.
Datos: PhoneArena, "Clash of Clans releases its biggest update since Clan Wars" (2017): la Base del constructor
queda cruzando el mar; para ir hay que reconstruir el barco.
Clash Ninja, "What is Builder Base 2.0": en mayo 2023 se renovó; desde el Taller nivel 6 el ataque tiene 2 etapas
y cada etapa da hasta 3 estrellas (6 en total).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
EP = Episode([
    dict(type="hook", kicker="TRIVIA DE LA BASE DEL CONSTRUCTOR", lines=[("SOLO EL 1%", "y"), ("ACIERTA", "w"), ("LAS TRES", "r")],
         sizes=(140, 140, 130), card=K + "arte_aniversario_paisaje.jpg", card_y=1400, dur=3.5, color=2,
         sticker=K + "estatua_maestro_constructor.png", sticker_h=360, sticker_x=850, sticker_y=1620, sticker_t=1.0,
         vo="Trivia de la Base del constructor. Solo el uno por ciento acierta las tres."),
    dict(type="trivia", q=["¿QUÉ TENÉS QUE", "REPARAR PARA IR A LA", "BASE DEL CONSTRUCTOR?"],
         options=["A) UN GLOBO", "B) UN BARCO", "C) UN PUENTE"], answer=1,
         source="PhoneArena, actualización de mayo 2017", dur=6.5, color=1,
         sticker=K + "maquina_dirigible_barril_rojo.png", sticker_h=230, sticker_x=880, sticker_y=1770, sticker_t=1.0,
         vo="¿Qué tenés que reparar para ir a la Base del constructor?"),
    dict(type="trivia", q=["DESDE 2023, ¿EN CUÁNTAS", "ETAPAS SE DIVIDE", "UN ATAQUE AHÍ?"],
         options=["A) 1 ETAPA", "B) 2 ETAPAS", "C) 3 ETAPAS"], answer=1,
         source="Clash Ninja, guía de la Base del constructor 2.0", dur=6.5, color=3,
         sticker=K + "estatua_constructor_martillo.png", sticker_h=240, sticker_x=880, sticker_y=1770, sticker_t=1.0,
         vo="Desde dos mil veintitrés, ¿en cuántas etapas se divide un ataque ahí?"),
    dict(type="trivia", q=["¿CUÁNTAS ESTRELLAS", "PODÉS SACAR COMO MÁXIMO", "EN UN SOLO ATAQUE?"],
         options=["A) 3 ESTRELLAS", "B) 5 ESTRELLAS", "C) 6 ESTRELLAS"], answer=2,
         source="Clash Ninja, guía de la Base del constructor 2.0", dur=6.5, color=4,
         sticker=K + "medalla_dorada_rombo.png", sticker_h=220, sticker_x=880, sticker_y=1770, sticker_t=1.0,
         vo="¿Cuántas estrellas podés sacar como máximo en un solo ataque?"),
    dict(type="outro", dur=3.0, color=5, vo="¿Cuántas acertaste? ¡Seguime para más de Clash!"),
], title="Trivia: base del constructor", bg_pool=[K + "arte_aniversario_paisaje.jpg", "capturas/boton_construir.jpg",
                                                 K + "arte_coliseo_en_las_nubes.jpg", "capturas/aldea_nueva_interfaz.jpg"])

if __name__ == "__main__":
    main(EP)
