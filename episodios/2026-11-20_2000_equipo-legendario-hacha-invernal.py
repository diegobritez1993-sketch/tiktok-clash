"""TikTok (novedades confirmadas, viernes 20:00): llega el equipo legendario, empezando por el hacha invernal del Rey.
Fuente: Supercell, blog oficial "An all-new Equipment rarity is coming to Clash of Clans" (17/11/2026), versión en
español: "equipo legendario", "hacha invernal", "evento de forjado a runa", "pase de la fragua" (9,99 USD, precio
regional; trae el hacha mejorada hasta nivel 15), gratis desde ayuntamiento 8, nivel máximo 33 (28-30 con ayuntamiento 16,
31-33 con ayuntamiento 18), llega "en una fecha posterior de este mismo año" (sin fecha exacta).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
SRC = "Supercell, blog oficial (17/11/2026)"
EP = Episode([
    dict(type="hook", kicker="OFICIAL", lines=[("LLEGA EL", "w"), ("EQUIPO", "w"), ("LEGENDARIO", "y")],
         sizes=(130, 150, 160), dur=3.5, color=4,
         card=K + "humor_rey_espejo_manga.jpg", card_y=1420,
         vo="¡Es oficial! Llega el equipo legendario a Clash."),
    dict(type="alert", lines=[("HACHA", "y"), ("INVERNAL", "w")], sub="PARA EL REY BÁRBARO",
         source=SRC, dur=4.0, color=1,
         sticker=K + "estatua_rey_barbaro.png", sticker_h=420, sticker_x=820, sticker_y=1540, sticker_t=1.2,
         vo="La primera pieza es el hacha invernal, para el Rey bárbaro."),
    dict(type="versus", title="¿CÓMO LA CONSEGUÍS?", left=("EVENTO", "GRATIS"), right=("PASE", "$9,99"),
         source=SRC, dur=4.0, color=2,
         vo="Gratis con un evento de forjado. El pase de nueve noventa y nueve dólares es opcional."),
    dict(type="stat", value=33, label="NIVEL MÁXIMO", sub="EL PASE LA TRAE EN NIVEL 15",
         source=SRC, dur=3.5, color=0,
         sticker=K + "cofre_madera_hierro.png", sticker_h=240, sticker_x=860, sticker_y=1620, sticker_t=1.5,
         vo="Sube hasta nivel treinta y tres. El pase te la da en nivel quince."),
    dict(type="list", title="LO QUE TENÉS QUE SABER", icon="check", step=0.7,
         items=["GRATIS: AYUNTAMIENTO 8+", "28 AL 30: AYUNTAMIENTO 16", "31 AL 33: AYUNTAMIENTO 18", "LLEGA ESTE AÑO, SIN FECHA"],
         source=SRC, dur=5.0, color=3,
         vo="Gratis desde Ayuntamiento ocho, los últimos niveles piden dieciséis y dieciocho. Llega este año, sin fecha."),
    dict(type="question", q=["¿PAGÁS EL PASE", "O VAS GRATIS?"], options=["PAGO EL PASE", "GRATIS"],
         dur=3.5, color=5, vo="¿Vos pagás el pase o la sacás gratis? Comentá."),
    dict(type="outro", dur=2.5, color=4),
], title="Llega el equipo legendario", bg_pool=["capturas/equipo_flecha_congelada.jpg", K + "arte_coliseo_en_las_nubes.jpg",
                                                  "capturas/heroe_reina_stats.jpg", K + "arte_aniversario_fiesta.jpg"])

if __name__ == "__main__":
    main(EP)
