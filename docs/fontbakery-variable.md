## FontBakery report

fontbakery version: 1.1.0







## Check results



<details><summary>[5] Cellforge-Italic[wght].ttf</summary>
<div>
<details>
    <summary>⚠️ <b>WARN</b> Detect any interpolation issues in the font. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#interpolation-issues">interpolation_issues</a></summary>
    <div>


> 
> When creating a variable font, the designer must make sure that corresponding
> paths have the same start points across masters, as well as that corresponding
> component shapes are placed in the same order within a glyph across masters.
> If this is not done, the glyph will not interpolate correctly.
> 
> Here we check for the presence of potential interpolation errors using the
> fontTools.varLib.interpolatable module.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3930





* ⚠️ **WARN** <p>Interpolation issues were found in the font:</p>
<pre><code>- Contour order differs in glyph 'germandbls': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56] in wght=400, [40, 26, 28, 37, 30, 32, 34, 35, 38, 45, 51, 56, 46, 44, 54, 47, 49, 50, 52, 53, 39, 41, 3, 27, 4, 10, 29, 13, 5, 31, 6, 33, 7, 8, 11, 14, 15, 43, 55, 36, 21, 1, 25, 9, 20, 16, 48, 17, 42, 2, 12, 22, 18, 19, 24, 23, 0] in wght=100.

- Contour order differs in glyph 'eacute': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49] in wght=400, [23, 26, 28, 30, 32, 33, 6, 35, 11, 9, 38, 39, 42, 13, 44, 41, 16, 17, 18, 48, 45, 21, 24, 25, 2, 27, 3, 29, 7, 4, 31, 5, 8, 36, 34, 10, 12, 37, 14, 40, 0, 22, 1, 43, 46, 15, 47, 19, 49, 20] in wght=100.

- Contour order differs in glyph 'backslash': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25] in wght=400, [8, 9, 10, 13, 14, 18, 21, 22, 12, 1, 2, 11, 0, 20, 15, 4, 16, 17, 5, 19, 3, 6, 23, 7, 24, 25] in wght=100.

- Contour order differs in glyph 'braceleft': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35] in wght=400, [25, 20, 22, 13, 24, 26, 28, 29, 8, 9, 10, 11, 19, 16, 3, 21, 4, 23, 12, 14, 5, 15, 1, 18, 6, 27, 7, 30, 17, 34, 2, 31, 32, 33, 0, 35] in wght=100.

- Contour order differs in glyph 'arrowright': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26] in wght=400, [2, 3, 5, 17, 16, 22, 26, 19, 23, 25, 10, 13, 14, 6, 18, 4, 0, 11, 20, 7, 8, 21, 24, 9, 1, 12, 15] in wght=100.

- Contour order differs in glyph 'V': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46] in wght=400, [27, 16, 19, 21, 22, 33, 26, 8, 35, 37, 39, 41, 43, 45, 46, 15, 1, 17, 18, 2, 20, 3, 4, 34, 9, 7, 29, 32, 0, 5, 25, 6, 30, 24, 36, 38, 31, 28, 23, 10, 40, 11, 42, 12, 44, 13, 14] in wght=100.

- Contour order differs in glyph 'braceright': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35] in wght=400, [15, 1, 18, 3, 22, 24, 34, 26, 28, 30, 31, 27, 17, 13, 6, 21, 12, 23, 33, 25, 11, 8, 35, 2, 14, 4, 9, 29, 10, 32, 0, 19, 16, 7, 5, 20] in wght=100.

- Contour order differs in glyph 'braceright': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35] in wght=300, [14, 1, 16, 3, 12, 30, 33, 17, 21, 8, 28, 20, 15, 13, 0, 25, 24, 23, 2, 31, 32, 34, 35, 4, 18, 5, 7, 11, 26, 27, 9, 29, 10, 19, 6, 22] in wght=500.

- Contour order differs in glyph 'yen': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48] in wght=400, [1, 20, 21, 22, 23, 25, 28, 31, 34, 36, 24, 39, 40, 43, 45, 15, 16, 47, 48, 5, 27, 2, 3, 37, 26, 6, 29, 4, 7, 8, 32, 33, 9, 35, 12, 10, 38, 11, 13, 42, 41, 44, 14, 46, 19, 0, 30, 17, 18] in wght=100.

- Contour order differs in glyph 'Aring': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81] in wght=400, [31, 34, 35, 37, 39, 42, 43, 12, 45, 47, 50, 52, 16, 55, 57, 15, 73, 81, 63, 65, 66, 67, 68, 70, 74, 76, 78, 80, 32, 33, 3, 7, 36, 4, 44, 38, 5, 40, 6, 41, 8, 0, 28, 1, 54, 56, 46, 9, 48, 49, 10, 51, 11, 53, 60, 61, 13, 14, 58, 59, 72, 17, 62, 18, 64, 19, 20, 21, 22, 69, 23, 71, 24, 25, 75, 26, 77, 79, 27, 30, 2, 29] in wght=100.

- 121 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: interpolation-issues]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts include an avar table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#mandatory-avar-table">mandatory_avar_table</a></summary>
    <div>


> 
> Most variable fonts should include an avar table to correctly define
> axes progression rates.
> 
> For example, a weight axis from 0% to 100% doesn't map directly to 100 to 1000,
> because a 10% progression from 0% may be too much to define the 200,
> while 90% may be too little to define the 900.
> 
> If the progression rates of axes is linear, this check can be ignored.
> Fontmake will also skip adding an avar table if the progression rates
> are linear. However, it is still recommended that designers visually proof
> each instance is at the expected weight, width etc.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3100





* ⚠️ **WARN** <p>This variable font does not have an avar table. Most variable fonts should include an avar table to correctly define axes progression rates.</p>
 [code: missing-avar]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>


> 
> It is a common practice to have math signs sharing the same width
> (preferably the same width as tabular figures accross the entire font family).
> 
> This probably comes from the will to avoid additional tabular math signs
> knowing that their design can easily share the same width.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3832





* ⚠️ **WARN** <p>The most common width is 600 among a set of 5 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 500:
less, equal, greater</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>


> 
> Some rasterizers encounter difficulties when rendering glyphs with
> overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points.
> When two segments share the same coordinates, they are considered
> overlapping.
> 




> Original proposal: https://github.com/google/fonts/issues/7594#issuecomment-2401909084





* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* A (U+0041): L&lt;&lt;198.0,300.0&gt;--&lt;198.0,400.0&gt;&gt; has the same coordinates as a previous segment.

* A (U+0041): L&lt;&lt;298.0,300.0&gt;--&lt;298.0,400.0&gt;&gt; has the same coordinates as a previous segment.

* A (U+0041): L&lt;&lt;362.0,700.0&gt;--&lt;362.0,800.0&gt;&gt; has the same coordinates as a previous segment.

* A (U+0041): L&lt;&lt;398.0,300.0&gt;--&lt;398.0,400.0&gt;&gt; has the same coordinates as a previous segment.

* A (U+0041): L&lt;&lt;462.0,700.0&gt;--&lt;462.0,800.0&gt;&gt; has the same coordinates as a previous segment.

* A (U+0041): L&lt;&lt;498.0,300.0&gt;--&lt;498.0,400.0&gt;&gt; has the same coordinates as a previous segment.

* A (U+0041): L&lt;&lt;166.0,150.0&gt;--&lt;66.0,150.0&gt;&gt; has the same coordinates as a previous segment.

* A (U+0041): L&lt;&lt;182.0,250.0&gt;--&lt;82.0,250.0&gt;&gt; has the same coordinates as a previous segment.

* A (U+0041): L&lt;&lt;198.0,350.0&gt;--&lt;98.0,350.0&gt;&gt; has the same coordinates as a previous segment.

* A (U+0041): L&lt;&lt;214.0,450.0&gt;--&lt;114.0,450.0&gt;&gt; has the same coordinates as a previous segment.

* 5046 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>
</div>
</details>

<details><summary>[5] Cellforge[wght].ttf</summary>
<div>
<details>
    <summary>⚠️ <b>WARN</b> Detect any interpolation issues in the font. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#interpolation-issues">interpolation_issues</a></summary>
    <div>


> 
> When creating a variable font, the designer must make sure that corresponding
> paths have the same start points across masters, as well as that corresponding
> component shapes are placed in the same order within a glyph across masters.
> If this is not done, the glyph will not interpolate correctly.
> 
> Here we check for the presence of potential interpolation errors using the
> fontTools.varLib.interpolatable module.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3930





* ⚠️ **WARN** <p>Interpolation issues were found in the font:</p>
<pre><code>- Contour order differs in glyph 'germandbls': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56] in wght=400, [40, 26, 51, 37, 29, 31, 34, 35, 38, 41, 42, 56, 15, 44, 54, 46, 48, 50, 52, 53, 39, 3, 27, 13, 4, 10, 28, 5, 30, 6, 32, 33, 7, 8, 11, 14, 45, 43, 55, 2, 9, 21, 20, 1, 25, 16, 47, 17, 49, 24, 23, 22, 18, 19, 0, 12, 36] in wght=100.

- Contour order differs in glyph 'eacute': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49] in wght=400, [23, 26, 28, 30, 32, 33, 6, 35, 12, 9, 38, 40, 42, 13, 44, 41, 16, 17, 46, 48, 45, 21, 24, 25, 2, 27, 3, 29, 7, 4, 31, 8, 5, 36, 34, 10, 11, 37, 14, 39, 0, 22, 1, 43, 18, 15, 47, 19, 49, 20] in wght=100.

- Contour order differs in glyph 'backslash': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25] in wght=400, [8, 9, 10, 13, 14, 18, 21, 22, 12, 1, 2, 11, 0, 20, 15, 4, 16, 17, 5, 19, 3, 6, 23, 7, 24, 25] in wght=100.

- Contour order differs in glyph 'braceleft': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35] in wght=400, [25, 19, 22, 13, 24, 26, 28, 29, 8, 9, 10, 11, 32, 15, 18, 20, 4, 23, 12, 5, 14, 16, 17, 21, 6, 27, 7, 30, 3, 33, 34, 31, 1, 2, 0, 35] in wght=100.

- Contour order differs in glyph 'arrowright': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26] in wght=400, [12, 3, 5, 18, 16, 20, 26, 17, 8, 25, 10, 13, 14, 6, 24, 0, 1, 4, 22, 7, 19, 21, 23, 9, 15, 11, 2] in wght=100.

- Contour order differs in glyph 'V': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46] in wght=400, [27, 16, 18, 20, 22, 33, 35, 32, 34, 37, 39, 40, 43, 44, 46, 15, 1, 17, 2, 19, 3, 21, 4, 8, 9, 5, 28, 29, 25, 23, 24, 7, 30, 26, 36, 38, 6, 31, 0, 10, 11, 41, 42, 12, 13, 45, 14] in wght=100.

- Contour order differs in glyph 'braceright': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35] in wght=400, [15, 1, 17, 3, 22, 24, 34, 26, 28, 30, 31, 27, 4, 13, 19, 21, 18, 23, 33, 25, 11, 35, 8, 5, 14, 0, 9, 29, 10, 32, 12, 16, 6, 20, 2, 7] in wght=100.

- Contour order differs in glyph 'yen': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48] in wght=400, [20, 1, 21, 22, 23, 25, 28, 31, 34, 36, 24, 42, 13, 44, 45, 15, 16, 47, 48, 5, 27, 2, 3, 37, 26, 6, 29, 0, 7, 19, 32, 33, 9, 35, 12, 10, 38, 39, 11, 43, 40, 41, 14, 46, 8, 30, 4, 17, 18] in wght=100.

- Contour order differs in glyph 'Aring': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81] in wght=400, [31, 34, 35, 37, 39, 42, 43, 12, 45, 49, 51, 52, 16, 55, 57, 15, 74, 81, 63, 64, 66, 67, 69, 70, 73, 76, 78, 80, 32, 33, 3, 7, 36, 4, 44, 38, 5, 40, 41, 6, 8, 28, 1, 0, 54, 56, 46, 47, 48, 9, 50, 10, 11, 53, 60, 61, 13, 14, 58, 59, 72, 17, 62, 18, 19, 65, 20, 21, 68, 22, 23, 71, 24, 25, 75, 26, 77, 27, 79, 29, 2, 30] in wght=100.

- Contour order differs in glyph 'five': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43] in wght=400, [30, 19, 21, 23, 25, 33, 28, 7, 35, 31, 10, 14, 43, 13, 38, 40, 42, 17, 11, 6, 20, 2, 22, 3, 24, 4, 26, 34, 9, 29, 37, 12, 32, 0, 8, 1, 36, 15, 39, 16, 41, 5, 27, 18] in wght=100.

- 112 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: interpolation-issues]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts include an avar table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#mandatory-avar-table">mandatory_avar_table</a></summary>
    <div>


> 
> Most variable fonts should include an avar table to correctly define
> axes progression rates.
> 
> For example, a weight axis from 0% to 100% doesn't map directly to 100 to 1000,
> because a 10% progression from 0% may be too much to define the 200,
> while 90% may be too little to define the 900.
> 
> If the progression rates of axes is linear, this check can be ignored.
> Fontmake will also skip adding an avar table if the progression rates
> are linear. However, it is still recommended that designers visually proof
> each instance is at the expected weight, width etc.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3100





* ⚠️ **WARN** <p>This variable font does not have an avar table. Most variable fonts should include an avar table to correctly define axes progression rates.</p>
 [code: missing-avar]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>


> 
> It is a common practice to have math signs sharing the same width
> (preferably the same width as tabular figures accross the entire font family).
> 
> This probably comes from the will to avoid additional tabular math signs
> knowing that their design can easily share the same width.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3832





* ⚠️ **WARN** <p>The most common width is 600 among a set of 5 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 500:
less, equal, greater</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>


> 
> Some rasterizers encounter difficulties when rendering glyphs with
> overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points.
> When two segments share the same coordinates, they are considered
> overlapping.
> 




> Original proposal: https://github.com/google/fonts/issues/7594#issuecomment-2401909084





* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* A (U+0041): L&lt;&lt;150.0,100.0&gt;--&lt;50.0,100.0&gt;&gt; has the same coordinates as a previous segment.

* A (U+0041): L&lt;&lt;150.0,200.0&gt;--&lt;50.0,200.0&gt;&gt; has the same coordinates as a previous segment.

* A (U+0041): L&lt;&lt;150.0,300.0&gt;--&lt;50.0,300.0&gt;&gt; has the same coordinates as a previous segment.

* A (U+0041): L&lt;&lt;150.0,400.0&gt;--&lt;50.0,400.0&gt;&gt; has the same coordinates as a previous segment.

* A (U+0041): L&lt;&lt;150.0,500.0&gt;--&lt;50.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* A (U+0041): L&lt;&lt;150.0,600.0&gt;--&lt;50.0,600.0&gt;&gt; has the same coordinates as a previous segment.

* A (U+0041): L&lt;&lt;150.0,300.0&gt;--&lt;150.0,400.0&gt;&gt; has the same coordinates as a previous segment.

* A (U+0041): L&lt;&lt;250.0,300.0&gt;--&lt;250.0,400.0&gt;&gt; has the same coordinates as a previous segment.

* A (U+0041): L&lt;&lt;250.0,700.0&gt;--&lt;250.0,800.0&gt;&gt; has the same coordinates as a previous segment.

* A (U+0041): L&lt;&lt;350.0,300.0&gt;--&lt;350.0,400.0&gt;&gt; has the same coordinates as a previous segment.

* 6681 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 10 | 43 | 6 | 183 | 0 | 
| 0% | 0% | 0% | 4% | 18% | 2% | 76% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
