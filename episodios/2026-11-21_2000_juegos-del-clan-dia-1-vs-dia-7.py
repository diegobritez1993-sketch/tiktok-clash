"""TikTok (humor, sábado 20:00): los Juegos del clan, del día 1 al día 7. Humor (sin datos); Juegos del clan 22-28/11
(Supercell, blog oficial 01/11/2026). Tope individual de 4.000 puntos (Sportskeeda, guía Juegos del clan nov. 2026)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
EP = Episode([
    dict(type="hook", kicker="MAÑANA EMPIEZAN", lines=[("JUEGOS DEL CLAN:", "w"), ("DÍA 1", "g"), ("VS DÍA 7", "r")],
         sizes=(110, 160, 160), dur=3.5, color=3,
         card=K + "humor_barbaro_rey_asustados.jpg", card_y=1420,
         vo="Juegos del clan: el día uno contra el día siete. Todos pasamos por esto."),
    dict(type="hook", kicker="DÍA 1", lines=[("\"ESTA VEZ", "w"), ("HAGO LOS 4.000", "y"), ("EN UNA TARDE\"", "w")],
         sizes=(120, 120, 120), dur=3.5, color=1,
         sticker=K + "estatua_barbaro_estrella.png", sticker_h=420, sticker_x=540, sticker_y=1450, sticker_t=1.0,
         vo="Día uno: esta vez hago los cuatro mil puntos en una tarde."),
    dict(type="list", title="DÍA 3", icon="chat", step=0.8,
         items=["\"BORRO ESTE, ES MUY DIFÍCIL\"", "\"ESTE TAMBIÉN\"", "\"Y ESTE... TAMBIÉN\""],
         dur=4.5, color=4, bg="capturas/guerra_desde_chat.jpg",
         vo="Día tres: borro este que es difícil. Y este. Y este también."),
    dict(type="versus", title="DÍA 5", left=("EL LÍDER", "¡VAMOS!"), right=("EL CLAN", "DURMIENDO"),
         dur=4.0, color=0,
         sticker=K + "aldeana_pelirroja_sorprendida.png", sticker_h=360, sticker_x=820, sticker_y=1560, sticker_t=1.6,
         vo="Día cinco: el líder grita que falta poco. En línea, dos personas."),
    dict(type="alert", lines=[("DÍA 7, 23:59", "r"), ("FALTAN", "w"), ("200 PUNTOS", "y")], sub="Y EL QUE NO HIZO NADA ELIGE PREMIO",
         dur=4.5, color=2,
         vo="Día siete, último minuto, faltan doscientos puntos... y el que no hizo nada viene a elegir premio."),
    dict(type="question", q=["¿EN QUÉ DÍA", "TE RENDÍS VOS?"], options=["DÍA 1", "DÍA 3", "NUNCA"],
         dur=3.5, color=5, vo="¿Y vos en qué día te rendís? Contame."),
    dict(type="outro", dur=2.5, color=3),
], title="Juegos del clan: día 1 vs día 7", bg_pool=[K + "arte_aniversario_fiesta.jpg", "capturas/menu_eventos_1.jpg",
                                                      "capturas/aldea_nueva_interfaz.jpg", K + "arte_aniversario_paisaje.jpg"])

if __name__ == "__main__":
    main(EP)
