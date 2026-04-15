[app]

# Название приложения (как будет отображаться на экране телефона)
title = Условные знаки

# Имя пакета (должно быть уникальным, строчными буквами, без пробелов)
package.name = sportsymbolstrainer

# Домен (обычно org.имяпроекта)
package.domain = org.orient

# Точка входа — ваш основной Python файл
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt

# Версия приложения
version = 1.0

# Зависимости (добавьте сюда любые библиотеки, которые используете)
# Например: kivymd для красивого дизайна, pillow для работы с картинками
requirements = python3,kivy,kivymd,pillow

# Ориентация экрана (portrait — вертикальная)
orientation = portrait

# Полноэкранный режим (0 — с панелью уведомлений, 1 — полностью)
fullscreen = 0

# Путь к иконке (положите файл icon.png 512x512 в корень проекта)
icon.filename = %(source.dir)s/icon.png

# Заставка при загрузке (опционально)
# presplash.filename = %(source.dir)s/presplash.png

# Точка входа
resource.entrypoint = main.py

# Разрешения Android (если нужно сохранять прогресс обучения)
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Функции Android
android.features = android.hardware.screen.portrait

#
# Настройки Buildozer
#
[buildozer]

# Уровень логирования (2 — оптимально для GitHub Actions)
log_level = 2

# Версия NDK (стабильная для Kivy)
android.ndk = 25c

# Целевая версия Android API
android.api = 33

# Минимальная версия Android (поддерживает 99% устройств)
android.minapi = 21
android.ndk_api = 21

# Архитектуры процессора
android.archs = arm64-v8a, armeabi-v7a

# Режим отладки (True для тестовой сборки)
android.debug = True

# Версия Python (3.10 оптимальна)
python.version = 3.10

# ВАЖНО: Фикс для GitHub Actions
p4a.branch = release-2022.12.20

# Дополнительные настройки для KivyMD (если используете)
android.add_src = 

# Если у вас есть папка с изображениями условных знаков — укажите её здесь
source.include_patterns = images/*.png,data/*.json,symbols/*.png
