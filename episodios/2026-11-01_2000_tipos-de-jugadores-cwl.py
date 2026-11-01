"""TikTok (humor): los tipos de jugadores que aparecen en la Liga de guerras de clanes.
Dato: CWL del 1 al 11 de noviembre 2026 (calendario oficial de Supercell, ver calendario/2026-11.md). El resto es humor.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
EP = Episode([
    dict(type="hook", kicker="ARRANCÓ LA CWL", lines=[("¿CUÁL DE", "w"), ("ESTOS SOS VOS?", "y")], sizes=(130, 130),
         card=K + "humor_barbaro_cine_palomitas.jpg", card_y=1300, dur=3.5, color=2),
    dict(type="list", title="CLÁSICOS DE LA CWL", icons=["clock", "alert", "chat"], step=0.6,
         items=["ATACA EN EL ÚLTIMO MINUTO", "SE OLVIDA DE ATACAR", "\"YA ATACO\" Y NO ATACA"],
         dur=4.5, color=0, sticker=K + "aldeana_pelirroja_sorprendida.png", sticker_h=420, sticker_x=820,
         sticker_y=1450, sticker_t=2.2),
    dict(type="list", title="Y NUNCA FALTAN...", icons=["star", "up", "check"], step=0.6,
         items=["MIRA LA REPE 10 VECES", "PIDE EL MISMO RIVAL", "EL LÍDER QUE NO DUERME"],
         dur=4.5, color=1, card=K + "humor_barbaro_rey_asustados.jpg", card_y=1520, card_t=2.2),
    dict(type="alert", lines=[("CWL: DEL 1", "w"), ("AL 11 DE NOV.", "y")], sub="¡NO TE OLVIDES DE ATACAR!",
         source="Calendario oficial de Supercell, noviembre 2026", dur=4.0, color=4),
    dict(type="question", q=["¿CUÁL ES EL", "DE TU CLAN?"], options=["EL DEL ÚLTIMO MINUTO", "EL QUE NO ATACA",
         "EL LÍDER QUE NO DUERME"], dur=4.5, color=3),
    dict(type="outro", dur=3.0, color=5),
], title="Tipos de jugadores en la CWL", bg_pool=["capturas/guerra_desde_chat.jpg", "capturas/base_guerra_th17_armada.jpg",
                                                  K + "humor_barbaro_cine_palomitas.jpg", "capturas/base_th18_antidos_2.jpg"])

if __name__ == "__main__":
    main(EP)
