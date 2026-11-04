"""TikTok (¿qué pasaría si...? / humor): ¿y si los constructores hicieran huelga en plena Martillomanía?
Escenario imaginario, sin datos. Única referencia real: Martillomanía 1 al 16/11 (calendario oficial de Supercell, nov. 2026).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
EP = Episode([
    dict(type="hook", kicker="¿QUÉ PASARÍA SI...?", lines=[("¿Y SI LOS", "w"), ("CONSTRUCTORES", "y"), ("HACEN HUELGA?", "r")],
         sizes=(130, 130, 130), sticker=K + "estatua_constructor_martillo.png", sticker_h=480, sticker_y=1420,
         dur=3.5, color=4, vo="¿Y si los constructores hicieran huelga en plena Martillomanía?"),
    dict(type="list", title="SUS RECLAMOS", icons=["alert", "alert", "alert"], step=0.7,
         items=["NO MÁS MURALLAS", "VACACIONES PAGAS", "SIESTA DESPUÉS DE COMER"],
         dur=4.5, color=0, sticker=K + "aldeana_pelirroja_sorprendida.png", sticker_h=420, sticker_x=820,
         sticker_y=1450, sticker_t=2.2, vo="Sus reclamos: no más murallas, vacaciones pagas y siesta después de comer."),
    dict(type="versus", title="EN MARTILLOMANÍA", left=("VOS", "ON"), right=("ELLOS", "OFF"),
         dur=4.0, color=1, card="capturas/lista_mejoras.jpg", card_y=1450, card_t=1.6,
         vo="Vos prendido para mejorar, y ellos apagados de brazos cruzados."),
    dict(type="alert", lines=[("TU ALDEA", "w"), ("SIN MEJORAS", "r")], sub="LAS MURALLAS, IGUAL QUE SIEMPRE",
         dur=4.0, color=2, vo="Tu aldea sin una sola mejora. Las murallas, igual que siempre."),
    dict(type="hook", kicker="LA NEGOCIACIÓN", lines=[("¿CABAÑA", "w"), ("DORADA", "y"), ("PARA TODOS?", "w")],
         sizes=(130, 160, 120), sticker=K + "edificio_cabana_constructor_dorada.png", sticker_h=440, sticker_y=1420,
         dur=3.5, color=3, vo="¿La solución? Una cabaña dorada para cada uno."),
    dict(type="question", q=["¿QUÉ LES DARÍAS", "VOS?"], options=["MÁS GEMAS", "VACACIONES", "NADA, ¡A LABURAR!"],
         dur=4.0, color=5, vo="¿Y vos qué les darías? Comentalo."),
    dict(type="outro", dur=2.5, color=4),
], title="Huelga de constructores", bg_pool=["capturas/aldea_nueva_interfaz.jpg", "capturas/lista_mejoras_filtro.jpg",
                                             K + "arte_aniversario_paisaje.jpg", "capturas/base_guerra_th18_armada.jpg"])

if __name__ == "__main__":
    main(EP)
