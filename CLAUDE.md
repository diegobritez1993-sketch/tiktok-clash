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
3. **Investigar qué está pasando en Clash** (antes de elegir temas), con WebSearch/WebFetch:
   - X/Twitter: cuenta oficial de Clash of Clans y creadores/insiders conocidos (buscar "Clash of Clans" + "sneak peek",
     "leak", "Town Hall 19", "update", "maintenance" de los últimos días).
   - Reddit r/ClashOfClans, foros/comunidad oficial de Supercell, blog oficial supercell.com, Clash Ninja, la wiki.
   - Buscar: novedades, sneak peeks, eventos que arrancan o terminan, cambios de balance, filtraciones/rumores,
     curiosidades y debates que estén generando comentarios.
4. **Elegir 2 temas** de pilares distintos, priorizando lo que tenga más potencial de engagement. Pilares de esta cuenta:
   - **Tips** rápidos (recursos, mejoras, eventos, errores comunes, equipamiento, cosas que pocos saben).
   - **¿Sabías que...? / curiosidades** del juego y de Supercell.
   - **Historia de Clash** (lanzamiento, cómo llegaron ayuntamientos/héroes/tropas, actualizaciones míticas).
   - **Humor / "¿Qué pasaría si...?"** (situaciones graciosas que todo jugador vivió, escenarios imaginarios).
   - **Filtraciones y rumores**: SOLO con fuente identificable. En pantalla y en el texto marcarlos siempre como
     "RUMOR" o "FILTRACIÓN" / "NO CONFIRMADO" y nombrar de dónde salió. Nunca presentarlos como hecho.
   - **Lo que dice la comunidad / "Esto mejoraría el juego"** (debates, pedidos de la comunidad, opiniones polémicas
     con pregunta para comentar).
   - **Novedades / eventos del mes** (fechas verificadas; prioridad si hay algo con fecha cercana).
   - **Trivia**: **3 por semana, los lunes, miércoles y viernes en el video de las 13:00**. 1-3 escenas `trivia`
     (pregunta con 3 opciones, una correcta y verificada), con hook tipo "SOLO EL 1% ACIERTA ESTA".
   **NO hacer** tutoriales de ataque ni videos de diseños/links de bases: eso lo graba Diego aparte, a mano.
   Ganchos tipo clickbait están bien ("¿SE VIENE EL TH19?", "NADIE TE DIJO ESTO", "¡OJO CON ESTO!") siempre que
   el video cumpla lo que promete el gancho: nada falso ni engañoso.
   **Verificación**: preferir supercell.com, la wiki, clash.ninja y medios serios. Nunca inventar cifras, fechas ni nombres.
   Si un dato no se puede confirmar, no usarlo como hecho (a lo sumo como rumor con fuente).
   Nombres de tropas/hechizos/equipamiento en **español tal como aparecen en el juego** (ej. "Flecha congelada",
   "Supermontapuercos", "Gólem meteórico"). Si no estás seguro del nombre en español, reformular sin nombrarlo.
   Fechas/horas de eventos: dar la hora de Paraguay (UTC-3) y aclarar UTC si aporta.
5. **Escribir el episodio** en `episodios/AAAA-MM-DD_HHMM_slug.py` copiando la estructura de un episodio existente.
   - Duración 20-26 s. Escenas de 3-5 s. Empezar SIEMPRE con un `hook` fuerte (pregunta o dato que sorprenda).
   - Tipos de escena del motor: `hook`, `stat`, `change`, `list`, `versus`, `alert`, `question`, `trivia`, `outro`
     (ver docstring de `motor/clash_engine.py`). Variar tipos y colores entre videos; no repetir la misma estructura.
   - Terminar con `question` (para comentarios) en al menos 1 de los 2 videos del día, y siempre con `outro`.
   - `source="..."` en la escena donde aparece el dato (texto chico abajo).
   - Titulares en MAYÚSCULAS y cortos; ítems de lista de máximo ~28 caracteres.
   - **Imágenes de Clash (SIEMPRE)**: cada video debe verse claramente de Clash of Clans. Usar las capturas propias
     de Diego de `capturas/` (ver `capturas/INDICE.md`): pasar `bg_pool=[3-4 capturas relacionadas al tema]` al
     `Episode` y poner al menos una `card="capturas/..."` (idealmente en el hook). El motor agrega solo la etiqueta
     "CLASH OF CLANS" en la primera escena. Dinámico: variar fondos, tarjetas y tipos de escena.
   - **Prohibido**: descargar arte oficial, logos, personajes o capturas de otros desde internet, o dibujar personajes
     del juego. Las únicas imágenes del juego son las de `capturas/` (capturas propias de Diego y, cuando las mande,
     el kit oficial de creador de Supercell en `capturas/kit_creador/`). Preferir imágenes del kit cuando tengan
     relación directa con el tema. Si hacen falta imágenes nuevas para un tema, avisarle a Diego en el resumen.
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
