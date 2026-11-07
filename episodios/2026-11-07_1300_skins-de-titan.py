"""TikTok (novedades del mes): skins de titán, una nueva cada dos días en noviembre 2026.
Fuente: Supercell, blog oficial "Clash of Titans Is Hot Off The Press" (01/11/2026): Grand Titan (Gran centinela)
1-30/11 en el Pase de oro; Titan King (Rey bárbaro) 5-30/11; Titan Prince (Príncipe de los esbirros) 7-30/11;
Titan Champion (Campeona real) 9-30/11; Titan Queen (Reina arquera) 11-30/11; Titan Duke (Duque dragón) 13-30/11.
(Se evita el nombre completo en español del Príncipe y el Duque: en pantalla solo "PRÍNCIPE" y "DUQUE".)
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
SRC = "Supercell, blog oficial (01/11/2026)"
EP = Episode([
    dict(type="hook", kicker="TEMPORADA DE TITANES", lines=[("¡HOY SALE", "w"), ("UNA SKIN", "y"), ("NUEVA!", "y")],
         sizes=(140, 170, 170), card="capturas/heroe_reina_stats.jpg", card_y=1450, dur=3.5, color=2,
         sticker=K + "estatua_rey_barbaro.png", sticker_h=380, sticker_x=860, sticker_y=1650, sticker_t=1.2,
         vo="¡Hoy sale una skin nueva de titán!"),
    dict(type="stat", title="ESTE NOVIEMBRE", value=6, prefix="", suffix="", label="SKINS DE TITÁN",
         sub="UNA NUEVA CADA DOS DÍAS", source=SRC, dur=3.5, color=0,
         vo="Este mes son seis skins de titán, una cada dos días."),
    dict(type="list", title="YA SALIERON", icons=["star", "check", "check"], step=0.7,
         items=["GRAN CENTINELA: PASE DE ORO", "REY BÁRBARO: 5/11", "PRÍNCIPE: HOY 7/11"], source=SRC,
         dur=4.5, color=1, vo="El Gran centinela viene en el Pase de oro, el Rey salió el cinco y hoy el Príncipe."),
    dict(type="list", title="LO QUE VIENE", icons=["clock", "clock", "clock"], step=0.7,
         items=["CAMPEONA REAL: 9/11", "REINA ARQUERA: 11/11", "DUQUE: 13/11"], source=SRC, dur=4.5, color=3,
         sticker=K + "decoracion_fuente_reina_xl.png", sticker_h=380, sticker_x=820, sticker_y=1500, sticker_t=2.4,
         vo="Después vienen la Campeona el nueve, la Reina el once y el Duque el trece."),
    dict(type="alert", lines=[("DISPONIBLES", "w"), ("HASTA EL 30/11", "y")], sizes=(130, 120),
         sub="ESPERÁ A VERLAS TODAS", source=SRC, dur=3.5, color=4,
         vo="Están hasta el treinta: esperá a verlas todas antes de gastar."),
    dict(type="question", q=["¿CUÁL TE", "VAS A COMPRAR?"], options=["REY", "REINA", "CAMPEONA", "NINGUNA"],
         dur=4.0, color=5, vo="¿Cuál te vas a comprar? Comentalo."),
    dict(type="outro", dur=2.5, color=2),
], title="Skins de titán", bg_pool=["capturas/aldea_nueva_interfaz.jpg", K + "arte_coliseo_en_las_nubes.jpg",
                                    "capturas/heroe_reina_stats.jpg", "capturas/menu_eventos_2.jpg"])

if __name__ == "__main__":
    main(EP)
