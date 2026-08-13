from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.join(os.path.dirname(__file__), "icons")
os.makedirs(OUT, exist_ok=True)

TILE = (228, 200, 154)      # --tile
TILE_SHADOW = (184, 152, 95)
INK = (59, 42, 26)          # --tile-ink
BOARD = (22, 70, 58)        # dark board green background

FONT_BOLD = "C:/Windows/Fonts/georgiab.ttf"
FONT_SANS = "C:/Windows/Fonts/arialbd.ttf"


def rounded_gradient_tile(size, radius_ratio=0.16):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    radius = int(size * radius_ratio)
    # simple two-tone diagonal gradient approximation
    for y in range(size):
        t = y / size
        r = int(TILE[0] + (TILE_SHADOW[0] - TILE[0]) * t)
        g = int(TILE[1] + (TILE_SHADOW[1] - TILE[1]) * t)
        b = int(TILE[2] + (TILE_SHADOW[2] - TILE[2]) * t)
        draw.line([(0, y), (size, y)], fill=(r, g, b, 255))
    mask = Image.new("L", (size, size), 0)
    mdraw = ImageDraw.Draw(mask)
    mdraw.rounded_rectangle([0, 0, size - 1, size - 1], radius=radius, fill=255)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    return out


def make_icon(size, pad_ratio, filename, background=None):
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    if background is not None:
        bd = ImageDraw.Draw(canvas)
        bd.rectangle([0, 0, size, size], fill=background)

    pad = int(size * pad_ratio)
    tile_size = size - 2 * pad
    tile = rounded_gradient_tile(tile_size)
    canvas.paste(tile, (pad, pad), tile)

    draw = ImageDraw.Draw(canvas)
    letter_font = ImageFont.truetype(FONT_BOLD, int(tile_size * 0.58))
    letter = "S"
    bbox = draw.textbbox((0, 0), letter, font=letter_font)
    lw, lh = bbox[2] - bbox[0], bbox[3] - bbox[1]
    lx = pad + (tile_size - lw) / 2 - bbox[0]
    ly = pad + (tile_size - lh) / 2 - bbox[1] - tile_size * 0.03
    draw.text((lx, ly), letter, font=letter_font, fill=INK)

    val_font = ImageFont.truetype(FONT_SANS, max(int(tile_size * 0.14), 10))
    val = "1"
    vbbox = draw.textbbox((0, 0), val, font=val_font)
    vw, vh = vbbox[2] - vbbox[0], vbbox[3] - vbbox[1]
    vx = pad + tile_size - vw - tile_size * 0.10 - vbbox[0]
    vy = pad + tile_size - vh - tile_size * 0.08 - vbbox[1]
    draw.text((vx, vy), val, font=val_font, fill=INK)

    canvas.save(os.path.join(OUT, filename))
    print("wrote", filename, size)


# Standard PWA icons (transparent-safe background matches board so it looks fine on any home screen)
make_icon(192, 0.09, "icon-192.png", background=BOARD)
make_icon(512, 0.09, "icon-512.png", background=BOARD)
# Maskable icon: keep the tile within the safe zone (~40% padding total for maskable spec)
make_icon(512, 0.20, "icon-512-maskable.png", background=BOARD)
# Apple touch icon: iOS ignores transparency, needs opaque background, no rounding (iOS rounds itself)
make_icon(180, 0.09, "apple-touch-icon.png", background=BOARD)

# favicon
fav = Image.open(os.path.join(OUT, "icon-192.png")).resize((32, 32), Image.LANCZOS)
fav.save(os.path.join(OUT, "favicon.png"))
print("done")
