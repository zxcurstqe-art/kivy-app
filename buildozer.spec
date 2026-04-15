[app]

title = Условные знаки
package.name = sporttrainer
package.domain = org.orient

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt

version = 1.0

requirements = python3,kivy==2.2.1

orientation = portrait
fullscreen = 0

resource.entrypoint = main.py

android.permissions = INTERNET
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 30

[buildozer]

log_level = 2

android.debug = True
android.arch = armeabi-v7a

p4a.branch = develop
python.version = 3.9
