"""TikTok (novedades + rumor): qué pasa con los guardianes en el Ayuntamiento 19.
Datos: entrevista de Judo Sloth 2 a un diseñador de Supercell (05/08/2026) según clashbuilder.com y cocbasedrop.com
(ago. 2026): los guardianes dejan el Ayuntamiento, se conserva el progreso, no hace falta mejorarlos para pasar al TH19;
dónde van a quedar NO está definido. Nombres en español: blog oficial Supercell TH18 ("guardianes").
Rumor: fusión de tropas en TH19, listado como "Unconfirmed" en clashofpatates.com/en/leaks (publicado por BG).
TH19 Clash On 13-15/11: calendario oficial de noviembre 2026.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
SRC = "Diseñador de Supercell en Judo Sloth (ago. 2026)"
EP = Episode([
    dict(type="hook", kicker="AYUNTAMIENTO 19", lines=[("¿ADIÓS", "w"), ("GUARDIANES?", "r")],
         sizes=(170, 150), card=K + "humor_barbaro_rey_asustados.jpg", card_y=1380, dur=3.5, color=0,
         vo="En el Ayuntamiento diecinueve los guardianes se van. ¿Qué pasa con los tuyos?"),
    dict(type="list", title="LO QUE DIJO SUPERCELL", icon="check", step=0.6,
         items=["SALEN DEL AYUNTAMIENTO", "NO PERDÉS EL PROGRESO", "NO HACE FALTA MAXEARLOS"],
         source=SRC, dur=5.0, color=3, sticker=K + "banner_jugador_ayuntamiento.png", sticker_h=230,
         sticker_x=880, sticker_y=1590, sticker_t=2.4,
         vo="Lo dijo Supercell: salen del Ayuntamiento, no perdés el progreso y no hace falta mejorarlos."),
    dict(type="hook", kicker="SIN DEFINIR", lines=[("¿DÓNDE VAN", "y"), ("A QUEDAR?", "y"), ("NADIE LO SABE", "w")],
         sizes=(130, 130, 100), source="Supercell no definió el lugar", dur=3.5, color=1,
         sticker=K + "aldeana_pelirroja_sorprendida.png", sticker_h=380, sticker_y=1400, sticker_t=1.0,
         vo="Dónde van a quedar todavía no lo dijeron."),
    dict(type="alert", lines=[("RUMOR", "r"), ("¿FUSIÓN DE TROPAS?", "y")], sub="NO CONFIRMADO",
         source="Filtración de BG en Clash of Patates, sin confirmar", dur=4.0, color=2,
         vo="Y ojo, rumor sin confirmar: se habla de fusionar tropas en el diecinueve."),
    dict(type="stat", value=13, label="DE NOVIEMBRE", sub="ARRANCA EL CLASH ON DEL TH19 (HASTA EL 15)",
         source="Calendario oficial de Supercell", dur=3.5, color=4,
         sticker=K + "boton_eventos_calendario.png", sticker_h=190, sticker_x=880, sticker_y=1740, sticker_t=1.4,
         vo="El trece de noviembre arranca el Clash On y vamos a saber más."),
    dict(type="question", q=["¿TE GUSTA", "ESTE CAMBIO?"], options=["SÍ", "NO", "ME DA IGUAL"],
         dur=4.0, color=5, vo="¿Te gusta este cambio? Comentalo."),
    dict(type="outro", dur=2.5, color=1),
], title="Guardianes TH19", bg_pool=["capturas/base_guerra_th18_armada.jpg", K + "arte_coliseo_en_las_nubes.jpg",
                                     "capturas/aldea_nueva_interfaz.jpg", "capturas/base_th18_antidos_1.jpg"])

if __name__ == "__main__":
    main(EP)
