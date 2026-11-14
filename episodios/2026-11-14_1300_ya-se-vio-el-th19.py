"""TikTok (novedades): ¡ya se vio el TH19! Primer adelanto del Clash On (13-15/11).
Fuentes: GamingonPhone 13/11/2026 "Town Hall 19 is hitting Clash of Clans soon" (primer adelanto de creadores: 27 millones de
oro y 13 días, modos del Ayuntamiento, 5ª defensa aérea, +25 muros = 350, dos defensas nuevas); Sportsdunia 14/11/2026
"New Squads Announced" (modos del Ayuntamiento: 15 bárbaros, 15 arqueras, 4 magos; revelado en el Clash On).
Fecha de salida: sin anunciar. No se nombran las defensas nuevas (nombre en español no verificado).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
SRC = "Clash On vía GamingonPhone (13/11/2026)"
EP = Episode([
    dict(type="hook", kicker="OFICIAL", lines=[("¡YA SE VIO", "w"), ("EL TH19!", "y")],
         sizes=(150, 180), dur=4.0, color=2,
         card="capturas/aldea_nueva_interfaz.jpg", card_y=1380,
         sticker=K + "aldeana_pelirroja_sorprendida.png", sticker_h=400, sticker_x=850, sticker_y=1660, sticker_t=0.9,
         vo="Supercell ya mostró el Ayuntamiento diecinueve. Mirá lo que trae."),
    dict(type="stat", title="MEJORAR AL TH19", value=27, suffix=" MILLONES", label="DE ORO",
         sub="Y 13 DÍAS DE MEJORA", source=SRC, dur=4.0, color=4,
         sticker=K + "duende_con_bolsa.png", sticker_h=240, sticker_x=880, sticker_y=1460, sticker_t=2.0,
         vo="Mejorarlo cuesta veintisiete millones de oro y trece días."),
    dict(type="list", title="TU AYUNTAMIENTO DEFIENDE", icon="star", step=0.6,
         items=["MODO BÁRBAROS: 15", "MODO ARQUERAS: 15", "MODO MAGOS: 4", "O SIN TROPAS (ORIGINAL)"],
         source="GamingonPhone y Sportsdunia (nov. 2026)", dur=5.0, color=1,
         sticker=K + "barbaro_realista_espada.png", sticker_h=300, sticker_x=900, sticker_y=1765, sticker_t=3.2,
         vo="Y el Ayuntamiento ahora suelta tropas: quince bárbaros, quince arqueras o cuatro magos."),
    dict(type="list", title="Y MÁS DEFENSA", icon="up", step=0.6,
         items=["QUINTA DEFENSA AÉREA", "+25 MUROS (350 EN TOTAL)", "2 DEFENSAS NUEVAS"],
         source=SRC, dur=4.5, color=3, bg="capturas/base_guerra_th18_armada.jpg",
         vo="Suma una quinta defensa aérea, veinticinco muros más y dos defensas nuevas."),
    dict(type="alert", lines=[("¿CUÁNDO", "w"), ("SALE?", "y")], sub="TODAVÍA SIN FECHA OFICIAL",
         source="Supercell no anunció la fecha", dur=3.5, color=0,
         vo="¿Cuándo sale? Supercell todavía no dio la fecha."),
    dict(type="outro", dur=2.5, color=2),
], title="Ya se vio el TH19", bg_pool=["capturas/aldea_nueva_interfaz.jpg", K + "arte_coliseo_en_las_nubes.jpg",
                                       "capturas/base_guerra_th18_vacia.jpg", "capturas/lista_mejoras.jpg"])

if __name__ == "__main__":
    main(EP)
