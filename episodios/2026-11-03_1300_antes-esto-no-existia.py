"""TikTok (historia de Clash): cosas que antes no existían en Clash of Clans.
Datos (Wikipedia, "Clash of Clans"): Desafíos amistosos (update mayo 2016), Juegos del clan (dic. 2017),
Liga de guerras de clanes (update oct. 2018), entrenar tropas gratis desde julio 2022, Equipamiento de héroes (dic. 2023),
marzo 2025 ("Clash Anytime"): se eliminaron los tiempos de entrenamiento y la espera para curar héroes.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
SRC = "Wikipedia, \"Clash of Clans\""
EP = Episode([
    dict(type="hook", kicker="HISTORIA DE CLASH", lines=[("ANTES", "w"), ("ESTO NO", "y"), ("EXISTÍA", "y")],
         sizes=(130, 160, 170), sticker=K + "estatua_constructor_martillo.png", sticker_h=460, sticker_y=1400,
         dur=3.5, color=4, vo="Los veteranos lo saben: antes esto no existía."),
    dict(type="list", title="LLEGARON DESPUÉS", icons=["star", "star", "star"], step=0.6,
         items=["2016: DESAFÍOS AMISTOSOS", "2017: JUEGOS DEL CLAN", "2018: LIGA DE GUERRAS"],
         source=SRC, dur=4.5, color=1, card="capturas/guerra_desde_chat.jpg", card_y=1520, card_t=2.2,
         vo="Los desafíos amistosos, los Juegos del clan y la Liga de guerras llegaron después."),
    dict(type="change", name="ENTRENAR TROPAS", label="DESDE JULIO DE 2022", before="COSTABA", after="GRATIS",
         up=True, source=SRC, dur=4.0, color=3, vo="Y entrenar tropas costaba recursos, hasta julio de dos mil veintidós."),
    dict(type="hook", kicker="EQUIPAMIENTO DE HÉROES", lines=[("RECIÉN", "w"), ("EN DICIEMBRE", "w"), ("DE 2023", "y")],
         sizes=(120, 120, 180), source=SRC, dur=4.0, color=2,
         sticker=K + "estatua_rey_barbaro.png", sticker_h=380, sticker_x=850, sticker_y=1540, sticker_t=2.0,
         vo="El equipamiento de héroes recién llegó en diciembre de dos mil veintitrés."),
    dict(type="alert", lines=[("MARZO 2025:", "w"), ("CHAU ESPERAS", "y")], sub="TROPAS Y HÉROES AL TOQUE",
         source=SRC, dur=4.0, color=0, vo="Y en marzo de dos mil veinticinco se acabó esperar tropas y héroes."),
    dict(type="question", q=["¿DESDE QUÉ AÑO", "JUGÁS VOS?"], options=["ANTES DE 2016", "2016 A 2020", "DESPUÉS DE 2020"],
         dur=3.5, color=5, vo="¿Y vos desde qué año jugás? Contame."),
    dict(type="outro", dur=2.5, color=4),
], title="Antes esto no existía", bg_pool=[K + "arte_aniversario_fiesta.jpg", "capturas/aldea_nueva_interfaz.jpg",
                                          "capturas/heroe_reina_stats.jpg", K + "arte_aniversario_paisaje.jpg"])

if __name__ == "__main__":
    main(EP)
