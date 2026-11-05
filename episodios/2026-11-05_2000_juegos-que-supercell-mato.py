"""TikTok (¿sabías que? / Supercell): Supercell cerró más juegos de los que lanzó.
Fuente: Wikipedia, "Supercell (company)": fundada el 14/05/2010 en Helsinki; primer juego Gunshine.net (2011, navegador,
abandonado); 7 juegos lanzados (Hay Day, Clash of Clans, Boom Beach, Clash Royale, Brawl Stars, Squad Busters, mo.co);
13 títulos discontinuados (entre ellos Smash Land, Rush Wars, Clash Quest, Clash Mini, Clash Heroes, Everdale).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
SRC = "Wikipedia, \"Supercell (company)\""
EP = Episode([
    dict(type="hook", kicker="¿SABÍAS QUE...?", lines=[("SUPERCELL", "y"), ("MATÓ MÁS JUEGOS", "w"), ("DE LOS QUE LANZÓ", "r")],
         sizes=(150, 110, 105), card=K + "humor_barbaro_rey_asustados.jpg",
         card_y=1430, card_t=1.0, dur=3.5, color=1, vo="¿Sabías que Supercell cerró más juegos de los que lanzó?"),
    dict(type="versus", title="JUEGOS DE SUPERCELL", left=("LANZADOS", "7"), right=("CERRADOS", "13"),
         source=SRC, dur=4.0, color=3, vo="Siete juegos lanzados, y trece que se cerraron o abandonaron."),
    dict(type="list", title="ALGUNOS QUE CERRARON", icon="down", step=0.6,
         items=["CLASH MINI", "CLASH QUEST", "CLASH HEROES", "RUSH WARS", "EVERDALE"], source=SRC,
         dur=4.5, color=0, sticker=K + "aldeana_pelirroja_sorprendida.png", sticker_h=400, sticker_x=840,
         sticker_y=1480, sticker_t=2.4, vo="Clash Mini, Clash Quest, Clash Heroes, Rush Wars y Everdale."),
    dict(type="hook", kicker="SU PRIMER JUEGO", lines=[("NO FUE CLASH:", "w"), ("GUNSHINE", "y"), ("EN 2011", "w")],
         sizes=(120, 170, 130), source=SRC, dur=4.0, color=2,
         sticker=K + "estatua_rey_barbaro.png", sticker_h=420, sticker_y=1450, sticker_t=1.5,
         vo="Y su primer juego no fue Clash: fue Gunshine, de navegador, en dos mil once."),
    dict(type="hook", kicker="CLASH OF CLANS", lines=[("SALIÓ EN", "w"), ("2012", "y"), ("Y SIGUE VIVO", "g")],
         sizes=(120, 200, 120), dur=4.0, color=4,
         card="capturas/aldea_nueva_interfaz.jpg", card_y=1450, card_t=1.8,
         vo="Clash salió en dos mil doce, y acá sigue, más vivo que nunca."),
    dict(type="question", q=["¿CUÁL QUERÉS", "QUE VUELVA?"], options=["CLASH MINI", "CLASH QUEST", "RUSH WARS"],
         dur=4.0, color=5, vo="¿Cuál querés que vuelva? Comentalo."),
    dict(type="outro", dur=2.5, color=1),
], title="Juegos que Supercell cerró", bg_pool=[K + "arte_aniversario_fiesta.jpg", "capturas/aldea_nueva_interfaz.jpg",
                                               K + "arte_coliseo_en_las_nubes.jpg", K + "arte_aniversario_paisaje.jpg"])

if __name__ == "__main__":
    main(EP)
