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


def generate_colors(accent_color):
    color_palette = {
        "black-d": "#282C34",
        "black-l": "#5A6374",
        "blue": "#61AFEF",
        "cyan": "#56B6C2",
        "green": "#98C379",
        "yellow": "#E5C07B",
        "orange": "#E29678",
        "red": "#E06C75",
        "purple": "#C678DD",
        "white-d": "#DCDFE4",
        "white-l": "#FFFFFF",
    }

    color_list = ["yellow", "purple", "blue", "orange", "green", "red"]

    background = color_palette["black-d"]
    background_ = color_palette["black-l"]
    foreground = color_palette["white-d"]
    foreground_ = color_palette["white-l"]
    accent = color_palette[accent_color]
    error = color_palette["red"]
    warning = color_palette["yellow"]

    colors = f"""
    "activityBar.background": "{background}",
    "activityBar.activeBorder": "{accent}",
    "activityBar.border": "{background_}",
    "activityBar.activeBackground": "{background_}",
    "activityBar.foreground": "{foreground}",
    "activityBarBadge.background": "{accent}",
    "activityBarBadge.foreground": "{background}",
    "button.foreground": "{background}",
    "button.background": "{mix(accent,.7,background_)}",
    "button.hoverBackground": "{mix(accent,.9,background_)}",
    "editor.background": "{background}",
    "editor.foreground": "{foreground}",
    "editor.selectionBackground": "{mix(accent,.3)}",
    "editor.lineHighlightBackground": "{mix(accent,.1)}",
    "editorCursor.foreground": "{foreground}",
    "editorLineNumber.foreground": "{mix(accent,.7)}",
    "editorLineNumber.activeForeground": "{accent}",
    "editorBracketMatch.background": "{mix(accent,.25)}",
    "editorBracketMatch.border": "{mix(accent,.25)}",
    "editorLink.activeForeground": "{accent}",
    "editorError.foreground": "{error}",
    "editorWarning.foreground": "{warning}",
    "focusBorder": "{accent}",
    "menu.background": "{background}",
    "menu.foreground": "{foreground}",
    "menu.border":"{mix(accent,.2,background)}",
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
    "textLink.foreground": "{mix(accent,.6,foreground)}",
    "textLink.activeForeground": "{accent}",
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
    "titleBar.border": "{background}",
    "editorBracketHighlight.foreground1": "{color_palette[color_list[0]]}",
    "editorBracketHighlight.foreground2": "{color_palette[color_list[1]]}",
    "editorBracketHighlight.foreground3": "{color_palette[color_list[2]]}",
    "editorBracketHighlight.foreground4": "{color_palette[color_list[3]]}",
    "editorBracketHighlight.foreground5": "{color_palette[color_list[4]]}",
    "editorBracketHighlight.foreground6": "{color_palette[color_list[5]]}",
    "diffEditor.insertedTextBackground": "{mix(color_palette['green'],.15)}",
    "diffEditor.removedTextBackground": "{mix(color_palette['red'],.15)}",
    "editorGutter.addedBackground": "{color_palette['green']}",
    "editorGutter.deletedBackground": "{color_palette['red']}",
    "editorGutter.modifiedBackground": "{color_palette['blue']}",
    "diffEditor.insertedLineBackground": "{mix(color_palette['green'],.1)}",
    "diffEditor.removedLineBackground": "{mix(color_palette['green'],.1)}",
    "quickInput.background": "{background}",
    "quickInput.foreground": "{foreground}",
    "quickInput.border": "{mix(accent,.1,background)}",
    "quickInputList.focusBackground": "{mix(accent,.2,background)}",
    "quickInputList.focusForeground": "{foreground}",
"""

    tokenColors = f"""
    {{ "scope": "comment", "settings": {{ "foreground": "{background_}" }} }},
    {{ "scope": "string", "settings": {{ "foreground": "{color_palette['red']}" }} }},
    {{ "scope": "constant.numeric", "settings": {{ "foreground": "{color_palette['purple']}" }} }},
    {{ "scope": "keyword", "settings": {{ "foreground": "{color_palette['blue']}" }} }},
    {{ "scope": "entity.name.function", "settings": {{ "foreground": "{color_palette['green']}" }} }},
    {{ "scope": "storage.type", "settings": {{ "foreground": "{color_palette['yellow']}" }} }},
    {{ "scope": "variable", "settings": {{ "foreground": "{color_palette['cyan']}" }} }}
"""

    settings = f"""{{
    "workbench.colorCustomizations": {{{colors}  }},
    "editor.tokenColorCustomizations": {{
        "textMateRules": [{tokenColors}    ]
    }}
    }}
"""

    themes = f"""{{
  "colors": {{{colors}  }},
  "tokenColors": [{tokenColors}  ]
}}
"""

    return (settings, themes)


accent_colors = [
    ("black-l", "Black"),
    ("blue", "Blue"),
    ("cyan", "Cyan"),
    ("green", "Green"),
    ("yellow", "Yellow"),
    ("red", "Red"),
    ("orange", "Orange"),
    ("purple", "Purple"),
]

# (settings, themes) = generate_colors("green")
# with open("./.vscode/settings.json", "w") as o:
#     o.write(settings)

for theme_name, file_name in accent_colors:
    (settings, themes) = generate_colors(theme_name)
    with open(f"./colorthemes/OneHalfDark/{file_name}.json", "w") as o:
        o.write(themes)
