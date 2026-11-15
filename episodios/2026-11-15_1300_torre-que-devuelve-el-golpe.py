"""TikTok (novedades): segundo adelanto del TH19 (Clash On, 13-15/11/2026).
Fuentes (consultadas el 15/11/2026): The Last War, "Sneak Peek 2, Torre Pirotecnica, Torre degli Spuntoni e nuova Pozione
Eroica" (14/11/2026); clashofclans.fr, "HDV19 Sneak Peek #2" (14/11/2026); GamingonPhone 13-14/11/2026.
- Torre nueva (TH19): no ataca sola, devuelve daño cuando la golpean (6% de la vida de la tropa nivel 1, 9% nivel 2),
  sigue funcionando congelada; 500.000 de elixir oscuro, 15 días.
- Defensa por fusión: Torre de arqueras nivel 21 + otra defensa (las fuentes no coinciden en cuál: no se nombra);
  10 casillas, tierra y aire, sin punto ciego, chispas que salpican detrás.
- Hechizo nuevo (Heroic Spell): desde TH17 (Fábrica de hechizos nivel 10), 2 espacios, hasta -40% de daño (nivel 4),
  más velocidad, las tropas terrestres pasan los muros.
Valores de adelanto: pueden cambiar. Nombres en español de la torre y del hechizo sin verificar: no se nombran.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
SRC = "Adelanto 2 TH19 vía The Last War (14/11/2026)"
EP = Episode([
    dict(type="hook", kicker="TH19 · ADELANTO 2", lines=[("LA TORRE QUE", "w"), ("TE DEVUELVE", "y"), ("EL GOLPE", "y")],
         sizes=(120, 140, 160), dur=3.5, color=0,
         card="capturas/base_guerra_th18_armada.jpg", card_y=1420,
         sticker=K + "aldeana_pelirroja_sorprendida.png", sticker_h=380, sticker_x=860, sticker_y=1700, sticker_t=0.9,
         vo="El Ayuntamiento diecinueve trae una torre que te devuelve el golpe."),
    dict(type="list", title="TORRE NUEVA (SOLO TH19)", icon="star", step=0.6,
         items=["NO ATACA SOLA", "SI LA GOLPEÁS, TE PEGA", "SIGUE AUNQUE LA CONGELES", "500.000 DE OSCURO"],
         source=SRC, dur=4.5, color=2,
         vo="No ataca sola: si la golpeás, te pega. Y ni congelada se apaga."),
    dict(type="change", name="DAÑO QUE DEVUELVE", label="% DE LA VIDA DE LA TROPA", before="6%", after="9%",
         note="NIVEL 1 A NIVEL 2", up=True, source=SRC, dur=3.5, color=4,
         sticker=K + "personaje_azul_tronco_pinchos.png", sticker_h=330, sticker_x=870, sticker_y=1650, sticker_t=1.6,
         vo="Devuelve el seis por ciento de la vida de la tropa, y el nueve en nivel dos."),
    dict(type="list", title="Y UNA DEFENSA FUSIÓN", icon="up", step=0.55,
         items=["TORRE DE ARQUERAS + OTRA", "PEGA A TIERRA Y AIRE", "SIN PUNTO CIEGO", "CHISPAS QUE SALPICAN"],
         source=SRC, dur=4.0, color=1, bg="capturas/base_guerra_th18_vacia.jpg",
         vo="Además, una defensa que nace de fusionar la Torre de arqueras. Sin punto ciego."),
    dict(type="list", title="HECHIZO NUEVO (DESDE TH17)", icon="check", step=0.6,
         items=["HASTA -40% DE DAÑO", "TROPAS MÁS RÁPIDAS", "PASAN LOS MUROS", "OCUPA 2 ESPACIOS"],
         source="Adelanto 2 (valores pueden cambiar)", dur=4.5, color=5,
         sticker=K + "hechizo_pocion_rosa_pulpo.png", sticker_h=280, sticker_x=880, sticker_y=1640, sticker_t=2.6,
         vo="Y un hechizo nuevo desde el Ayuntamiento diecisiete: menos daño, más velocidad y pasa muros."),
    dict(type="question", q=["¿QUÉ TE GUSTA", "MÁS?"], options=["LA TORRE", "LA FUSIÓN", "EL HECHIZO"], dur=3.5, color=3,
         vo="¿Qué te gusta más? Comentalo."),
    dict(type="outro", dur=2.5, color=0),
], title="La torre que devuelve el golpe", bg_pool=["capturas/aldea_nueva_interfaz.jpg", K + "arte_coliseo_en_las_nubes.jpg",
                                                     "capturas/base_th18_antidos_2.jpg", K + "arte_batalla_esqueletos_bruja.jpg"])

if __name__ == "__main__":
    main(EP)
