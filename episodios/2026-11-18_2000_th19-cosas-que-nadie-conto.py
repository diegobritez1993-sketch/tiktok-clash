"""TikTok (tips / cosas que pocos saben, miércoles 20:00): cambios escondidos de la actualización del TH19.
Fuente: Supercell, notas oficiales "The Clash of Titans Update Is Rolling Out" (16/11/2026):
- Desafíos amistosos: quedan abiertos 24 h con tabla (estrellas, %, tiempo), hasta 3 ataques por jugador, 15 espectadores.
- Traducción en el dispositivo solo en el chat global (Google Translate); primer uso por idioma baja hasta 90 MB.
- Amigos de Supercell ID: una sola lista, sirve en todos los juegos de Supercell; agregar por QR, link o ID.
- Se eliminó la tabla "Top Players" (mejores jugadores).
- Vuelve la animación clásica al subir de nivel de experiencia.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
SRC = "Supercell, notas oficiales del TH19 (16/11/2026)"
EP = Episode([
    dict(type="hook", kicker="ACTUALIZACIÓN DEL TH19", lines=[("NADIE TE", "w"), ("CONTÓ", "w"), ("ESTO", "y")],
         sizes=(150, 150, 190), dur=3.5, color=0,
         card=K + "humor_barbaro_rey_asustados.jpg", card_y=1420,
         vo="Todos hablan del TH diecinueve, pero nadie te contó esto."),
    dict(type="list", title="DESAFÍOS AMISTOSOS", icon="check", step=0.6,
         items=["ABIERTOS 24 HORAS", "TABLA CON RANKING", "HASTA 3 ATAQUES C/U", "15 ESPECTADORES"],
         source=SRC, dur=5.0, color=1,
         sticker=K + "boton_batalla_oficial.png", sticker_h=200, sticker_x=880, sticker_y=1460, sticker_t=2.6,
         vo="Los desafíos amistosos ahora quedan abiertos un día entero, con ranking y hasta tres ataques por jugador."),
    dict(type="stat", value=90, suffix=" MB", label="TRADUCTOR EN EL CHAT GLOBAL",
         sub="se baja una vez por idioma", source=SRC, dur=4.0, color=2,
         sticker=K + "aldeana_pelirroja_sorprendida.png", sticker_h=340, sticker_x=820, sticker_y=1640, sticker_t=1.6,
         vo="El chat global ahora traduce solo. Ojo: el paquete de cada idioma pesa hasta noventa megas."),
    dict(type="alert", lines=[("UNA SOLA LISTA", "y"), ("DE AMIGOS", "w")], sub="PARA TODOS LOS JUEGOS DE SUPERCELL",
         source=SRC, dur=4.0, color=4,
         sticker=K + "boton_clan.png", sticker_h=200, sticker_x=540, sticker_y=1480, sticker_t=1.2,
         vo="Y tus amigos ahora son uno solo para todos los juegos de Supercell."),
    dict(type="list", title="TAMBIÉN CAMBIÓ", icon="star", step=0.7,
         items=["CHAU TABLA TOP JUGADORES", "VUELVE ANIMACIÓN DE NIVEL"], source=SRC, dur=4.0, color=3,
         card=K + "humor_rey_espejo_manga.jpg", card_y=1230,
         vo="Se fue la tabla de mejores jugadores y volvió la animación clásica al subir de nivel."),
    dict(type="question", q=["¿CUÁL TE GUSTÓ", "MÁS?"], options=["DESAFÍOS", "TRADUCTOR", "AMIGOS"],
         dur=3.5, color=5, vo="¿Cuál te gustó más? Comentá."),
    dict(type="outro", dur=2.5, color=0),
], title="TH19: cosas que nadie te contó", bg_pool=["capturas/aldea_nueva_interfaz.jpg", K + "arte_coliseo_en_las_nubes.jpg",
                                                     "capturas/guerra_desde_chat.jpg", K + "arte_aniversario_fiesta.jpg"])

if __name__ == "__main__":
    main(EP)
