# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['mousemover.py'],
    pathex=[],
    binaries=[],
    datas=[('config.yml', '.'), ('.\\resource', 'resource'), ('ui_mainwindow.py', '.'), ('ui_handler.py', '.'), ('mouse_handler.py', '.')],
    hiddenimports=['PyQt5.QtWidgets', 'win32api', 'win32con'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='XCoderServerMonitor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['resource\\icon.ico'],
)
