"""TikTok: ¡ES OFICIAL! El TH19 se muestra del 13 al 15/11 (seguimiento del rumor del 31/10).
Fuente: calendario oficial de Supercell "November Season Calendar" 2026 (capturas/kit_creador/oficial_calendario_noviembre_2026.jpg,
ver calendario/2026-11.md): "TH19 Clash On & Creator Sneak Peeks" 13-15 nov; CWL 1-11; Martillomanía 1-16;
Último desafío del TH18 9-16; Juegos del clan 22-28. La FECHA DE SALIDA del TH19 sigue sin anunciarse.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
EP = Episode([
    dict(type="hook", kicker="¡OFICIAL!", lines=[("EL TH19", "y"), ("YA TIENE", "w"), ("FECHA DE SHOW", "w")],
         sizes=(190, 120, 120), card=K + "oficial_calendario_noviembre_2026.jpg", card_y=1350, dur=3.5, color=0),
    dict(type="alert", lines=[("DEL 13 AL 15", "y"), ("DE NOVIEMBRE", "w")], sizes=(140, 110),
         sub="CLASH ON DEL TH19", source="Calendario oficial de Supercell, noviembre 2026", dur=4.0, color=2,
         sticker=K + "boton_eventos_calendario.png", sticker_h=240, sticker_y=1440, sticker_t=1.2),
    dict(type="versus", title="¿QUÉ ESTÁ CONFIRMADO?", left=("SE MUESTRA", "13 AL 15"), right=("SALE", "SIN FECHA"),
         source="Supercell solo confirmó el Clash On, no la salida", dur=4.0, color=1),
    dict(type="list", title="NOVIEMBRE EN CLASH", icons=["star", "clock", "alert", "check"], step=0.55,
         items=["CWL: 1 AL 11", "MARTILLOMANÍA: 1 AL 16", "ÚLTIMO DESAFÍO TH18: 9 AL 16", "JUEGOS DEL CLAN: 22 AL 28"],
         source="Calendario oficial de Supercell, noviembre 2026", dur=5.0, color=3),
    dict(type="hook", kicker="TIP", lines=[("¿MARTILLOMANÍA?", "y"), ("TERMINÁ MEJORAS", "w"), ("ANTES DEL TH19", "w")],
         sizes=(110, 100, 100), sticker=K + "edificio_cabana_constructor_dorada.png", sticker_h=460, sticker_y=1400,
         dur=3.5, color=4),
    dict(type="outro", dur=3.0, color=5),
], title="El TH19 es oficial", bg_pool=["capturas/aldea_nueva_interfaz.jpg", "capturas/base_guerra_th18_armada.jpg",
                                        "capturas/menu_eventos_1.jpg", "capturas/lista_mejoras.jpg"])

if __name__ == "__main__":
    main(EP)
