from PyQt5.QtCore import QLibraryInfo

plugins_path = QLibraryInfo.location(QLibraryInfo.PluginsPath)
print(f"Plugins path: {plugins_path}")

# To get platform plugins specifically
from PyQt5.QtGui import QGuiApplication
import sys

app = QGuiApplication(sys.argv)
platforms = app.platformName()
print(f"Current platform: {platforms}")
