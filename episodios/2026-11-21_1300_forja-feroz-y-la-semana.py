"""TikTok (novedades / eventos de la semana, sábado 13:00): héroes armados con huesos de máquinas de asedio
(desafío de la forja feroz) + lo que queda de noviembre, día por día.
Fuentes (consultadas el 21/11/2026):
- Supercell, blog oficial "Clash of Titans Is Hot Off The Press" (01/11/2026) / en español "Se escucha el fragor de la
  lucha de titanes":
  * 24/11 al 1/12: "Fully Forged Challenge" = "desafío de la forja feroz": "Assemble Heroes built from the bones of
    Siege Machines" (héroes armados con piezas/huesos de máquinas de asedio). No dice premios ni ayuntamiento.
  * 22 al 28/11: Juegos del clan; tropas de refuerzo los primeros cuatro días.
  * 20 al 26/11: evento de tropas desechables.
  * 16 al 23/11: caza del tesoro (ayuntamientos 1 a 17).
  * skins de titán y cosméticos de las Tierras baldías: hasta el 30/11.
- Supercell, blog oficial "Estrellas, aperitivos y jefes presumidos" (10/11/2026): primeros premios de Medallas
  competitivas el lunes 23/11.
No se dan horas (el post no las da).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
SRC = "Supercell, blog oficial (01/11/2026)"
EP = Episode([
    dict(type="hook", kicker="SE VIENE", lines=[("¿HÉROES HECHOS", "w"), ("CON MÁQUINAS", "y"), ("DE ASEDIO?", "y")],
         sizes=(110, 130, 130), dur=3.5, color=4,
         sticker=K + "maquina_taladro_calavera.png", sticker_h=460, sticker_x=540, sticker_y=1380, sticker_t=0.6,
         vo="¿Héroes armados con máquinas de asedio? Sí, se viene."),
    dict(type="alert", lines=[("DESAFÍO DE LA", "w"), ("FORJA FEROZ", "y")], sub="DEL 24/11 AL 1/12",
         source=SRC, dur=4.0, color=0,
         sticker=K + "maquina_dirigible_barril_rojo.png", sticker_h=380, sticker_x=810, sticker_y=1560, sticker_t=1.3,
         vo="Es el desafío de la forja feroz: héroes hechos con huesos de máquinas de asedio, del veinticuatro al primero."),
    dict(type="list", title="TU SEMANA EN CLASH", icon="star", step=0.65,
         items=["22: JUEGOS DEL CLAN", "23: PAGO DE MEDALLAS", "23: FIN CAZA DEL TESORO", "24: FORJA FEROZ",
                "26: FIN TROPAS DESECHABLES"],
         source="Supercell, blog oficial (01/11 y 10/11/2026)", dur=5.0, color=1,
         vo="Mañana Juegos del clan, el lunes cobrás medallas y termina la caza del tesoro, el martes forja feroz."),
    dict(type="versus", title="JUEGOS DEL CLAN", left=("22 AL 25", "REFUERZOS"), right=("26 AL 28", "NORMAL"),
         source=SRC, dur=4.0, color=3,
         sticker=K + "duende_con_bolsa.png", sticker_h=300, sticker_x=540, sticker_y=1560, sticker_t=1.4,
         vo="Ojo: en los Juegos del clan, los refuerzos están solo los primeros cuatro días."),
    dict(type="stat", value=30, prefix="", suffix="/11", label="ÚLTIMO DÍA", sub="SKINS DE TITÁN Y TIERRAS BALDÍAS",
         source=SRC, dur=3.5, color=2,
         card=K + "oficial_calendario_noviembre_2026.jpg", card_y=1800,
         vo="Y las skins de titán se van el treinta. Últimos días."),
    dict(type="question", q=["¿QUÉ HÉROE", "QUERÉS VER FORJADO?"], options=["REY", "REINA", "CENTINELA"],
         dur=3.5, color=5, vo="¿Qué héroe querés ver armado con máquinas? Comentá."),
    dict(type="outro", dur=2.5, color=4),
], title="Forja feroz y tu semana", bg_pool=[K + "arte_coliseo_en_las_nubes.jpg", "capturas/menu_eventos_1.jpg",
                                              "capturas/aldea_nueva_interfaz.jpg", "capturas/menu_eventos_2.jpg"])

if __name__ == "__main__":
    main(EP)
