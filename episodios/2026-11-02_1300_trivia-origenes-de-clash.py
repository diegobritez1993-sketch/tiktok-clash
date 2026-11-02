"""TikTok (trivia, lunes 13:00): 3 preguntas sobre los orígenes de Clash of Clans.
Datos (Wikipedia "Clash of Clans"): salió en iOS el 2/8/2012; en Android (Google Play) el 7/10/2013;
la Base del constructor llegó con la actualización del 22/05/2017.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
SRC = "Wikipedia, \"Clash of Clans\""
EP = Episode([
    dict(type="hook", kicker="TRIVIA", lines=[("SOLO EL 1%", "y"), ("ACIERTA", "w"), ("LAS 3", "w")],
         sizes=(150, 130, 130), card=K + "arte_aniversario_fiesta.jpg", card_y=1350, dur=3.5, color=4),
    dict(type="trivia", q=["¿EN QUÉ AÑO", "SALIÓ CLASH?"], options=["A) 2010", "B) 2012", "C) 2014"], answer=1,
         source=SRC, dur=6.5, color=1),
    dict(type="trivia", q=["¿DÓNDE SALIÓ", "PRIMERO?"], options=["A) ANDROID", "B) IPHONE (iOS)", "C) LOS DOS JUNTOS"],
         answer=1, source="Wikipedia (Android: 2013)", dur=6.5, color=2),
    dict(type="trivia", q=["¿EN QUÉ AÑO LLEGÓ LA", "BASE DEL CONSTRUCTOR?"], options=["A) 2015", "B) 2017", "C) 2019"],
         answer=1, source=SRC, dur=6.5, color=3,
         sticker=K + "estatua_constructor_martillo.png", sticker_h=300, sticker_x=880, sticker_y=1730, sticker_t=1.0),
    dict(type="outro", dur=3.0, color=0, sticker=K + "torta_aniversario_14.png", sticker_h=360, sticker_y=1560),
], title="Trivia: orígenes de Clash", bg_pool=[K + "arte_aniversario_paisaje.jpg", "capturas/aldea_nueva_interfaz.jpg",
                                              K + "arte_aniversario_fiesta.jpg", "capturas/boton_construir.jpg"])

if __name__ == "__main__":
    main(EP)
