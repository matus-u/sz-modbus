
def openSubWindow(parent, window):
    window.show()
    window.raise_()
    window.activateWindow()
    window.move(window.pos().x(), parent.pos().y() + 60)
