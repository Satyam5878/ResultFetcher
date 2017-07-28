import sys
from cx_Freeze import setup, Executable

Include = ["main.py","ImageFetcher.py"]
build_exe_options = {"packages":["os","main","ImageFetcher"],"excludes":["tkinter"],"include_files":Include,"bin_includes":"F:\\Projects\\Python\\Projects\\ManitResultFetcher"}

base =None
if sys.platform =="win32":
    base = "Win32GUI"

setup(name = "ManitResultFetcher",
      version = "0.1",
      description =  "MyTester",
      options = {"build_exe":build_exe_options},
      executables = [Executable("opener.py",base=base)])
