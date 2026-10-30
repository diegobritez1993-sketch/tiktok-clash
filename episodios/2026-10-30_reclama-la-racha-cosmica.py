"""TikTok: aviso para reclamar la recompensa de la Racha cósmica.
Fuentes: pantalla del evento en el juego (reclamar antes del 1/11 08:00 UTC = 05:00 Paraguay);
GamingonPhone, eventos de octubre 2026 (evento del 16 al 30 de octubre, reclamable hasta el 1 de noviembre).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

EP = Episode([
    dict(type="hook", kicker="¡OJO!", lines=[("NO PIERDAS", "w"), ("TU", "w"), ("RECOMPENSA", "y")], icon="gift", dur=3.5),
    dict(type="alert", lines=[("LA RACHA CÓSMICA", "w"), ("YA TERMINÓ", "r")], sub="RECLAMALA ANTES DEL 1/11", dur=4.0,
         source="Evento del 16 al 30 de octubre"),
    dict(type="list", title="TENÉS HASTA EL 1/11", icon="clock", step=0.6,
         items=["08:00 UTC", "05:00 PARAGUAY / ARGENTINA", "02:00 MÉXICO", "09:00 ESPAÑA"],
         source="Juego: reclamar antes del 1/11 08:00 UTC", dur=4.5),
    dict(type="list", title="CÓMO HACERLO", icon="check", step=0.6,
         items=["ENTRÁ AL JUEGO", "ABRÍ EL EVENTO DE LA RACHA", "RECLAMÁ TUS PREMIOS"], dur=4.0),
    dict(type="question", q=["¿LLEGASTE A LA", "RACHA DE 7 DÍAS?"], options=["SÍ", "NO"], dur=4.0),
    dict(type="outro", dur=3.0),
], title="Reclamá la Racha cósmica")

if __name__ == "__main__":
    main(EP)
