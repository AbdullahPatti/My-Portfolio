# One-shot generator for the inline SVG visuals. Output: viz/<name>.svg fragments.
import random, math, os, sys

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

G1, G2, G3, G4 = "#1E2024", "#2B2E34", "#3A3E46", "#5B6069"
MUTE, CLOUD, WHITE = "#8D929B", "#F4F5F7", "#FFFFFF"
SUN, SUNSOFT, RED = "#FFC629", "#FFE8A0", "#FF5A4F"


def ur(x, y, w, h, text, size=16, color=G1, align="right", extra=""):
    return (f'<foreignObject x="{x}" y="{y}" width="{w}" height="{h}">'
            f'<div xmlns="http://www.w3.org/1999/xhtml" class="viz-ur" dir="rtl" lang="ur" '
            f'style="font-size:{size}px;color:{color};text-align:{align};{extra}">{text}</div></foreignObject>')


def wave(x, y, w, h, n, color, seed, gap=2, env=True, colors=None):
    r = random.Random(seed)
    bw = (w - gap * (n - 1)) / n
    out = []
    for i in range(n):
        e = math.sin(math.pi * (i + .5) / n) if env else 1
        a = max(.12, (0.35 + 0.65 * r.random()) * (0.4 + 0.6 * e))
        bh = h * a
        c = colors[i] if colors else color
        out.append(f'<rect x="{x + i * (bw + gap):.1f}" y="{y - bh / 2:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="{min(bw / 2, 2):.1f}" fill="{c}"/>')
    return "".join(out)


def svg(name, label, body, w=640, h=400):
    s = f'<svg class="viz" viewBox="0 0 {w} {h}" role="img" aria-label="{label}" xmlns="http://www.w3.org/2000/svg">{body}</svg>'
    open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8").write(s)


def glow(id_, cx, cy, color=SUN, op=.22):
    return (f'<defs><radialGradient id="{id_}" cx="{cx}" cy="{cy}" r="75%"><stop offset="0" stop-color="{color}" stop-opacity="{op}"/>'
            f'<stop offset="1" stop-color="{color}" stop-opacity="0"/></radialGradient></defs>')


SHADOW = lambda id_: f'<defs><filter id="{id_}" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#1E2024" flood-opacity=".16"/></filter></defs>'

# ---------------- Sachai Check ----------------
svg("sachai", "An Urdu image post scanned by OCR and judged False with 87 percent confidence, and a voice note flagged as a deepfake", f'''
{glow("sc-g", "85%", "0%")}
<rect width="640" height="400" fill="{G1}"/><rect width="640" height="400" fill="url(#sc-g)"/>
<g transform="translate(32 32)">
  <rect width="272" height="216" rx="22" fill="{G2}" stroke="{G3}"/>
  <circle cx="28" cy="28" r="11" fill="{G4}"/>
  <rect x="48" y="20" width="86" height="7" rx="3.5" fill="{G4}"/><rect x="48" y="32" width="54" height="6" rx="3" fill="{G3}"/>
  <text x="252" y="32" text-anchor="end" class="m" font-size="10" fill="{MUTE}">SHARED 12K</text>
  <rect x="16" y="54" width="240" height="116" rx="14" fill="#15171A"/>
  {ur(28, 64, 216, 100, "بجلی کی قیمتوں میں پچاس فیصد کمی کا اعلان", 19, WHITE, "center")}
  <rect class="scan" x="16" y="58" width="240" height="2" fill="{SUN}"/>
  <path d="M10 66V48h18M244 48h18v18M262 158v18h-18M28 176H10v-18" stroke="{SUN}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="16" y="198" class="m" font-size="10.5" fill="{SUN}" letter-spacing="1">VLM OCR · CLAIM EXTRACTED</text>
</g>
<g transform="translate(308 128)"><circle r="13" fill="{SUN}"/><path d="M-4-5l6 5-6 5" stroke="{G1}" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>
<g transform="translate(336 32)">
  <rect width="272" height="216" rx="22" fill="{WHITE}"/>
  <text x="20" y="32" class="m" font-size="10" fill="{MUTE}" letter-spacing="1">TEXT VERDICT</text>
  <rect x="164" y="18" width="90" height="22" rx="11" fill="{SUNSOFT}"/><text x="209" y="33" text-anchor="middle" class="m" font-size="10" fill="{G1}">Gemini judge</text>
  <text x="20" y="84" class="s" font-size="46" fill="{G1}">False</text>
  <rect x="150" y="52" width="102" height="36" rx="18" fill="#FFE3E1"/>
  {ur(150, 50, 102, 40, "جھوٹی خبر", 15, "#C4261D", "center")}
  <text x="20" y="116" font-size="11.5" fill="{G4}">Confidence</text><text x="252" y="116" text-anchor="end" font-size="11.5" font-weight="700" fill="{G1}">87%</text>
  <rect x="20" y="124" width="232" height="8" rx="4" fill="#ECEEF1"/><rect x="20" y="124" width="202" height="8" rx="4" fill="{SUN}"/>
  <text x="20" y="158" class="m" font-size="9.5" fill="{MUTE}" letter-spacing="1">EVIDENCE · DATED RSS</text>
  <circle cx="25" cy="176" r="3.5" fill="{G1}"/><text x="36" y="180" font-size="11.5" fill="{G1}">Regulator notice, 10 Nov: tariff unchanged</text>
  <circle cx="25" cy="198" r="3.5" fill="{G1}"/><text x="36" y="202" font-size="11.5" fill="{G1}">National daily, 12 Nov: claim denied</text>
</g>
<g transform="translate(32 268)">
  <rect width="576" height="100" rx="22" fill="{G2}" stroke="{G3}"/>
  <circle cx="50" cy="50" r="24" fill="{SUN}"/>
  <path d="M50 38a5 5 0 0 1 5 5v8a5 5 0 0 1-10 0v-8a5 5 0 0 1 5-5zM41 50a9 9 0 0 0 18 0M50 59v5" stroke="{G1}" stroke-width="2.4" fill="none" stroke-linecap="round"/>
  <text x="88" y="44" font-size="14" font-weight="600" fill="{WHITE}">Voice note · 0:14</text>
  <text x="88" y="64" font-size="11.5" fill="{MUTE}">Urdu · unseen speaker</text>
  {wave(236, 50, 200, 54, 46, "#7C818A", 7)}
  <rect x="456" y="22" width="100" height="28" rx="14" fill="{RED}" fill-opacity=".16"/>
  <circle cx="474" cy="36" r="4" fill="{RED}"/><text x="484" y="40" font-size="12" font-weight="600" fill="{RED}">Deepfake</text>
  <text x="506" y="74" text-anchor="middle" class="m" font-size="10.5" fill="{MUTE}">XLS-R · 8.6% EER</text>
</g>''')

# ---------------- Nabz Scribe (Android) ----------------
def bubble(x, y, w, h, fill, content):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}"/>' + content

phone_wave = wave(70, 112, 116, 30, 26, SUN, 3)
svg("nabz", "An Android phone running Nabz Scribe offline, transcribing an Urdu, Punjabi and English consultation and printing a prescription", f'''
{glow("nb-g", "75%", "10%", SUN, .35)}{SHADOW("nb-sh")}
<rect width="640" height="400" fill="{CLOUD}"/><rect width="640" height="400" fill="url(#nb-g)"/>
<g transform="translate(64 14)" filter="url(#nb-sh)">
  <rect x="214" y="86" width="4" height="44" rx="2" fill="{G3}"/><rect x="214" y="142" width="4" height="26" rx="2" fill="{G3}"/>
  <rect width="216" height="372" rx="36" fill="{G1}"/>
  <rect x="8" y="8" width="200" height="356" rx="29" fill="{WHITE}"/>
  <circle cx="108" cy="23" r="5.5" fill="{G1}"/>
  <text x="26" y="27" font-size="10.5" font-weight="600" fill="{G1}">10:24</text>
  <path d="M158 22.5l6-2.2 .1-4a1 1 0 0 1 2 0l-.1 4 6 2.2v1.6l-6-1.4-.1 3 1.8 1.3v1.2l-2.8-.8-2.8.8v-1.2l1.8-1.3.1-3-6 1.4z" fill="{G1}"/>
  <rect x="178" y="18" width="16" height="9" rx="2.5" fill="none" stroke="{G1}" stroke-width="1.3"/><rect x="180" y="20" width="10" height="5" rx="1" fill="{G1}"/>
  <text x="22" y="62" class="s" font-size="17" fill="{G1}">Nabz Scribe</text>
  <rect x="142" y="48" width="54" height="20" rx="10" fill="{SUNSOFT}"/><text x="169" y="62" text-anchor="middle" font-size="9.5" font-weight="600" fill="{G1}">Offline</text>
  <rect x="18" y="78" width="180" height="66" rx="18" fill="{G1}"/>
  <circle cx="34" cy="96" r="4" fill="{RED}"/><text x="44" y="100" class="m" font-size="10" fill="{WHITE}">REC 00:37</text>
  <text x="186" y="100" text-anchor="end" class="m" font-size="9" fill="{MUTE}">UR · EN · PA</text>
  {wave(30, 124, 156, 26, 30, SUN, 3)}
  {bubble(18, 154, 128, 34, CLOUD, ur(24, 155, 116, 32, "بخار کب سے ہے؟", 13, G1))}
  {bubble(30, 194, 168, 34, SUNSOFT, ur(34, 195, 158, 32, "تین دن سے، رات کو زیادہ ہوتا ہے", 11, G1))}
  {bubble(18, 234, 180, 30, CLOUD, f'<text x="28" y="253" font-size="10" fill="{G1}" textLength="160" lengthAdjust="spacingAndGlyphs">No antibiotics. Paracetamol 500.</text>')}
  {bubble(18, 270, 140, 34, CLOUD, ur(24, 271, 96, 32, "بوہتا پانی پیو", 13, G1) + f'<text x="140" y="291" text-anchor="middle" class="m" font-size="8.5" fill="{MUTE}">PA</text>')}
  <rect x="18" y="316" width="180" height="32" rx="16" fill="{SUN}"/><text x="108" y="336" text-anchor="middle" font-size="11.5" font-weight="700" fill="{G1}">Write prescription</text>
  <rect x="80" y="354" width="56" height="4" rx="2" fill="{G1}" opacity=".45"/>
</g>
<path d="M292 200c26 0 30-30 58-30" stroke="{G4}" stroke-width="2" stroke-dasharray="4 5" fill="none"/>
<g transform="translate(352 44) rotate(2.5)" filter="url(#nb-sh)">
  <rect width="250" height="300" rx="10" fill="{WHITE}"/>
  <text x="22" y="52" class="s" font-size="38" font-style="italic" fill="{G1}">Rx</text>
  <text x="228" y="34" text-anchor="end" class="m" font-size="9.5" fill="{MUTE}">OPD · LAHORE</text>
  <text x="228" y="50" text-anchor="end" class="m" font-size="9.5" fill="{MUTE}">AGE 34 · M</text>
  <line x1="22" y1="68" x2="228" y2="68" stroke="#E6E8EC"/>
  <text x="22" y="96" font-size="13" font-weight="600" fill="{G1}">Tab. Paracetamol 500 mg</text>
  <text x="22" y="114" class="m" font-size="10.5" fill="{G4}">1 + 0 + 1 · 3 days</text>
  <text x="22" y="146" font-size="13" font-weight="600" fill="{G1}">Oral fluids</text>
  <text x="22" y="164" class="m" font-size="10.5" fill="{G4}">2 L daily</text>
  <rect x="22" y="182" width="206" height="30" rx="10" fill="#E9F8EE"/>
  <path d="M34 197l4 4 8-8" stroke="#1F9D55" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="54" y="201" font-size="11.5" font-weight="600" fill="#167A42">No antibiotics · negation kept</text>
  <line x1="22" y1="232" x2="228" y2="232" stroke="#E6E8EC" stroke-dasharray="3 4"/>
  <text x="22" y="256" class="m" font-size="10" fill="{G4}">37.6 s audio → 11.6 s</text>
  <text x="22" y="274" class="m" font-size="10" fill="{G4}">on-device · phone CPU</text>
</g>''')

# ---------------- TaxChronos ----------------
years = [2019, 2020, 2021, 2022, 2023, 2024]
cards = []
for i, yr in enumerate(years):
    y = 34 + i * 46
    hot = yr == 2022
    dx = 26 if hot else 0
    fill = SUN if hot else WHITE
    cards.append(f'<g transform="translate({32 + dx} {y})"><rect width="196" height="38" rx="12" fill="{fill}" stroke="{"none" if hot else "#E3E5E9"}"/>'
                 f'<text x="14" y="16" class="m" font-size="9" fill="{G1 if hot else MUTE}">ITO 2001 · v{yr}</text>'
                 f'<text x="14" y="30" font-size="11.5" font-weight="600" fill="{G1}">As of 30 June {yr}</text></g>')
svg("tax", "Versions of Pakistani tax law from 2019 to 2024 with 2022 pulled out, an Urdu question, and a LangGraph retrieve, grade, rewrite loop", f'''
{SHADOW("tx-sh")}
<rect width="640" height="400" fill="{CLOUD}"/>
{"".join(cards)}
<text x="32" y="330" class="m" font-size="10" fill="{G4}" letter-spacing="1">12 STATUTES · 840 PAST VERSIONS</text>
<path d="M254 191c24 0 22-40 54-60" stroke="{G4}" stroke-width="1.6" stroke-dasharray="4 4" fill="none"/>
<g filter="url(#tx-sh)"><rect x="300" y="30" width="308" height="62" rx="22" fill="{G1}"/>
{ur(314, 34, 280, 54, "۲۰۲۲ میں تنخواہ پر ٹیکس کی شرح کیا تھی؟", 16, WHITE)}</g>
<defs><marker id="tx-ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0l10 5-10 5z" fill="{G4}"/></marker></defs>
<g font-size="12" font-weight="600">
<rect x="318" y="128" width="104" height="36" rx="18" fill="{WHITE}" stroke="#DADDE2"/><text x="370" y="151" text-anchor="middle" fill="{G1}">Retrieve</text>
<rect x="494" y="128" width="96" height="36" rx="18" fill="{G1}"/><text x="542" y="151" text-anchor="middle" fill="{WHITE}">Grade</text>
<rect x="406" y="206" width="104" height="36" rx="18" fill="{WHITE}" stroke="#DADDE2"/><text x="458" y="229" text-anchor="middle" fill="{G1}">Rewrite</text>
</g>
<path d="M426 146h62" stroke="{G4}" stroke-width="1.6" marker-end="url(#tx-ar)"/>
<path d="M542 168c0 30-12 54-26 54" stroke="{G4}" stroke-width="1.6" fill="none" marker-end="url(#tx-ar)"/>
<path d="M402 224c-34 0-40-30-38-54" stroke="{G4}" stroke-width="1.6" fill="none" marker-end="url(#tx-ar)"/>
<text x="560" y="194" class="m" font-size="9.5" fill="{MUTE}">weak?</text>
<path d="M590 146c26 0 20 120-8 146" stroke="{SUN}" stroke-width="2.4" fill="none" marker-end="url(#tx-ar)"/>
<text x="604" y="226" class="m" font-size="9.5" fill="{G4}" transform="rotate(90 604 226)">relevant</text>
<g filter="url(#tx-sh)"><rect x="300" y="274" width="270" height="92" rx="20" fill="{WHITE}"/></g>
<text x="318" y="298" class="m" font-size="9.5" fill="{MUTE}" letter-spacing="1">CITED ANSWER · TAX YEAR 2022</text>
<text x="318" y="322" font-size="13" font-weight="600" fill="{G1}">Sec. 149, ITO 2001 — salary slabs</text>
<text x="318" y="340" font-size="11.5" fill="{G4}">as the law stood on 30 June 2022</text>
<text x="318" y="356" class="m" font-size="9.5" fill="{MUTE}">pgvector + full-text · RRF</text>''')

# ---------------- WhisperBench ----------------
segs = ["ur"] * 12 + ["en"] * 8 + ["ur"] * 6 + ["en"] * 10 + ["ur"] * 12
cols = [("#D9DBDF" if s == "ur" else SUN) for s in segs]
n = len(segs)
bw = (576 - 2 * (n - 1)) / n
switch_x = [32 + i * (bw + 2) - 1 for i in range(1, n) if segs[i] != segs[i - 1]]
switch = "".join(f'<line x1="{x:.1f}" y1="44" x2="{x:.1f}" y2="148" stroke="{RED}" stroke-width="1.4" stroke-dasharray="3 3"/><circle cx="{x:.1f}" cy="44" r="4" fill="{RED}"/>' for x in switch_x)
svg("whisper", "A code-mixed Urdu-English waveform with errors clustered at the language switch points, and a reference versus Whisper transcript", f'''
{glow("wb-g", "10%", "100%")}
<rect width="640" height="400" fill="{G1}"/><rect width="640" height="400" fill="url(#wb-g)"/>
<text x="32" y="30" class="m" font-size="10" fill="{MUTE}" letter-spacing="1">CODE-MIXED CLIP · 4 SWITCH POINTS</text>
<rect x="470" y="17" width="40" height="18" rx="9" fill="#D9DBDF"/><text x="490" y="30" text-anchor="middle" class="m" font-size="9.5" fill="{G1}">UR</text>
<rect x="516" y="17" width="40" height="18" rx="9" fill="{SUN}"/><text x="536" y="30" text-anchor="middle" class="m" font-size="9.5" fill="{G1}">EN</text>
<rect x="562" y="17" width="46" height="18" rx="9" fill="{RED}" fill-opacity=".2"/><text x="585" y="30" text-anchor="middle" class="m" font-size="9.5" fill="{RED}">ERR</text>
{wave(32, 98, 576, 92, n, None, 11, colors=cols)}
{switch}
<g transform="translate(32 170)">
  <rect width="576" height="110" rx="20" fill="{G2}" stroke="{G3}"/>
  <text x="20" y="34" class="m" font-size="9.5" fill="{MUTE}" letter-spacing="1">REFERENCE</text>
  {ur(110, 10, 446, 40, 'میں نے <b class="en">meeting</b> کو <b class="en">reschedule</b> کر دیا', 16, WHITE)}
  <line x1="20" y1="56" x2="556" y2="56" stroke="{G3}"/>
  <text x="20" y="88" class="m" font-size="9.5" fill="{MUTE}" letter-spacing="1">WHISPER</text>
  {ur(110, 64, 446, 40, 'میں نے <s class="err">میٹنگ</s> کو <s class="err">ری شیڈول</s> کر دیا', 16, WHITE)}
</g>
<g transform="translate(32 300)">
  <text x="0" y="40" class="s" font-size="44" fill="{WHITE}">0.899</text><text x="0" y="66" font-size="11.5" fill="{MUTE}">best WER</text>
  <text x="168" y="40" class="s" font-size="44" fill="{SUN}">&gt;0.93</text><text x="168" y="66" font-size="11.5" fill="{MUTE}">switch-point error</text>
  <g class="m" font-size="10" fill="{G1}">
  <rect x="380" y="18" width="60" height="26" rx="13" fill="#D9DBDF"/><text x="410" y="35" text-anchor="middle">Tiny</text>
  <rect x="448" y="18" width="60" height="26" rx="13" fill="#D9DBDF"/><text x="478" y="35" text-anchor="middle">Base</text>
  <rect x="516" y="18" width="60" height="26" rx="13" fill="{SUN}"/><text x="546" y="35" text-anchor="middle">Small</text></g>
  <text x="576" y="66" text-anchor="end" class="m" font-size="10" fill="{MUTE}">327 clips · 11 speakers</text>
</g>''')

# ---------------- Daily Digest ----------------
cx, cy, R = 150, 270, 112
ticks = []
for i, hr in enumerate([6, 7, 8, 9, 10]):
    a = math.pi - i * math.pi / 4
    x, y = cx + R * math.cos(a), cy - R * math.sin(a)
    on = hr == 7
    ticks.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{19 if on else 15}" fill="{SUN if on else WHITE}" stroke="{"none" if on else "#DADDE2"}"/>'
                 f'<text x="{x:.1f}" y="{y + 4:.1f}" text-anchor="middle" font-size="{12 if on else 11}" font-weight="{700 if on else 500}" fill="{G1}">{hr}</text>')
rays = "".join(f'<line x1="{cx + 30 * math.cos(math.radians(a)):.1f}" y1="{cy - 30 * math.sin(math.radians(a)):.1f}" x2="{cx + 42 * math.cos(math.radians(a)):.1f}" y2="{cy - 42 * math.sin(math.radians(a)):.1f}" stroke="{SUN}" stroke-width="3" stroke-linecap="round"/>' for a in range(15, 180, 30))
stories = [("Economy", "Policy-rate decision, explained", .92), ("Tech", "Lahore startups and the AI hiring wave", .81), ("Weather", "Heat advisory issued for Punjab", .67)]
rows = ""
for i, (tag, t, s) in enumerate(stories):
    y = 104 + i * 80
    rows += (f'<g transform="translate(324 {y})"><text x="0" y="0" class="m" font-size="9.5" fill="{MUTE}" letter-spacing="1">{i + 1:02d} · {tag.upper()}</text>'
             f'<text x="0" y="20" font-size="13" font-weight="600" fill="{G1}">{t}</text>'
             f'<rect x="0" y="32" width="200" height="6" rx="3" fill="#ECEEF1"/><rect x="0" y="32" width="{200 * s:.0f}" height="6" rx="3" fill="{SUN if i == 0 else G1}"/>'
             f'<text x="262" y="39" text-anchor="end" class="m" font-size="10" fill="{G4}">PK {s:.2f}</text></g>')
svg("digest", "A sunrise dial of delivery hours with 7 AM chosen, above a morning email of three stories ranked by Pakistan relevance", f'''
{SHADOW("dd-sh")}{glow("dd-g", "20%", "90%", SUN, .4)}
<rect width="640" height="400" fill="{CLOUD}"/><rect width="640" height="400" fill="url(#dd-g)"/>
<text x="38" y="50" class="m" font-size="10" fill="{G4}" letter-spacing="1">DELIVERY HOUR · PKT</text>
<text x="38" y="84" class="s" font-size="30" fill="{G1}">Good morning.</text>
<path d="M{cx - R} {cy}A{R} {R} 0 0 1 {cx + R} {cy}" stroke="#DADDE2" stroke-width="2" fill="none" stroke-dasharray="2 6" stroke-linecap="round"/>
{rays}<path d="M{cx - 24} {cy}a24 24 0 0 1 48 0z" fill="{SUN}"/>
<line x1="20" y1="{cy}" x2="290" y2="{cy}" stroke="{G1}" stroke-width="2" stroke-linecap="round"/>
{"".join(ticks)}
<text x="{cx}" y="{cy + 34}" text-anchor="middle" class="m" font-size="10" fill="{G4}">15+ readers · each at their hour</text>
<g filter="url(#dd-sh)"><rect x="300" y="30" width="310" height="340" rx="24" fill="{WHITE}"/></g>
<circle cx="330" cy="62" r="12" fill="{G1}"/><path d="M324 58l6 5 6-5" stroke="{SUN}" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<text x="350" y="59" font-size="12.5" font-weight="700" fill="{G1}">Your 7:00 AM brief</text>
<text x="350" y="74" font-size="10.5" fill="{MUTE}">Daily Digest · summarized by Gemini</text>
<line x1="324" y1="88" x2="586" y2="88" stroke="#ECEEF1"/>
{rows}''')

# ---------------- CRMind ----------------
stages = ["New", "Qualified", "Proposal", "Won", "Lost"]
counts = [3, 2, 2, 1, 1]
col_w, gap, x0 = 108, 9, 30
k = ""
for i, (st, c) in enumerate(zip(stages, counts)):
    x = x0 + i * (col_w + gap)
    k += f'<rect x="{x}" y="128" width="{col_w}" height="244" rx="16" fill="#ECEEF1"/>'
    k += f'<text x="{x + 12}" y="150" font-size="11" font-weight="700" fill="{G1}">{st}</text><text x="{x + col_w - 12}" y="150" text-anchor="end" class="m" font-size="10" fill="{MUTE}">{c}</text>'
    for j in range(c):
        if i == 1 and j == 1:
            continue
        y = 162 + j * 62
        k += (f'<rect x="{x + 8}" y="{y}" width="{col_w - 16}" height="52" rx="10" fill="{WHITE}"/>'
              f'<rect x="{x + 18}" y="{y + 12}" width="{48 + (i * 7 + j * 13) % 22}" height="6" rx="3" fill="{G3}"/>'
              f'<rect x="{x + 18}" y="{y + 24}" width="{34 + (i * 5 + j * 9) % 20}" height="5" rx="2.5" fill="#D3D6DB"/>'
              f'<circle cx="{x + 26}" cy="{y + 40}" r="5" fill="{SUN if (i + j) % 3 == 0 else "#C9CCD2"}"/>')
won = x0 + 3 * (col_w + gap)
k += f'<rect x="{won + 8}" y="162" width="{col_w - 16}" height="52" rx="10" fill="{G1}"/><text x="{won + 18}" y="184" font-size="11" font-weight="700" fill="{SUN}">Closed</text><text x="{won + 18}" y="200" class="m" font-size="9.5" fill="{MUTE}">PKR 1.2M</text>'
kpis = [("Pipeline value", "PKR 4.8M"), ("Revenue won", "PKR 1.2M"), ("Total leads", "27"), ("Win rate", "32%")]
kp = ""
for i, (l, v) in enumerate(kpis):
    x = 30 + i * 146
    kp += f'<rect x="{x}" y="28" width="136" height="80" rx="18" fill="{WHITE}"/><text x="{x + 16}" y="54" font-size="10.5" fill="{MUTE}">{l}</text><text x="{x + 16}" y="88" class="s" font-size="22" fill="{G1}">{v}</text>'
kp += f'<rect x="30" y="28" width="136" height="80" rx="18" fill="none" stroke="{SUN}" stroke-width="2"/>'
svg("crm", "A five-stage sales pipeline with a lead card being dragged and a Gemini summary suggesting a follow-up email", f'''
{SHADOW("cr-sh")}
<rect width="640" height="400" fill="{CLOUD}"/>
{kp}{k}
<g transform="translate(166 214) rotate(-5)" filter="url(#cr-sh)">
  <rect width="132" height="60" rx="12" fill="{WHITE}" stroke="{SUN}" stroke-width="2"/>
  <text x="14" y="24" font-size="11.5" font-weight="700" fill="{G1}">Hassan Traders</text>
  <text x="14" y="42" class="m" font-size="9.5" fill="{G4}">PKR 650K · warm</text>
</g>
<path d="M286 262l0 18 5-5 4 9 4-2-4-9 7 0z" fill="{G1}" stroke="{WHITE}" stroke-width="1.4" stroke-linejoin="round"/>
<g transform="translate(330 240)" filter="url(#cr-sh)">
  <rect width="272" height="110" rx="20" fill="{G1}"/>
  <path d="M24 22c1 7 3 9 10 10-7 1-9 3-10 10-1-7-3-9-10-10 7-1 9-3 10-10z" fill="{SUN}"/>
  <text x="42" y="37" font-size="12" font-weight="700" fill="{WHITE}">Gemini summary</text>
  <text x="18" y="62" font-size="11.5" fill="#D9DBDF">High intent: asked for pricing twice.</text>
  <text x="18" y="80" font-size="11.5" fill="#D9DBDF">Suggest a follow-up this week.</text>
  <rect x="160" y="88" width="98" height="0" fill="none"/>
  <text x="254" y="98" text-anchor="end" font-size="11" font-weight="700" fill="{SUN}">Draft email →</text>
</g>''')

# ---------------- Research: Robustness ----------------
doms = ["Senti", "Hate", "Abuse", "Fake", "QA", "Pol."]
r = random.Random(4)
cells = ""
cs, gx, gy = 30, 326, 162
for i in range(6):
    for j in range(6):
        if i == j:
            v = .9 + r.random() * .08
        elif 3 in (i, j):
            v = .08 + r.random() * .12
        else:
            v = .35 + r.random() * .35
        cells += f'<rect x="{gx + j * (cs + 4)}" y="{gy + i * (cs + 4)}" width="{cs}" height="{cs}" rx="7" fill="{SUN if v > .85 else G1}" fill-opacity="{1 if v > .85 else round(v * .9 + .06, 2)}"/>'
labels = "".join(f'<text x="{gx - 8}" y="{gy + i * 34 + 19}" text-anchor="end" class="m" font-size="9.5" fill="{G4}">{d}</text>' for i, d in enumerate(doms))
labels += "".join(f'<text x="{gx + j * 34 + 15}" y="{gy - 8}" text-anchor="middle" class="m" font-size="9.5" fill="{G4}">{d}</text>' for j, d in enumerate(doms))
svg("robust", "The same Urdu sentence in Nastaliq and Roman script, above a train-to-test domain transfer matrix where fake news does not transfer", f'''
{SHADOW("rb-sh")}{glow("rb-g", "0%", "0%", SUN, .35)}
<rect width="640" height="400" fill="{CLOUD}"/><rect width="640" height="400" fill="url(#rb-g)"/>
<g filter="url(#rb-sh)"><rect x="30" y="34" width="234" height="96" rx="22" fill="{WHITE}"/></g>
<text x="50" y="58" class="m" font-size="9.5" fill="{MUTE}" letter-spacing="1">NASTALIQ</text>
{ur(46, 64, 202, 56, "یہ فلم بہت اچھی تھی", 22, G1)}
<g filter="url(#rb-sh)"><rect x="30" y="150" width="234" height="96" rx="22" fill="{G1}"/></g>
<text x="50" y="174" class="m" font-size="9.5" fill="{MUTE}" letter-spacing="1">ROMAN URDU</text>
<text x="50" y="214" class="s" font-size="19" font-style="italic" fill="{WHITE}" textLength="190" lengthAdjust="spacingAndGlyphs">yeh film bohat achi thi</text>
<path d="M147 130v20" stroke="{SUN}" stroke-width="3" stroke-linecap="round"/><circle cx="147" cy="140" r="9" fill="{SUN}"/><path d="M143 140h8M148 136l3 4-3 4" stroke="{G1}" stroke-width="1.8" fill="none" stroke-linecap="round"/>
<text x="30" y="290" class="s" font-size="46" fill="{G1}">188,309</text>
<text x="30" y="314" font-size="12" fill="{G4}">examples across 26 released datasets</text>
<text x="30" y="350" class="m" font-size="10" fill="{G4}" letter-spacing="1">SCRIPT · DOMAIN · CODE-MIX</text>
<text x="{gx}" y="56" class="m" font-size="9.5" fill="{MUTE}" letter-spacing="1">TRANSFER MATRIX · TRAIN ↓ TEST →</text>
<text x="{gx}" y="86" class="s" font-size="19" fill="{G1}">Fake news does not transfer.</text>
<text x="{gx}" y="108" font-size="11.5" fill="{G4}">Encoders lose 13.5–47.6 macro-F1 across 80 shifts;</text>
<text x="{gx}" y="124" font-size="11.5" fill="{G4}">few-shot LLMs win 30 of 42 paired comparisons.</text>
{labels}{cells}''')

# ---------------- Research: Compression ----------------
r = random.Random(9)
px = ""
for i in range(8):
    for j in range(8):
        sky = 200 - i * 9
        c = f"rgb({70 + i * 6},{110 + i * 8},{sky + 40})"
        px += f'<rect x="{40 + j * 22}" y="{60 + i * 22}" width="22" height="22" fill="{c}"/>'
plane = f'<path d="M64 168l60-22 24-36 10 2-12 30 36-12 10-16 8 2-6 22 18 4-2 6-20-2-58 24-36 6z" fill="#F4F5F7"/>'
patch = ""
for i in range(4):
    for j in range(4):
        patch += f'<rect x="{150 + j * 11}" y="{170 + i * 11}" width="11" height="11" fill="{r.choice([SUN, RED, "#3FD0C9", "#B46CFF", WHITE, G1])}"/>'
bars = [("Full model", 61.2, WHITE, "61.2%"), ("Pruned", 61.2, SUN, "held"), ("Dense, same size", 52.9, RED, "52.9%")]
bb = ""
for i, (l, v, c, t) in enumerate(bars):
    y = 134 + i * 64
    w = (v - 40) / 25 * 250
    bb += (f'<text x="300" y="{y}" font-size="11.5" fill="#D9DBDF">{l}</text>'
           f'<rect x="300" y="{y + 9}" width="250" height="14" rx="7" fill="{G3}"/><rect x="300" y="{y + 9}" width="{w:.0f}" height="14" rx="7" fill="{c}"/>'
           f'<text x="608" y="{y + 21}" text-anchor="end" class="m" font-size="10.5" fill="{c if c != "#D9DBDF" else MUTE}">{t}</text>')
svg("compress", "An airplane image with an adversarial patch misread as a frog, and patched accuracy showing pruned models hold while equally small dense models fall from 61.2 to 52.9 percent", f'''
{glow("cp-g", "0%", "100%")}
<defs><clipPath id="cp-c"><rect x="40" y="60" width="176" height="176" rx="18"/></clipPath></defs>
<rect width="640" height="400" fill="{G1}"/><rect width="640" height="400" fill="url(#cp-g)"/>
<text x="40" y="44" class="m" font-size="10" fill="{MUTE}" letter-spacing="1">CIFAR-10 · RESNET-18 ZOO</text>
<g clip-path="url(#cp-c)">{px}{plane}</g>
{patch}<rect x="148" y="168" width="48" height="48" fill="none" stroke="{SUN}" stroke-width="2" stroke-dasharray="3 3"/>
<rect x="40" y="252" width="176" height="36" rx="18" fill="{G2}" stroke="{G3}"/>
<text x="58" y="275" font-size="12" fill="#D9DBDF">airplane</text><text x="128" y="275" font-size="12" fill="{MUTE}">→</text><text x="150" y="275" font-size="12" font-weight="700" fill="{RED}">frog</text>
<text x="40" y="330" class="s" font-size="22" fill="{WHITE}">Capacity, not sparsity.</text>
<text x="40" y="352" font-size="11.5" fill="{MUTE}">2× / 4× / 8× compression · 3 seeds</text>
<text x="300" y="64" class="m" font-size="9.5" fill="{MUTE}" letter-spacing="1">PATCHED ACCURACY</text>
<text x="300" y="92" class="s" font-size="22" fill="{WHITE}">Who survives the patch?</text>
{bb}
<rect x="300" y="330" width="176" height="28" rx="14" fill="{G2}" stroke="{G3}"/><text x="388" y="348" text-anchor="middle" class="m" font-size="10" fill="{SUN}">CERTIFIED · PATCHCLEANSER</text>''')

# ---------------- Research: Shortcut ----------------
def doc(x, y, h, fill, line):
    lines = "".join(f'<rect x="{x + 16}" y="{y + 18 + k * 13}" width="{(88 - (k * 17) % 30)}" height="5" rx="2.5" fill="{line}"/>' for k in range(int((h - 26) / 13)))
    return f'<rect x="{x}" y="{y}" width="120" height="{h}" rx="14" fill="{fill}"/>' + lines
real_h, fake_h = 84, 286
svg("shortcut", "A fake Urdu article 3.4 times longer than a real one; a model learns length, and transfer collapses from 0.771 to 0.005 macro-F1", f'''
{SHADOW("sh-sh")}
<rect width="640" height="400" fill="{CLOUD}"/>
<g filter="url(#sh-sh)">{doc(36, 370 - real_h, real_h, WHITE, "#D3D6DB")}{doc(176, 370 - fake_h, fake_h, G1, G4)}</g>
<text x="96" y="{370 - real_h - 14}" text-anchor="middle" class="m" font-size="10" fill="{G4}" letter-spacing="1">REAL</text>
<text x="236" y="{370 - fake_h - 14}" text-anchor="middle" class="m" font-size="10" fill="{G4}" letter-spacing="1">FAKE</text>
<path d="M312 84v286" stroke="{SUN}" stroke-width="2.5"/><path d="M304 84h16M304 370h16" stroke="{SUN}" stroke-width="2.5" stroke-linecap="round"/>
<rect x="290" y="210" width="44" height="28" rx="14" fill="{SUN}"/><text x="312" y="229" text-anchor="middle" font-size="13" font-weight="700" fill="{G1}">3.4×</text>
<text x="364" y="66" class="m" font-size="9.5" fill="{MUTE}" letter-spacing="1">WHAT THE CLASSIFIER LEARNED</text>
<text x="364" y="100" class="s" font-size="30" fill="{G1}">Length, not</text>
<text x="364" y="134" class="s" font-size="30" font-style="italic" fill="{G1}">content.</text>
<text x="364" y="182" class="m" font-size="9.5" fill="{MUTE}" letter-spacing="1">TRANSFER MACRO-F1</text>
<path d="M368 214C430 214 460 214 490 252S560 316 600 318" stroke="{G1}" stroke-width="3" fill="none" stroke-linecap="round"/>
<circle cx="368" cy="214" r="6" fill="{G1}"/><circle cx="600" cy="318" r="7" fill="{RED}"/>
<text x="368" y="204" font-size="14" font-weight="700" fill="{G1}" dy="-6">0.771</text>
<text x="600" y="300" text-anchor="end" font-size="14" font-weight="700" fill="{RED}">0.005</text>
<g class="m" font-size="9.5" fill="{G1}">
<rect x="364" y="342" width="62" height="24" rx="12" fill="{WHITE}" stroke="#DADDE2"/><text x="395" y="358" text-anchor="middle">XLM-R</text>
<rect x="432" y="342" width="90" height="24" rx="12" fill="{WHITE}" stroke="#DADDE2"/><text x="477" y="358" text-anchor="middle">TF-IDF + LR</text>
<rect x="528" y="342" width="48" height="24" rx="12" fill="{WHITE}" stroke="#DADDE2"/><text x="552" y="358" text-anchor="middle">SVM</text></g>''')

# ---------------- Research: Bitcoin ----------------
r = random.Random(21)
price = 100
cand = ""
n = 34
for i in range(n):
    vol = 3.4 if 13 <= i <= 23 else 1.4
    o = price
    c = o + r.gauss(0.15, vol)
    hi = max(o, c) + abs(r.gauss(0, vol * .6))
    lo = min(o, c) - abs(r.gauss(0, vol * .6))
    price = c
    X = 40 + i * 16.6
    sc = lambda v: 200 - (v - 88) * 6.5
    up = c >= o
    col = SUN if up else "#7C818A"
    cand += f'<line x1="{X + 5:.1f}" y1="{sc(hi):.1f}" x2="{X + 5:.1f}" y2="{sc(lo):.1f}" stroke="{col}" stroke-width="1.4"/>'
    cand += f'<rect x="{X:.1f}" y="{min(sc(o), sc(c)):.1f}" width="10" height="{max(2, abs(sc(o) - sc(c))):.1f}" rx="2" fill="{col}"/>'
svg("bitcoin", "Hourly Bitcoin candles with a high-volatility regime shaded; Reddit sentiment and price features pass a volatility gate to an up prediction", f'''
<rect width="640" height="400" fill="{G1}"/>
<rect x="{40 + 13 * 16.6 - 6:.0f}" y="40" width="{11 * 16.6 + 4:.0f}" height="190" rx="14" fill="{SUN}" fill-opacity=".09"/>
<text x="{40 + 13 * 16.6 + 4:.0f}" y="60" class="m" font-size="9.5" fill="{SUN}" letter-spacing="1">HIGH-VOL REGIME</text>
<text x="40" y="34" class="m" font-size="10" fill="{MUTE}" letter-spacing="1">BTC / USD · HOURLY · 3,491 OBSERVATIONS</text>
{cand}
<g transform="translate(40 262)" font-size="12">
  <rect width="150" height="44" rx="22" fill="{G2}" stroke="{G3}"/><text x="18" y="27" font-weight="600" fill="{WHITE}">FinBERT</text><text x="132" y="27" text-anchor="end" class="m" font-size="9.5" fill="{MUTE}">REDDIT</text>
  <rect y="58" width="150" height="44" rx="22" fill="{G2}" stroke="{G3}"/><text x="18" y="85" font-weight="600" fill="{WHITE}">BiLSTM</text><text x="132" y="85" text-anchor="end" class="m" font-size="9.5" fill="{MUTE}">PRICE</text>
  <path d="M150 22c40 0 40 29 74 29M150 80c40 0 40-29 74-29" stroke="{G4}" stroke-width="1.8" fill="none"/>
  <rect x="224" y="24" width="150" height="54" rx="27" fill="{SUN}"/><text x="299" y="47" text-anchor="middle" font-weight="700" fill="{G1}">Regime gate</text><text x="299" y="64" text-anchor="middle" class="m" font-size="9.5" fill="{G1}">24 h volatility</text>
  <path d="M374 51h40" stroke="{G4}" stroke-width="1.8"/>
  <text x="400" y="44" class="s" font-size="30" fill="{WHITE}">↑ Up</text><text x="400" y="66" class="m" font-size="10" fill="{MUTE}">6 h horizon</text>
  <text x="566" y="44" text-anchor="end" class="s" font-size="30" fill="{SUN}">0.551</text><text x="566" y="66" text-anchor="end" class="m" font-size="10" fill="{MUTE}">macro-F1</text>
</g>''')
print("ok", sorted(os.listdir(OUT)))
