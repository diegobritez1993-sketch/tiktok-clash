"""TikTok (lo que dice la comunidad / "esto mejoraría el juego"): 3 ideas de fans publicadas en r/ClashOfClans.
Fuentes (GamingonPhone):
- "Clash of Clans fan shares an idea of having clan member notes..." (22/06/2023): u/FreeVeeThree, notas visibles bajo el
  rango de cada miembro (vacaciones, cuentas para donar), con filtro y moderables por líder/colíder.
- "A Clash of Clans fan has pitched the concept of trading resources within the clan" (13/03/2023): u/Serious_Wrangler5611,
  pedir un objeto mágico a cambio de otro que te sobra; críticas: cuentas alternativas y bots.
- "Clash of Clans redditor designs clan capital upgrade log concept" (04/07/2022): u/Winter_Permission328, registro de
  mejoras de la Capital con mejora fijada, top 5 de aportes y opción de ocultar tus aportes.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
G = "Reddit u/{} · GamingonPhone"
EP = Episode([
    dict(type="hook", kicker="LO QUE PIDE LA COMUNIDAD", lines=[("3 IDEAS DE FANS", "y"), ("QUE MEJORARÍAN", "w"), ("CLASH", "y")],
         sizes=(120, 110, 190), card="capturas/aldea_nueva_interfaz.jpg", card_y=1480, dur=3.5, color=1,
         sticker=K + "estatua_constructor_martillo.png", sticker_h=360, sticker_x=870, sticker_y=1660, sticker_t=1.2,
         vo="Tres ideas de fans que mejorarían Clash. Mirá la tercera."),
    dict(type="list", title="1. NOTAS EN EL CLAN", icon="check", step=0.6,
         items=["UN MENSAJE BAJO TU RANGO", "AVISAR SI TE VAS", "MARCAR CUENTA DONADORA"],
         source=G.format("FreeVeeThree"), dur=4.5, color=3, sticker=K + "boton_clan.png", sticker_h=220,
         sticker_x=880, sticker_y=1560, sticker_t=2.2,
         vo="Uno: notas en el clan, para avisar que te vas de vacaciones o que sos cuenta donadora."),
    dict(type="hook", kicker="IDEA 2", lines=[("INTERCAMBIAR", "y"), ("OBJETOS MÁGICOS", "w"), ("EN EL CLAN", "w")],
         sizes=(140, 110, 120), source=G.format("Serious_Wrangler5611"), dur=3.5, color=2,
         sticker=K + "libro_atril_purpura.png", sticker_h=400, sticker_y=1420, sticker_t=1.0,
         vo="Dos: cambiar con tu clan los objetos mágicos que te sobran."),
    dict(type="versus", title="¿BUENA IDEA?", left=("A FAVOR", "ÚTIL"), right=("EN CONTRA", "BOTS"),
         source="Críticas en Reddit: cuentas alt y bots", dur=4.0, color=0,
         vo="Suena bien, pero muchos temen que lo usen cuentas alternativas y bots."),
    dict(type="list", title="3. REGISTRO EN LA CAPITAL", icons=["star", "up", "check"], step=0.6,
         items=["FIJAR UNA MEJORA ARRIBA", "TOP 5 DE APORTES", "OCULTAR TUS APORTES"],
         source=G.format("Winter_Permission328"), dur=4.5, color=5,
         vo="Tres: un registro de mejoras en la Capital, con una mejora fijada y el top cinco de aportes."),
    dict(type="question", q=["¿CUÁL", "AGREGARÍAS?"], options=["NOTAS", "INTERCAMBIO", "REGISTRO"],
         dur=4.0, color=4,
         vo="¿Cuál agregarías vos? Dejalo en los comentarios."),
    dict(type="outro", dur=2.5, color=1),
], title="Ideas de la comunidad", bg_pool=["capturas/guerra_desde_chat.jpg", "capturas/aldea_nueva_interfaz.jpg",
                                           K + "arte_aniversario_paisaje.jpg", "capturas/lista_mejoras.jpg"])

if __name__ == "__main__":
    main(EP)
