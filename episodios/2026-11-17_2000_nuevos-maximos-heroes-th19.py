"""TikTok (novedades confirmadas, martes 20:00).
Fuente: Supercell, notas oficiales "The Clash of Titans Update Is Rolling Out" (16/11/2026):
- Sala de héroes 13 en TH19. Niveles máximos: Rey bárbaro 115, Reina arquera 115, Príncipe de los esbirros 100,
  Gran centinela 90, Campeona real 60, Duque dragón 30.
- Castillo del clan 15: +5 de capacidad de tropas (60).
- Muros: 25 más (350 en total), nivel 20.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
SRC = "Supercell, notas oficiales del TH19 (16/11/2026)"
EP = Episode([
    dict(type="hook", kicker="YA ESTÁ EL TH19", lines=[("¿HASTA DÓNDE", "w"), ("SUBEN TUS", "w"), ("HÉROES?", "y")],
         sizes=(120, 130, 170), dur=3.5, color=2,
         card=K + "humor_rey_espejo_manga.jpg", card_y=1430,
         vo="Ya está el TH diecinueve. ¿Hasta dónde suben tus héroes?"),
    dict(type="list", title="NUEVOS NIVELES MÁXIMOS", icon="up", step=0.55,
         items=["REY BÁRBARO: 115", "REINA ARQUERA: 115", "PRÍNCIPE: 100", "GRAN CENTINELA: 90",
                "CAMPEONA REAL: 60", "DUQUE DRAGÓN: 30"],
         source=SRC, dur=5.5, color=1,
         vo="Rey y Reina hasta ciento quince, el Príncipe hasta cien, el Centinela noventa, la Campeona sesenta y el Duque treinta."),
    dict(type="change", name="CASTILLO DEL CLAN", label="TROPAS DE REFUERZO", before="55", after="60",
         note="nivel 15 en el TH19", up=True, source=SRC, dur=4.0, color=3,
         sticker=K + "boton_clan.png", sticker_h=200, sticker_x=200, sticker_y=1250, sticker_t=2.0,
         vo="Y el Castillo del clan ahora entra sesenta tropas de refuerzo, cinco más."),
    dict(type="alert", lines=[("+25 MUROS", "y"), ("350 EN TOTAL", "w")], sub="HASTA NIVEL 20",
         source=SRC, dur=4.0, color=4,
         sticker=K + "estatua_rey_barbaro.png", sticker_h=360, sticker_x=540, sticker_y=1480, sticker_t=1.2,
         vo="Y sí: veinticinco muros más, trescientos cincuenta en total."),
    dict(type="question", q=["¿CUÁNTOS NIVELES", "LE FALTAN A TU REY?"], options=["0 A 10", "11 A 30", "MÁS DE 30"],
         dur=3.5, color=5, vo="¿Cuántos niveles le faltan a tu Rey? Comentá."),
    dict(type="outro", dur=2.5, color=2),
], title="TH19: nuevos máximos de héroes", bg_pool=["capturas/heroe_reina_stats.jpg", K + "arte_coliseo_en_las_nubes.jpg",
                                                    "capturas/aldea_nueva_interfaz.jpg", K + "arte_batalla_esqueletos_bruja.jpg"])

if __name__ == "__main__":
    main(EP)
