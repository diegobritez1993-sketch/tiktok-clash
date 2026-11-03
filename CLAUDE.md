# TikTok @misterd.coc — producción automática de videos de Clash of Clans

Cuenta de TikTok de Diego (Paraguay, zona America/Asuncion), creador de Clash of Clans ("Clash con Mister").
Español rioplatense/paraguayo con voseo ("mirá", "tenés", "dejalo"). Videos verticales 1080x1920, sin cara ni voz:
motion graphics con texto + efectos de sonido, generados con `motor/clash_engine.py`.

**Dos destinos, dos marcas de Metricool (desde el 03/11/2026):**
- Marca **7762882** ("misterd.coc") → **SOLO TikTok**. Su YouTube es OTRO canal y otro nicho: NUNCA programar Clash ahí.
- Marca **7849138** ("Clash con mister") → YouTube de Clash (canal UC1ThKx6_pha-AnoBvPv0PUA): los MISMOS videos como Shorts,
  a la misma hora que el TikTok.

## Tarea diaria (cada ejecución programada)
Dejar programados en Metricool **2 videos por día: 13:00 y 20:00 (America/Asuncion)**: TikTok (marca 7762882) +
el mismo video como Short en YouTube de Clash (marca 7849138).
1. `git pull`. Leer este archivo, `historial.md` completo (no repetir tema, dato ni gancho) y el calendario oficial
   del mes en `calendario/AAAA-MM.md` si existe (fechas de eventos confirmadas por Supercell: base para temas de eventos).
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
   - **Audio: SIEMPRE música de fondo + efectos de sonido.** El motor genera solo una música gaming original y alegre
     (activa automáticamente desde el 01/11/2026) y los efectos de cada escena. No pasar `music=False` nunca.
   - **VOZ EN OFF (SIEMPRE, desde el 03/11/2026)**: poner `vo="..."` en cada escena (menos el outro, que dice solo
     "¡Seguime para más novedades de Clash!"). Voz masculina gratuita Piper (`motor/voz/`, se instala sola con pip).
     Frases cortas en voseo que acompañen el texto en pantalla (no leer todo literal), ~2,5 palabras por segundo de escena.
     Escribir los números con letras ("trece de noviembre", "Ayuntamiento diecinueve") y evitar siglas que la voz lea mal
     (decir "Liga de guerras" en vez de "CWL", "TH diecinueve" o "Ayuntamiento diecinueve" en vez de "TH19"). En trivia, la
     voz lee la pregunta y deja la cuenta regresiva sin hablar. Si la voz falla (piper no instala), el video sale igual sin voz:
     avisarle a Diego en el resumen.
   - Titulares en MAYÚSCULAS y cortos; ítems de lista de máximo ~28 caracteres.
   - **Imágenes de Clash (SIEMPRE)**: cada video debe verse claramente de Clash of Clans. Usar las capturas propias
     de Diego de `capturas/` (ver `capturas/INDICE.md`): pasar `bg_pool=[3-4 capturas relacionadas al tema]` al
     `Episode` y poner al menos una `card="capturas/..."` (idealmente en el hook). El motor agrega solo la etiqueta
     "CLASH OF CLANS" en la primera escena. Dinámico: variar fondos, tarjetas y tipos de escena.
   - **Kit de creador (`capturas/kit_creador/`, ver su `INDICE.md`)**: cuando haya una imagen relacionada al tema, USARLA.
     PNG transparentes → `sticker="capturas/kit_creador/x.png"` (sin marco, con sombra, entra con rebote y flota;
     `sticker_x`, `sticker_y`, `sticker_h`, `sticker_t`, `sticker_flip`). Ideal: un sticker en el hook y 1-2 más en otras
     escenas, ubicados donde no tapen texto (y≈1200-1400 o a un costado con sticker_x≈800 y sticker_h≈420).
     JPG con fondo (artes de aniversario, humor manga, etc.) → `bg_pool` o `card=`. Mezclar kit + capturas de Diego.
     Los artes de humor (bárbaro en el cine, rey en el espejo, bárbaro y rey asustados) son ideales para el pilar Humor.
     Lo de WWE solo para temas de esa colab. No nombrar en pantalla personajes cuyo nombre en español no esté verificado.
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
   - **Metricool: desde el 03/11/2026 Diego tiene plan Starter (hasta 5 marcas)**. Programar normal. Solo si `createScheduledPost`
     falla por límite/cupo/plan (o cualquier rechazo), NO reintentar. Pasar a **modo manual**: el video ya está en el repo;
     mandarlo con `SendUserFile` (el .mp4, para que Diego lo descargue en el celular) y con `SendUserMessage` un mensaje
     listo para copiar: hora a la que tiene que subirlo (13:00 o 20:00), TÍTULO, TEXTO completo con los 3 hashtags,
     el link raw del mp4 y el recordatorio de marcar "contenido generado con IA" en TikTok. En historial.md poner
     "MANUAL" en la columna Hora junto a la hora. Si el cupo ya se agotó ese mes (un rechazo anterior en historial),
     ir directo a modo manual sin intentar Metricool. El cupo se renueva al empezar cada mes.
   - **Short de YouTube (mismo video, misma hora)**: `createScheduledPost` con blogId `7849138`, providers
     `[{"network":"youtube"}]`, media = la MISMA URL que se usó para TikTok, autoPublish true, draft false, text = el mismo
     texto del TikTok (con sus 3 hashtags), `youtubeData`: `{"title":<mismo título>,"type":"short","privacy":"public",
     "tags":[3-5 tags del tema + "clash of clans"],"category":"GAMING","madeForKids":false,"isAiGeneratedContent":false}`.
     Antes, revisar con getScheduledPosts (brandId 7849138) que ese horario no esté ya ocupado. Si YouTube falla, no
     reintentar: mandarle a Diego el video + título + 3 hashtags para que lo suba a mano.
9. Agregar una fila por video a `historial.md` y hacer push.
10. Mandar al usuario (SendUserMessage) un resumen corto: títulos, horarios, que quedaron en TikTok y en YouTube, y link del planner.
11. (Ya NO se manda el paquete manual para YouTube: desde el 03/11/2026 los Shorts se programan solos en la marca 7849138.
    Solo si falla Metricool, mandar video + título + 3 hashtags como respaldo.)

## Reglas
- Nunca repetir un tema del historial. Nunca publicar datos no verificados.
- No borrar videos ni publicaciones existentes, ni tocar los posts de YouTube del otro nicho (marca 7762882).
- Si algo falla (push denegado, Metricool rechaza el video), no reintentar en bucle: dejar el video en el repo y avisar al usuario.
