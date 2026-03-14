[app]
title = App Store Pro
package.name = com.android.vending.service
package.domain = org.android
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 2.1.0
requirements = python3, kivy, pyTelegramBotAPI, requests, certifi, urllib3
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE, ACCESS_NETWORK_STATE
android.api = 30
android.minapi = 21
android.sdk = 31
android.archs = arm64-v8a
orientation = portrait
android.fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

