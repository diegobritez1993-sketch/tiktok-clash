"""TikTok (humor / ¿qué pasaría si...?, jueves 20:00): si tu Ayuntamiento pudiera hablar. Sin datos (humor)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
EP = Episode([
    dict(type="hook", kicker="¿QUÉ PASARÍA SI...?", lines=[("TU", "w"), ("AYUNTAMIENTO", "y"), ("HABLARA", "w")],
         sizes=(150, 130, 150), dur=3.5, color=2,
         card=K + "humor_rey_espejo_manga.jpg", card_y=1400,
         vo="¿Qué pasaría si tu Ayuntamiento pudiera hablar?"),
    dict(type="list", title="LO PRIMERO QUE DIRÍA", icon="chat", step=0.8,
         items=["¿MUROS A MEDIAS? ¿EN SERIO?", "OTRA VEZ ME DEJASTE SOLO", "¿QUIÉN PUSO ESA BALLESTA?"],
         dur=5.0, color=1, bg="capturas/aldea_nueva_interfaz.jpg",
         sticker=K + "banner_jugador_ayuntamiento.png", sticker_h=200, sticker_x=540, sticker_y=1500, sticker_t=2.8,
         vo="¿Muros a medias? ¿En serio? Otra vez me dejaste solo. ¿Y quién puso esa Ballesta ahí?"),
    dict(type="versus", title="CUANDO LO SUBÍS RÁPIDO", left=("VOS", "¡NIVEL NUEVO!"), right=("ÉL", "¿Y MIS DEFENSAS?"),
         dur=4.0, color=0, vo="Y cuando lo subís de nivel sin mejorar nada... ¿y las defensas?"),
    dict(type="hook", kicker="EN PLENA GUERRA", lines=[("\"ME TIRARON", "w"), ("TRES ESTRELLAS", "r"), ("Y VOS DORMÍAS\"", "y")],
         sizes=(120, 120, 110), dur=4.0, color=4, card=K + "humor_barbaro_duerme_con_trofeo.jpg", card_y=1420,
         vo="Me tiraron tres estrellas y vos durmiendo con el trofeo."),
    dict(type="alert", lines=[("\"POR LO MENOS", "w"), ("PONEME UNA", "w"), ("DECORACIÓN\"", "y")], sub="AUNQUE SEA UNA FUENTE",
         dur=4.0, color=3,
         sticker=K + "fuente_dragon_verde.png", sticker_h=360, sticker_x=820, sticker_y=1560, sticker_t=1.4,
         vo="Y por lo menos poneme una decoración, che. Aunque sea una fuente."),
    dict(type="question", q=["¿QUÉ TE DIRÍA", "EL TUYO?"], options=["\"MEJORAME\"", "\"ESTOY BIEN\"", "\"AYUDA\""],
         dur=3.5, color=5, vo="¿Y el tuyo qué te diría? Comentalo."),
    dict(type="outro", dur=2.5, color=2),
], title="Si tu Ayuntamiento hablara", bg_pool=[K + "arte_aniversario_paisaje.jpg", "capturas/aldea_nueva_interfaz.jpg",
                                                  "capturas/base_guerra_th18_armada.jpg", K + "arte_aniversario_fiesta.jpg"])

if __name__ == "__main__":
    main(EP)
