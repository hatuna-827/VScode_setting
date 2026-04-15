def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def mix(color, rate, base=""):
    if base == "":
        return color + ("0" + hex(int(0xFF * rate))[2:])[-2:]
    else:
        base_rgb = hex_to_rgb(base)
        color_rgb = hex_to_rgb(color)
        mixed = tuple(
            int(b * (1 - rate) + c * rate) for b, c in zip(base_rgb, color_rgb)
        )
        return rgb_to_hex(mixed)


color_palette = {
    "black-d": "#282C34",
    "black-l": "#5A6374",
    "red": "#E06C75",
    "green": "#98C379",
    "yellow": "#E5C07B",
    "blue": "#61AFEF",
    "purple": "#C678DD",
    "cyan": "#56B6C2",
    "white-d": "#DCDFE4",
    "white-l": "#FFFFFF",
}

background = color_palette["black-d"]
background_ = color_palette["black-l"]
foreground = color_palette["white-d"]
foreground_ = color_palette["white-l"]
accent = color_palette["red"]
error = color_palette["red"]
warning = color_palette["yellow"]

settings = f"""{{
  //"workbench.colorTheme": "Visual Studio Light",
  "workbench.colorCustomizations": {{
    "activityBar.background": "{background}",
    "activityBar.activeBorder": "{accent}",
    "activityBar.border": "{background_}",
    "activityBar.activeBackground": "{background_}",
    "activityBar.foreground": "{foreground}",
    "activityBarBadge.background": "{accent}",
    "activityBarBadge.foreground": "{background}",
    "button.foreground": "{background}",
    "button.background": "{accent}",
    "button.hoverBackground": "{foreground}",
    "editor.background": "{background}",
    "editor.foreground": "{foreground}",
    "editor.selectionBackground": "{mix(accent,.3)}",
    "editor.lineHighlightBackground": "{mix(accent,.1)}",
    "editorCursor.foreground": "{foreground}",
    "editorLineNumber.foreground": "{mix(accent,.7)}",
    "editorLineNumber.activeForeground": "{accent}",
    "editorBracketMatch.background": "{mix(accent,.25)}",
    "editorBracketMatch.border": "{mix(accent,.25)}",
    "editorError.foreground": "{error}",
    "editorWarning.foreground": "{warning}",
    "focusBorder": "{accent}",
    "menu.background": "{background}",
    "menu.foreground": "{foreground}",
    "menu.border":"{foreground}",
    "menu.selectionBackground": "{accent}",
    "menu.selectionForeground": "{foreground}",
    "menu.separatorBackground": "{foreground}",
    "panel.background": "{background}",
    "panelTitle.activeBorder": "{accent}",
    "statusBar.noFolderBackground": "{accent}",
    "statusBar.foreground": "{foreground_}",
    "statusBarItem.hoverForeground": "{foreground_}",
    "statusBar.background": "{accent}",
    "statusBarItem.remoteBackground": "{accent}",
    "statusBarItem.remoteForeground": "{foreground_}",
    "statusBar.border": "{accent}",
    "sideBarTitle.background": "{mix(accent,.25)}",
    "sideBarSectionHeader.background": "{mix(accent,.25)}",
    "sideBar.background": "{background}",
    "sideBar.foreground": "{foreground}",
    "sideBar.dropBackground": "{mix(accent,.4)}",
    "scrollbarSlider.activeBackground": "{accent}",
    "scrollbarSlider.hoverBackground": "{accent}",
    "scrollbarSlider.background": "{mix(accent,.5)}",
    "tab.activeBackground": "{mix(accent,.5)}",
    "tab.activeForeground": "{foreground_}",
    "tab.activeBorderTop": "{mix(accent,.5)}",
    "tab.inactiveBackground": "{mix(accent,.3)}",
    "tab.inactiveForeground": "{foreground}",
    "tab.hoverBackground": "{mix(accent,.5)}",
    "tab.border": "{background}",
    "tab.unfocusedActiveBackground": "{mix(accent,.2)}",
    "tab.unfocusedInactiveBackground": "{mix(accent,.1)}",
    "tab.unfocusedHoverBackground": "{mix(accent,.3)}",
    "editorGroupHeader.tabsBackground": "{background}",
    "terminal.background": "{background}",
    "terminal.foreground": "{foreground}",
    "terminalCommandDecoration.defaultBackground": "{accent}",
    "terminalCommandDecoration.errorBackground": "{color_palette['red']}",
    "terminalCommandDecoration.successBackground": "{color_palette['green']}",
    "terminalCommandGuide.foreground": "{accent}",
    "terminalCursor.foreground": "{accent}",
    "progressBar.background": "{accent}",
    "titleBar.activeBackground": "{background}",
    "titleBar.border": "{background}"
  }},
  "editor.tokenColorCustomizations": {{
    "comments": "{background_}",
    "strings": "{color_palette['red']}",
    "numbers": "{color_palette['purple']}",
    "keywords": "{color_palette['blue']}",
    "functions": "{color_palette['green']}",
    "types": "{color_palette['yellow']}",
    "variables": "{color_palette['cyan']}"
  }}
}}
"""

with open("./.vscode/settings.json", "w") as o:
    o.write(settings)
