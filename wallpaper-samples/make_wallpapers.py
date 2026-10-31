import numpy as np
from PIL import Image

W, H = 1320, 2868  # iPhone 17 Pro Max native resolution
OUT = "/home/user/blog/wallpaper-samples"
rng = np.random.default_rng(7)

y, x = np.mgrid[0:H, 0:W].astype(np.float32)
u, v = x / W, y / H  # 0..1 coordinates


def hexrgb(h):
    h = h.lstrip("#")
    return np.array([int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)], np.float32)


def grain(img, amount):
    n = rng.normal(0, amount, (H, W, 1)).astype(np.float32)
    return img + n


def smooth_noise(scale, seed):
    """Cheap smooth noise: sum of random sine waves."""
    r = np.random.default_rng(seed)
    out = np.zeros((H, W), np.float32)
    for _ in range(6):
        a = r.uniform(0, 2 * np.pi)
        f = r.uniform(0.6, 1.6) * scale
        p = r.uniform(0, 2 * np.pi)
        out += np.sin((np.cos(a) * u + np.sin(a) * v * H / W) * f * 2 * np.pi + p)
    return out / 6


def save(img, name):
    img = np.clip(img, 0, 1)
    Image.fromarray((img * 255 + 0.5).astype(np.uint8)).save(f"{OUT}/{name}.png", optimize=True)


# 1. DUNE: warm mesh gradient, soft blobs, film grain
def dune():
    # a diagonal gradient, bent by two layers of smooth noise, then mapped to a palette
    wu = u + 0.18 * smooth_noise(0.7, 1)
    wv = v + 0.10 * smooth_noise(0.9, 2)
    wu = wu + 0.10 * np.sin(wv * 5.0 + 1.3)
    t = np.clip(0.35 * wu + 0.75 * wv + 0.08 * np.sin(wu * 6.0) - 0.05, 0, 1)
    stops = [(0.00, "#f2e8dc"), (0.30, "#ecc9a8"), (0.52, "#df8f63"),
             (0.70, "#b65a3a"), (0.86, "#7e3b2a"), (1.00, "#3f2019")]
    img = np.zeros((H, W, 3), np.float32)
    for (t0, c0), (t1, c1) in zip(stops, stops[1:]):
        k = np.clip((t - t0) / (t1 - t0), 0, 1)
        k = k * k * (3 - 2 * k)  # smoothstep for silky transitions
        inside = ((t >= t0) & (t <= t1))[..., None]
        img = np.where(inside, hexrgb(c0) * (1 - k[..., None]) + hexrgb(c1) * k[..., None], img)
    return grain(img, 0.03)


# 2. HALO: luminous ring on near black, OLED friendly
def halo():
    img = np.ones((H, W, 3), np.float32) * hexrgb("#07070a")
    cx, cy = 0.5 * W, 0.66 * H
    dx, dy = x - cx, y - cy
    r = np.sqrt(dx ** 2 + dy ** 2)
    ang = np.arctan2(dy, dx)
    R = 0.62 * W
    ring = np.exp(-((r - R) / (0.018 * W)) ** 2)
    glow = np.exp(-((r - R) / (0.16 * W)) ** 2) * 0.35
    inner = np.exp(-(r / (0.9 * W)) ** 2) * 0.06
    # light strongest at top of the ring, fading around the sides
    bright = (0.5 + 0.5 * np.cos(ang + np.pi / 2)) ** 1.8
    t = (np.cos(ang * 1.0 + 0.6) + 1) / 2  # colour shift around the ring
    col = hexrgb("#7aa2ff")[None, None] * (1 - t[..., None]) + hexrgb("#ffb38a")[None, None] * t[..., None]
    light = ((ring * 1.1 + glow) * bright + inner)[..., None]
    img = img + col * light
    img = img + hexrgb("#ffffff") * (ring * bright ** 3 * 0.5)[..., None]
    return grain(img, 0.022)


# 3. FOLD: layered paper bands in sage, soft shadows
def fold():
    tones = ["#e8e9df", "#d6dacb", "#c2c9b4", "#a9b39b", "#8e9a82", "#6f7b66", "#55604f"]
    img = np.ones((H, W, 3), np.float32) * hexrgb(tones[0])
    n = len(tones) - 1
    for i in range(1, len(tones)):
        base = 0.30 + i * 0.095
        amp = 0.045 + 0.01 * i
        edge = base + amp * np.sin(u * np.pi * (1.1 + 0.15 * i) + i * 0.9) + 0.012 * smooth_noise(0.8, 10 + i)
        d = (v - edge) * H  # pixels below the edge
        mask = np.clip(d / 2.0 + 0.5, 0, 1)[..., None]  # antialiased edge
        shadow = (np.exp(-np.clip(-d, 0, None) / 38.0) * (d < 0) * 0.16)[..., None]
        img = img * (1 - shadow)
        # subtle vertical shading inside each band
        shade = 1 + 0.06 * np.clip(d / (0.12 * H), 0, 1)[..., None]
        img = img * (1 - mask) + (hexrgb(tones[i]) / shade) * mask
        highlight = (np.exp(-np.clip(d, 0, None) / 3.0) * (d >= 0) * 0.10)[..., None]
        img = img + highlight
    return grain(img, 0.02)


for name, fn in [("01_dune", dune), ("02_halo", halo), ("03_fold", fold)]:
    save(fn(), name)
    print("saved", name)
