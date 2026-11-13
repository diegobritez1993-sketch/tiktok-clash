"""TikTok (trivia, viernes 13:00): 3 preguntas sobre el clan.
Datos: AppTrigger 02/05/2022 "Clan Capital now live" (Capital del clan llegó el 2 de mayo de 2022).
Mobile Matters, "Complete Guide to Clan War Leagues": cada clan va en un grupo con otros 7 (8 clanes por grupo).
Sportskeeda, "Clan roles in Clash of Clans": un clan es una comunidad de hasta 50 jugadores.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
EP = Episode([
    dict(type="hook", kicker="TRIVIA DEL CLAN", lines=[("¿SABÉS TODO", "w"), ("DE TU CLAN?", "y"), ("SOLO EL 1% SÍ", "r")],
         sizes=(130, 140, 120), card="capturas/guerra_desde_chat.jpg", card_y=1400, dur=3.5, color=5,
         sticker=K + "boton_clan.png", sticker_h=240, sticker_x=880, sticker_y=1700, sticker_t=1.2,
         vo="Trivia del clan. Solo el uno por ciento acierta las tres."),
    dict(type="trivia", q=["¿CUÁNTOS JUGADORES", "COMO MÁXIMO PUEDE", "TENER UN CLAN?"],
         options=["A) 30 JUGADORES", "B) 50 JUGADORES", "C) 100 JUGADORES"], answer=1,
         source="Sportskeeda, roles del clan (hasta 50 jugadores)", dur=6.5, color=1,
         vo="¿Cuántos jugadores como máximo puede tener un clan?"),
    dict(type="trivia", q=["¿EN QUÉ AÑO LLEGÓ", "LA CAPITAL", "DEL CLAN?"],
         options=["A) 2019", "B) 2022", "C) 2024"], answer=1,
         source="AppTrigger, 02/05/2022: llega la Capital del clan", dur=6.5, color=3,
         sticker=K + "edificio_base_cristal_azul.png", sticker_h=240, sticker_x=880, sticker_y=1770, sticker_t=1.0,
         vo="¿En qué año llegó la Capital del clan?"),
    dict(type="trivia", q=["EN LA LIGA DE GUERRAS,", "¿CUÁNTOS CLANES", "HAY POR GRUPO?"],
         options=["A) 6 CLANES", "B) 8 CLANES", "C) 10 CLANES"], answer=1,
         source="Mobile Matters, guía de la Liga de guerras", dur=6.5, color=4,
         sticker=K + "medalla_dorada_rombo.png", sticker_h=220, sticker_x=880, sticker_y=1770, sticker_t=1.0,
         vo="En la Liga de guerras, ¿cuántos clanes hay en cada grupo?"),
    dict(type="outro", dur=3.0, color=2, vo="¿Cuántas acertaste? ¡Seguime para más de Clash!"),
], title="Trivia: clan", bg_pool=["capturas/guerra_desde_chat.jpg", K + "arte_coliseo_en_las_nubes.jpg",
                                  "capturas/menu_eventos_1.jpg", "capturas/aldea_nueva_interfaz.jpg"])

if __name__ == "__main__":
    main(EP)
