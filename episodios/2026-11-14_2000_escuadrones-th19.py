"""TikTok (novedades / debate): llegan los escuadrones con la actualización del TH19.
Fuentes: Sportsdunia 14/11/2026 "Clash of Clans New Squads Announced" (revelado en el Clash On: desde Ayuntamiento 8, nuevo
cuartel, 12 escuadrones, se despliegan con un toque, ocupan menos espacio que las mismas tropas sueltas, nivel 2 desde el TH19
con habilidades); GamingonPhone 13/11/2026 (escuadrones desde TH8, 12 variantes, mejoras y habilidades con el TH19).
"Escuadrones": nombre usado por creadores en español en el adelanto. No se nombran las habilidades (nombre en español no verificado).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
SRC = "Clash On vía Sportsdunia (14/11/2026)"
EP = Episode([
    dict(type="hook", kicker="LLEGA CON EL TH19", lines=[("¿ATACAR CON", "w"), ("UN SOLO TOQUE?", "y")],
         sizes=(140, 130), dur=4.5, color=5,
         card="capturas/tropa_supermontapuercos.jpg", card_y=1380,
         sticker=K + "jinete_mangual_de_pie.png", sticker_h=420, sticker_x=860, sticker_y=1640, sticker_t=1.0,
         vo="Con el Ayuntamiento diecinueve llegan los escuadrones. ¿Atacar con un solo toque?"),
    dict(type="list", title="ASÍ FUNCIONAN", icon="check", step=0.65,
         items=["DESDE AYUNTAMIENTO 8", "12 ESCUADRONES", "SE SUELTAN DE UN TOQUE", "OCUPAN MENOS ESPACIO"],
         source=SRC, dur=5.5, color=1,
         sticker=K + "edificio_rojo_dorado_espadas.png", sticker_h=300, sticker_x=850, sticker_y=1600, sticker_t=3.4,
         vo="Se desbloquean desde Ayuntamiento ocho, son doce, se sueltan de un toque y ocupan menos espacio."),
    dict(type="versus", title="ESPACIO QUE OCUPAN", left=("SUELTAS", "MÁS"), right=("ESCUADRÓN", "MENOS"),
         source=SRC, dur=4.0, color=4, bg=K + "arte_batalla_esqueletos_bruja.jpg",
         vo="Las mismas tropas, pero en escuadrón te ocupan menos lugar en el ejército."),
    dict(type="change", name="ESCUADRONES", label="CON EL AYUNTAMIENTO 19", before="NIVEL 1", after="NIVEL 2",
         note="y ganan habilidades especiales", up=True, source="GamingonPhone y Sportsdunia (nov. 2026)",
         dur=4.0, color=3, vo="Y con el Ayuntamiento diecinueve suben a nivel dos y ganan habilidades especiales."),
    dict(type="question", q=["¿MEJORA EL JUEGO", "O LO FACILITA?"], options=["LO MEJORA", "LO HACE FÁCIL", "NI FU NI FA"],
         dur=4.0, color=2,
         vo="¿Esto mejora el juego o lo hace demasiado fácil? Comentá."),
    dict(type="outro", dur=2.5, color=5),
], title="Escuadrones TH19", bg_pool=["capturas/aldea_nueva_interfaz.jpg", K + "arte_aniversario_paisaje.jpg",
                                      "capturas/guerra_desde_chat.jpg", "capturas/tropa_golem_meteorico.jpg"])

if __name__ == "__main__":
    main(EP)
