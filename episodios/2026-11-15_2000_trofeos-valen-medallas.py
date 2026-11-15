"""TikTok (tips / novedades confirmadas): desde la semana del 16/11 tus trofeos se convierten en Medallas competitivas.
Fuente: Supercell, blog oficial en español "Estrellas, aperitivos y jefes presumidos" (10/11/2026):
- Debajo de la Liga de Leyendas, los trofeos se convierten en medallas competitivas al reiniciarse al final de cada torneo;
  la cantidad depende de si ascendés o descendés. En Leyendas se ganan cada semana de batalla.
- No son retroactivas (todos arrancan de cero). El nivel del ayuntamiento limita cuántas podés guardar.
- Leyendas I: mínimo garantizado de 2000. Leyendas II: hasta 3500 (40 trofeos en cada ataque y defensa).
- Primera semana: la del 16/11; primeros premios el lunes 23/11.
- Tienda de prestigio: junta la tienda del modo competitivo, la de la Liga de guerras (LGC) y la tienda lujosa; cada una con su divisa.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
SRC = "Supercell, blog oficial (10/11/2026)"
EP = Episode([
    dict(type="hook", kicker="¡OJO! DESDE MAÑANA", lines=[("TUS TROFEOS", "w"), ("VALEN MEDALLAS", "y")],
         sizes=(140, 130), dur=3.5, color=4,
         card="capturas/boton_batalla.jpg", card_y=1380,
         sticker=K + "medalla_dorada_rombo.png", sticker_h=330, sticker_x=870, sticker_y=1680, sticker_t=0.8,
         vo="Ojo: desde mañana tus trofeos se convierten en medallas."),
    dict(type="list", title="MEDALLAS COMPETITIVAS", icon="star", step=0.6,
         items=["ARRANCA EL LUNES 16", "PRIMER PAGO: LUNES 23", "MÁS SI SUBÍS DE LIGA", "TODOS DESDE CERO"],
         source=SRC, dur=5.0, color=1,
         vo="Arrancan el lunes dieciséis y el primer pago llega el veintitrés. Si subís de liga, ganás más."),
    dict(type="versus", title="EN LIGA DE LEYENDAS", left=("MÍNIMO EN I", "2K"), right=("HASTA EN II", "3,5K"),
         source="Supercell (II: con 40 trofeos por ataque y defensa)", dur=4.0, color=2,
         vo="En Leyendas uno, mínimo dos mil por semana. En Leyendas dos, hasta tres mil quinientas."),
    dict(type="list", title="TIENDA DE PRESTIGIO", icon="check", step=0.55,
         items=["TIENDA COMPETITIVA", "TIENDA DE LIGA DE GUERRAS", "TIENDA LUJOSA", "TODO EN UN LUGAR"],
         source=SRC, dur=4.5, color=3,
         sticker=K + "cofre_rosa_hexagono.png", sticker_h=280, sticker_x=880, sticker_y=1640, sticker_t=2.6,
         vo="Y la nueva Tienda de prestigio junta tres tiendas en una, cada una con su moneda."),
    dict(type="alert", lines=[("TIP:", "w"), ("ACUMULAR TIENE TOPE", "y")], sizes=(110, 100), sub="DEPENDE DE TU AYUNTAMIENTO",
         source=SRC, dur=3.5, color=0,
         vo="Tip: no podés guardar infinitas, el tope depende de tu Ayuntamiento."),
    dict(type="question", q=["¿EN QUÉ LIGA", "ESTÁS VOS?"], options=["LEYENDAS", "MÁS ABAJO", "NI IDEA"], dur=3.5, color=5,
         vo="¿En qué liga estás vos? Contame."),
    dict(type="outro", dur=2.5, color=4),
], title="Tus trofeos valen medallas", bg_pool=["capturas/aldea_nueva_interfaz.jpg", "capturas/menu_eventos_1.jpg",
                                                 K + "arte_coliseo_en_las_nubes.jpg", "capturas/guerra_desde_chat.jpg"])

if __name__ == "__main__":
    main(EP)
