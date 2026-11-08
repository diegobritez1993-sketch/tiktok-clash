"""TikTok (novedades del mes): mañana 9/11 arrancan el evento masivo de tropa, el último desafío del TH18 y el 10/11 el Superyeti.
Fuente: Supercell, blog oficial "Clash of Titans Is Hot Off The Press" (01/11/2026): "Take 25 M.O.M.M.As into battle for free
at Town Hall 10 and above" (9/11); "the final Town Hall 18 Challenge" 9-15/11; Troop Spotlight Super Yeti 10-16/11
(Ice Cubes -> Super Medals); "Town Hall 19 lands mid-month". (El nombre en español de la tropa no está verificado:
en pantalla se dice "25 TROPAS GRATIS".)
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
SRC = "Supercell, blog oficial (01/11/2026)"
EP = Episode([
    dict(type="hook", kicker="MAÑANA 9 DE NOVIEMBRE", lines=[("¡TE REGALAN", "w"), ("25 TROPAS", "y"), ("GRATIS!", "g")],
         sizes=(140, 170, 170), card="capturas/menu_eventos_1.jpg", card_y=1400, dur=3.5, color=3,
         sticker=K + "cofre_calavera_morado.png", sticker_h=360, sticker_x=850, sticker_y=1640, sticker_t=1.2,
         vo="¡Mañana te regalan veinticinco tropas gratis! Prestá atención."),
    dict(type="stat", title="EVENTO MASIVO", value=25, prefix="", suffix="", label="TROPAS GRATIS",
         sub="SOLO EL 9/11 · TH10 O MÁS", source=SRC, dur=3.5, color=0,
         vo="Son veinticinco tropas para atacar, desde Ayuntamiento diez."),
    dict(type="alert", lines=[("ÚLTIMO DESAFÍO", "w"), ("DEL TH18", "y")], sizes=(110, 140),
         sub="DEL 9 AL 15 DE NOVIEMBRE", source=SRC, dur=4.0, color=4,
         vo="También arranca el último desafío del Ayuntamiento dieciocho."),
    dict(type="list", title="LA SEMANA QUE VIENE", icons=["star", "star", "clock"], step=0.7,
         items=["9/11: 25 TROPAS GRATIS", "10/11: SEMANA DEL SUPERYETI", "TH19: A MITAD DE MES"], source=SRC,
         dur=4.5, color=1, sticker=K + "yeti_azul_con_canasta.png", sticker_h=400, sticker_x=820, sticker_y=1500, sticker_t=2.2,
         vo="El diez es la semana del Superyeti y el Ayuntamiento diecinueve cae a mitad de mes."),
    dict(type="question", q=["¿PARA QUÉ VAS", "A USAR LAS TROPAS?"], options=["GUERRA", "FARMEAR", "NI ME ENTERÉ"],
         dur=4.0, color=2, vo="¿Para qué las vas a usar? Contámelo en los comentarios."),
    dict(type="outro", dur=2.5, color=5),
], title="Mañana 25 tropas gratis", bg_pool=["capturas/menu_eventos_1.jpg", "capturas/aldea_nueva_interfaz.jpg",
                                              K + "arte_coliseo_en_las_nubes.jpg", "capturas/menu_eventos_2.jpg"])

if __name__ == "__main__":
    main(EP)
