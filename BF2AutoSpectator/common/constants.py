APP_NAME = 'BF2AutoSpectator'
APP_VERSION = '0.6.9'
BF2_EXE = 'BF2.exe'
BF2_WINDOW_TITLE = 'BF2 (v1.5.3153-802.0, pid:'
TESSERACT_EXE = 'tesseract.exe'
WINDOW_TITLE_BAR_HEIGHT = 31
WINDOW_SHADOW_SIZE = 8
HISTCMP_MAX_DELTA = 0.2
DEFAULT_CAMERA_VIEW_HISTCMP_MAX_DELTA = 0.175
PLAYER_ROTATION_PAUSE_DURATION = 5
TEAMS_SPAWN_MENU_LEFT = ['usmc', 'eu', 'navy-seal', 'sas', 'rebels-left', 'spetsnaz-left', 'peglegs', 'canada-left',
                         'russia-left']
TEAMS_SPAWN_MENU_RIGHT = ['china', 'mec', 'mec-sf', 'insurgent', 'rebels-right', 'spetsnaz-right', 'undead',
                          'russia-right', 'canada-right']
COORDINATES = {
    '720p': {
        # format for click coordinates: tuple(x coordinate, y coordinate)
        # legacy mouse moves use relative offsets instead of absolute coordinates, but are stored the same way
        'clicks': {
            'bfhq-menu-item': (111, 50),
            'multiplayer-menu-item': (331, 50),
            'join-internet-menu-item': (111, 85),
            'quit-menu-item': (1182, 50),
            'connect-to-ip-button': (111, 452),
            'connect-to-ip-ok-button': (777, 362),
            'disconnect-prompt-yes-button': (706, 394),
            'disconnect-button': (1210, 725),
            'game-message-close-button': (806, 412),
            'join-game-button': (1210, 725),
            'spawnpoint-deselect': (250, 50),
            'suicide-button': (469, 459)
        },
        # format for ocr coordinates: tuple(x coordinate, y coordinate, width, height)
        'ocr': {
            'quit-menu-item': [(1152, 11, 83, 689)],
            'game-message-header': [(392, 192, 758, 503)],
            'game-message-text': [(392, 214, 418, 488)],
            'connect-to-ip-button': [(42, 417, 1128, 285)],
            'disconnect-prompt-header': [(329, 227, 841, 475)],
            'disconnect-button': [(1125, 694, 63, 10)],
            'play-now-button': [(1087, 695, 101, 7)],
            'join-game-button': [(1155, 694, 45, 10)],
            'map-briefing-header': [(16, 81, 1149, 619)],
            'special-forces-class-label': [(52, 94, 1088, 608)],
            'spawn-selected-text': [(520, 4, 568, 700)],
            'suicide-button': [(932, 647, 273, 54)],
            'console-command': [(1, 230, 1274, 480)],
            'eor-header-items': [(64, 51, 1125, 649), (271, 51, 906, 649), (486, 51, 697, 649), (688, 51, 476, 649)],
            'eor-map-details': [(761, 83, 309, 620), (1248, 539, 12, 164), (1197, 517, 13, 183)]
        },
        'hists': {
            'teams': [(60, 38, 1179, 669), (201, 38, 1038, 669)],
            'menu': {
                'multiplayer': (221, 3, 859, 716),
                'join-internet': (10, 42, 1071, 677)
            },
            'eor': {
                'score-list': (10, 42, 1071, 677),
                'top-players': (221, 42, 860, 677),
                'top-scores': (434, 42, 647, 677),
                'map-briefing': (646, 42, 435, 677)
            },
            'spawn-menu': {
                'close-button': (1232, 38, 23, 664)
            },
            'scoreboard': {
                'table-icons-left': (367, 89, 675, 607),
                'table-icons-right': (992, 89, 50, 607)
            }
        }
    },
    '900p': {
        # format for click coordinates: tuple(x coordinate, y coordinate)
        # legacy mouse moves use relative offsets instead of absolute coordinates, but are stored the same way
        'clicks': {
            'bfhq-menu-item': (138, 52),
            'multiplayer-menu-item': (410, 52),
            'join-internet-menu-item': (138, 97),
            'quit-menu-item': (1468, 52),
            'connect-to-ip-button': (122, 558),
            'connect-to-ip-ok-button': (958, 440),
            'disconnect-prompt-yes-button': (885, 487),
            'disconnect-button': (1468, 906),
            'game-message-close-button': (1002, 501),
            'join-game-button': (1468, 906),
            'spawnpoint-deselect': (250, 50),
            'suicide-button': (497, 455)
        },
        # format for ocr coordinates: tuple(x coordinate, y coordinate, width, height)
        'ocr': {
            'quit-menu-item': [(1441, 16, 112, 862)],
            'game-message-header': [(492, 243, 956, 632)],
            'game-message-text': [(492, 269, 588, 611)],
            'connect-to-ip-button': [(54, 520, 1412, 358)],
            'disconnect-prompt-header': [(412, 284, 1056, 591)],
            'disconnect-button': [(1410, 869, 82, 11)],
            'play-now-button': [(1347, 869, 123, 9)],
            'join-game-button': [(1442, 869, 60, 13)],
            'map-briefing-header': [(18, 102, 1441, 776)],
            'special-forces-class-label': [(65, 118, 1371, 762)],
            'spawn-selected-text': [(650, 5, 709, 877)],
            'suicide-button': [(1165, 810, 347, 70)],
            'console-command': [(1, 230, 1594, 660)],
            'eor-header-items': [(80, 63, 1406, 815), (339, 63, 1131, 815), (607, 63, 872, 815), (861, 63, 596, 815)],
            'eor-map-details': [(948, 103, 402, 776), (1556, 675, 20, 207), (1492, 648, 14, 230)]
        },
        'hists': {
            'teams': [(73, 46, 1467, 836), (249, 46, 1291, 836)],
            'menu': {
                'multiplayer': (277, 3, 1074, 896),
                'join-internet': (12, 53, 1339, 846)
            },
            'eor': {
                'score-list': (12, 53, 1339, 846),
                'top-players': (276, 53, 1075, 846),
                'top-scores': (542, 53, 809, 846),
                'map-briefing': (808, 53, 543, 846)
            },
            'spawn-menu': {
                'close-button': (1541, 47, 30, 830)
            },
            'scoreboard': {
                'table-icons-left': (457, 111, 845, 761),
                'table-icons-right': (1240, 111, 62, 761)
            }
        }
    },
    # format for spawn coordinates: list(team 0 tuple, team 1 tuple, alternate spawn tuple...)
    # with tuple(x offset, y offset)
    'spawns': {
        'dalian-plant': {
            '16': [(361, 237), (400, 325)],
            '32': [(618, 218), (292, 296)],
            '64': [(618, 218), (296, 296)]
        },
        'strike-at-karkand': {
            '16': [(490, 390), (463, 98)],
            '32': [(444, 397), (529, 96), (418, 237), (355, 131), (401, 186), (418, 139), (454, 102)],
            '64': [(382, 390), (569, 160), (356, 236), (339, 186), (294, 131), (393, 101), (466, 149), (468, 96), (521, 117)]
        },
        'dragon-valley': {
            '16': [(333, 154), (530, 308)],
            '32': [(487, 98), (497, 358), (438, 159), (360, 243), (439, 257), (392, 319)],
            '64': [(517, 56), (476, 363), (404, 55), (458, 118), (396, 137), (466, 177), (426, 160), (432, 225), (377, 283), (432, 294), (400, 337)]
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
            '32': [(313, 163), (566, 158), (403, 291), (461, 320), (498, 274), (564, 253), (536, 206)],
            '64': [(314, 159), (569, 156), (432, 198), (403, 291), (461, 320), (498, 274), (564, 253), (536, 206)]
        },
        'wake-island-2007': {
            '64': [(359, 158), (524, 290), (445, 194), (503, 192), (434, 274), (469, 297)]
        },
        'zatar-wetlands': {
            '16': [(304, 251), (559, 277)],
            '32': [(271, 199), (594, 316)],
            '64': [(372, 44), (604, 336)]
        },
        'sharqi-peninsula': {
            '16': [(495, 209), (360, 284)],
            '32': [(475, 222), (321, 130), (436, 225), (403, 222), (412, 255), (372, 203)],
            '64': [(476, 220), (321, 128), (436, 225), (403, 222), (422, 194), (412, 255), (372, 203)]
        },
        'kubra-dam': {
            '16': [(555, 240), (391, 145)],
            '32': [(491, 140), (336, 330), (426, 150), (339, 135), (383, 254), (376, 184), (332, 240), (304, 210)],
            '64': [(494, 137), (336, 330), (426, 150), (382, 93), (339, 135), (383, 254), (376, 184), (332, 240), (304, 210)]
        },
        'operation-clean-sweep': {
            '16': [(392, 113), (525, 361)],
            '32': [(373, 120), (549, 332), (379, 251), (426, 333), (489, 336), (528, 378)],
            '64': [(326, 120), (579, 249), (334, 241), (376, 316), (435, 320), (473, 360), (490, 310), (563, 289)]
        },
        'mashtuur-city': {
            '16': [(503, 316), (406, 155)],
            '32': [(560, 319), (328, 89), (481, 294), (452, 238), (328, 89), (560, 319), (393, 194), (356, 274)],
            '64': [(563, 319), (328, 89), (519, 220), (481, 294), (452, 238), (328, 89), (560, 319), (393, 194), (356, 274)]
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
            '32': [(602, 257), (270, 208), (445, 233), (404, 291), (383, 231), (333, 262), (297, 277)],
            '64': [(588, 268), (280, 154), (435, 258), (403, 316), (381, 256), (333, 287), (297, 302), (280, 247)]
        },
        'songhua-stalemate': {
            '16': [(529, 252), (345, 248)],
            '32': [(561, 247), (305, 234), (502, 247), (462, 305), (305, 234), (561, 247), (416, 219), (369, 242)],
            '64': [(561, 247), (305, 234), (502, 247), (530, 143), (458, 295), (305, 234), (561, 247), (402, 339), (416, 219), (369, 242)]
        },
        'operation-harvest': {
            '16': [(314, 342), (585, 124)],
            '32': [(315, 389), (506, 93)],
            '64': [(544, 393), (509, 93), (486, 333), (401, 272), (498, 232), (555, 196), (500, 164)]
        },
        'operation-smoke-screen': {
            '16': [(398, 88), (506, 358)],
            '32': [(434, 98), (466, 383)]
        },
        'warlord': {
            '16': [(385, 347), (425, 100), (401, 263), (448, 143), (401, 143)],
            '32': [(465, 372), (427, 108), (398, 309), (460, 273), (412, 227), (427, 178), (453, 107)],
            '64': [(440, 370), (403, 111), (376, 309), (433, 277), (393, 231), (480, 201), (406, 183), (431, 111)]
        },
        'surge': {
            '16': [(415, 355), (425, 138), (429, 253)],
            '32': [(465, 389), (406, 84), (398, 206), (475, 221), (528, 117), (404, 150)],
            '64': [(467, 380), (411, 99), (318, 307), (442, 273), (473, 231), (517, 141), (323, 152), (406, 165)]
        },
        'night-flight': {
            '16': [(495, 106), (453, 314), (495, 226), (375, 235)],
            '32': [(495, 108), (435, 331), (480, 177), (386, 184), (447, 246)],
            '64': [(544, 120), (391, 337), (439, 131), (432, 195), (346, 202), (401, 258)]
        },
        'mass-destruction': {
            '16': [(540, 108), (414, 324), (552, 250), (403, 241)],
            '32': [(386, 372), (504, 179), (373, 318), (473, 328), (455, 233), (530, 317)],
            '64': [(386, 369), (481, 120), (373, 318), (473, 333), (530, 315), (455, 233), (509, 176)]
        },
        'devils-perch': {
            '16': [(472, 203), (369, 218), (467, 296), (411, 203), (401, 249)],
            '32': [(519, 236), (350, 232), (457, 182), (443, 252), (426, 302), (386, 214)],
            '64': [(397, 172), (324, 277), (578, 306), (415, 236), (401, 294), (561, 272), (507, 277), (459, 262), (386, 334), (355, 263)]
        },
        'ghost-town': {
            '16': [(498, 299), (378, 139), (447, 232), (339, 236)],
            '32': [(419, 358), (461, 124)],
            '64': [(419, 358), (461, 124)]
        },
        'the-iron-gator': {
            '16': [(411, 204), (471, 303), (384, 158), (425, 223)],
            '32': [(339, 187), (494, 151), (349, 201), (381, 248), (370, 220), (406, 273), (389, 265)],
            '64': [(339, 187), (494, 151), (349, 201), (381, 248), (370, 220), (406, 273), (389, 265)]
        },
        'leviathan': {
            '16': [(323, 96), (578, 324), (325, 155), (387, 206), (508, 236)],
            '32': [(271, 225), (621, 285), (342, 204), (335, 168), (402, 291), (449, 322), (402, 229)],
            '64': [(264, 215), (618, 287), (330, 202), (332, 172), (401, 100), (399, 274), (451, 185), (446, 322), (544, 212)]
        },
        'dalian-2v2': {
            '16': [(573, 296), (375, 108)],
            '32': [(607, 238), (307, 307)],
            '64': [(607, 238), (307, 307)]
        },
        'sharqi-2v2': {
            # All sizes are the exact same
            '16': [(328, 73), (462, 380)],
            '32': [(328, 73), (462, 380)],
            '64': [(328, 73), (462, 380)]
        },
        'dragon-2v2': {
            # 32 and 64 size are broken (no spawn menu)
            '16': [(322, 155), (490, 299)],
        },
        'daqing-2v2': {
            # All sizes are the exact same
            '16': [(425, 354), (503, 102)],
            '32': [(425, 354), (503, 102)],
            '64': [(425, 354), (503, 102)]
        },
        'black-beards-atol': {
            '16': [(308, 238), (560, 230)],
            '32': [(444, 360), (440, 120)],
            '64': [(426, 395), (453, 94)]
        },
        'black-beards-atol-ctf': {
            # 64 is the only available size
            '64': [(412, 395), (443, 78)]
        },
        'blue-bayou': {
            '16': [(364, 130), (504, 324)],
            '32': [(355, 153), (485, 329)],
            '64': [(363, 163), (480, 324)]
        },
        'blue-bayou-ctf': {
            # 64 is the only available size
            '64': [(363, 128), (505, 325)]
        },
        'blue-bayou-zombie': {
            # 64 is the only available size and primary team spawns currently do not work reliably because
            # you sometimes need to select the zombie class first
            '64': [(396, 183), (378, 203)]
        },
        'crossbones-keep': {
            '16': [(448, 324), (450, 185)],
            '32': [(315, 379), (450, 185)],
            '64': [(315, 379), (450, 185)]
        },
        'crossbones-keep-zombie': {
            # 64 is the only available size and primary team spawns currently do not work reliably because
            # you sometimes need to select the zombie class first
            '64': [(453, 145), (456, 112)]
        },
        'dead-calm': {
            '16': [(406, 127), (474, 302)],
            '32': [(274, 355), (600, 90)],
            '64': [(274, 355), (600, 90)]
        },
        'frylar': {
            '16': [(500, 240), (366, 200)],
            '32': [(500, 240), (366, 200)],
            '64': [(500, 240), (366, 200)]
        },
        'frylar-ctf': {
            # 64 is the only available size
            '64': [(500, 240), (366, 200)]
        },
        'frylar-zombie': {
            # 64 is the only available size and primary team spawns currently do not work reliably because
            # you sometimes need to select the zombie class first
            '64': [(539, 246), (457, 230)]
        },
        'lost-at-sea': {
            '16': [(565, 356), (327, 118)],
            '32': [(565, 356), (327, 118)],
            '64': [(565, 356), (327, 118)]
        },
        'ome-hearty-beach': {
            '16': [(348, 208), (580, 180)],
            '32': [(296, 208), (560, 238)],
            '64': [(296, 208), (560, 238)]
        },
        'ome-hearty-beach-zombie': {
            # 64 is the only available size and primary team spawns currently do not work reliably because
            # you sometimes need to select the zombie class first
            '64': [(315, 215), (423, 240)]
        },
        'pelican-point': {
            '16': [(472, 120), (455, 365)],
            '32': [(433, 139), (421, 295)],
            '64': [(433, 139), (338, 331)]
        },
        'pelican-point-ctf': {
            # 64 is the only available size
            '64': [(462, 117), (385, 340)]
        },
        'pressgang-port': {
            '16': [(428, 80), (452, 385)],
            '32': [(442, 139), (438, 325)],
            '64': [(442, 68), (440, 398)]
        },
        'pressgang-port-ctf': {
            # 64 is the only available size
            '64': [(440, 383), (441, 81)]
        },
        'sailors-warning': {
            '16': [(273, 268), (610, 268)],
            '32': [(273, 268), (610, 268)],
            '64': [(273, 268), (610, 268)]
        },
        'shallow-draft': {
            '16': [(523, 120), (326, 353)],
            '32': [(523, 117), (340, 334)],
            '64': [(526, 114), (340, 334)]
        },
        'shallow-draft-ctf': {
            # 64 is the only available size
            '64': [(522, 112), (340, 334)]
        },
        'shipwreck-shoals': {
            '16': [(359, 278), (468, 258)],
            '32': [(359, 278), (468, 258)],
            '64': [(359, 278), (468, 258)]
        },
        'shipwreck-shoals-ctf': {
            # 64 is the only available size
            '64': [(418, 101), (495, 364)]
        },
        'shiver-me-timbers': {
            '16': [(537, 362), (392, 127)],
            '32': [(547, 235), (438, 107)],
            '64': [(547, 242), (429, 168)]
        },
        'shiver-me-timbers-ctf': {
            # 64 is the only available size
            '64': [(540, 272), (315, 110)]
        },
        'storm-the-bastion': {
            '16': [(501, 348), (345, 158)],
            '32': [(510, 98), (370, 180)],
            '64': [(454, 188), (274, 383)]
        },
        'storm-the-bastion-zombie': {
            # Primary team spawns currently do not work reliably because you sometimes
            # need to select the zombie class first
            '32': [(411, 238), (411, 264)],
            '64': [(526, 293), (403, 210)]
        },
        'stranded': {
            '16': [(353, 290), (510, 178)],
            '32': [(608, 401), (278, 78)],
            '64': [(608, 401), (278, 78)]
        },
        'stranded-ctf': {
            # 64 is the only available size
            '64': [(353, 290), (507, 178)]
        },
        'wake-island-1707': {
            '16': [(390, 304), (521, 157)],
            '32': [(560, 350), (492, 106)],
            '64': [(534, 319), (350, 155)]
        },
        'yukon-bridge': {
            '16': [(578, 226), (291, 231)],
            '32': [(569, 229), (291, 234), (434, 205)],
            '64': [(567, 223), (301, 234), (434, 203)]
        },
        'rocky-mountains': {
            '16': [(461, 110), (458, 343)],
            '32': [(468, 30), (461, 413)],
            '64': [(436, 30), (433, 410)]
        },
        'stalingrad-snow': {
            '16': [(426, 63), (444, 402)],
            '32': [(579, 134), (442, 342)],
            '64': [(351, 63), (451, 410), (445, 64), (535, 61)]
        },
        'spring-thaw': {
            # 32 is the only available size
            '32': [(481, 82), (327, 371)]
        },
        'frostbite-night': {
            # 16 is the only available size
            '16': [(574, 270), (355, 169)],
        },
        'frostbite': {
            # No 64 size available
            '16': [(550, 372), (359, 95)],
            '32': [(596, 232), (287, 392)]
        },
        'christmas-hill': {
            # 32 is the only available size
            '32': [(428, 239), (423, 77)]
        },
        'blitzkrieg': {
            # 16 is the only available size
            '16': [(576, 134), (351, 355)]
        },
        'alpin-ressort': {
            '16': [(398, 214), (523, 263)],
            '32': [(516, 230), (305, 219)],
            '64': [(312, 86), (497, 328)]
        },
        'snowy-park-day': {
            # 16 is the only available size
            '16': [(438, 227), (451, 227)]
        },
        'snowy-park': {
            # 16 is the only available size
            '16': [(438, 227), (451, 227)]
        },
        'winter-wake-island': {
            # Map offers all sizes, but they are all the same
            '16': [(359, 158), (524, 290), (445, 194), (503, 192), (434, 274), (469, 297)],
            '32': [(359, 158), (524, 290), (445, 194), (503, 192), (434, 274), (469, 297)],
            '64': [(359, 158), (524, 290), (445, 194), (503, 192), (434, 274), (469, 297)]
        },
    }
}
