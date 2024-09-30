from cx_Freeze import setup, Executable

build_exe_options = {
    "excludes": [
        "tkinter",
        "sqlite3",
        "email",
    ],
    "include_msvcr": True,
    "optimize": 2,
}

setup(
    name="quick-subtitles",
    version="0.0.1",
    description="An easy way to generate SRT subtitles from a video in Windows.",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base="Console", target_name="quick-subtitles")],
)
