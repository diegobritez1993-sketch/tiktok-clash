# TikTok @misterd.coc — producción automática de videos de Clash of Clans

Cuenta de TikTok de Diego (Paraguay, zona America/Asuncion), creador de Clash of Clans ("Clash con Mister").
Español rioplatense/paraguayo con voseo ("mirá", "tenés", "dejalo"). Videos verticales 1080x1920, sin cara ni voz:
motion graphics con texto + efectos de sonido, generados con `motor/clash_engine.py`.

**SOLO TikTok.** Nunca programar estos videos en YouTube ni en otra red (YouTube es otro canal y otro nicho).

## Tarea diaria (cada ejecución programada)
Dejar programados en Metricool **2 videos por día: 13:00 y 20:00 (America/Asuncion)**, solo en TikTok.
1. `git pull`. Leer este archivo y `historial.md` completo (no repetir tema, dato ni gancho).
2. Revisar con `getScheduledPosts` (brandId 7762882, timezone America/Asuncion, hoy y mañana) qué horarios de **TikTok**
   ya están ocupados (ignorar los posts de YouTube). Producir un video por cada horario libre de HOY (13:00 / 20:00)
   que todavía no haya pasado; si los dos de hoy ya están ocupados o pasaron, producir para los libres de mañana.
   Máximo 2 videos por ejecución. Nunca duplicar un horario.
3. **Elegir temas** alternando estos pilares (los 2 del día de pilares distintos):
   - **Eventos y novedades del mes**: eventos que empiezan/terminan, temporada, Liga de Clanes (CWL), juegos del clan,
     sneak peeks, cambios de balance, mantenimiento. Siempre con fechas verificadas. Prioridad si hay algo con fecha cercana.
   - **Tips**: estrategia de ataque/defensa, gestión de recursos, mejoras, errores comunes, equipamiento de héroes.
   - **Historia de Clash**: lanzamiento del juego, cómo llegaron los ayuntamientos/héroes, actualizaciones históricas.
   - **¿Sabías que...? / curiosidades**: datos raros o poco conocidos del juego o de Supercell.
4. **Verificar todo con WebSearch/WebFetch**: preferir supercell.com (blog de Clash of Clans), Clash of Clans Wiki (fandom),
   clash.ninja y medios serios. Nunca inventar cifras, fechas ni nombres. Si un dato no se puede confirmar, no usarlo.
   Nombres de tropas/hechizos/equipamiento en **español tal como aparecen en el juego** (ej. "Flecha congelada",
   "Supermontapuercos", "Gólem meteórico"). Si no estás seguro del nombre en español, reformular sin nombrarlo.
   Fechas/horas de eventos: dar la hora de Paraguay (UTC-3) y aclarar UTC si aporta.
5. **Escribir el episodio** en `episodios/AAAA-MM-DD_HHMM_slug.py` copiando la estructura de un episodio existente.
   - Duración 20-26 s. Escenas de 3-5 s. Empezar SIEMPRE con un `hook` fuerte (pregunta o dato que sorprenda).
   - Tipos de escena del motor: `hook`, `stat`, `change`, `list`, `versus`, `alert`, `question`, `outro`
     (ver docstring de `motor/clash_engine.py`). Variar tipos y colores entre videos; no repetir la misma estructura.
   - Terminar con `question` (para comentarios) en al menos 1 de los 2 videos del día, y siempre con `outro`.
   - `source="..."` en la escena donde aparece el dato (texto chico abajo).
   - Titulares en MAYÚSCULAS y cortos; ítems de lista de máximo ~28 caracteres.
   - **Prohibido**: personajes, logos, capturas o arte de Clash of Clans/Supercell. Solo texto, formas e íconos del motor.
6. **Revisar antes de renderizar**: `python episodios/X.py preview /tmp/prev` (un cuadro por escena) y MIRAR `hoja.jpg`
   con Read. Corregir textos encimados, cortados o fuera de pantalla. Recién ahí:
   `python episodios/X.py build publicados/<mismo-nombre>.mp4`.
7. `git add` (episodio + mp4 + historial) → commit → `git push` a `main`. El video queda público en
   `https://raw.githubusercontent.com/diegobritez1993-sketch/tiktok-clash/main/publicados/<archivo>.mp4`.
   Verificar con `curl -sI` que responde `HTTP/2 200` antes de programar.
8. **Programar** con `createScheduledPost` (blogId `7762882`), fecha con offset -03:00:
   - providers `[{"network":"tiktok"}]` — SOLO tiktok. media `[<url raw>]`, autoPublish true, draft false.
   - `tiktokData`: `{"privacyOption":"PUBLIC_TO_EVERYONE","title":<título>,"isAigc":true,"disableComment":false,"disableDuet":false,"disableStitch":false,"autoAddMusic":false,"commercialContentThirdParty":false,"commercialContentOwnBrand":false}`
   - **Título (SIEMPRE, obligatorio)**: adecuado al contenido del video, que diga de qué trata y enganche;
     máx ~60 caracteres, 1-2 emojis, voseo. Nunca genérico ni repetido.
   - `text`: 1-2 frases + pregunta para comentar + (si hay dato) "Fuente: ..." + hashtags.
   - **Hashtags: EXACTAMENTE 3**, al final del texto. El primero SIEMPRE `#clashofclans`; los otros 2 relacionados
     con el tema del video (ej. `#clashofclans #cwl #clashtips`, `#clashofclans #cambiosdebalance #supercell`).
9. Agregar una fila por video a `historial.md` y hacer push.
10. Mandar al usuario (SendUserMessage) un resumen corto: títulos, horarios y link del planner de Metricool.

## Reglas
- Nunca repetir un tema del historial. Nunca publicar datos no verificados.
- No borrar videos ni publicaciones existentes, ni tocar los posts de YouTube.
- Si algo falla (push denegado, Metricool rechaza el video), no reintentar en bucle: dejar el video en el repo y avisar al usuario.
