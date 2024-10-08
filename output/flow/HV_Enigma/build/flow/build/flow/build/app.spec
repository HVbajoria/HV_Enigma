# -*- mode: python ; coding: utf-8 -*-
import sys
from PyInstaller.utils.hooks import collect_data_files, collect_all, copy_metadata

sys.setrecursionlimit(sys.getrecursionlimit() * 5)

datas = [('connections', 'connections'), ('flow', 'flow'), ('settings.json', '.'), ('main.py', '.'), ('utils.py', '.'),
('logo.png', '.'), ('config.json', '.'), ('/usr/local/python/3.12.1/lib/python3.12/site-packages/streamlit/runtime', './streamlit/runtime')]


all_packages = ['openai', 'opentelemetry-sdk', 'tiktoken', 'ruamel.yaml', 'docstring_parser', 'psutil', 'jsonschema', 'filetype', 'flask', 'python-dateutil', 'fastapi', 'azure-identity', 'azure-ai-ml', 'azureml-ai-monitoring', 'httpx', 'sqlalchemy', 'pandas', 'python-dotenv', 'keyring', 'pydash', 'cryptography', 'colorama', 'tabulate', 'filelock', 'marshmallow', 'gitpython', 'strictyaml', 'waitress', 'azure-monitor-opentelemetry-exporter', 'pyarrow', 'pillow', 'opentelemetry-exporter-otlp-proto-http', 'flask-restx', 'flask-cors', 'pyinstaller', 'streamlit', 'streamlit-quill', 'bs4', 'argcomplete']
meta_packages = ['opentelemetry-api'] + ['openai', 'opentelemetry-sdk', 'tiktoken', 'ruamel.yaml', 'docstring_parser', 'psutil', 'jsonschema', 'filetype', 'flask', 'python-dateutil', 'fastapi', 'azure-identity', 'azure-ai-ml', 'azureml-ai-monitoring', 'httpx', 'sqlalchemy', 'pandas', 'python-dotenv', 'keyring', 'pydash', 'cryptography', 'colorama', 'tabulate', 'filelock', 'marshmallow', 'gitpython', 'strictyaml', 'waitress', 'azure-monitor-opentelemetry-exporter', 'pyarrow', 'pillow', 'opentelemetry-exporter-otlp-proto-http', 'flask-restx', 'flask-cors', 'pyinstaller', 'streamlit', 'streamlit-quill', 'bs4', 'argcomplete']

for package in all_packages:
    datas += collect_data_files(package)

for package in meta_packages:
    datas += copy_metadata(package)

opentelemetry_datas, opentelemetry_binaries, opentelemetry_hiddenimports = collect_all('opentelemetry')
promptflow_datas, promptflow_binaries, promptflow_hiddenimports = collect_all('promptflow')

datas += opentelemetry_datas
datas += promptflow_datas
datas += collect_data_files('streamlit_quill')
datas += collect_data_files('keyrings.alt', include_py_files=True)
datas += copy_metadata('keyrings.alt')

hidden_imports = ['win32timezone', 'opentelemetry.context.contextvars_context', 'streamlit.runtime.scriptrunner.magic_funcs'] + ['openai', 'opentelemetry.sdk', 'tiktoken', 'ruamel.yaml', 'docstring_parser', 'psutil', 'jsonschema', 'filetype', 'flask', 'python.dateutil', 'fastapi', 'azure.identity', 'azure.ai.ml', 'azureml.ai.monitoring', 'httpx', 'sqlalchemy', 'pandas', 'python.dotenv', 'keyring', 'pydash', 'cryptography', 'colorama', 'tabulate', 'filelock', 'marshmallow', 'gitpython', 'strictyaml', 'waitress', 'azure.monitor.opentelemetry.exporter', 'pyarrow', 'pillow', 'opentelemetry.exporter.otlp.proto.http', 'flask_restx', 'flask_cors', 'pyinstaller', 'streamlit', 'streamlit_quill', 'bs4', 'argcomplete']
hidden_imports += opentelemetry_hiddenimports
hidden_imports += promptflow_hiddenimports

binaries = []
binaries += opentelemetry_binaries
binaries += promptflow_binaries

block_cipher = None

pfcli_a = Analysis(
    ['app.py', 'main.py', 'utils.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pfcli_pyz = PYZ(pfcli_a.pure, pfcli_a.zipped_data, cipher=block_cipher)

pfcli_exe = EXE(
    pfcli_pyz,
    pfcli_a.scripts,
    pfcli_a.binaries,
    pfcli_a.zipfiles,
    pfcli_a.datas,
    [],
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    contents_directory='.',
)
