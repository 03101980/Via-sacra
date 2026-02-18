[app]
title = Via Sacra
package.name = viasacra
package.domain = org.meuapp
source.dir = .
# Inclui as extensões das suas pastas assets, imagens e fontes
source.include_exts = py,png,jpg,jpeg,ttf,otf,json,kv
version = 0.1
requirements = python3,kivy

# (Opcional) Se usar KivyMD, mude a linha acima para:
# requirements = python3,kivy==2.2.1,kivymd,pillow

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1