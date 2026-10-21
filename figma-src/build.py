"""Zarqand landing: template.html -> desktop.html / mobile.html with fonts and images inlined.

html_to_figma does not fetch external URLs, so every font and image is embedded as a data URI.
"""
import base64
import math
import pathlib
import re
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent
IMG_DIR = ROOT.parent / "assets" / "ai"
FONT_DIR = ROOT / "fonts"


def b64(path: pathlib.Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()


def font_css() -> str:
    css = (FONT_DIR / "fonts.css").read_text()
    blocks = re.findall(r"/\* ([\w-]+) \*/\s*(@font-face \{.*?\})", css, re.S)
    out = []
    for subset, block in blocks:
        if subset not in ("latin", "latin-ext"):
            continue
        url = re.search(r"url\((https://[^)]+)\)", block).group(1)
        local = FONT_DIR / url.rsplit("/", 1)[1]
        if not local.exists():
            urllib.request.urlretrieve(url, local)
        out.append(block.replace(url, "data:font/woff2;base64," + b64(local)))
    return "\n".join(dict.fromkeys(out))


def stamp(text: str, radius: int) -> str:
    """Letters set around a circle as individually rotated spans (no SVG textPath, which converts poorly)."""
    step = 360 / len(text)
    spans = []
    for i, ch in enumerate(text):
        a = i * step
        x = radius + radius * 0.84 * math.sin(math.radians(a))
        y = radius - radius * 0.84 * math.cos(math.radians(a))
        ch = "&nbsp;" if ch == " " else ch
        spans.append(
            f'<span style="left:{x:.1f}px;top:{y:.1f}px;transform:translate(-50%,-50%) rotate({a:.1f}deg)">{ch}</span>'
        )
    return "".join(spans)


def build(mode: str) -> None:
    html = (ROOT / "template.html").read_text()
    html = html.replace("{{FONTS}}", font_css())
    html = html.replace("{{MODE}}", mode)
    r = 80 if mode == "d" else 58
    html = html.replace("{{STAMP}}", stamp("ZARQAND · TOSHKENT · [YIL] · ", r))
    html = html.replace("{{STAMP_R}}", str(r * 2))
    for name in re.findall(r"\{\{IMG:(\w+)\}\}", html):
        html = html.replace("{{IMG:%s}}" % name, "data:image/jpeg;base64," + b64(IMG_DIR / f"{name}.jpg"))
    out = ROOT / ("desktop.html" if mode == "d" else "mobile.html")
    out.write_text(html)
    print(out.name, round(len(html) / 1e6, 2), "MB")


if __name__ == "__main__":
    build("d")
    build("m")
