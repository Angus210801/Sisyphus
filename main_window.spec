# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

datas = [
    ('config', 'config'),
    ('test_scripts', 'test_scripts'),
    ('log', 'log'),
	('ui','ui')
]


a = Analysis(
    ['main_window.py'],
    pathex=[],
    binaries=[],
    datas=datas,  # Use the datas list here
	hiddenimports = [
    "logging",
    "os",
    "random",
    "shutil",
    "sys",
    "zipfile",
    "time",
    "urllib3",
    "selenium.webdriver",
    "selenium.webdriver.common.by",
    "selenium.webdriver.common.keys",
    "selenium.webdriver.support.select",
    "test_scripts.testcase_element_exist",
    "ftplib",
    "re",
    "winreg",
    "requests",
    "PyQt5.QtCore",
    "PyQt5.QtGui",
    "PyQt5.QtWidgets",
    "selenium",
    "threading",
    "concurrent.futures",
    "test_scripts.testcase_action",
    "test_scripts.testcase_linux",
    "test_scripts.testcase_windows",
    "config.devices_name_list",
    "log.logs",
    "test_scripts.testcase_chromedriver_update",
    "ui.controller"
],
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
    name='main_window',
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
    icon='config\\jabra.ico',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main_window',
)
