"""TikTok (novedades/eventos): Finales del Mundial de Clash (World Championship) 14 y 15 de noviembre 2026.
Datos: X oficial @CoCEsports ("World Finals 2026 are coming NOVEMBER 14-15", evento broadcast-first);
Yahoo Tech 30/10/2026: US$700.000 en las finales, 1º US$300.000, 8 equipos, doble eliminación, guerras al mejor de una,
se ve en YouTube, Twitch y Facebook. Campeón 2025: Tribe Gaming (worlds.competitiveclash.network).
Hora de las transmisiones: no anunciada -> no se dice.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
EP = Episode([
    dict(type="hook", kicker="EL MISMO FINDE DEL TH19", lines=[("SE JUEGA EL", "w"), ("MUNDIAL", "y"), ("DE CLASH", "y")],
         sizes=(110, 170, 150), card=K + "arte_coliseo_en_las_nubes.jpg", card_y=1380, dur=3.5, color=2),
    dict(type="alert", lines=[("14 Y 15", "y"), ("DE NOVIEMBRE", "w")], sizes=(150, 110), sub="FINALES MUNDIALES 2026",
         source="X oficial @CoCEsports", dur=4.0, color=0),
    dict(type="stat", title="PREMIO TOTAL", value=700000, prefix="US$ ", label="EN LAS FINALES",
         sub="US$ 300.000 PARA EL CAMPEÓN", source="Yahoo Tech, 30/10/2026", dur=4.0, color=3,
         sticker=K + "cofre_madera_hierro.png", sticker_h=210, sticker_x=540, sticker_y=1460, sticker_t=2.2),
    dict(type="list", title="CÓMO SE JUEGA", icons=["star", "alert", "check"], step=0.6,
         items=["8 EQUIPOS", "DOBLE ELIMINACIÓN", "CADA RONDA: 1 GUERRA"],
         source="Yahoo Tech, 30/10/2026", dur=4.5, color=1),
    dict(type="question", q=["¿QUIÉN GANA", "ESTE AÑO?"], options=["REPITE TRIBE GAMING", "UN CAMPEÓN NUEVO"],
         source="competitiveclash.network (campeón 2025)", dur=4.5, color=5),
    dict(type="outro", dur=3.0, color=4),
], title="Mundial de Clash 2026", bg_pool=[K + "arte_coliseo_en_las_nubes.jpg", "capturas/guerra_desde_chat.jpg",
                                          "capturas/base_guerra_th18_armada.jpg", "capturas/menu_eventos_2.jpg"])

if __name__ == "__main__":
    main(EP)
