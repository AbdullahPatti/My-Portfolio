# Portfolio — Muhammad Abdullah Haroon

Plain HTML/CSS/JS. No framework, no dependencies. Open `index.html` or deploy the folder on Vercel (preset "Other").

## Structure
- `index.html` — the built page (all content + inline SVG visuals)
- `css/style.css` — design tokens (graphite / cloud white / sunshine yellow), Liquid-Glass nav and widgets
- `js/app.js` — nav, reveal-on-scroll, stacking cards for Research/Projects, contact form (Formspree)
- `fonts/web/` — Gazpacho subset to woff2 (display serif). Body uses SF Pro on Apple devices, Inter elsewhere; Urdu uses Noto Nastaliq Urdu.
- `assets/logos/` — local brand logos (no CDN at runtime); `assets/orgs/` — QuickFuel, Optimus Automate, PACT logos
- `tools/` — source for the page: `index.tpl.html` (content, with `{{t|logo|Name}}` tag shorthand) and `viz.py` (the project/research visuals)

## Editing
Small text edits: edit `index.html` directly.
Bigger changes (new tags, visuals): edit `tools/index.tpl.html` / `tools/viz.py`, then:

    python tools/viz.py tools/viz
    python tools/build.py tools/index.tpl.html tools/viz index.html

Visuals are inline SVG (not `<img>`) so the page fonts — including Nastaliq — render inside them.

## CV
Keep the résumé at `Abdullah_Haroon_CV.pdf`. Site sections are numbered 01–08 in the same order as the CV.
