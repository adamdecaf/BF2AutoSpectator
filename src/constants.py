APP_NAME = 'bf2-auto-spectator'
APP_VERSION = '0.3.1'
BF2_EXE = 'BF2.exe'
BF2_WINDOW_TITLE = 'BF2 (v1.5.3153-802.0, pid:'
TESSERACT_EXE = 'tesseract.exe'
HISTCMP_MAX_DELTA = 0.2
PLAYER_ROTATION_PAUSE_DURATION = 5
COORDINATES = {
    '720p': {
        # format for click coordinates: tuple(x coordinate, y coordinate)
        # legacy mouse moves use relative offsets instead of absolute coordinates, but are stored the same way
        'clicks': {
            'bfhq-menu-item': (111, 50),
            'multiplayer-menu-item': (331, 50),
            'quit-menu-item': (1182, 50),
            'connect-to-ip-button': (111, 452),
            'connect-to-ip-ok-button': (777, 362),
            'disconnect-button': (1210, 725),
            'game-message-close-button': (806, 412),
            'join-game-button': (1210, 725),
            'spawnpoint-deselect': (250, 50),
            'suicide-button': (469, 459)
        },
        # format for ocr coordinates: tuple(x coordinate, y coordinate, width, height)
        'ocr': {
            'quit-menu-item': (1160, 42, 45, 20),
            'game-message-header': (400, 223, 130, 25),
            'game-message-text': (400, 245, 470, 18),
            'connect-to-ip-button': (50, 448, 110, 18),
            'disconnect-button': (1133, 725, 92, 16),
            'eor-header-items': (72, 82, 740, 20),
            'join-game-button': (1163, 725, 80, 16),
            'map-briefing-header': (24, 112, 115, 20),
            'special-forces-class-label': (60, 125, 140, 18),
            'eor-map-name': (769, 114, 210, 17),
            'eor-map-size': (1256, 570, 20, 17),
            'suicide-button': (940, 678, 75, 19)
        },
        'hists': {
            'teams': [(68, 69, 41, 13), (209, 69, 41, 13)]
        }
    },
    '900p': {
        # format for click coordinates: tuple(x coordinate, y coordinate)
        # legacy mouse moves use relative offsets instead of absolute coordinates, but are stored the same way
        'clicks': {
            'bfhq-menu-item': (138, 52),
            'multiplayer-menu-item': (410, 52),
            'quit-menu-item': (1468, 52),
            'connect-to-ip-button': (122, 558),
            'connect-to-ip-ok-button': (958, 440),
            'disconnect-button': (1468, 906),
            'game-message-close-button': (1002, 501),
            'join-game-button': (1468, 906),
            'spawnpoint-deselect': (250, 50),
            'suicide-button': (497, 455)
        },
        # format for ocr coordinates: tuple(x coordinate, y coordinate, width, height)
        'ocr': {
            'quit-menu-item': (1449, 47, 47, 22),
            'game-message-header': (500, 274, 152, 25),
            'game-message-text': (500, 300, 520, 20),
            'connect-to-ip-button': (62, 551, 134, 22),
            'disconnect-button': (1418, 900, 108, 20),
            'eor-header-items': (88, 94, 924, 22),
            'join-game-button': (1450, 900, 98, 18),
            'map-briefing-header': (26, 133, 141, 22),
            'special-forces-class-label': (73, 149, 164, 20),
            'eor-map-name': (956, 134, 250, 21),
            'eor-map-size': (1564, 706, 24, 18),
            'suicide-button': (1173, 841, 88, 20)
        },
        'hists': {
            'teams': [(81, 77, 60, 18), (257, 77, 60, 18)]
        }
    },
    # format for spawn coordinates: list(team 0 tuple, team 1 tuple) with tuple(x offset, y offset)
    'spawns': {
        'dalian-plant': {
            '16': [(361, 237), (400, 325)],
            '32': [(618, 218), (292, 296)],
            '64': [(618, 218), (296, 296)]
        },
        'strike-at-karkand': {
            '16': [(490, 390), (463, 98)],
            '32': [(444, 397), (529, 96)],
            '64': [(382, 390), (569, 160)]
        },
        'dragon-valley': {
            '16': [(333, 154), (530, 308)],
            '32': [(487, 98), (497, 358)],
            '64': [(517, 56), (476, 363)]
        },
        'fushe-pass': {
            '16': [(565, 201), (380, 272)],
            '32': [(537, 309), (322, 189)],
            '64': [(562, 132), (253, 312)]
        },
        'daqing-oilfields': {
            '16': [(397, 324), (474, 106)],
            '32': [(504, 353), (363, 138)],
            '64': [(500, 346), (363, 137)]
        },
        'gulf-of-oman': {
            '16': [(416, 355), (434, 122)],
            '32': [(313, 302), (606, 94)],
            '64': [(308, 326), (581, 132)]
        },
        'road-to-jalalabad': {
            '16': [(382, 315), (487, 133)],
            '32': [(313, 163), (566, 158)],
            '64': [(314, 159), (569, 156)]
        },
        'wake-island-2007': {
            '64': [(359, 158), (524, 290)]
        },
        'zatar-wetlands': {
            '16': [(304, 251), (559, 277)],
            '32': [(271, 199), (594, 316)],
            '64': [(372, 44), (604, 336)]
        },
        'sharqi-peninsula': {
            '16': [(495, 209), (360, 284)],
            '32': [(475, 222), (321, 130)],
            '64': [(476, 220), (321, 128)]
        },
        'kubra-dam': {
            '16': [(555, 240), (391, 145)],
            '32': [(491, 140), (336, 330)],
            '64': [(494, 137), (336, 330)]
        },
        'operation-clean-sweep': {
            '16': [(392, 113), (525, 361)],
            '32': [(373, 120), (549, 332)],
            '64': [(326, 120), (579, 249)]
        },
        'mashtuur-city': {
            '16': [(503, 316), (406, 155)],
            '32': [(560, 319), (328, 89)],
            '64': [(563, 319), (328, 89)]
        },
        'midnight-sun': {
            '16': [(551, 196), (344, 259)],
            '32': [(591, 207), (293, 274)],
            '64': [(590, 207), (317, 287)]
        },
        'operation-road-rage': {
            '16': [(566, 158), (332, 311)],
            '32': [(419, 32), (457, 409)],
            '64': [(419, 32), (458, 407)]
        },
        'taraba-quarry': {
            '16': [(567, 355), (357, 85)],
            '32': [(569, 346), (310, 379)]
        },
        'great-wall': {
            '16': [(312, 186), (544, 199)],
            '32': [(529, 122), (368, 360)]
        },
        'highway-tampa': {
            '16': [(579, 312), (330, 380)],
            '32': [(612, 246), (426, 54)],
            '64': [(612, 246), (428, 52)]
        },
        'operation-blue-pearl': {
            '16': [(586, 317), (309, 169)],
            '32': [(602, 257), (270, 208)],
            '64': [(588, 268), (280, 154)]
        },
        'songhua-stalemate': {
            '16': [(529, 252), (345, 248)],
            '32': [(561, 247), (305, 234)],
            '64': [(565, 244), (306, 234)]
        },
        'operation-harvest': {
            '16': [(314, 342), (585, 124)],
            '32': [(315, 389), (506, 93)],
            '64': [(544, 393), (509, 93)]
        },
        'operation-smoke-screen': {
            '16': [(398, 88), (506, 358)],
            '32': [(434, 98), (466, 383)]
        }
    }
}
