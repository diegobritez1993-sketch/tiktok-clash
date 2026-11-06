"""TikTok (trivia, viernes 13:00): 3 preguntas sobre la historia de los Ayuntamientos, antes del TH19.
Datos (Prima Games, "Clash of Clans TH18 Expected Release Date and Details"): TH10 23/05/2013, TH11 10/12/2015,
TH12 11/06/2018, TH13 09/12/2019, TH14 12/04/2021, TH15 10/10/2022, TH16 12/12/2023, TH17 26/11/2024;
TH18 noviembre 2025 (Clash Ninja). Diciembre = 3 ayuntamientos (TH11, TH13, TH16); noviembre = 2 (TH17, TH18).
Entre TH10 y TH11 pasaron más de 2 años (2 años y medio).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from clash_engine import Episode, main

K = "capturas/kit_creador/"
SRC = "Prima Games, fechas de salida de cada Ayuntamiento"
EP = Episode([
    dict(type="hook", kicker="ANTES DEL TH19", lines=[("SOLO EL 1%", "y"), ("ACIERTA", "w"), ("LAS 3", "r")],
         sizes=(160, 140, 160), card="capturas/aldea_nueva_interfaz.jpg", card_y=1400, dur=3.5, color=4,
         sticker=K + "banner_jugador_ayuntamiento.png", sticker_h=240, sticker_x=900, sticker_y=1740, sticker_t=1.2,
         vo="Antes del Ayuntamiento diecinueve: solo el uno por ciento acierta las tres."),
    dict(type="trivia", q=["¿EN QUÉ AÑO SALIÓ", "EL AYUNTAMIENTO 10?"],
         options=["A) 2013", "B) 2015", "C) 2016"], answer=0,
         source="Prima Games (TH10: 23/05/2013)", dur=6.5, color=1,
         vo="¿En qué año salió el Ayuntamiento diez?"),
    dict(type="trivia", q=["¿CUÁNTO SE ESPERÓ", "ENTRE EL TH10 Y EL TH11?"],
         options=["A) 6 MESES", "B) 1 AÑO", "C) MÁS DE 2 AÑOS"], answer=2,
         source="Prima Games (TH11: 10/12/2015)", dur=6.5, color=2,
         sticker=K + "estatua_constructor_martillo.png", sticker_h=300, sticker_x=880, sticker_y=1700, sticker_t=1.0,
         vo="¿Cuánto hubo que esperar entre el diez y el once?"),
    dict(type="trivia", q=["¿EN QUÉ MES SALIERON", "MÁS AYUNTAMIENTOS?"],
         options=["A) OCTUBRE", "B) NOVIEMBRE", "C) DICIEMBRE"], answer=2,
         source="Prima Games y Clash Ninja (TH11, TH13 y TH16 en dic.)", dur=6.5, color=3,
         vo="¿En qué mes salieron más ayuntamientos?"),
    dict(type="outro", dur=3.0, color=0, vo="¿Cuántas acertaste? ¡Seguime para más de Clash!"),
], title="Trivia: ayuntamientos", bg_pool=["capturas/aldea_nueva_interfaz.jpg", K + "arte_coliseo_en_las_nubes.jpg",
                                           "capturas/lista_mejoras.jpg", K + "arte_aniversario_paisaje.jpg"])

if __name__ == "__main__":
    main(EP)
