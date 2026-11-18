import os
import sys
import urllib.request
import base64
import tempfile
import subprocess
from PIL import Image

output_dir = r"d:\github\bhargava562\assets\buttons"
os.makedirs(output_dir, exist_ok=True)

headers = {"User-Agent": "Mozilla/5.0"}

buttons_config = [
    {
        "file": "portfolio.svg",
        "id": "portfolio",
        "label": "PORTFOLIO",
        "accent": "#00FF9C",
        "url": "https://img.icons8.com/fluency/96/domain.png",
        "width": 144
    },
    {
        "file": "linkedin.svg",
        "id": "linkedin",
        "label": "LINKEDIN",
        "accent": "#0A66C2",
        "url": "https://img.icons8.com/fluency/96/linkedin.png",
        "width": 136
    },
    {
        "file": "github.svg",
        "id": "github",
        "label": "GITHUB",
        "accent": "#FFFFFF",
        "url": "https://img.icons8.com/fluency/96/github.png",
        "width": 120
    },
    {
        "file": "leetcode.svg",
        "id": "leetcode",
        "label": "LEETCODE",
        "accent": "#FFA116",
        "url": "https://img.icons8.com/external-tal-revivo-color-tal-revivo/96/external-level-up-your-coding-skills-and-quickly-land-a-job-logo-color-tal-revivo.png",
        "width": 136
    },
    {
        "file": "gmail.svg",
        "id": "gmail",
        "label": "GMAIL",
        "accent": "#EA4335",
        "url": "https://img.icons8.com/fluency/96/gmail.png",
        "width": 112
    },
    {
        "file": "hackerrank.svg",
        "id": "hackerrank",
        "label": "HACKERRANK",
        "accent": "#00EA64",
        "url": "https://img.icons8.com/external-tal-revivo-color-tal-revivo/96/external-hackerrank-is-a-technology-company-that-focuses-on-competitive-programming-logo-color-tal-revivo.png",
        "width": 154
    },
    {
        "file": "codeforces.svg",
        "id": "codeforces",
        "label": "CODEFORCES",
        "accent": "#1F8ACB",
        "url": "https://img.icons8.com/external-tal-revivo-color-tal-revivo/96/external-codeforces-programming-competitions-and-contests-programming-community-logo-color-tal-revivo.png",
        "width": 154
    },
    {
        "file": "codolio.svg",
        "id": "codolio",
        "label": "CODOLIO",
        "accent": "#00FF9C",
        "is_codolio": True,
        "width": 128
    },
    {
        "file": "x.svg",
        "id": "x",
        "label": "X / TWITTER",
        "accent": "#E2E8F0",
        "url": "https://img.icons8.com/fluency/96/twitterx.png",
        "width": 162
    }
]

print("Rendering Codolio 96x96 transparent PNG...")
edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
codolio_req = urllib.request.Request("https://codolio.com/codolio_assets/codolio.svg", headers=headers)
codolio_svg = urllib.request.urlopen(codolio_req).read().decode("utf-8")
codolio_html = f"""<!DOCTYPE html>
<html>
<head>
<style>
body {{ margin: 0; padding: 0; background: transparent; overflow: hidden; width: 96px; height: 96px; display: flex; align-items: center; justify-content: center; }}
svg {{ width: 96px; height: 96px; }}
</style>
</head>
<body>
{codolio_svg}
</body>
</html>"""

temp_html = os.path.join(tempfile.gettempdir(), "codolio_render.html")
temp_png = os.path.join(tempfile.gettempdir(), "codolio_render.png")
with open(temp_html, "w", encoding="utf-8") as f:
    f.write(codolio_html)

subprocess.run([
    edge,
    "--headless",
    "--disable-gpu",
    "--default-background-color=00000000",
    "--window-size=96,96",
    f"--screenshot={temp_png}",
    temp_html
], check=True)

with open(temp_png, "rb") as f:
    codolio_b64 = base64.b64encode(f.read()).decode("utf-8")

print(f"Codolio PNG rendered successfully (b64 len={len(codolio_b64)}).")

for btn in buttons_config:
    if btn.get("is_codolio"):
        b64 = codolio_b64
    else:
        print(f"Fetching {btn['label']} from {btn['url']}...")
        req = urllib.request.Request(btn["url"], headers=headers)
        img_data = urllib.request.urlopen(req).read()
        b64 = base64.b64encode(img_data).decode("utf-8")
    
    w = btn["width"]
    arrow_x = w - 18
    accent = btn["accent"]
    btn_id = btn["id"]
    label = btn["label"]
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {w} 36" width="{w}" height="36" role="img" aria-label="{label}">
  <title>{label}</title>
  <defs>
    <style>
      .btn-bg {{ transition: fill 0.2s ease; }}
      .btn-border {{ transition: stroke 0.2s ease, stroke-width 0.2s ease; }}
      .btn-arrow {{ transition: transform 0.2s ease, opacity 0.2s ease; }}
      .btn-group:hover .btn-bg {{ fill: #131c31; }}
      .btn-group:hover .btn-border {{ stroke-width: 1.5; stroke-opacity: 1; }}
      .btn-group:hover .btn-arrow {{ opacity: 1; transform: translate({arrow_x + 1}px, 12.5px); }}
      .btn-text {{
        font-family: 'JetBrains Mono', Consolas, 'Fira Code', 'Segoe UI Mono', monospace;
        font-size: 12.5px;
        font-weight: 700;
        letter-spacing: 0.5px;
        fill: #FFFFFF;
      }}
    </style>
    <linearGradient id="bg-grad-{btn_id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d1424" />
      <stop offset="100%" stop-color="#080d1a" />
    </linearGradient>
    <linearGradient id="glow-{btn_id}" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{accent}" stop-opacity="0.12" />
      <stop offset="100%" stop-color="{accent}" stop-opacity="0.0" />
    </linearGradient>
  </defs>
  <g class="btn-group" cursor="pointer">
    <!-- Background card -->
    <rect class="btn-bg" x="0.5" y="0.5" width="{w - 1}" height="35" rx="7.5" fill="url(#bg-grad-{btn_id})" />
    <rect x="0.5" y="0.5" width="{w - 1}" height="35" rx="7.5" fill="url(#glow-{btn_id})" />
    <rect class="btn-border" x="0.5" y="0.5" width="{w - 1}" height="35" rx="7.5" fill="none" stroke="{accent}" stroke-width="1" stroke-opacity="0.65" />
    
    <!-- Icon -->
    <image x="10" y="8" width="20" height="20" preserveAspectRatio="xMidYMid meet" xlink:href="data:image/png;base64,{b64}" href="data:image/png;base64,{b64}" />
    
    <!-- Text Label -->
    <text class="btn-text" x="38" y="18" dominant-baseline="central">{label}</text>
    
    <!-- Subtle arrow indicator ↗ -->
    <g class="btn-arrow" transform="translate({arrow_x}, 13.5)" stroke="{accent}" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" fill="none" opacity="0.75">
      <path d="M1 7.5 L7.5 1 M3 1 L7.5 1 L7.5 5.5" />
    </g>
  </g>
</svg>
"""
    target_path = os.path.join(output_dir, btn["file"])
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Wrote {btn['file']} ({w}x36, len={len(svg)})")

print("All 9 button SVGs created successfully!")
