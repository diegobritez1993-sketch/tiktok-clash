"""Trivia LARGA para YouTube (horizontal 1920x1080, ~4 minutos) — canal de Clash de Diego.

Estructura: intro (8 s) -> N preguntas -> outro (10 s). Cada pregunta:
  10 s PREGUNTA (texto + 3 opciones, la voz la lee)  ->  30 s CUENTA REGRESIVA (aro + números, tic-tac)
  -> 6 s RESPUESTA (la correcta en verde + dato, la voz la dice).
Con 5 preguntas dura ~4:08.

Uso en un episodio:
    from trivia_larga import TriviaLarga, main
    EP = TriviaLarga(
        title="...",
        intro=dict(lines=[("¿ACERTÁS", "w"), ("LAS 5?", "y")], kicker="TRIVIA DE CLASH", vo="...",
                   sticker="capturas/kit_creador/x.png", bg="capturas/kit_creador/arte_x.jpg"),
        preguntas=[dict(q="¿EN QUÉ AÑO SALIÓ CLASH OF CLANS?", options=["2010", "2012", "2014"], answer=1,
                        vo="Pregunta uno. ¿En qué año salió Clash of Clans? ¿Dos mil diez, dos mil doce o dos mil catorce?",
                        dato="Salió el 2 de agosto de 2012 en iPhone", vo_dato="¡La be! Salió el dos de agosto de dos mil doce.",
                        source="Wikipedia", sticker="capturas/kit_creador/x.png", bg="capturas/..."), ...],
        outro_vo="...", thumb=dict(lines=[("¿ACERTÁS", "w"), ("LAS 5?", "y")], sticker="capturas/kit_creador/x.png"))
    main(EP)   # python episodios/X.py preview DIR | build publicados/X.mp4  (build también genera X_miniatura.jpg)
Solo imágenes de capturas/ (capturas de Diego + kit de creador). Música + efectos + voz en off siempre.
"""
import math, os, subprocess, sys, wave, zlib
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from clash_engine import (text_img, fit, pill, icon, cap_sticker, load_cap, make_music, tts, clamp, ease_out, back,
                          PALETTE, WHITE, YELLOW, GREEN, RED, GREY, FB, FM, ROOT)

W, H, FPS = 1920, 1080, 30
T_INTRO, T_Q, T_CD, T_REV, T_OUTRO = 8.0, 10.0, 30.0, 6.0, 10.0
LETTERS = "ABC"
OPT_COL = [(30, 120, 230), (240, 130, 20), (140, 60, 220)]

def paste(canvas, im, cx, cy, scale=1.0, alpha=1.0):
    if scale <= 0.01 or alpha <= 0.01: return
    if abs(scale - 1) > 1e-3:
        im = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.BILINEAR)
    if alpha < 1:
        im = im.copy(); im.putalpha(im.getchannel("A").point(lambda v: int(v * alpha)))
    x, y = int(cx - im.width / 2), int(cy - im.height / 2)
    x0, y0 = max(0, x), max(0, y); x1, y1 = min(W, x + im.width), min(H, y + im.height)
    if x1 > x0 and y1 > y0: canvas.alpha_composite(im.crop((x0 - x, y0 - y, x1 - x, y1 - y)), (x0, y0))

def wrap(text, size, maxw, **kw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if cur and text_img(t, size, **kw).width > maxw: lines.append(cur); cur = w
        else: cur = t
    if cur: lines.append(cur)
    return lines

def block(text, size, maxw, max_lines=2, gap=-8, **kw):
    """Texto en varias líneas centrado, como una sola imagen."""
    while True:
        lines = wrap(text, size, maxw, **kw)
        if len(lines) <= max_lines or size <= 34: break
        size -= 4
    ims = [text_img(l, size, **kw) for l in lines]
    w = max(i.width for i in ims); h = sum(i.height for i in ims) + gap * (len(ims) - 1)
    out = Image.new("RGBA", (w, h), (0, 0, 0, 0)); y = 0
    for i in ims: out.alpha_composite(i, ((w - i.width) // 2, y)); y += i.height + gap
    return out

_bgc = {}
def bg_big(path, ci):
    key = (path, ci)
    if key not in _bgc:
        tint = np.array(PALETTE[ci % len(PALETTE)][1], np.float32)
        if path:
            im = load_cap(path, tuple(int(v) for v in tint))
            sc = max(W / im.width, H / im.height) * 1.12
            im = im.resize((int(im.width * sc), int(im.height * sc)), Image.LANCZOS).filter(ImageFilter.GaussianBlur(7))
            arr = np.asarray(im).astype(np.float32) * 0.40 + tint * 0.32
        else:
            arr = np.zeros((int(H * 1.12), int(W * 1.12), 3), np.float32) + tint
        hh, ww = arr.shape[:2]
        yy, xx = np.mgrid[0:hh, 0:ww]
        vig = np.clip(1.2 - np.sqrt(((xx - ww / 2) / ww) ** 2 + ((yy - hh / 2) / hh) ** 2) * 1.4, 0.35, 1)[..., None]
        _bgc[key] = Image.fromarray(np.clip(arr * vig, 0, 255).astype(np.uint8))
    return _bgc[key]

def background(path, ci, t, lt):
    big = bg_big(path, ci); z = 1.0 + 0.05 * min(lt, 40) / 40
    cw, ch = int(W / z), int(H / z)
    x0 = (big.width - cw) // 2 + int(40 * math.sin(t * 0.15)); y0 = (big.height - ch) // 2 + int(15 * math.cos(t * 0.11))
    return big.crop((x0, y0, x0 + cw, y0 + ch)).resize((W, H), Image.BILINEAR).convert("RGBA")

_cards = {}
def option_card(i, text, state="normal"):
    """state: normal | right | wrong"""
    key = (i, text, state)
    if key in _cards: return _cards[key]
    cw, chh = 560, 190
    im = Image.new("RGBA", (cw + 20, chh + 20), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((10, 18, cw + 10, chh + 18), radius=28, fill=(0, 0, 0, 150))
    fill = {"normal": (20, 22, 40, 235), "right": (40, 175, 90, 255), "wrong": (35, 35, 45, 200)}[state]
    edge = {"normal": OPT_COL[i] + (255,), "right": (180, 255, 200, 255), "wrong": (80, 80, 90, 255)}[state]
    d.rounded_rectangle((10, 10, cw + 10, chh + 10), radius=28, fill=fill, outline=edge, width=7)
    d.ellipse((34, 10 + chh / 2 - 46, 126, 10 + chh / 2 + 46), fill=edge if state != "wrong" else (80, 80, 90, 255))
    L = text_img(LETTERS[i], 60, stroke=5); im.alpha_composite(L, (80 - L.width // 2, int(10 + chh / 2 - L.height / 2 + 4)))
    tb = block(text, 52, 380, max_lines=2, stroke=6, fill=WHITE if state != "wrong" else GREY)
    im.alpha_composite(tb, (150 + (400 - tb.width) // 2, int(10 + chh / 2 - tb.height / 2 + 4)))
    if state == "right":
        ck = icon("check", 110, WHITE); im.alpha_composite(ck, (cw - 70, -2))
    _cards[key] = im; return im

def ring(n_left, frac, size=210):
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0)); d = ImageDraw.Draw(im); p = 14
    d.ellipse((p, p, size - p, size - p), fill=(10, 10, 20, 210), outline=(255, 255, 255, 60), width=14)
    col = YELLOW if n_left > 10 else (RED if n_left <= 5 else (255, 150, 30))
    d.arc((p, p, size - p, size - p), -90, -90 + 360 * frac, fill=col, width=16)
    t = text_img(str(n_left), 96 if n_left > 9 else 104, fill=col, stroke=8)
    im.alpha_composite(t, ((size - t.width) // 2, (size - t.height) // 2 + 6)); return im

class TriviaLarga:
    def __init__(self, title, intro, preguntas, outro_vo=None, thumb=None, bg_pool=None):
        self.title, self.intro, self.qs = title, intro, preguntas
        self.outro_vo = outro_vo or "¿Cuántas acertaste? Dejá tu puntaje en los comentarios y suscribite para más trivias de Clash."
        self.thumb = thumb or dict(lines=intro["lines"], sticker=intro.get("sticker"))
        pool = bg_pool or [intro.get("bg")]
        for k, q in enumerate(self.qs): q.setdefault("bg", pool[k % len(pool)]); q.setdefault("color", k + 1)
        self.n = len(self.qs)
        self.T_each = T_Q + T_CD + T_REV
        self.total = T_INTRO + self.n * self.T_each + T_OUTRO

    def where(self, t):
        if t < T_INTRO: return "intro", None, t
        t2 = t - T_INTRO
        k = int(t2 // self.T_each)
        if k >= self.n: return "outro", None, t2 - self.n * self.T_each
        return "q", k, t2 - k * self.T_each

    def header(self, c, k, t):
        d = ImageDraw.Draw(c)
        d.rounded_rectangle((40, 18, W - 40, 28), radius=5, fill=(0, 0, 0, 120))
        d.rounded_rectangle((40, 18, 40 + max(10, (W - 80) * t / self.total), 28), radius=5, fill=(255, 255, 255, 230))
        paste(c, pill("TRIVIA DE CLASH OF CLANS", (214, 140, 0), 34, WHITE), W / 2, 76)
        if k is not None:
            paste(c, pill(f"PREGUNTA {k + 1} DE {self.n}", (20, 20, 40), 34, YELLOW), 230, 76)
            for j in range(self.n):
                x = W - 90 - (self.n - 1 - j) * 46
                d.ellipse((x - 14, 62, x + 14, 90), fill=(255, 214, 10, 255) if j < k else ((255, 255, 255, 255) if j == k else (255, 255, 255, 70)))

    def frame(self, t):
        part, k, lt = self.where(t)
        if part == "intro":
            it = self.intro; c = background(it.get("bg"), 0, t, lt)
            self.header(c, None, t)
            if it.get("kicker"): paste(c, pill(it["kicker"], (214, 48, 32), 50), W / 2 - 230 if it.get("sticker") else W / 2, 230, back((lt - 0.1) / 0.3))
            y = 400; x = W / 2 - 230 if it.get("sticker") else W / 2
            for j, (txt, ck) in enumerate(it["lines"]):
                im = fit(txt, 150, maxw=1100, fill={"w": WHITE, "y": YELLOW, "g": GREEN, "r": RED}[ck], stroke=12)
                paste(c, im, x, y + im.height / 2, back((lt - 0.3 - 0.18 * j) / 0.35) * (1 + 0.02 * math.sin(lt * 4 + j)))
                y += im.height - 10
            sub = it.get("sub", f"{self.n} PREGUNTAS · 30 SEGUNDOS CADA UNA")
            paste(c, fit(sub, 52, maxw=1100, stroke=6, fill=GREY), x, y + 60, ease_out((lt - 1.2) / 0.4))
            if it.get("sticker"):
                paste(c, cap_sticker(it["sticker"], 680, 700), 1480, 600 + 14 * math.sin(lt * 2.2), back((lt - 0.5) / 0.4))
        elif part == "outro":
            c = background(self.intro.get("bg"), 4, t, lt); self.header(c, None, t)
            paste(c, fit("¿CUÁNTAS ACERTASTE?", 130, maxw=1700, fill=YELLOW, stroke=12), W / 2, 330, back((lt - 0.2) / 0.35))
            paste(c, fit("DEJÁ TU PUNTAJE EN LOS COMENTARIOS", 64, maxw=1600, stroke=7), W / 2, 500, back((lt - 0.6) / 0.35))
            paste(c, pill("SUSCRIBITE PARA MÁS TRIVIAS", (214, 30, 30), 64), W / 2, 680, back((lt - 1.0) / 0.35) * (1 + 0.04 * math.sin(lt * 6)))
            paste(c, icon("star", 130), W / 2, 880, back((lt - 1.4) / 0.35))
        else:
            q = self.qs[k]; c = background(q["bg"], q["color"], t, lt); self.header(c, k, t)
            qa = block(q["q"], 84, 1640, max_lines=2, stroke=9)
            paste(c, qa, W / 2, 255, back((lt - 0.15) / 0.35))
            rev = lt >= T_Q + T_CD; rl = lt - T_Q - T_CD
            for i, o in enumerate(q["options"]):
                st = "normal" if not rev else ("right" if i == q["answer"] else "wrong")
                sc = back((lt - 0.8 - 0.35 * i) / 0.3)
                if rev and i == q["answer"]: sc *= 1 + 0.08 * math.exp(-rl * 3) * math.sin(rl * 18) + 0.04
                paste(c, option_card(i, o, st), 360 + 600 * i, 560, sc)
            if q.get("sticker"):
                paste(c, cap_sticker(q["sticker"], 300, 340), 170, 880 + 10 * math.sin(lt * 2), back((lt - 1.5) / 0.4))
            if not rev:
                if lt >= T_Q:
                    cl = lt - T_Q; left = max(1, math.ceil(T_CD - cl))
                    pulse = 1 + (0.06 * math.exp(-((cl % 1) * 8)) if left <= 5 else 0)
                    paste(c, ring(left, 1 - cl / T_CD), W / 2, 855, back(cl / 0.3) * pulse)
                    paste(c, fit("¡COMENTÁ TU RESPUESTA!", 44, maxw=900, stroke=6), W / 2, 1010, ease_out((cl - 0.3) / 0.3) * (0.92 + 0.08 * math.sin(cl * 3)))
                else:
                    paste(c, fit("PENSALO BIEN...", 50, maxw=900, stroke=6, fill=GREY), W / 2, 860, ease_out((lt - 2.5) / 0.4))
            else:
                paste(c, block(q.get("dato", ""), 56, 1300, max_lines=2, stroke=7, fill=YELLOW), W / 2, 850, back((rl - 0.4) / 0.35))
                if q.get("source"):
                    paste(c, fit("Fuente: " + q["source"], 30, maxw=1200, stroke=4, font=FM, fill=GREY), W / 2, 1040, ease_out((rl - 0.8) / 0.3))
        rgb = c.convert("RGB")
        if lt < 0.12 and part != "q" or (part == "q" and (lt < 0.12 or 0 <= lt - T_Q - T_CD < 0.12)):
            ref = lt if lt < 0.12 else lt - T_Q - T_CD
            rgb = Image.blend(rgb, Image.new("RGB", rgb.size, WHITE), 0.6 * (1 - ref / 0.12))
        return rgb

    # ---------- sonido ----------
    def audio(self, path):
        SR = 44100; n = int(SR * (self.total + 0.5)); sfx = np.zeros(n, np.float32); vox = np.zeros(n, np.float32)
        nr = np.random.default_rng(3)
        def add(arr, sig, at, g=1.0):
            i = int(at * SR)
            if i < 0 or i >= n: return
            m = min(len(sig), n - i); arr[i:i + m] += sig[:m] * g
        def env(m, a, r): tt = np.arange(m) / SR; return np.minimum(1, tt / a) * np.exp(-tt / r)
        def tone(f, dur, r=0.08, a=0.003):
            m = int(SR * dur); tt = np.arange(m) / SR; return (np.sin(2 * np.pi * f * tt) * env(m, a, r)).astype(np.float32)
        def impact(dur=0.5, f0=140, f1=38):
            m = int(SR * dur); tt = np.arange(m) / SR
            ph = 2 * np.pi * np.cumsum(f1 + (f0 - f1) * np.exp(-tt * 9)) / SR
            return np.tanh((np.sin(ph) * np.exp(-tt * 5) + nr.standard_normal(m) * np.exp(-tt * 60) * 0.6) * 2.2).astype(np.float32)
        def whoosh(dur=0.5):
            m = int(SR * dur); x = np.cumsum(nr.standard_normal(m)); x -= np.convolve(x, np.ones(40) / 40, "same")
            return (x / (np.abs(x).max() + 1e-9) * np.sin(np.pi * np.linspace(0, 1, m)) ** 2).astype(np.float32)
        def voice(txt, at, room):
            v = tts(txt, room, SR)
            if v is not None: add(vox, v, at, 1.0)
        add(sfx, impact(0.7), 0.0, 0.8); voice(self.intro.get("vo", ""), 0.6, T_INTRO - 1.0) if self.intro.get("vo") else None
        for k, q in enumerate(self.qs):
            t0 = T_INTRO + k * self.T_each
            add(sfx, whoosh(0.5), t0 - 0.35, 0.5); add(sfx, impact(0.5), t0, 0.7)
            for i in range(3): add(sfx, tone(700 + 120 * i, 0.12, 0.03), t0 + 0.8 + 0.35 * i, 0.45)
            voice(q.get("vo", q["q"]), t0 + 0.5, T_Q - 0.8)
            for s in range(int(T_CD)):                      # tic-tac
                ts = t0 + T_Q + s; last = T_CD - s <= 5
                add(sfx, tone(2400 if s % 2 == 0 else 1900, 0.03, 0.006), ts, 0.55 if last else 0.25)
                if last: add(sfx, tone(880, 0.15, 0.05), ts, 0.35)
            voice("¡Tenés treinta segundos! Comentá tu respuesta.", t0 + T_Q + 0.2, 3.0)
            tr = t0 + T_Q + T_CD
            add(sfx, impact(0.7), tr, 0.8)
            add(sfx, (tone(1568, 0.6, 0.12) + 0.4 * tone(3136, 0.6, 0.1)), tr + 0.1, 0.6)
            voice(q.get("vo_dato", q.get("dato", "")), tr + 0.6, T_REV - 0.8)
        to = T_INTRO + self.n * self.T_each
        add(sfx, whoosh(0.5), to - 0.35, 0.5); add(sfx, impact(0.6), to, 0.7); voice(self.outro_vo, to + 0.5, T_OUTRO - 1.0)
        sfx /= (np.abs(sfx).max() + 1e-9)
        mus = make_music(self.total, zlib.crc32(self.title.encode()) % 100000, SR)[:n]
        talking = np.convolve((np.abs(vox) > 0.02).astype(np.float32), np.ones(int(SR * 0.3)) / (SR * 0.3), "same")
        duck = 1 - 0.65 * np.clip(talking * 3, 0, 1)
        mix = sfx * 0.55 + mus * 0.26 * duck + vox * 0.95
        mix = np.tanh(mix * 1.05); mix = mix / (np.abs(mix).max() + 1e-9) * 0.88
        pcm = (np.repeat(mix[:, None], 2, axis=1) * 32767).astype(np.int16)
        with wave.open(path, "wb") as wf:
            wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes(pcm.tobytes())

    def thumbnail(self, out):
        th = self.thumb; c = background(th.get("bg", self.intro.get("bg")), 2, 0, 0)
        d = ImageDraw.Draw(c)
        paste(c, pill("TRIVIA DE CLASH", (214, 48, 32), 80), 560, 170)
        y = 330
        for txt, ck in th["lines"]:
            im = fit(txt, 230, maxw=1150, fill={"w": WHITE, "y": YELLOW, "g": GREEN, "r": RED}[ck], stroke=16)
            paste(c, im, 560, y + im.height / 2); y += im.height - 20
        if th.get("sticker"): paste(c, cap_sticker(th["sticker"], 900, 760), 1480, 560)
        c.convert("RGB").resize((1280, 720), Image.LANCZOS).save(out, quality=92)

    def build(self, out):
        wav = out + ".wav"; self.audio(wav)
        p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                              "-r", str(FPS), "-i", "-", "-i", wav, "-c:v", "libx264", "-preset", "veryfast", "-crf", "21",
                              "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", out],
                             stdin=subprocess.PIPE)
        for fi in range(int(self.total * FPS)):
            p.stdin.write(self.frame(fi / FPS).tobytes())
        p.stdin.close(); p.wait(); os.remove(wav)
        self.thumbnail(out[:-4] + "_miniatura.jpg")
        print("ok", out, f"{self.total:.1f}s", "+ miniatura")

    def preview(self, outdir, times):
        os.makedirs(outdir, exist_ok=True); ims = []
        for t in times:
            im = self.frame(float(t)); im.save(os.path.join(outdir, f"t{float(t):06.1f}.png")); ims.append(im.resize((480, 270)))
        cols = 3; sheet = Image.new("RGB", (480 * cols, 270 * ((len(ims) + cols - 1) // cols)))
        for i, im in enumerate(ims): sheet.paste(im, ((i % cols) * 480, (i // cols) * 270))
        sheet.save(os.path.join(outdir, "hoja.jpg")); self.thumbnail(os.path.join(outdir, "miniatura.jpg"))
        print("preview", os.path.join(outdir, "hoja.jpg"))

def main(ep):
    if len(sys.argv) >= 3 and sys.argv[1] == "build": ep.build(sys.argv[2])
    elif len(sys.argv) >= 3 and sys.argv[1] == "preview":
        times = sys.argv[3:] or [5.0, T_INTRO + 4, T_INTRO + T_Q + 12, T_INTRO + T_Q + T_CD + 3,
                                 T_INTRO + ep.T_each + T_Q + 27, ep.total - 4]
        ep.preview(sys.argv[2], times)
    else: print("uso: build SALIDA.mp4 | preview DIR [t ...]")
