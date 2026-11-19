"""TikTok (novedades / eventos del mes, jueves 13:00): mañana arranca el evento de tropas desechables + lo que queda de noviembre.
Fuentes (consultadas el 19/11/2026):
- Supercell, blog oficial en español "Se escucha el fragor de la lucha de titanes" (01/11/2026):
  * 20 al 26/11: "evento de tropas desechables" — "¡Llama a los refuerzos!"; las tropas se agotan al usarlas
    (en inglés: "your pantry isn't endless. Once you've used them all, they're gone").
  * 22 al 28/11: Juegos del Clan — "las tropas de refuerzo te acompañarán durante los primeros cuatro días".
  * 24/11 al 1/12: "desafío de la forja feroz" — héroes armados con piezas de máquinas de asedio (versión en inglés).
- El post no dice qué tropas son ni la hora de inicio: no se nombran.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
SRC = "Supercell, blog oficial (01/11/2026)"
EP = Episode([
    dict(type="hook", kicker="EVENTO NUEVO", lines=[("MAÑANA", "w"), ("LLEGAN LOS", "w"), ("REFUERZOS", "y")],
         sizes=(150, 130, 160), dur=3.5, color=4,
         card="capturas/menu_eventos_1.jpg", card_y=1400,
         vo="¡Ojo! Mañana llegan los refuerzos a Clash."),
    dict(type="alert", lines=[("TROPAS", "y"), ("DESECHABLES", "w")], sub="DEL 20 AL 26 DE NOVIEMBRE",
         source=SRC, dur=4.5, color=0,
         sticker=K + "barbaro_realista_espada.png", sticker_h=420, sticker_x=830, sticker_y=1560, sticker_t=1.4,
         vo="Del veinte al veintiséis de noviembre hay evento de tropas desechables: las llamás como refuerzo."),
    dict(type="versus", title="¿CÓMO FUNCIONAN?", left=("LAS USÁS", "SE GASTAN"), right=("SE TERMINAN", "NO VUELVEN"),
         source=SRC, dur=4.0, color=2,
         vo="Pero cuidado: cada una que usás se gasta, y cuando se terminan, no vuelven."),
    dict(type="list", title="TIP: GUARDALAS PARA...", icon="star", step=0.7,
         items=["LA ESTRELLA QUE FALTA", "ATAQUES DIFÍCILES", "NO EL PRIMER ATAQUE"],
         dur=4.5, color=3,
         sticker=K + "medalla_dorada_rombo.png", sticker_h=260, sticker_x=860, sticker_y=1560, sticker_t=2.4,
         vo="Mi consejo: no las tires en el primer ataque. Guardalas para la estrella que te falta."),
    dict(type="list", title="Y DESPUÉS SE VIENE", icon="check", step=0.7,
         items=["22-28: JUEGOS DEL CLAN", "CON REFUERZOS 4 DÍAS", "24/11: FORJA FEROZ"],
         source=SRC, dur=4.5, color=1,
         card="capturas/menu_eventos_2.jpg", card_y=1450,
         vo="Y ojo, del veintidós arrancan los Juegos del clan con refuerzos, y el veinticuatro la forja feroz."),
    dict(type="question", q=["¿LAS GUARDÁS", "O LAS GASTÁS YA?"], options=["LAS GUARDO", "LAS GASTO YA"],
         dur=3.5, color=5, vo="¿Vos las guardás o las gastás todas el primer día?"),
    dict(type="outro", dur=2.5, color=4),
], title="Mañana: tropas desechables", bg_pool=["capturas/menu_eventos_1.jpg", K + "arte_coliseo_en_las_nubes.jpg",
                                                  "capturas/evento_racha_reglas.jpg", K + "arte_batalla_esqueletos_bruja.jpg"])

if __name__ == "__main__":
    main(EP)
