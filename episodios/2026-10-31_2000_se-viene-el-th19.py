"""TikTok: ¿se viene el TH19? Rumores de fecha + lo que insinuó Supercell.
Fuentes:
- Clash Ninja, "Town Hall 18 is here" (17/11/2025): el TH18 ya estaba en el juego el 17/11/2025.
- Yahoo Tech, "Expected Dates for Clash of Clans Town Hall 19 and Hammer Jam 2026" (25/10/2026):
  fecha esperada TH19 23/11/2026, NO oficial (Supercell no la anunció).
- GamingonPhone (15/07/2026): Fernando Ferri (Community Manager de Supercell) en Judo Sloth Talks:
  tropas viejas "interesantes de nuevo", idea de juntar mascotas con el laboratorio y un 2º investigador. Ideas sin fecha.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

EP = Episode([
    dict(type="hook", kicker="RUMOR", lines=[("¿SE VIENE", "w"), ("EL TH19?", "y")], sizes=(130, 190),
         card="capturas/aldea_nueva_interfaz.jpg", card_y=1250, dur=3.5, color=2),
    dict(type="versus", title="¿SE REPITE LA HISTORIA?", left=("NOV 2025", "TH18"), right=("¿NOV 2026?", "TH19"),
         source="Clash Ninja: TH18 ya estaba el 17/11/2025", dur=4.0, color=1),
    dict(type="alert", lines=[("FECHA QUE", "w"), ("CIRCULA:", "w"), ("23 DE NOVIEMBRE", "y")], sizes=(100, 100, 120),
         sub="NO CONFIRMADO POR SUPERCELL", source="Yahoo Tech, 25/10/2026 (no oficial)", dur=4.0, color=0),
    dict(type="list", title="LO QUE INSINUÓ SUPERCELL", icons=["star", "check", "clock"], step=0.6,
         items=["TROPAS VIEJAS, ÚTILES OTRA VEZ", "MASCOTAS AL LABORATORIO", "¿2 INVESTIGACIONES A LA VEZ?"],
         source="F. Ferri (Supercell), Judo Sloth Talks, jul 2026", dur=5.0, color=3),
    dict(type="question", q=["¿QUÉ LE PEDÍS", "AL TH19?"], options=["HÉROE NUEVO", "TROPA NUEVA", "2º INVESTIGADOR"],
         dur=4.5, color=4),
    dict(type="outro", dur=3.0, color=5),
], title="¿Se viene el TH19?", bg_pool=["capturas/base_guerra_th18_armada.jpg", "capturas/lista_mejoras.jpg",
                                         "capturas/heroe_reina_stats.jpg", "capturas/aldea_nueva_interfaz.jpg"])

if __name__ == "__main__":
    main(EP)
