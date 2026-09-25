# Anonymous playtime telemetry.
#
# Records only: the code the student was given, an event type (join /
# progress / finish / leave), the scene checkpoint reached, and cumulative
# in-story playtime (renpy.get_game_runtime(), which excludes time spent in
# menus). No choices, clicks, or answers are recorded.
#
# TELEMETRY_REQUIRE_CODE is the single switch between the two builds:
#   True  -> tracked build. Prompts for the code the professor issued.
#   False -> open build. No prompt, logs everything under the "OPEN" code.
# Flip it, then re-export the Web build, for each of the two versions.
#
# Setup:
# 1. Deploy Story/Telemetry/apps_script.gs as a Google Apps Script Web App
#    (see comments in that file).
# 2. Paste the resulting /exec URL into TELEMETRY_URL below.
# Until TELEMETRY_URL is filled in, telemetry_send() silently does nothing.

define TELEMETRY_REQUIRE_CODE = True

init -1 python:
    import json as _telemetry_json

    TELEMETRY_URL = "https://script.google.com/macros/s/AKfycbynYI3oWEvoR0cRhW1cu9JWh1KijENq7o0jX7605RT-jTA-7jajpCYxoGJKxhRjOTRCvw/exec"

    # 100 codes. XGRH2N is reserved for your own testing so it doesn't mix
    # with real student data. The rest are for students plus spares.
    # Adding or changing codes means rebuilding and republishing the tracked build.
    TELEMETRY_VALID_CODES = frozenset([
        "367M7C", "4ZFG9K", "5NQG4C", "5QSK5F", "65GCG4",
        "8EHRZL", "9BLSGV", "9DP3MN", "BL23KP", "E7P482",
        "F54S5S", "GRMMYM", "GZG82V", "KNMLRS", "KQTSAK",
        "KT2GPV", "N9P49D", "UHU75H", "VKKMVJ", "XGA7JP",
        "XGRH2N",  # <- reserved for your own testing
        "2LE72Y", "3MTMPR", "3PY83A", "78E2AM", "8PGYRT",
        "8U79DM", "AKV9BU", "AUQLBW", "B9RVGT", "BMF9BQ",
        "BVFFRZ", "C6XEZ2", "C9GU7C", "HNL2QN", "J8DRPA",
        "KCUQB3", "KU97K7", "KUFFA9", "MMYXJF", "MWCDN8",
        "N7QA4G", "N838N4", "R7F3HG", "RDMYZK", "UGAF7G",
        "V7JGRA", "WJ8JFU", "YDDKUB", "YQ2TPR",
        "3KN46T", "3XNATM", "3YCJ28", "42T8WV", "4X2P2B",
        "4Y6ZBT", "6P8MUH", "6Q8UBJ", "7F88QW", "8ZWE46",
        "9FNUMM", "BZFW8G", "CVRF73", "DK4D36", "DL2CFU",
        "E3AF4K", "E7KGDB", "EGNH8N", "G9962N", "GDGVH8",
        "GR3J6D", "GXF3YG", "HEVD68", "HJC86U", "JH2ZXK",
        "JJ7YML", "JNY7Z7", "JR9RWX", "KNQ7UW", "KTBRC8",
        "LXJZEH", "MDMQGM", "MZWAUH", "N8LWN6", "NUDCZY",
        "P8HF7W", "Q9PMXB", "TK87KL", "U4MTXH", "U82M4N",
        "UDCBB9", "VG7PBH", "WBCDGA", "WEP6YA", "XBLKH7",
        "XBZ4XJ", "XF9RLX", "XGHURV", "YLDJUZ", "ZVFNQZ",
    ])

    def telemetry_send(scene, completed=False, event=None):
        if not TELEMETRY_URL:
            return

        resolved_event = event or ("finish" if completed else "progress")

        payload = {
            "code": persistent.telemetry_code,
            "event": resolved_event,
            "scene": scene,
            "elapsed_seconds": int(renpy.get_game_runtime()),
            "completed": completed,
        }

        try:
            renpy.fetch(
                TELEMETRY_URL,
                data=_telemetry_json.dumps(payload).encode("utf-8"),
                content_type="text/plain;charset=utf-8",
                timeout=3,
            )
        except Exception:
            pass  # a network hiccup should never interrupt the story

    def _telemetry_on_quit():
        # Best-effort only: fires on a normal desktop quit (window close,
        # in-game Quit button). Cannot fire reliably from a closed browser
        # tab on the web build, the per-scene progress pings are the
        # fallback duration signal there.
        telemetry_send("quit", event="leave")

    config.quit_action = Function(_telemetry_on_quit)

default persistent.telemetry_code = None

# A centered variant of the built-in "input" screen (screens.rpy:175), used
# only for the telemetry code prompt so nothing else in the game is affected.
screen telemetry_input_screen(prompt):
    style_prefix "input"

    window:
        xalign 0.5
        yalign 0.5

        vbox:
            xalign 0.5
            xsize gui.dialogue_width

            text prompt style "input_prompt" xalign 0.5
            input id "input" xalign 0.5

label telemetry_intro:
    if persistent.telemetry_code is None:
        if TELEMETRY_REQUIRE_CODE:
            python:
                entered_code = ""
                while entered_code not in TELEMETRY_VALID_CODES:
                    entered_code = renpy.input(
                        "Enter the code your instructor gave you:",
                        screen="telemetry_input_screen",
                    ).strip().upper()
                    if entered_code not in TELEMETRY_VALID_CODES:
                        renpy.notify("That code wasn't recognized. Please check it and try again.")
            $ persistent.telemetry_code = entered_code
        else:
            $ persistent.telemetry_code = "OPEN"

        $ telemetry_send("intro", event="join")

    scene black
    "This playthrough only records how long you spend in the story, nothing you click or type, so we can see whether playing helps with the exam."
    return
