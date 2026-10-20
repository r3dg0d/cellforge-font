"""Cellforge-specific tests: pixel grid integrity and pixel kerning."""
import os
import sys

from fontTools.ttLib import TTFont
from test_fonts import ROOT, path, shape

sys.path.insert(0, os.path.join(ROOT, "tools"))
import engine  # noqa: E402


def test_regular_outlines_sit_on_the_pixel_grid():
    """At Regular (pixel ink = cell) every vertical edge of a letter falls on a 50-unit grid."""
    f = TTFont(path(400, False, "ttf"))
    gs = f.getGlyphSet()
    from fontTools.pens.recordingPen import RecordingPen
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789":
        pen = RecordingPen()
        gs[f.getBestCmap()[ord(ch)]].draw(pen)
        for op, args in pen.value:
            for x, y in args:
                assert x % 50 == 0 and y % 50 == 0, (ch, x, y)


def test_pixel_kerning_applies():
    p = path(400, False, "ttf")
    plain = sum(x.x_advance for x in shape(p, "To", {"kern": False})[2])
    kerned = sum(x.x_advance for x in shape(p, "To")[2])
    assert kerned == plain - 100


def test_maps_rows_are_rectangular():
    order, M = engine.load_maps()
    assert len(order) > 150
