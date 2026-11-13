"""TikTok (humor, viernes 13): la mala suerte en Clash que todo jugador vivió. Sin datos (humor)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
EP = Episode([
    dict(type="hook", kicker="VIERNES 13", lines=[("LA MALA SUERTE", "w"), ("EN CLASH", "y"), ("EXISTE", "r")],
         sizes=(120, 140, 150), card=K + "humor_barbaro_rey_asustados.jpg", card_y=1400, dur=3.5, color=0,
         vo="Hoy es viernes trece. Y la mala suerte en Clash existe."),
    dict(type="alert", lines=[("99% Y", "y"), ("UNA ESTRELLA", "r")], sub="FALTÓ UN CAÑÓN EN LA ESQUINA",
         dur=4.0, color=0, sticker=K + "aldeana_pelirroja_sorprendida.png", sticker_h=400, sticker_x=820,
         sticker_y=1450, sticker_t=1.5,
         vo="Noventa y nueve por ciento y una estrella. Faltó un cañón en la esquina."),
    dict(type="list", title="MÁS MALA SUERTE", icon="down", step=0.8,
         items=["EL HECHIZO CAE AL LADO", "LA TROPA SE VA AL MURO", "EL HÉROE SE VA DE PASEO"],
         dur=5.0, color=2, sticker=K + "globo_calavera.png", sticker_h=320, sticker_x=850,
         sticker_y=1600, sticker_t=2.8,
         vo="El hechizo que cae al lado, la tropa que se va contra el muro, y el héroe que se va de paseo."),
    dict(type="versus", title="TU ORO", left=("ANTES DE DORMIR", "LLENO"), right=("AL DESPERTAR", "CERO"),
         dur=4.0, color=4, vo="Y tu oro: a tope antes de dormir, en cero al despertar."),
    dict(type="question", q=["¿CUÁL TE", "PASÓ HOY?"], options=["EL 99%", "EL HECHIZO", "EL ORO"],
         dur=4.0, color=1, vo="¿Cuál te pasó a vos? Contalo en los comentarios."),
    dict(type="outro", dur=2.5, color=0),
], title="Viernes 13", bg_pool=[K + "arte_temporada_luna_roja.jpg", "capturas/aldea_nueva_interfaz.jpg",
                                K + "arte_batalla_esqueletos_bruja.jpg", "capturas/base_guerra_th18_armada.jpg"])

if __name__ == "__main__":
    main(EP)
