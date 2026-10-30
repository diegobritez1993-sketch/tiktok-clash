"""TikTok: cambios de balance de octubre 2026.
Fuente: Supercell, "Balance Changes Incoming: October 2026" (17/10/2026)
https://supercell.com/en/games/clashofclans/blog/news/balance-changes-incoming-october-2026/
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

SRC = "Supercell, 17/10/2026"
EP = Episode([
    dict(type="hook", kicker="NOTICIA", lines=[("¡SUPERCELL", "w"), ("CAMBIÓ EL", "w"), ("BALANCE!", "y")], icon="alert", dur=3.5),
    dict(type="change", name="FLECHA CONGELADA", label="DAÑO A NIVEL MÁXIMO", before="168", after="175",
         note="+5% de ralentización en todos los niveles", source=SRC, dur=4.5),
    dict(type="list", title="TAMBIÉN SUBEN", icon="up", step=0.6,
         items=["VIDA: MONTAPUERCOS", "VIDA: SUPERMONTAPUERCOS", "VIDA: MINERO Y SUPERMINERO", "DAÑO: P.E.K.K.A", "VIDA: GÓLEM METEÓRICO"],
         source=SRC, dur=5.0),
    dict(type="hook", kicker="MI TEORÍA", lines=[("¿VUELVE LA", "w"), ("CAMINATA", "w"), ("DE REINA?", "y")], dur=3.5),
    dict(type="question", q=["¿VAS A PROBAR", "EL HÍBRIDO?"], options=["SÍ", "NO"], dur=4.0),
    dict(type="outro", dur=3.0),
], title="Cambios de balance octubre 2026")

if __name__ == "__main__":
    main(EP)
