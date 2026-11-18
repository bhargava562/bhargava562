import os
import sys
import urllib.request
import base64
import tempfile
import subprocess

output_dir = r"d:\github\bhargava562\assets\buttons"
os.makedirs(output_dir, exist_ok=True)

headers = {"User-Agent": "Mozilla/5.0"}

buttons_config = [
    {
        "file": "portfolio.svg",
        "id": "portfolio",
        "label": "Portfolio",
        "accent": "#00FF9C",
        "url": "https://img.icons8.com/fluency/96/domain.png",
    },
    {
        "file": "linkedin.svg",
        "id": "linkedin",
        "label": "LinkedIn",
        "accent": "#0A66C2",
        "url": "https://img.icons8.com/fluency/96/linkedin.png",
    },
    {
        "file": "github.svg",
        "id": "github",
        "label": "GitHub",
        "accent": "#FFFFFF",
        "url": "https://img.icons8.com/fluency/96/github.png",
    },
    {
        "file": "leetcode.svg",
        "id": "leetcode",
        "label": "LeetCode",
        "accent": "#FFA116",
        "url": "https://img.icons8.com/external-tal-revivo-color-tal-revivo/96/external-level-up-your-coding-skills-and-quickly-land-a-job-logo-color-tal-revivo.png",
    },
    {
        "file": "gmail.svg",
        "id": "gmail",
        "label": "Gmail",
        "accent": "#EA4335",
        "url": "https://img.icons8.com/fluency/96/gmail.png",
    },
    {
        "file": "hackerrank.svg",
        "id": "hackerrank",
        "label": "HackerRank",
        "accent": "#00EA64",
        "url": "https://img.icons8.com/external-tal-revivo-color-tal-revivo/96/external-hackerrank-is-a-technology-company-that-focuses-on-competitive-programming-logo-color-tal-revivo.png",
    },
    {
        "file": "codeforces.svg",
        "id": "codeforces",
        "label": "Codeforces",
        "accent": "#1F8ACB",
        "url": "https://img.icons8.com/external-tal-revivo-color-tal-revivo/96/external-codeforces-programming-competitions-and-contests-programming-community-logo-color-tal-revivo.png",
    },
    {
        "file": "codolio.svg",
        "id": "codolio",
        "label": "Codolio",
        "accent": "#00FF9C",
        "is_codolio": True,
    },
    {
        "file": "x.svg",
        "id": "x",
        "label": "X",
        "accent": "#E2E8F0",
        "url": "https://img.icons8.com/fluency/96/twitterx.png",
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

svg_width = 72
svg_height = 74
btn_size = 48
btn_x = (svg_width - btn_size) / 2 # 12.0
btn_y = 2.0
icon_size = 28
icon_x = btn_x + (btn_size - icon_size) / 2 # 22.0
icon_y = btn_y + (btn_size - icon_size) / 2 # 12.0
text_x = svg_width / 2 # 36.0
text_y = 66.0

for btn in buttons_config:
    if btn.get("is_codolio"):
        b64 = codolio_b64
    else:
        print(f"Fetching {btn['label']} from {btn['url']}...")
        req = urllib.request.Request(btn["url"], headers=headers)
        img_data = urllib.request.urlopen(req).read()
        b64 = base64.b64encode(img_data).decode("utf-8")
    
    accent = btn["accent"]
    btn_id = btn["id"]
    label = btn["label"]
    font_size = "10px" if len(label) > 8 else "11px"
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}" role="img" aria-label="{label}">
  <title>{label}</title>
  <defs>
    <style>
      .btn-bg {{ transition: fill 0.2s ease; }}
      .btn-border {{ transition: stroke 0.2s ease, stroke-width 0.2s ease, stroke-opacity 0.2s ease; }}
      .btn-label {{
        font-family: 'JetBrains Mono', Consolas, 'Fira Code', 'Segoe UI Mono', monospace;
        font-size: {font_size};
        font-weight: 600;
        letter-spacing: 0.3px;
        fill: #94a3b8;
        transition: fill 0.2s ease;
      }}
      .btn-group:hover .btn-bg {{ fill: #131c31; }}
      .btn-group:hover .btn-border {{ stroke-width: 1.6; stroke-opacity: 1; stroke: {accent}; }}
      .btn-group:hover .btn-label {{ fill: #ffffff; }}
    </style>
    <linearGradient id="bg-grad-{btn_id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d1424" />
      <stop offset="100%" stop-color="#080d1a" />
    </linearGradient>
    <linearGradient id="glow-{btn_id}" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{accent}" stop-opacity="0.15" />
      <stop offset="100%" stop-color="{accent}" stop-opacity="0.0" />
    </linearGradient>
  </defs>
  <g class="btn-group" cursor="pointer">
    <!-- Square Button Card (No text inside) -->
    <rect class="btn-bg" x="{btn_x + 0.5}" y="{btn_y + 0.5}" width="{btn_size - 1}" height="{btn_size - 1}" rx="10" fill="url(#bg-grad-{btn_id})" />
    <rect x="{btn_x + 0.5}" y="{btn_y + 0.5}" width="{btn_size - 1}" height="{btn_size - 1}" rx="10" fill="url(#glow-{btn_id})" />
    <rect class="btn-border" x="{btn_x + 0.5}" y="{btn_y + 0.5}" width="{btn_size - 1}" height="{btn_size - 1}" rx="10" fill="none" stroke="{accent}" stroke-width="1.2" stroke-opacity="0.65" />
    
    <!-- Centered Logo (Medium size) -->
    <image x="{icon_x}" y="{icon_y}" width="{icon_size}" height="{icon_size}" preserveAspectRatio="xMidYMid meet" xlink:href="data:image/png;base64,{b64}" href="data:image/png;base64,{b64}" />
    
    <!-- Text Label Below Button -->
    <text class="btn-label" x="{text_x}" y="{text_y}" text-anchor="middle">{label}</text>
  </g>
</svg>
"""
    target_path = os.path.join(output_dir, btn["file"])
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Wrote {btn['file']} ({svg_width}x{svg_height}, len={len(svg)})")

print("All 9 squared button SVGs created successfully!")
