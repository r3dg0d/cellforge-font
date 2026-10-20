## FontBakery report

fontbakery version: 1.1.0







## Check results



<details><summary>[6] PixelForge-Italic[wght].ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>


> 
> We need to check names are not already used, and today the best place to check
> that is http://namecheck.fontdata.com
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/494





* 💥 **ERROR** <p>Failed with KeyError: 'data'</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/fontdata_namecheck.py&quot;, line 24, in check_fontdata_namecheck
    if data[&quot;data&quot;][&quot;confidence&quot;][&quot;1.0&quot;] &gt; 0:
       ~~~~^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

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
<pre><code>- Contour order differs in glyph 'B': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62] in wght=400, [42, 28, 31, 40, 33, 35, 37, 38, 46, 15, 13, 51, 48, 16, 52, 50, 61, 53, 55, 20, 58, 60, 45, 14, 3, 29, 30, 4, 9, 32, 12, 43, 5, 34, 6, 36, 7, 10, 41, 47, 57, 44, 17, 49, 62, 0, 25, 8, 26, 2, 1, 18, 54, 19, 56, 23, 22, 27, 59, 21, 24, 11, 39] in wght=100.

- Contour order differs in glyph 'slash': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25] in wght=400, [16, 18, 19, 20, 22, 23, 24, 25, 17, 4, 11, 12, 13, 15, 8, 9, 5, 21, 2, 1, 0, 14, 10, 3, 6, 7] in wght=100.

- Contour order differs in glyph 'Ocircumflex': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66] in wght=400, [28, 30, 32, 34, 36, 38, 40, 10, 11, 44, 45, 14, 47, 13, 17, 15, 52, 54, 56, 58, 60, 62, 64, 66, 16, 41, 29, 2, 31, 3, 33, 4, 35, 5, 37, 6, 39, 9, 7, 42, 43, 46, 12, 1, 0, 25, 48, 51, 53, 50, 26, 8, 27, 18, 55, 19, 57, 20, 59, 21, 61, 22, 63, 23, 65, 49, 24] in wght=100.

- Contour order differs in glyph 'atilde': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60] in wght=400, [33, 31, 34, 32, 8, 39, 35, 37, 38, 42, 40, 46, 47, 17, 14, 16, 50, 52, 54, 43, 59, 44, 49, 23, 9, 29, 30, 3, 10, 6, 4, 7, 36, 13, 11, 12, 24, 25, 1, 51, 41, 45, 53, 58, 48, 0, 27, 5, 28, 26, 2, 18, 19, 55, 56, 20, 57, 21, 60, 15, 22] in wght=100.

- Contour order differs in glyph 'percent': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45] in wght=400, [37, 30, 22, 23, 8, 28, 29, 33, 40, 35, 31, 41, 12, 39, 44, 45, 27, 7, 9, 20, 1, 21, 2, 3, 24, 25, 16, 19, 5, 6, 34, 11, 4, 36, 0, 42, 10, 38, 32, 17, 18, 26, 43, 13, 14, 15] in wght=100.

- Contour order differs in glyph 'greater': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24] in wght=400, [7, 15, 9, 13, 12, 19, 18, 0, 8, 2, 10, 11, 4, 3, 14, 1, 16, 17, 22, 5, 20, 21, 6, 23, 24] in wght=100.

- Contour order differs in glyph 'greater': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24] in wght=300, [7, 1, 11, 20, 15, 21, 0, 8, 9, 10, 12, 13, 14, 16, 5, 3, 17, 18, 23, 19, 24, 6, 22, 2, 4] in wght=500.

- Contour order differs in glyph 'Atilde': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68] in wght=400, [54, 45, 33, 35, 38, 41, 42, 13, 43, 44, 47, 49, 50, 62, 52, 53, 55, 57, 59, 63, 66, 67, 51, 23, 56, 10, 40, 4, 34, 5, 37, 36, 6, 39, 8, 11, 9, 0, 25, 1, 46, 12, 27, 28, 3, 61, 48, 64, 32, 24, 16, 2, 31, 26, 17, 18, 58, 19, 60, 20, 21, 65, 22, 14, 68, 15, 7, 30, 29] in wght=100.

- Contour order differs in glyph 'ocircumflex': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54] in wght=400, [24, 26, 28, 30, 32, 8, 9, 36, 37, 12, 39, 11, 15, 13, 44, 46, 48, 50, 52, 54, 14, 33, 25, 2, 27, 3, 29, 4, 31, 7, 5, 34, 35, 38, 10, 1, 0, 23, 40, 43, 45, 42, 21, 22, 6, 16, 47, 17, 49, 18, 51, 19, 53, 41, 20] in wght=100.

- Contour order differs in glyph 'W': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57] in wght=400, [35, 36, 25, 27, 28, 31, 33, 34, 41, 42, 39, 11, 44, 45, 47, 49, 52, 54, 56, 57, 8, 24, 9, 2, 37, 26, 38, 3, 4, 29, 30, 5, 32, 6, 7, 0, 20, 1, 43, 10, 40, 21, 23, 22, 12, 13, 46, 14, 48, 15, 50, 51, 16, 53, 17, 55, 18, 19] in wght=100.

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
equal, greater, less</p>
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

<details><summary>[6] PixelForge[wght].ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>


> 
> We need to check names are not already used, and today the best place to check
> that is http://namecheck.fontdata.com
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/494





* 💥 **ERROR** <p>Failed with KeyError: 'data'</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/fontdata_namecheck.py&quot;, line 24, in check_fontdata_namecheck
    if data[&quot;data&quot;][&quot;confidence&quot;][&quot;1.0&quot;] &gt; 0:
       ~~~~^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

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
<pre><code>- Contour order differs in glyph 'B': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62] in wght=400, [42, 29, 31, 40, 33, 35, 37, 38, 46, 15, 13, 52, 49, 16, 17, 20, 61, 53, 55, 56, 58, 60, 45, 14, 28, 3, 30, 4, 9, 12, 32, 43, 5, 34, 6, 36, 7, 10, 41, 47, 57, 44, 51, 50, 62, 0, 27, 11, 8, 1, 26, 18, 54, 19, 48, 22, 23, 25, 59, 21, 24, 2, 39] in wght=100.

- Contour order differs in glyph 'slash': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25] in wght=400, [16, 18, 19, 21, 22, 23, 24, 25, 17, 4, 13, 9, 1, 11, 14, 10, 5, 20, 2, 8, 12, 0, 15, 3, 6, 7] in wght=100.

- Contour order differs in glyph 'Ocircumflex': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66] in wght=400, [25, 30, 32, 34, 36, 38, 40, 10, 11, 44, 45, 14, 51, 13, 54, 50, 52, 17, 56, 58, 60, 62, 64, 66, 49, 41, 29, 2, 31, 3, 33, 4, 35, 5, 37, 6, 39, 42, 7, 9, 43, 46, 12, 0, 26, 28, 48, 47, 53, 16, 1, 8, 27, 18, 55, 19, 57, 20, 59, 21, 61, 22, 63, 23, 65, 24, 15] in wght=100.

- Contour order differs in glyph 'atilde': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60] in wght=400, [33, 31, 34, 32, 8, 39, 35, 37, 38, 42, 41, 46, 47, 17, 14, 16, 50, 51, 54, 43, 59, 44, 49, 23, 9, 29, 30, 10, 3, 6, 4, 7, 36, 13, 11, 12, 0, 26, 25, 53, 40, 45, 52, 58, 48, 5, 1, 27, 24, 28, 2, 18, 19, 55, 56, 20, 57, 21, 60, 15, 22] in wght=100.

- Contour order differs in glyph 'percent': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45] in wght=400, [30, 31, 22, 23, 33, 28, 29, 39, 40, 36, 32, 41, 42, 43, 44, 45, 7, 8, 0, 17, 1, 21, 2, 3, 24, 19, 20, 26, 5, 6, 11, 34, 9, 16, 4, 35, 37, 10, 38, 25, 18, 27, 12, 13, 14, 15] in wght=100.

- Contour order differs in glyph 'greater': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24] in wght=400, [7, 15, 9, 13, 12, 19, 18, 0, 8, 2, 10, 11, 4, 3, 14, 1, 16, 17, 22, 5, 20, 21, 6, 23, 24] in wght=100.

- Contour order differs in glyph 'Atilde': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68] in wght=400, [55, 45, 33, 35, 38, 41, 42, 46, 43, 44, 66, 49, 50, 20, 52, 53, 54, 57, 59, 63, 65, 67, 51, 23, 40, 10, 13, 4, 34, 5, 37, 36, 6, 39, 11, 8, 9, 25, 31, 0, 47, 12, 1, 28, 29, 62, 48, 61, 3, 24, 16, 7, 27, 2, 17, 56, 18, 58, 19, 60, 21, 64, 22, 68, 14, 15, 30, 26, 32] in wght=100.

- Contour order differs in glyph 'ocircumflex': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54] in wght=400, [21, 26, 28, 30, 34, 8, 9, 36, 37, 12, 39, 11, 15, 42, 44, 45, 48, 50, 52, 54, 41, 33, 25, 2, 27, 3, 29, 4, 31, 7, 5, 32, 35, 38, 10, 0, 22, 23, 40, 43, 46, 14, 6, 1, 24, 16, 47, 17, 49, 18, 51, 19, 53, 13, 20] in wght=100.

- Contour order differs in glyph 'W': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57] in wght=400, [35, 36, 25, 26, 28, 30, 32, 34, 41, 42, 39, 11, 44, 46, 47, 49, 51, 54, 55, 57, 8, 24, 9, 2, 37, 38, 3, 27, 4, 29, 5, 31, 6, 33, 7, 20, 0, 1, 43, 10, 40, 23, 21, 22, 12, 45, 13, 14, 48, 15, 50, 16, 52, 53, 17, 18, 56, 19] in wght=100.

- Contour order differs in glyph 'acute': [0, 1, 2, 3, 4] in wght=400, [2, 4, 0, 3, 1] in wght=100.

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
equal, greater, less</p>
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
| 2 | 0 | 0 | 10 | 43 | 6 | 181 | 0 | 
| 1% | 0% | 0% | 4% | 18% | 2% | 75% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
