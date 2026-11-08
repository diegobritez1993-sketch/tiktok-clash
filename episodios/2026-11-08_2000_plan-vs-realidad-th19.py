"""TikTok (humor): tu plan vs la realidad cuando salga el TH19. Sin datos (humor), salvo "Town Hall 19 lands mid-month"
(Supercell, blog oficial 01/11/2026) y Clash On del TH19 del 13 al 15/11 (calendario oficial)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
EP = Episode([
    dict(type="hook", kicker="CUANDO SALGA EL TH19", lines=[("TU PLAN", "y"), ("VS", "w"), ("LA REALIDAD", "r")],
         sizes=(170, 110, 150), card=K + "humor_rey_espejo_manga.jpg", card_y=1400, dur=3.5, color=4,
         sticker=K + "aldeana_pelirroja_sorprendida.png", sticker_h=360, sticker_x=870, sticker_y=1650, sticker_t=1.2,
         vo="Cuando salga el Ayuntamiento diecinueve: tu plan contra la realidad."),
    dict(type="versus", title="LAS MEJORAS", left=("TU PLAN", "PAZ"), right=("REALIDAD", "LÍO"),
         dur=4.0, color=1, sticker=K + "edificio_cabana_constructor_dorada.png", sticker_h=380, sticker_y=1500, sticker_t=1.8,
         vo="Vos decís que vas a mejorar ordenado. Empezás todo junto."),
    dict(type="versus", title="EL ORO GUARDADO", left=("TU PLAN", "TODO"), right=("REALIDAD", "NADA"),
         dur=4.0, color=0, sticker=K + "duende_con_bolsa.png", sticker_h=380, sticker_y=1500, sticker_t=1.8,
         vo="Ibas a ahorrar. En una hora te quedaste sin oro."),
    dict(type="versus", title="ESTRELLAS EN GUERRA", left=("TU PLAN", "TRES"), right=("REALIDAD", "UNA"),
         dur=4.0, color=2, bg=K + "humor_barbaro_cine_palomitas.jpg",
         vo="Ibas por tres estrellas. Sacaste una y miraste la repe llorando."),
    dict(type="alert", lines=[("Y LOS MUROS", "w"), ("OTRA VEZ", "y"), ("PARA DESPUÉS", "r")], sizes=(120, 130, 110),
         sub="COMO SIEMPRE", dur=3.5, color=5, vo="Y los muros, como siempre, para después."),
    dict(type="question", q=["¿QUÉ MEJORÁS", "PRIMERO?"], options=["HÉROES", "DEFENSAS", "TROPAS", "MUROS"],
         dur=4.0, color=3, vo="¿Qué vas a mejorar primero? Comentalo."),
    dict(type="outro", dur=2.5, color=1),
], title="Plan vs realidad TH19", bg_pool=["capturas/aldea_nueva_interfaz.jpg", "capturas/lista_mejoras.jpg",
                                            "capturas/base_guerra_th18_armada.jpg", K + "arte_aniversario_paisaje.jpg"])

if __name__ == "__main__":
    main(EP)
