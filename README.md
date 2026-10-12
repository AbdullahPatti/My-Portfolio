# Portfolio — Muhammad Abdullah Haroon

Plain HTML/CSS/JS. No build step, no framework, no dependencies to install.

## Run it
Open `index.html` in a browser, or serve the folder with any static server.

## Deploy on Vercel
1. Push this folder to a GitHub repo.
2. Import it on vercel.com → Framework preset: "Other" → deploy. No build command needed.

## Files
- `index.html` — all content and structure
- `css/` — variables, base, layout, components, sections, projects (case studies + Why-me), responsive
- `js/` — nav, clock, cursor, counters, chart, filters, process, contact, main

## Three things to do before you deploy

### 1. Your photo
The hero uses **`Abdullah.jpg`** from the project root. Keep this filename (a portrait-oriented image works best, roughly 4:5). If the image cannot load, the site falls back to a clean monogram.

### 2. Your résumé
Keep your résumé PDF as `Abdullah_Haroon_CV.pdf` in the project root. Every résumé link in the site points to it.

### 3. Turn on the contact form
The Contact section now has a real form that emails you directly, not just a mailto link. It's wired to Formspree (formspree.io), free for personal use:
1. Sign up with abdullaharoon.work@gmail.com.
2. Create a new form, confirm the email link they send you.
3. Copy your form ID (looks like `xyzabcd`).
4. In `index.html`, find `action="https://formspree.io/f/YOUR_FORM_ID"` and replace `YOUR_FORM_ID` with yours.

Until you do that, the form shows "Form isn't connected yet" and people can still reach you through the plain email link right below it, so nothing is ever a dead end.

## What changed in this pass

Projects are now full case studies, not a grid of cards: problem, what you built, role, stack, and impact numbers, laid out like a real portfolio spotlight, left/right alternating per project. Each one has a hand-built mockup instead of a placeholder image, so nothing depends on AI image generation anymore:
- TaxChronos: a chat mockup with a real Urdu query bubble and an answer.
- Daily Digest: an inbox mockup with delivery-window badges.
- Urdu Robustness Benchmark: a real Urdu word rendered large, next to isometric 3D-style bars showing the 97/84/48 percent robustness tiers.
- WhisperBench: an audio waveform.
- FinSight: an actual mini dashboard, a donut chart, a bar chart, an SVG line chart, and a dollar figure, all in your site's colors.

If you'd rather swap any of these for a real screenshot later, that's a separate, simpler change, just say which project.

New section, "Why work with me", sits right after Projects. States plainly what you do (frontend, backend, infra, databases, AI automation with RAG/LLM/voice agents), the 4 to 6 week v1 timeline, and the no-handoff, I-stay-until-it-works line, in your own words.

Stack now shows real logos, pulled live from Simple Icons' CDN, grouped as Frontend, Backend, AI/ML/NLP, Databases, and Infrastructure, plus a "What I actually use, every day" row for VS Code, Cursor, Claude, and GitHub. A few niche AI tools (Qdrant, ChromaDB, Prompt Engineering) don't have official logos, so those just show as clean text tiles instead of a broken image, by design.

Hero shows you, not a chart. The macro-F1 collapse chart moved to where it actually belongs: inside the "When Benchmarks Mislead" paper card, as proof for that specific claim.

## Customizing colors
Every color is a CSS variable at the top of `css/variables.css`. Change `--accent` there and it updates buttons, links, chart bars, and underline animations everywhere at once.

## Optional, not required
Social share image: what shows up when the link is pasted into LinkedIn or WhatsApp. Save as `assets/og-image.jpg`, 1200×630. Best hand-built in Figma/Canva since it needs real text (your name and tagline); ask if you'd rather I generate one once your final photo is in.
