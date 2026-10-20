# Using PixelForge in terminals and editors

Install it first (see README). Font family name: **`PixelForge`**. Variable family: **`PixelForge`** (fontconfig exposes the named instances).
Because PixelForge is proportional, use it for UI and headings. Terminals expect a monospace font, so pick DotZero or NullType for terminal text.

## kitty (`~/.config/kitty/kitty.conf`)
```conf
font_family      family="PixelForge"
bold_font        auto
italic_font      auto
bold_italic_font auto
font_size        13.0
# font_features PixelForge-Regular +zero
```
## Alacritty (`~/.config/alacritty/alacritty.toml`, 0.13+ TOML)
```toml
[font]
size = 13.0
normal = { family = "PixelForge", style = "Regular" }
bold = { family = "PixelForge", style = "Bold" }
italic = { family = "PixelForge", style = "Italic" }
bold_italic = { family = "PixelForge", style = "Bold Italic" }
```
## foot (`~/.config/foot/foot.ini`)
```ini
[main]
font=PixelForge:size=12
```
## WezTerm (`~/.wezterm.lua`)
```lua
local wezterm = require 'wezterm'
return {
  font = wezterm.font('PixelForge', { weight = 'Regular' }),
  harfbuzz_features = { "zero=0" },
  font_size = 13.0,
}
```
## Ghostty (`~/.config/ghostty/config`)
```ini
font-family = PixelForge
font-size = 13
font-feature = +zero
```
## GNOME Terminal / Ptyxis
```sh
gsettings set org.gnome.desktop.interface monospace-font-name 'PixelForge 12'
```
## VS Code (`settings.json`)
```json
{
  "editor.fontFamily": "'PixelForge', monospace",
  "editor.fontLigatures": false,
  "terminal.integrated.fontFamily": "'PixelForge'"
}
```
## Neovim GUIs (Neovide etc.)
```lua
vim.o.guifont = "PixelForge:h13"
```
## Emacs
```elisp
(set-face-attribute 'default nil :family "PixelForge" :height 130)
```
## Powerline / Starship
U+E0A0–E0A2 and U+E0B0–E0B3 are included natively. No patching is needed for classic Powerline separators. Full Nerd Font icon sets are **not** included.
