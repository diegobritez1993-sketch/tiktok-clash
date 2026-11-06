"""TikTok (historia de Clash): el chat global se fue en 2019 y volvió en 2026.
Fuentes: Clash Ninja, "October 2019 update has arrived" (19/10/2019): Supercell sacó el chat global por el costo de
moderarlo, estafas, amenazas y comportamiento predatorio; a cambio mejoró el buscador de clanes.
GamingonPhone, "Clash of Clans brings back global chat after nearly seven years" (15/06/2026): vuelve con la
actualización de junio 2026; grupos de hasta 800 miembros (públicos, por invitación o privados); un grupo de 600 puede
pasar a comunidad de hasta 50.000; comunidades siempre públicas, filtro familiar y mensajes que se borran a las 12 h.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
S19 = "Clash Ninja, actualización de octubre 2019"
S26 = "GamingonPhone, 15/06/2026"
EP = Episode([
    dict(type="hook", kicker="HISTORIA DE CLASH", lines=[("¿TE ACORDÁS", "w"), ("DEL CHAT", "y"), ("GLOBAL?", "y")],
         sizes=(130, 170, 170), card="capturas/guerra_desde_chat.jpg", card_y=1490, dur=3.5, color=1,
         sticker=K + "boton_clan.png", sticker_h=230, sticker_x=880, sticker_y=1680, sticker_t=1.2,
         vo="¿Te acordás del chat global? Tiene una historia tremenda."),
    dict(type="alert", lines=[("2019:", "w"), ("LO BORRARON", "r")], sizes=(150, 130), sub="LO DECIDIÓ SUPERCELL",
         source=S19, dur=3.5, color=0, vo="En dos mil diecinueve, Supercell lo borró."),
    dict(type="list", title="¿POR QUÉ?", icon="down", step=0.6,
         items=["ESTAFAS", "AMENAZAS", "ACOSO", "CARÍSIMO DE MODERAR"], source=S19, dur=4.5, color=2,
         sticker=K + "aldeana_pelirroja_sorprendida.png", sticker_h=400, sticker_x=840, sticker_y=1480, sticker_t=2.4,
         vo="¿Por qué? Estafas, amenazas, acoso, y era carísimo de moderar."),
    dict(type="hook", kicker="JUNIO DE 2026", lines=[("¡VOLVIÓ!", "g"), ("CASI 7 AÑOS", "w"), ("DESPUÉS", "w")],
         sizes=(180, 120, 120), source=S26, dur=3.5, color=3,
         card=K + "humor_barbaro_rey_asustados.jpg", card_y=1430, card_t=1.4,
         vo="Y en junio de este año volvió, casi siete años después."),
    dict(type="list", title="PERO DISTINTO", icon="check", step=0.6,
         items=["GRUPOS DE HASTA 800", "COMUNIDADES DE 50.000", "MENSAJES DURAN 12 H", "FILTRO FAMILIAR"],
         source=S26, dur=4.5, color=5,
         vo="Pero distinto: grupos de ochocientos, comunidades de cincuenta mil y mensajes que duran doce horas."),
    dict(type="question", q=["¿ES MEJOR QUE", "EL VIEJO?"], options=["SÍ, MUCHO", "EL VIEJO ERA MEJOR", "NI LO USO"],
         dur=4.0, color=4, vo="¿Es mejor que el viejo? Comentalo."),
    dict(type="outro", dur=2.5, color=1),
], title="El chat global volvió", bg_pool=["capturas/guerra_desde_chat.jpg", K + "arte_aniversario_fiesta.jpg",
                                           "capturas/aldea_nueva_interfaz.jpg", K + "arte_coliseo_en_las_nubes.jpg"])

if __name__ == "__main__":
    main(EP)
