[app]

# (str) Title of your application
title = Pusat Administrasi Kelas SD

# (str) Package name
package.name = adminsekolah

# (str) Package domain (needed for android/ios packaging)
package.domain = org.sekolah

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Application versioning
version = 1.0.0

# (list) Permissions
permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API required
android.minapi = 24

# (str) Android NDK version
android.ndk = 25b

# (list) The Android archs to build for (hanya arm64-v8a agar cepat dan tidak kehabisan log/memori)
android.archs = arm64-v8a

# (bool) Accept SDK license automatically
android.accept_sdk_license = True

[buildozer]

# (int) Log level (1 = info standar agar log tidak dipotong GitHub)
log_level = 1

# (str) Path to build artifact storage
build_dir = ./.buildozer
