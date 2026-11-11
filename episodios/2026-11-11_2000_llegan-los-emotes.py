"""TikTok (novedades confirmadas): Supercell anunció emotes, cambio en el bono de estrellas y snacks nuevos.
Fuente: Supercell, blog oficial "Stars, Snacks and Showing Off" (10/11/2026): emotes después de las batallas, en el chat
del clan y en las clasificaciones; nunca durante la batalla en vivo; sets de 5 (juntás 4 y desbloqueás el bonus); no se
pueden desactivar al salir. Bono de estrellas según el Ayuntamiento (antes según la liga): 2 estrellas = snack de botín,
5 estrellas = botín + mineral + snack al azar. Snack de botín x2, x3 o x4 en la próxima batalla. Llega "más adelante este mes".
Nombres en español de los snacks no verificados: no se nombran.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
EP = Episode([
    dict(type="hook", kicker="CONFIRMADO POR SUPERCELL", lines=[("¡LLEGAN", "w"), ("LOS EMOTES", "y"), ("A CLASH!", "w")],
         sizes=(150, 150, 150), dur=3.5, color=2,
         sticker=K + "aldeana_pelirroja_sorprendida.png", sticker_h=420, sticker_x=830, sticker_y=1640, sticker_t=0.8,
         card="capturas/aldea_nueva_interfaz.jpg", card_y=1400,
         vo="¡Confirmado por Supercell! Llegan los emotes a Clash, este mes."),
    dict(type="list", title="ASÍ VAN A FUNCIONAR", icon="check", step=0.6,
         items=["DESPUÉS DE CADA BATALLA", "EN EL CHAT DEL CLAN", "NUNCA EN PLENA BATALLA", "SETS DE 5 PARA JUNTAR"],
         source="Supercell, blog oficial (10/11/2026)", dur=5.0, color=1,
         bg="capturas/guerra_desde_chat.jpg",
         vo="Aparecen después de cada batalla y en el chat del clan, nunca en pleno ataque. Y vienen en sets para juntar."),
    dict(type="alert", lines=[("OJO:", "y"), ("NO SE PUEDEN", "w"), ("DESACTIVAR", "r")],
         sub="AL MENOS AL PRINCIPIO", source="Supercell, blog oficial (10/11/2026)", dur=3.5, color=0,
         bg=K + "humor_barbaro_rey_asustados.jpg",
         vo="Ojo: al principio no se van a poder desactivar."),
    dict(type="versus", title="BONO DE ESTRELLAS", left=("ANTES", "TU LIGA"), right=("AHORA", "TU TH"),
         source="Supercell, blog oficial (10/11/2026)", dur=4.0, color=3,
         vo="Y cambia el bono de estrellas: ya no depende de tu liga, sino de tu Ayuntamiento."),
    dict(type="stat", value=4, prefix="x", label="BOTÍN EN UN ATAQUE", sub="SNACK NUEVO: x2, x3 O x4 (ORO, ELIXIR Y OSCURO)",
         source="Supercell, blog oficial (10/11/2026)", dur=4.0, color=4,
         sticker=K + "duende_con_bolsa.png", sticker_h=330, sticker_x=860, sticker_y=1600, sticker_t=1.8,
         vo="Además, un snack nuevo multiplica tu botín por dos, por tres o hasta por cuatro."),
    dict(type="question", q=["¿TE GUSTAN", "LOS EMOTES?"], options=["ME ENCANTAN", "ME DA IGUAL", "VAN A MOLESTAR"],
         dur=3.5, color=5, vo="¿Y a vos? ¿Te gustan los emotes o van a molestar?"),
    dict(type="outro", dur=2.5, color=2),
], title="Llegan los emotes", bg_pool=[K + "arte_aniversario_fiesta.jpg", "capturas/aldea_nueva_interfaz.jpg",
                                       K + "arte_coliseo_en_las_nubes.jpg", "capturas/menu_eventos_2.jpg"])

if __name__ == "__main__":
    main(EP)
