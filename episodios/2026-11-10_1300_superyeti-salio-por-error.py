"""TikTok (¿sabías que? + novedades): el Superyeti salió por error antes de tiempo, y desde hoy tiene su semana.
Datos: Yeti presentado el 05/12/2019 en la actualización del TH13 (AppTrigger, 05/12/2019).
Superyeti liberado por error a principios de abril 2025 y retirado (Sportskeeda, "Super Yeti release date and stats", may. 2025).
Salida oficial 12/05/2025 con su Mini Spotlight (Supercell, blog oficial "Mini Spotlight Event: Super Yeti", 12/05/2025).
Tropa destacada Superyeti 10-16/11/2026: Supercell, blog oficial 01/11/2026 (ver calendario/2026-11.md); se juega con
estrellas en multijugador y se canjean premios (TrophyCoach, guía noviembre 2026).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
EP = Episode([
    dict(type="hook", kicker="¿SABÍAS QUE...?", lines=[("EL SUPERYETI", "w"), ("SALIÓ", "y"), ("POR ERROR", "r")],
         sizes=(120, 140, 170), sticker=K + "yeti_azul_con_canasta.png", sticker_h=520, sticker_y=1330,
         sticker_t=0.8, dur=3.5, color=5,
         vo="¿Sabías que el Superyeti salió por error, antes de tiempo?"),
    dict(type="hook", kicker="DICIEMBRE", lines=[("EL YETI", "w"), ("LLEGÓ EN 2019", "y"), ("CON EL TH13", "w")],
         sizes=(130, 120, 110), source="AppTrigger, 05/12/2019", dur=3.5, color=1,
         card="capturas/lista_mejoras.jpg", card_y=1400,
         vo="Primero llegó el Yeti, en diciembre de dos mil diecinueve, con el Ayuntamiento trece."),
    dict(type="alert", lines=[("ABRIL 2025", "y"), ("¡APARECIÓ", "w"), ("SIN AVISO!", "r")],
         sub="LO SOLTARON SIN QUERER", source="Sportskeeda (mayo 2025)", dur=4.5, color=0,
         sticker=K + "aldeana_pelirroja_sorprendida.png", sticker_h=340, sticker_x=920, sticker_y=1720, sticker_t=1.6,
         vo="En abril de dos mil veinticinco apareció en el juego sin aviso. Supercell lo soltó sin querer y lo retiró."),
    dict(type="stat", value=12, label="DE MAYO DE 2025", sub="SALIÓ OFICIAL, CON SU PROPIO EVENTO",
         source="Supercell, blog oficial (12/05/2025)", dur=3.5, color=4,
         vo="El doce de mayo salió oficial, con su propio evento."),
    dict(type="list", title="DESDE HOY: SU SEMANA", icon="star", step=0.6,
         items=["DEL 10 AL 16 DE NOVIEMBRE", "SUMÁ CON ESTRELLAS EN MULTI", "CANJEÁ PREMIOS DEL EVENTO"],
         source="Supercell, blog oficial (01/11/2026)", dur=4.5, color=3,
         sticker=K + "cofre_rosa_hexagono.png", sticker_h=300, sticker_x=840, sticker_y=1560, sticker_t=2.4,
         vo="Y desde hoy vuelve su semana: del diez al dieciséis, sumá con estrellas y canjeá premios."),
    dict(type="question", q=["¿USÁS EL", "SUPERYETI?"], options=["SIEMPRE", "A VECES", "NUNCA"],
         dur=3.5, color=2, vo="¿Vos usás el Superyeti? Contame."),
    dict(type="outro", dur=2.5, color=5),
], title="Superyeti por error", bg_pool=[K + "arte_coliseo_en_las_nubes.jpg", "capturas/aldea_nueva_interfaz.jpg",
                                         "capturas/menu_eventos_1.jpg", "capturas/tropa_golem_meteorico.jpg"])

if __name__ == "__main__":
    main(EP)
