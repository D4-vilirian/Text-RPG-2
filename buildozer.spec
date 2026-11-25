[app]

title = TextRPG 2
package.name = textrpg2
package.domain = org.davithecreator
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 1.0

requirements = python3==3.11.6,hostpython3==3.11.6,pygame==2.5.2,sdl2,sdl2_image,sdl2_mixer,sdl2_ttf

orientation = portrait
fullscreen = 1

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

p4a.branch = develop

[buildozer]

log_level = 2
warn_on_root = 1
