# Using Cellforge in terminals and editors

Install it first (see README). Font family name: **`Cellforge`**. Variable family: **`Cellforge`** (fontconfig exposes the named instances).
Because Cellforge is proportional, use it for UI and headings. Terminals expect a monospace font, so pick Zerodot or NullType for terminal text.

## kitty (`~/.config/kitty/kitty.conf`)
```conf
font_family      family="Cellforge"
bold_font        auto
italic_font      auto
bold_italic_font auto
font_size        13.0
# font_features Cellforge-Regular +zero
```
## Alacritty (`~/.config/alacritty/alacritty.toml`, 0.13+ TOML)
```toml
[font]
size = 13.0
normal = { family = "Cellforge", style = "Regular" }
bold = { family = "Cellforge", style = "Bold" }
italic = { family = "Cellforge", style = "Italic" }
bold_italic = { family = "Cellforge", style = "Bold Italic" }
```
## foot (`~/.config/foot/foot.ini`)
```ini
[main]
font=Cellforge:size=12
```
## WezTerm (`~/.wezterm.lua`)
```lua
local wezterm = require 'wezterm'
return {
  font = wezterm.font('Cellforge', { weight = 'Regular' }),
  harfbuzz_features = { "zero=0" },
  font_size = 13.0,
}
```
## Ghostty (`~/.config/ghostty/config`)
```ini
font-family = Cellforge
font-size = 13
font-feature = +zero
```
## GNOME Terminal / Ptyxis
```sh
gsettings set org.gnome.desktop.interface monospace-font-name 'Cellforge 12'
```
## VS Code (`settings.json`)
```json
{
  "editor.fontFamily": "'Cellforge', monospace",
  "editor.fontLigatures": false,
  "terminal.integrated.fontFamily": "'Cellforge'"
}
```
## Neovim GUIs (Neovide etc.)
```lua
vim.o.guifont = "Cellforge:h13"
```
## Emacs
```elisp
(set-face-attribute 'default nil :family "Cellforge" :height 130)
```
## Powerline / Starship
U+E0A0–E0A2 and U+E0B0–E0B3 are included natively. No patching is needed for classic Powerline separators. Full Nerd Font icon sets are **not** included.
