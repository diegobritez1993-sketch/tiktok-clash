"""TikTok (humor): cosas que todo jugador de Clash hizo alguna vez. Sin datos (humor)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
EP = Episode([
    dict(type="hook", kicker="CONFESIÓN", lines=[("NO MIENTAS:", "w"), ("VOS TAMBIÉN", "y"), ("HICISTE ESTO", "r")],
         sizes=(120, 130, 140), card=K + "humor_rey_espejo_manga.jpg", card_y=1380, dur=3.5, color=2,
         vo="No mientas, vos también hiciste esto en Clash."),
    dict(type="list", title="CONFESIONES DE CLASH", icon="check", step=0.7,
         items=["GASTAR GEMAS SIN QUERER", "ALARMA PARA EL CONSTRUCTOR", "ENTRAR SOLO A RECOLECTAR"],
         dur=5.0, color=0, sticker=K + "estatua_constructor_martillo.png", sticker_h=330, sticker_x=850,
         sticker_y=1570, sticker_t=2.6,
         vo="Gastar gemas sin querer, poner alarma para el constructor, y entrar solo a recolectar."),
    dict(type="versus", title="BUSCAR RIVAL", left=("LO QUE DECÍS", "UNA MÁS"), right=("LO QUE HACÉS", "50 MÁS"),
         dur=4.0, color=4, vo="Y buscar rival: decís una más... y tocás siguiente cincuenta veces."),
    dict(type="hook", kicker="EL CLÁSICO", lines=[("IRTE A DORMIR", "w"), ("CON EL ORO", "y"), ("A TOPE", "r")],
         sizes=(120, 130, 160), card=K + "humor_barbaro_duerme_con_trofeo.jpg", card_y=1400, dur=4.0, color=1,
         vo="Y el clásico: irte a dormir con el oro a tope. A la mañana, ni rastro."),
    dict(type="question", q=["¿CUÁNTAS", "HICISTE?"], options=["TODAS", "ALGUNA", "NINGUNA (MENTIRA)"],
         dur=4.0, color=3, vo="¿Cuántas hiciste vos? Confesalo en los comentarios."),
    dict(type="outro", dur=2.5, color=2),
], title="Vos también", bg_pool=["capturas/aldea_nueva_interfaz.jpg", K + "arte_aniversario_paisaje.jpg",
                                 "capturas/lista_mejoras_filtro.jpg", K + "arte_aniversario_fiesta.jpg"])

if __name__ == "__main__":
    main(EP)
