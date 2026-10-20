# QA results (local build 2026-10-19, nixos)

* pytest: 53 passed, 18 sk
* Visual regression: 0 changed pixels vs tests/reference (54 sheets: 18 styles × ASCII / Latin-1 / terminal; see visual-regression.md)
* FontBakery 1.1.0, universal profile. Columns: ERROR | FATAL | FAIL | WARN | SKIP | INFO | PASS
  * ttf: | 0 | 0 | 0 | 54 | 677 | 54 | 1297 | 0 | 
  * otf: | 0 | 0 | 0 | 36 | 821 | 54 | 1171 | 0 | 
  * variable: | 0 | 0 | 0 | 10 | 43 | 6 | 183 | 0 | 

## Known FontBakery results
* `fontdata_namecheck` passes after the rename.
* ERROR `opentype/monospace` on OTF (monospace families): FontBakery bug, `KeyError: 'glyf'` on CFF fonts. The same check passes on the TTFs (WARN only: numberOfHMetrics=1, which is fontTools' valid optimisation).
* WARN `contour_count`: expected. Pixel, dot, and stroke construction gives different contour counts than reference fonts.
* WARN `soft_hyphen`: U+00AD is kept for Latin-1 completeness.
* FAIL: none.

## Environment notes
On NixOS the pip fontbakery wheel's bundled `ots-sanitize` was replaced by nixpkgs `opentype-sanitizer`, and libstdc++ was provided via `LD_LIBRARY_PATH`. OTS passes.
