"""TikTok (novedades + filtraciones): mañana 13/11 arranca el Clash On del Ayuntamiento 19 (13-15/11, adelantos de creadores).
Fuentes: calendario oficial de Supercell, noviembre 2026 (Clash On 13-15/11); Supercell, blog oficial 01/11/2026 (TH19 "a mitad
de mes", sin fecha exacta). FILTRACIONES NO CONFIRMADAS: GamingonPhone 11/11/2026 citando posts de r/ClashOfClansLeaks
(costo ~30 millones de oro, +5 niveles a todos los héroes, defensa nueva, hechizo nuevo). Sportsdunia 12/11/2026 repite costo
y niveles de héroes como "leaks". No se nombra la defensa (nombre en español no verificado).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
EP = Episode([
    dict(type="hook", kicker="MAÑANA 13/11", lines=[("¿QUÉ TRAE", "w"), ("EL TH19?", "y")],
         sizes=(150, 170), dur=4.5, color=1,
         card="capturas/aldea_nueva_interfaz.jpg", card_y=1380,
         sticker=K + "aldeana_pelirroja_sorprendida.png", sticker_h=400, sticker_x=850, sticker_y=1650, sticker_t=0.9,
         vo="Mañana Supercell empieza a mostrar el Ayuntamiento diecinueve. ¿Qué trae?"),
    dict(type="alert", lines=[("CLASH ON", "y"), ("DEL TH19", "w"), ("13 AL 15 NOV", "w")],
         sub="ADELANTOS DE CREADORES", source="Calendario oficial de Supercell, nov. 2026",
         dur=4.5, color=0, bg=K + "arte_coliseo_en_las_nubes.jpg",
         vo="Del trece al quince hay Clash On, con adelantos de creadores. La fecha de salida, todavía sin anunciar."),
    dict(type="hook", kicker="NO CONFIRMADO", lines=[("FILTRACIÓN", "r"), ("DE REDDIT", "w")],
         sizes=(150, 130), dur=3.5, color=2, card=K + "humor_barbaro_rey_asustados.jpg", card_y=1400,
         source="r/ClashOfClansLeaks vía GamingonPhone (11/11/2026)",
         vo="Ojo: esto es filtración, no está confirmado. Viene de Reddit."),
    dict(type="list", title="RUMOR: LO QUE SE FILTRÓ", icon="star", step=0.7,
         items=["~30 MILLONES DE ORO", "+5 NIVELES A CADA HÉROE", "UNA DEFENSA NUEVA", "UN HECHIZO NUEVO"],
         source="RUMOR: r/ClashOfClansLeaks (vía GamingonPhone)", dur=5.5, color=4,
         sticker=K + "duende_con_bolsa.png", sticker_h=260, sticker_x=900, sticker_y=1765, sticker_t=3.0,
         vo="Se habla de unos treinta millones de oro, cinco niveles más por héroe, una defensa nueva y un hechizo nuevo."),
    dict(type="question", q=["¿QUÉ QUERÉS", "QUE TRAIGA?"], options=["HÉROE NUEVO", "DEFENSA NUEVA", "MÁS CONSTRUCTORES"],
         dur=4.0, color=5, vo="¿Y vos qué querés que traiga? Dejalo en los comentarios."),
    dict(type="outro", dur=2.5, color=1),
], title="Mañana se ve el TH19", bg_pool=["capturas/aldea_nueva_interfaz.jpg", K + "arte_aniversario_paisaje.jpg",
                                          "capturas/lista_mejoras.jpg", "capturas/base_guerra_th18_armada.jpg"])

if __name__ == "__main__":
    main(EP)
