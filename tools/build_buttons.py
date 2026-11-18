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
        "accent": "#E2E8F0",
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

svg_width = 104
svg_height = 96
icon_size = 64
icon_x = (svg_width - icon_size) / 2 # 20.0
icon_y = 4.0
text_x = svg_width / 2 # 52.0
text_y = 86.0

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
    font_size = "11.5px" if len(label) > 8 else "13px"
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}" role="img" aria-label="{label}">
  <title>{label}</title>
  <defs>
    <filter id="shadow-{btn_id}" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="4" stdDeviation="4.5" flood-color="#000000" flood-opacity="0.65" />
      <feDropShadow dx="0" dy="2" stdDeviation="6" flood-color="{accent}" flood-opacity="0.45" />
    </filter>
    <style>
      .btn-logo {{
        filter: url(#shadow-{btn_id});
        transition: transform 0.2s ease, filter 0.2s ease;
      }}
      .btn-label {{
        font-family: 'JetBrains Mono', Consolas, 'Fira Code', 'Segoe UI Mono', monospace;
        font-size: {font_size};
        font-weight: 600;
        letter-spacing: 0.3px;
        fill: #94a3b8;
        transition: fill 0.2s ease;
      }}
      .btn-group:hover .btn-logo {{
        transform: translateY(-2px);
      }}
      .btn-group:hover .btn-label {{
        fill: #ffffff;
      }}
    </style>
  </defs>
  <g class="btn-group" cursor="pointer">
    <!-- Elevated Logo with Ambient Glow & Drop Shadow -->
    <image class="btn-logo" x="{icon_x}" y="{icon_y}" width="{icon_size}" height="{icon_size}" preserveAspectRatio="xMidYMid meet" xlink:href="data:image/png;base64,{b64}" href="data:image/png;base64,{b64}" />
    
    <!-- Text Label Below Button -->
    <text class="btn-label" x="{text_x}" y="{text_y}" text-anchor="middle">{label}</text>
  </g>
</svg>
"""
    target_path = os.path.join(output_dir, btn["file"])
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Wrote {btn['file']} ({svg_width}x{svg_height}, len={len(svg)})")

print("All 9 elevated logo button SVGs created successfully!")
