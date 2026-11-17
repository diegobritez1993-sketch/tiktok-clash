"""TikTok (tips / novedades confirmadas, martes 13:00).
Fuente: Supercell, notas oficiales "The Clash of Titans Update Is Rolling Out" (16/11/2026):
- El TH19 salió el 16/11 (mantenimiento ese día, Sportsdunia 16/11/2026).
- Bajan costo y tiempo de mejoras del contenido de TH16 a TH18: ~63 niveles de edificios y trampas y ~230 niveles de
  tropas, hechizos, héroes, mascotas y guardianes.
- Se eliminan las supercargas de defensa aérea, tesla oculta, ballesta, minas, recolectores, etc.; las supercargas
  sin terminar se devuelven (refund).
- Mena: la "Glowy" pasa de 5 a 3 gemas y la "Starry" de 35 a 20 gemas (no nombramos el tipo en español).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
SRC = "Supercell, notas oficiales del TH19 (16/11/2026)"
EP = Episode([
    dict(type="hook", kicker="YA SALIÓ EL TH19", lines=[("¿SOS TH16,", "w"), ("17 O 18?", "w"), ("ESTO TE CONVIENE", "y")],
         sizes=(130, 130, 110), dur=3.5, color=4,
         card="capturas/lista_mejoras.jpg", card_y=1420,
         sticker=K + "estatua_constructor_martillo.png", sticker_h=400, sticker_x=850, sticker_y=1650, sticker_t=1.0,
         vo="¿Sos TH dieciséis, diecisiete o dieciocho? Esto te conviene."),
    dict(type="stat", title="MÁS BARATOS Y RÁPIDOS", value=230, prefix="+", label="NIVELES DE TROPAS,",
         sub="HECHIZOS, HÉROES Y MASCOTAS", source=SRC, dur=4.5, color=1,
         sticker=K + "duende_con_bolsa.png", sticker_h=260, sticker_x=870, sticker_y=1730, sticker_t=2.0,
         vo="Con el TH diecinueve bajaron costo y tiempo de más de doscientos treinta niveles de tropas, hechizos y héroes."),
    dict(type="list", title="Y TAMBIÉN", icon="down", step=0.6,
         items=["63 NIVELES DE EDIFICIOS", "Y TRAMPAS MÁS BARATOS", "TH16, TH17 Y TH18"],
         source=SRC, dur=4.0, color=3,
         vo="Y también sesenta y tres niveles de edificios y trampas."),
    dict(type="alert", lines=[("¡CHAU", "w"), ("SUPERCARGAS!", "r")], sub="SI TENÍAS UNA A MEDIAS, TE DEVUELVEN",
         source="Supercell, notas del TH19: defensas y recolectores", dur=4.5, color=0,
         sticker=K + "aldeana_pelirroja_sorprendida.png", sticker_h=360, sticker_x=820, sticker_y=1500, sticker_t=1.4,
         vo="Ojo: sacaron las supercargas de varias defensas y recolectores. Si tenías una a medias, te devuelven lo gastado."),
    dict(type="change", name="MENA MÁS BARATA", label="LA MÁS CARA, EN GEMAS", before="35", after="20",
         note="y otra baja de 5 a 3 gemas", up=False, source=SRC, dur=4.0, color=2,
         sticker=K + "icono_diamante.png", sticker_h=200, sticker_x=200, sticker_y=1250, sticker_t=1.6,
         vo="Y la mena en gemas también baja: la más cara pasa de treinta y cinco a veinte."),
    dict(type="question", q=["¿QUÉ VAS A", "MEJORAR AHORA?"], options=["HÉROES", "TROPAS", "DEFENSAS"],
         dur=3.5, color=5, vo="¿Qué vas a mejorar ahora? Contame en los comentarios."),
    dict(type="outro", dur=2.5, color=1),
], title="TH19: rebajas para TH16-18", bg_pool=["capturas/lista_mejoras_filtro.jpg", "capturas/aldea_nueva_interfaz.jpg",
                                                K + "arte_aniversario_paisaje.jpg", "capturas/base_guerra_th18_armada.jpg"])

if __name__ == "__main__":
    main(EP)
