"""Packages the analyzer into an application.
Librosa 0.9.2 has to be used, since pyinstaller cant package >=0.10.0.
See https://github.com/librosa/librosa/issues/1705.
"""
import PyInstaller.__main__
import os


PyInstaller.__main__.run(
    [
        "--icon=gui/img/birdnet-icon.ico",
        "--name=BirdNET-Analyzer",
        "--noconfirm",
        "--clean",
        "--add-data=eBird_taxonomy_codes_2021E.json" + os.pathsep + ".",
        "--add-data=checkpoints" + os.pathsep + "checkpoints",
        "--add-data=example" + os.pathsep + "example",
        "--add-data=labels" + os.pathsep + "labels",
        "--additional-hooks-dir=extra-hooks",
        "analyze.py",
    ]
)
