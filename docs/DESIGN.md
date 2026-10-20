# PixelForge design notes

PixelForge is drawn on a **5-column, 8-row cap grid** (x-height 6 rows, 2-row descenders, 2 rows for accents). That gives a 10-row body, and each pixel is a 100-unit cell. I tested smaller grids (5×7) and larger ones (8×12). 5×7 can't give a distinct x-height plus descenders, and 8×12 loses the chunky arcade read at UI sizes. 5×8 is the smallest grid where `a e s` get a real two-storey structure and `g j p q y` real descenders.

* **Regular** is the true bitmap: pixel ink = cell, so every edge sits on the 100-unit grid (tested).
* **Thin → Light** draw pixels as small squares joined by bridges, and diagonals become explicit stair steps. This is a skeleton of the bitmap, not a shrunken copy.
* **Medium → Black** grow stems horizontally (up to 176 units) more than bars vertically (up to 130). Growth into any one-pixel counter is capped at 18/15 units, so `m`, `e`, `B`, `8`, `#` stay open at Black. The advance grows with the stem so spacing keeps the rhythm.
* **Italics** shift each pixel row 16 units to the right: a drawn stepped slant with horizontal rows, at ≈9.1°.
* **Kerning** is pixel kerning. A pair tightens by exactly one pixel when every shared row keeps at least two pixels of paper between the glyphs.

## Variable font
Built from all 9 masters per slope, with overlaps preserved and OVERLAP_SIMPLE flagged. Intermediate weights interpolate pixel ink width, so they are smooth but off-grid. Use the statics where exact pixel edges matter.

## Engine
pixel map → weighted pixel rectangles + bridges + stepped diagonals → pathops union
