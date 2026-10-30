"""TikTok: se viene la Martillomanía (1/11/2026) + tips para aprovecharla.
Fuentes: cuenta regresiva en el juego (empieza el 1/11); Supercell, "HAMMER JAM Kickstarts the November Season" (nov 2025:
-50% tiempo y costo de mejoras); Clash Ninja, "When is Hammer Jam?" (tips: pociones, no usar libros/martillos,
mejoras largas el último día).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

EP = Episode([
    dict(type="hook", kicker="SE VIENE", lines=[("¡LLEGA LA", "w"), ("MARTILLO-", "y"), ("MANÍA!", "y")], icon="alert",
         sizes=(110, 170, 170), dur=3.0, color=4),
    dict(type="alert", lines=[("EMPIEZA EL", "w"), ("1 DE NOVIEMBRE", "y")], sub="¡YA HAY CUENTA REGRESIVA!",
         source="Cuenta regresiva en el juego", dur=3.5, color=0),
    dict(type="stat", title="EN EDICIONES ANTERIORES", value=50, prefix="-", suffix="%", label="TIEMPO Y COSTO",
         sub="de las mejoras · confirmalo en el juego", source="Supercell, Martillomanía nov. 2025", dur=4.0, color=1),
    dict(type="list", title="ANTES DE QUE EMPIECE", icon="check", step=0.6,
         items=["GUARDÁ RECURSOS", "NO EMPIECES MEJORAS LARGAS", "JUNTÁ POCIONES"], dur=4.5, color=3),
    dict(type="list", title="DURANTE EL EVENTO", icons=["star", "alert", "clock"], step=0.6,
         items=["USÁ POCIONES DE CONSTRUCTOR", "GUARDÁ LIBROS Y MARTILLOS", "ÚLTIMO DÍA: MEJORAS LARGAS"],
         source="Clash Ninja", dur=4.5, color=2),
    dict(type="question", q=["¿QUÉ VAS A", "MEJORAR PRIMERO?"], options=["HÉROES", "DEFENSAS", "TROPAS"], dur=4.0, color=5),
    dict(type="outro", dur=3.0, color=4),
], title="Se viene la Martillomanía")

if __name__ == "__main__":
    main(EP)
