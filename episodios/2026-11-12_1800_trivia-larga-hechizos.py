"""TRIVIA LARGA (YouTube 16:9) — Hechizos. Jueves 12/11/2026 18:00.
Fuentes (consultadas el 12/11/2026):
- Pocket Gamer, "Spell Factory: Clash of Clans building breakdown": Fábrica de hechizos nivel 1 = Hechizo de rayo (TH5).
- Coc.Guide, "Poison Spell": "Poison Spells do not affect structures"; dura 16 s.
- Coc.Guide, "Clone Spell": el hechizo ocupa 3 espacios de hechizo.
- Pocket Gamer, "Jump spell stats and strategies": las tropas en su radio saltan los muros.
- GameZone, "Check out Clash of Clans' new Earthquake Spell in action": el terremoto es un hechizo oscuro de la Fábrica de hechizos oscuros.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from trivia_larga import TriviaLarga, main

K = "capturas/kit_creador/"
EP = TriviaLarga(
    title="Trivia larga: Hechizos",
    intro=dict(kicker="SOLO EL 1% ACIERTA LAS 5", lines=[("¿CUÁNTO SABÉS", "w"), ("DE LOS HECHIZOS", "w"), ("DE CLASH?", "y")],
               vo="Trivia de Clash. Cinco preguntas sobre hechizos. Treinta segundos para cada una. ¿Te animás?",
               sticker=K + "bruja_con_calavera.png", bg=K + "arte_batalla_esqueletos_bruja.jpg"),
    preguntas=[
        dict(q="¿CUÁL ES EL PRIMER HECHIZO QUE DESBLOQUEÁS?", options=["CURACIÓN", "RAYO", "FURIA"], answer=1,
             vo="Pregunta uno. ¿Cuál es el primer hechizo que desbloqueás? ¿Curación, rayo o furia?",
             dato="El Hechizo de rayo llega con la Fábrica de hechizos, en el Ayuntamiento 5",
             vo_dato="¡La be! El rayo es el primero, en el Ayuntamiento cinco.",
             source="Pocket Gamer, \"Spell Factory\" (guía)", sticker=K + "runa_naranja_brillante.png",
             bg=K + "arte_aniversario_paisaje.jpg"),
        dict(q="¿QUÉ HECHIZO NO LE HACE DAÑO A LOS EDIFICIOS?", options=["RAYO", "TERREMOTO", "VENENO"], answer=2,
             vo="Pregunta dos. ¿Qué hechizo no le hace daño a los edificios? ¿Rayo, terremoto o veneno?",
             dato="El Hechizo de veneno afecta a las tropas enemigas, no a los edificios",
             vo_dato="¡La ce! El veneno no toca los edificios: es solo para las tropas.",
             source="Coc.Guide, \"Poison Spell\"", sticker=K + "bruja_con_calavera.png",
             bg=K + "arte_temporada_luna_roja.jpg"),
        dict(q="¿CUÁNTOS ESPACIOS OCUPA EL HECHIZO DE CLONACIÓN?", options=["1", "2", "3"], answer=2,
             vo="Pregunta tres. ¿Cuántos espacios ocupa el Hechizo de clonación? ¿Uno, dos o tres?",
             dato="Ocupa 3 espacios de hechizo y duplica tropas por un rato",
             vo_dato="¡La ce! Ocupa tres espacios de hechizo.",
             source="Coc.Guide, \"Clone Spell\"", sticker=K + "aldeana_pelirroja_sorprendida.png",
             bg=K + "arte_aniversario_fiesta.jpg"),
        dict(q="¿QUÉ HECHIZO HACE QUE TUS TROPAS SALTEN LOS MUROS?", options=["SALTO", "CELERIDAD", "HIELO"], answer=0,
             vo="Pregunta cuatro. ¿Qué hechizo hace que tus tropas salten los muros? ¿Salto, celeridad o hielo?",
             dato="Las tropas dentro de su radio pasan por encima de los muros",
             vo_dato="¡La a! El Hechizo de salto, el mejor amigo de los muros altos.",
             source="Pocket Gamer, \"Jump spell\" (guía)", sticker=K + "estatua_barbaro_estrella.png",
             bg=K + "arte_coliseo_en_las_nubes.jpg"),
        dict(q="¿DÓNDE SE PREPARA EL HECHIZO DE TERREMOTO?",
             options=["FÁBRICA NORMAL", "FÁBRICA OSCURA", "TALLER DE ASEDIO"], answer=1,
             vo="Pregunta cinco, la última. ¿Dónde se prepara el Hechizo de terremoto? ¿En la fábrica normal, en la oscura o en el taller de asedio?",
             dato="El terremoto es un hechizo oscuro: sale de la Fábrica de hechizos oscuros",
             vo_dato="¡La be! Es un hechizo oscuro, de la fábrica de hechizos oscuros.",
             source="GameZone, \"Clash of Clans' new Earthquake Spell\"", sticker=K + "maquina_taladro_calavera.png",
             bg=K + "arte_batalla_esqueletos_bruja.jpg"),
    ],
    thumb=dict(lines=[("¿ACERTÁS", "w"), ("LAS 5?", "y")], sticker=K + "hechizo_pocion_rosa_pulpo.png",
               bg=K + "arte_batalla_esqueletos_bruja.jpg"),
)

if __name__ == "__main__":
    main(EP)
