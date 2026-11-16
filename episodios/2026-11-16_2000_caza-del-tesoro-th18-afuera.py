"""TikTok (novedades / eventos de la semana, lunes 20:00).
Fuente: Supercell, blog oficial en español "Se escucha el fragor de la lucha de titanes" (01/11/2026):
- 16-23/11: "Regresa la caza del tesoro para los ayuntamientos de nivel 1 a 17" (el TH18 queda afuera).
- 15-30/11: vuelven los cosméticos de noviembre 2025: rey matón, reina furiosa, príncipe blindado, centinela chamán,
  luchadora nómada (+ paisaje).
- 10-16/11: semana del superyeti (termina hoy).
- 22-28/11: Juegos del clan; tropas de refuerzo los primeros cuatro días.
- 24/11-1/12: desafío de la forja feroz.
- "El ayuntamiento de nivel 19 llegará a mitad de mes" (sin fecha exacta; al 16/11 sigue sin anunciarse, clashscout.gg).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
SRC = "Supercell, blog oficial (01/11/2026)"
EP = Episode([
    dict(type="hook", kicker="ARRANCA HOY", lines=[("¿SOS TH18?", "y"), ("ESTE EVENTO", "w"), ("NO ES PARA VOS", "r")],
         sizes=(140, 130, 120), dur=3.5, color=0,
         card="capturas/menu_eventos_2.jpg", card_y=1400,
         sticker=K + "aldeana_pelirroja_sorprendida.png", sticker_h=380, sticker_x=860, sticker_y=1640, sticker_t=1.0,
         vo="¿Sos Ayuntamiento dieciocho? El evento de hoy no es para vos."),
    dict(type="alert", lines=[("CAZA DEL TESORO", "y"), ("16 AL 23/11", "w")], sizes=(110, 120),
         sub="SOLO HASTA AYUNTAMIENTO 17", source=SRC, dur=4.0, color=4,
         sticker=K + "cofre_madera_hierro.png", sticker_h=300, sticker_x=540, sticker_y=1450, sticker_t=1.2,
         vo="Vuelve la caza del tesoro, del dieciséis al veintitrés, pero solo hasta Ayuntamiento diecisiete."),
    dict(type="list", title="VUELVEN ESTAS SKINS", icon="star", step=0.55,
         items=["REY MATÓN", "REINA FURIOSA", "PRÍNCIPE BLINDADO", "CENTINELA CHAMÁN", "LUCHADORA NÓMADA"],
         source=SRC + ": hasta el 30/11", dur=5.0, color=2,
         vo="Además vuelven las skins del año pasado, hasta el treinta de noviembre."),
    dict(type="list", title="LO QUE SE VIENE", icon="check", step=0.6,
         items=["HOY: TERMINA EL SUPERYETI", "22 AL 28: JUEGOS DEL CLAN", "24/11: FORJA FEROZ", "TH19: SIN FECHA AÚN"],
         source=SRC, dur=5.0, color=1,
         sticker=K + "boton_eventos_calendario.png", sticker_h=220, sticker_x=830, sticker_y=1700, sticker_t=2.8,
         vo="Hoy termina el Superyeti, el veintidós arrancan los Juegos del clan y el TH diecinueve todavía no tiene fecha."),
    dict(type="question", q=["¿CUÁNDO CREÉS", "QUE SALE EL TH19?"], options=["ESTA SEMANA", "LA QUE VIENE", "EN DICIEMBRE"],
         dur=3.5, color=3, source="Supercell: \"a mitad de mes\"",
         vo="¿Cuándo creés que sale el TH diecinueve? Comentá."),
    dict(type="outro", dur=2.5, color=5),
], title="Caza del tesoro: TH18 afuera", bg_pool=["capturas/menu_eventos_1.jpg", K + "arte_coliseo_en_las_nubes.jpg",
                                                  "capturas/aldea_nueva_interfaz.jpg", K + "arte_aniversario_fiesta.jpg"])

if __name__ == "__main__":
    main(EP)
