# Portfolio &mdash; Mohammed Zain Rafeeque

Source code for **<https://portfoliozain-cwg6.vercel.app/>** &mdash; my personal portfolio site, built as a single-file static page deployed on Vercel.

[![Deploy](https://img.shields.io/badge/▶_Live_Site-portfoliozain.vercel.app-22d3ee?style=for-the-badge)](https://portfoliozain-cwg6.vercel.app/)
[![Vercel](https://img.shields.io/badge/Hosted-Vercel-000000?style=flat-square&logo=vercel)](https://vercel.com)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](#license)

---

## What's inside

A hand-coded portfolio focused on:

- **Hero with hire-me CTAs** &mdash; "Open to Work" status badge, downloadable CV, email + LinkedIn DM buttons
- **Featured project block** &mdash; latest shipped (DocIntel) gets dedicated above-the-fold treatment
- **Project grid** &mdash; 9 projects total: 5 with live demos (cyan badge + Live Demo button), 3 private client/employer work (lock badge), the rest with code links
- **Work experience** &mdash; reverse-chronological with company logos, role titles, year ranges, and concise impact descriptions
- **Categorized skills** &mdash; Languages / LLMs &amp; RAG / AI Platforms / ML &amp; DL / Backend &amp; Infra / Frontend &amp; Deploy
- **Education + certifications** &mdash; degree, courses, AI/ML certifications

## Tech stack

- **Single-file HTML** with inline `<style>` &mdash; no build step, no framework, no bloat
- **Inline SVG icons** for crisp rendering at any zoom
- **WebP images** (compressed via `compress_images.py`) &mdash; full page weight is ~1.1 MB
- **Inter** + **JetBrains Mono** fonts via Google Fonts
- **Open Graph + Twitter** meta tags for clean LinkedIn/Slack share previews
- **JSON-LD `Person` schema** for Google knowledge-panel signals
- **`robots.txt` + `sitemap.xml`** for crawlability
- **Mobile breakpoints** at 768 px (tablet) and 480 px (phone)

## Run locally

```bash
git clone https://github.com/ZainRafeeque/portfoliozain.git
cd portfoliozain
# It's a static site — open index.html in any browser, or:
python -m http.server 5500
# Then visit http://localhost:5500
```

## Re-compress images

If you swap in a new screenshot, re-run the compression script (Pillow required):

```bash
pip install Pillow
python compress_images.py
```

Outputs `.webp` versions of every PNG/JPG at &le;1600 px wide, q=82.

## Deploy

Pushes to `main` auto-deploy to Vercel within ~30 seconds. Vercel auto-detects this as a static site &mdash; no build configuration needed.

## File layout

```
portfoliozain/
├── index.html               # Everything — markup + styles + scripts inlined
├── compress_images.py       # PIL script: PNG/JPG → WebP @ ≤1600px
├── robots.txt
├── sitemap.xml
├── Zain-Rafeeque-CV-2026.pdf  # CV linked from the hero "Download CV" button
├── *.webp                   # Project screenshots, profile photo, company logos
└── README.md                # This file
```

## Author

**Mohammed Zain Rafeeque** &mdash; AI Engineer
- 🌐 Portfolio: <https://portfoliozain-cwg6.vercel.app/>
- 💼 LinkedIn: <https://linkedin.com/in/zain-rafeeque/>
- 📧 Email: zainrafeeque@gmail.com
- 🐙 GitHub: <https://github.com/ZainRafeeque>

## License

MIT &mdash; feel free to fork and adapt the layout/structure for your own portfolio. Please don't republish my profile photo, project screenshots, or CV verbatim.
