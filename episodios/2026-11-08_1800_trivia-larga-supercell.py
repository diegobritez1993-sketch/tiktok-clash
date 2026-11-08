"""TRIVIA LARGA (YouTube 16:9) — Supercell. Domingo 8/11/2026 18:00.
Fuente de todos los datos: Wikipedia, "Supercell (company)" (consultada el 08/11/2026):
fundada 14/5/2010 en Helsinki, Finlandia; Hay Day iOS 21/6/2012 (Clash iOS 2/8/2012); CEO y cofundador Ilkka Paananen;
Clash Royale iOS y Android 2/3/2016; junio 2016: consorcio Halti (Tencent 50%) compró 81,4% de Supercell.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from trivia_larga import TriviaLarga, main

K = "capturas/kit_creador/"
SRC = "Wikipedia, \"Supercell (company)\""
EP = TriviaLarga(
    title="Trivia larga: Supercell",
    intro=dict(kicker="SOLO EL 1% ACIERTA LAS 5", lines=[("¿CUÁNTO SABÉS", "w"), ("DE LOS CREADORES", "w"), ("DE CLASH?", "y")],
               vo="Trivia de Clash. Cinco preguntas sobre Supercell, los creadores del juego. Treinta segundos para cada una. ¿Te animás?",
               sticker=K + "estatua_constructor_martillo.png", bg=K + "arte_coliseo_en_las_nubes.jpg"),
    preguntas=[
        dict(q="¿DE QUÉ PAÍS ES SUPERCELL?", options=["SUECIA", "FINLANDIA", "NORUEGA"], answer=1,
             vo="Pregunta uno. ¿De qué país es Supercell? ¿Suecia, Finlandia o Noruega?",
             dato="Se fundó el 14 de mayo de 2010 en Helsinki, Finlandia",
             vo_dato="¡La be! Es de Finlandia, nació en Helsinki en dos mil diez.",
             source=SRC, sticker=K + "estatua_maestro_constructor.png", bg=K + "arte_aniversario_paisaje.jpg"),
        dict(q="¿QUÉ JUEGO DE SUPERCELL SALIÓ ANTES QUE CLASH OF CLANS?",
             options=["HAY DAY", "BOOM BEACH", "CLASH ROYALE"], answer=0,
             vo="Pregunta dos. ¿Qué juego de Supercell salió antes que Clash of Clans? ¿Hay Day, Boom Beach o Clash Royale?",
             dato="Hay Day salió en iPhone en junio de 2012; Clash, en agosto",
             vo_dato="¡La a! Hay Day salió unas semanas antes, en dos mil doce.",
             source=SRC, sticker=K + "duende_con_bolsa.png", bg=K + "arte_aniversario_fiesta.jpg"),
        dict(q="¿CÓMO SE LLAMA EL CEO Y COFUNDADOR DE SUPERCELL?",
             options=["HIDEO KOJIMA", "GABE NEWELL", "ILKKA PAANANEN"], answer=2,
             vo="Pregunta tres. ¿Cómo se llama el director y cofundador de Supercell? ¿Hideo Kojima, Gabe Newell o Ilkka Paananen?",
             dato="Ilkka Paananen fundó la empresa junto a otros cinco socios",
             vo_dato="¡La ce! Es Ilkka Paananen, uno de los seis fundadores.",
             source=SRC, sticker=K + "aldeana_pelirroja_sorprendida.png", bg=K + "arte_batalla_esqueletos_bruja.jpg"),
        dict(q="¿EN QUÉ AÑO SALIÓ CLASH ROYALE?", options=["2014", "2016", "2018"], answer=1,
             vo="Pregunta cuatro. ¿En qué año salió Clash Royale? ¿Dos mil catorce, dos mil dieciséis o dos mil dieciocho?",
             dato="Salió el 2 de marzo de 2016 en iPhone y Android",
             vo_dato="¡La be! Salió en marzo de dos mil dieciséis.",
             source=SRC, sticker=K + "carta_dorada_q.png", bg=K + "arte_aniversario_paisaje.jpg"),
        dict(q="¿QUÉ GIGANTE ESTUVO DETRÁS DE LA COMPRA DE SUPERCELL EN 2016?",
             options=["NINTENDO", "MICROSOFT", "TENCENT"], answer=2,
             vo="Pregunta cinco, la última. ¿Qué gigante estuvo detrás de la compra de Supercell en dos mil dieciséis?",
             dato="Un consorcio con Tencent compró el 81,4% de Supercell",
             vo_dato="¡La ce! Un grupo con Tencent compró la mayoría de la empresa.",
             source=SRC, sticker=K + "cofre_madera_hierro.png", bg=K + "arte_coliseo_en_las_nubes.jpg"),
    ],
    thumb=dict(lines=[("¿ACERTÁS", "w"), ("LAS 5?", "y")], sticker=K + "estatua_constructor_martillo.png", bg=K + "arte_coliseo_en_las_nubes.jpg"),
)

if __name__ == "__main__":
    main(EP)
