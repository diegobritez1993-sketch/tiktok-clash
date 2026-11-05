"""TikTok (tip / evento): en la Martillomanía los colectores producen el doble y guardan el doble.
Fuente: Supercell, blog oficial "Clash of Titans Is Hot Off The Press" (01/11/2026): Hammer Jam 1-15/11,
"50% off upgrade timers and costs, plus a 2x boost to resource collector capacities and production".
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
SRC = "Supercell, blog oficial (01/11/2026)"
EP = Episode([
    dict(type="hook", kicker="¡OJO CON ESTO!", lines=[("TUS COLECTORES", "w"), ("RINDEN EL", "w"), ("DOBLE", "y")],
         sizes=(115, 120, 200), sticker=K + "duende_con_bolsa.png", sticker_h=460, sticker_y=1420,
         dur=3.5, color=2, vo="¡Ojo! Ahora mismo tus colectores rinden el doble."),
    dict(type="stat", title="EN LA MARTILLOMANÍA", value=2, prefix="x", suffix="", label="PRODUCCIÓN Y CAPACIDAD",
         sub="DE LOS COLECTORES DE RECURSOS", dur=4.0, color=0,
         card="capturas/aldea_nueva_interfaz.jpg", card_y=1450, card_t=1.8,
         vo="En la Martillomanía producen el doble y guardan el doble."),
    dict(type="list", title="LO QUE TRAE", icons=["up", "up", "star"], step=0.7,
         items=["PRODUCCIÓN x2", "CAPACIDAD x2", "MEJORAS A MITAD DE PRECIO"],
         source=SRC, dur=4.5, color=3, vo="Producción doble, capacidad doble y mejoras a mitad de precio y de tiempo."),
    dict(type="hook", kicker="TIP", lines=[("MEJORÁ TUS", "w"), ("COLECTORES", "y"), ("AHORA", "w")],
         sizes=(130, 150, 150), sticker=K + "recurso_monedas_turquesa.png", sticker_h=380, sticker_x=800,
         sticker_y=1450, sticker_t=1.5, dur=4.0, color=1,
         card="capturas/lista_mejoras.jpg", card_y=1450, card_t=1.2,
         vo="Tip: si los tenés atrasados, mejoralos ahora, que salen a mitad de precio."),
    dict(type="alert", lines=[("SE TERMINA", "w"), ("A MITAD DE MES", "r")], sub="NO LO DEJES PASAR",
         source="Supercell: Martillomanía del 1 al 15/11", dur=4.0, color=4,
         vo="Y no te duermas, que se termina a mitad de mes."),
    dict(type="outro", dur=2.5, color=5),
], title="Colectores al doble", bg_pool=["capturas/aldea_nueva_interfaz.jpg", "capturas/lista_mejoras_filtro.jpg",
                                         K + "arte_aniversario_paisaje.jpg", "capturas/menu_eventos_1.jpg"])

if __name__ == "__main__":
    main(EP)
