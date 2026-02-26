from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStyleFactory
from PyQt5.QtCore import Qt, QPoint, QTimer
from PyQt5.QtGui import QPainter, QColor, QPen, QPainterPath
import sys
import os
import argparse

class SpotlightWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Create central widget
        self.central_widget = TransparentWidget(self)
        self.setCentralWidget(self.central_widget)
        
        # Set up window properties
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # Set window to fullscreen
        screen = QApplication.desktop().screenGeometry()
        self.setGeometry(screen)
        
        # Initialize mouse position
        self.mouse_pos = QPoint(0, 0)
        
        # Track mouse movement
        self.setMouseTracking(True)
        self.central_widget.setMouseTracking(True)
        
        # Set up timer for auto-hide
        self.hide_timer = QTimer(self)
        self.hide_timer.timeout.connect(self.on_timer_timeout)
        self.hide_timer.setSingleShot(True)
        self.hide_timeout = args.timeout
        
        # Show the window
        self.show()

    def mouseMoveEvent(self, event):
        # Show the widget if it's hidden
        if not self.central_widget.is_visible:
            self.central_widget.is_visible = True
            
        # Update mouse position
        self.central_widget.mouse_pos = event.pos()
        self.central_widget.update()
        
        # Reset the timer
        self.hide_timer.start(self.hide_timeout)

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            QApplication.quit()

    def on_timer_timeout(self):
        self.central_widget.is_visible = False
        self.central_widget.update()

class TransparentWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mouse_pos = QPoint(0, 0)
        self.spotlight_radius = args.spotlight_radius
        self.is_visible = True

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.is_visible:
            # Create semi-transparent dark overlay
            painter.fillRect(self.rect(), QColor(0, 0, 0, 127))

            # Create spotlight effect (transparent circle)
            painter.setCompositionMode(QPainter.CompositionMode_Clear)
            painter.setBrush(Qt.SolidPattern)
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(self.mouse_pos, self.spotlight_radius, self.spotlight_radius)
        else:
            # Make everything transparent when not visible
            painter.setCompositionMode(QPainter.CompositionMode_Clear)
            painter.fillRect(self.rect(), Qt.transparent)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Spotlight functionality for mouse cursor. Right Click to exit.')
    parser.add_argument('--spotlight_radius', type=int, default=75, help='Spotlight radius')
    parser.add_argument('--timeout', type=int, default=400, help='Timeout (ms) for spotlight to vanish after cursor stops moving')
    args = parser.parse_args()
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)

    app = QApplication(sys.argv)
    window = SpotlightWindow()
    sys.exit(app.exec_())
