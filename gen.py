#!/usr/bin/env python3
"""Peka.ai.id logo concepts - deterministic PIL rendering."""
from PIL import Image, ImageDraw

BG = (0x11, 0x11, 0x11)
YL = (0xFF, 0xD6, 0x0A)
S = 1080

def concept1_signal_p(path):
    """Bold P + AI spark star. The spark is the universal AI symbol."""
    from PIL import ImageFont
    im = Image.new("RGB", (S, S), BG)
    d = ImageDraw.Draw(im)
    cx = S // 2
    f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 560)
    t = "P"
    bb = d.textbbox((0, 0), t, font=f)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    d.text((cx - 60 - tw / 2 - bb[0], 540 - th / 2 - bb[1]), t, font=f, fill=YL)
    # 4-point spark
    scx, scy, R, r = 800, 300, 120, 26
    pts = []
    import math
    for i in range(8):
        ang = math.pi / 2 + i * math.pi / 4
        rad = R if i % 2 == 0 else r
        pts.append((scx + rad * math.cos(ang), scy - rad * math.sin(ang)))
    d.polygon(pts, fill=YL)
    im.save(path)

def concept2_pulse_node(path):
    """Bold P with a tilted orbit ring behind it. Tech/AI signal, no clutter."""
    from PIL import ImageFont
    im = Image.new("RGBA", (S, S), BG + (255,))
    d = ImageDraw.Draw(im)
    cx = S // 2
    # orbit ring first (behind the letter)
    layer = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    dl = ImageDraw.Draw(layer)
    dl.ellipse([cx - 350, 540 - 145, cx + 350, 540 + 145], outline=YL + (255,), width=28)
    layer = layer.rotate(-18, resample=Image.BICUBIC, center=(cx, 540))
    im = Image.alpha_composite(im, layer)
    # P on top
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 520)
    t = "P"
    bb = d.textbbox((0, 0), t, font=f)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    d.text((cx - tw / 2 - bb[0], 540 - th / 2 - bb[1]), t, font=f, fill=YL + (255,))
    im.convert("RGB").save(path)

if __name__ == "__main__":
    import os
    os.makedirs("/home/hatch/workspace/peka-logo", exist_ok=True)
    concept1_signal_p("/home/hatch/workspace/peka-logo/concept1-signal-p.png")
    concept2_pulse_node("/home/hatch/workspace/peka-logo/concept2-pulse-node.png")
    print("done")
