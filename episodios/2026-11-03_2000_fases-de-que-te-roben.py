"""TikTok (humor): las 5 fases de que te roben la aldea. Sin datos que verificar (humor de situaciones que todo jugador vivió)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
EP = Episode([
    dict(type="hook", kicker="TE ATACARON MIENTRAS DORMÍAS", lines=[("LAS 5 FASES", "y"), ("DE QUE TE", "w"), ("ROBEN TODO", "r")],
         sizes=(150, 120, 140), card=K + "humor_barbaro_duerme_con_trofeo.jpg", card_y=1380, dur=3.5, color=0,
         vo="Las cinco fases de que te roben todo. ¿Cuál te pasó?"),
    dict(type="list", title="FASE 1 Y 2", icons=["alert", "down"], step=0.7,
         items=["NEGACIÓN: \"NO PUEDE SER\"", "IRA: TIRÁS EL CELU"],
         dur=4.0, color=2, sticker=K + "aldeana_pelirroja_sorprendida.png", sticker_h=440, sticker_x=800,
         sticker_y=1400, sticker_t=1.8, vo="Primero no lo podés creer. Después te dan ganas de tirar el celu."),
    dict(type="versus", title="FASE 3: LA REPE", left=("ÉL", "TRIPLE"), right=("VOS", "MIRANDO"),
         dur=4.0, color=1, bg=K + "humor_barbaro_cine_palomitas.jpg", sticker=K + "duende_con_bolsa.png", sticker_h=400, sticker_y=1480, sticker_t=1.8,
         vo="Fase tres: mirás la repetición como si fuera una peli."),
    dict(type="alert", lines=[("FASE 4:", "w"), ("¡VENGANZA!", "r")], sub="Y PERDÉS IGUAL",
         dur=4.0, color=4, vo="Fase cuatro: vas a vengarte... y perdés igual."),
    dict(type="hook", kicker="FASE 5", lines=[("ACEPTACIÓN", "g"), ("Y A FARMEAR", "w"), ("DE NUEVO", "y")],
         sizes=(150, 120, 120), card=K + "humor_barbaro_rey_asustados.jpg", card_y=1420, dur=4.0, color=3,
         vo="Y la fase cinco: aceptarlo y volver a farmear."),
    dict(type="question", q=["¿EN QUÉ FASE", "TE QUEDÁS VOS?"], options=["LA IRA", "LA VENGANZA", "ACEPTACIÓN"],
         dur=4.0, color=5, vo="¿En qué fase te quedás vos? Comentalo."),
    dict(type="outro", dur=2.5, color=2),
], title="Las 5 fases de que te roben", bg_pool=["capturas/aldea_nueva_interfaz.jpg", "capturas/base_th18_antidos_1.jpg",
                                                 K + "humor_barbaro_cine_palomitas.jpg", "capturas/base_guerra_th18_armada.jpg"])

if __name__ == "__main__":
    main(EP)
