import sys
from cx_Freeze import setup, Executable

packages = ["GraphicalInterface", "ImageEditor", "CSVParser"]
build_exe_options = {"includes": ["tkinter", "tkfilebrowser"], "packages": packages}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="IAS",
    version="1.0",
    description="ImageAreaSelection",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)