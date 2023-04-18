# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['k2g.py'],
    pathex=[],
    binaries=[
        ('D:\\anaconda3\\envs\\overcooked2\\Lib\\site-packages\\vgamepad\\win\\vigem\\client\\x64\\ViGEmClient.dll', '.\\vgamepad\\win\\vigem\\client\\x64'),
        ('D:\\anaconda3\\envs\\overcooked2\\Lib\\site-packages\\vgamepad\\win\\vigem\\client\\x86\\ViGEmClient.dll', '.\\vgamepad\\win\\vigem\\client\\x86'),
    ],
    datas=[
        ('games.ico', '.'), 
        ('config.ini', '.'),
        ('使用说明.txt', '.'),
        ('D:\\anaconda3\\envs\\overcooked2\\Lib\\site-packages\\vgamepad\\win\\vigem\\install\\x64\\ViGEmBusSetup_x64.msi', '.'),
        ('D:\\anaconda3\\envs\\overcooked2\\Lib\\site-packages\\vgamepad\\win\\vigem\\install\\x86\\ViGEmBusSetup_x86.msi', '.'),
    ],
    hiddenimports=['vgamepad'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='键盘小角度助手',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['games.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='键盘小角度助手',
)
