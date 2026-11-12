"""TikTok (humor / ¿qué pasaría si...?): si las tropas de Clash tuvieran un grupo de chat. Sin datos (humor)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
EP = Episode([
    dict(type="hook", kicker="¿QUÉ PASARÍA SI...?", lines=[("LAS TROPAS", "w"), ("TUVIERAN UN", "w"), ("GRUPO DE CHAT", "y")],
         sizes=(130, 130, 130), dur=4.0, color=4,
         card=K + "humor_barbaro_cine_palomitas.jpg", card_y=1400,
         vo="¿Qué pasaría si las tropas de Clash tuvieran un grupo de chat?"),
    dict(type="list", title="MENSAJES DEL GRUPO", icon="check", step=0.8,
         items=["ROMPEMUROS: ¿OTRA VEZ YO?", "CURANDERA: ¿Y A MÍ QUIÉN?", "MONTAPUERCOS: YO SALTO", "DUENDE: YO VOY AL ORO"],
         dur=6.0, color=1, bg="capturas/guerra_desde_chat.jpg",
         sticker=K + "duende_con_bolsa.png", sticker_h=300, sticker_x=870, sticker_y=1620, sticker_t=3.6,
         vo="El Rompemuros: ¿otra vez yo? La Curandera: ¿y a mí quién me cura? Y el duende, solo por el oro."),
    dict(type="versus", title="EL BÁRBARO EN EL GRUPO", left=("LO QUE ESCRIBE", "¡AH!"), right=("LO QUE QUISO DECIR", "¡AH!"),
         dur=4.0, color=0, vo="Y el Bárbaro... siempre escribe lo mismo."),
    dict(type="hook", kicker="SILENCIO TOTAL", lines=[("P.E.K.K.A", "r"), ("ESTÁ", "w"), ("ESCRIBIENDO...", "y")],
         sizes=(150, 120, 120), dur=4.0, color=2, card=K + "humor_barbaro_rey_asustados.jpg", card_y=1400,
         vo="Y cuando aparece P.E.K.K.A escribiendo... se callan todos."),
    dict(type="question", q=["¿QUIÉN SERÍA", "EL ADMIN?"], options=["REY BÁRBARO", "EL CONSTRUCTOR", "P.E.K.K.A"],
         dur=4.0, color=3, vo="¿Quién sería el admin del grupo? Comentalo."),
    dict(type="outro", dur=2.5, color=4),
], title="Grupo de las tropas", bg_pool=[K + "arte_aniversario_fiesta.jpg", "capturas/aldea_nueva_interfaz.jpg",
                                         K + "arte_aniversario_paisaje.jpg", "capturas/guerra_desde_chat.jpg"])

if __name__ == "__main__":
    main(EP)
