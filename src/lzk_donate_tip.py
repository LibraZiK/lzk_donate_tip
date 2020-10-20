#!/usr/bin/python3

import os
import signal
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QLocale, QTranslator, QTimer, QSettings, QLibraryInfo
from PyQt5.QtGui import QPalette, QIcon

import ui_donate

def getCodeRoot():
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def signalHandler(sig, frame):
    if sig in (signal.SIGINT, signal.SIGTERM):
        QApplication.quit()

def isDarkTheme(widget):
    return bool(
        widget.palette().brush(QPalette.Active, QPalette.WindowText).color().lightness()
        > 128)

class DonateDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = ui_donate.Ui_Dialog()
        self.ui.setupUi(self)

        if not isDarkTheme(self):
            self.ui.labelLogo.setText(
                "<html><head/><body><p><img src=\":/logo-LZK3_light.svg\"/></p></body></html>")
    
    def notAgainChecked(self):
        return bool(self.ui.checkBox.checkState())
    
    def setTipOfTheDay(self, day):
        message = _translate('tip of day', "<html><head/><body><p>Do you know <span style=\" font-weight:600;\">ALT+F2</span> shortcut ?</p><p><br/>This shortcut allows you to start very quicky<br/>any software by typing its name.</p><p>This way, you don't have to create many and many<br/>shortcuts on the desktop.</p></body></html>")
        
        # la valeur après le modulo doit être égale au nombre de messages
        tip_day = day % 2
        
        if tip_day == 0:
            # ça ça me paraît pertinent
            message = _translate('tip of day', "<html><head/><body><p>Do you know <span style=\" font-weight:600;\">ALT+F2</span> shortcut ?</p><p><br/>This shortcut allows you to start very quicky<br/>any software by typing its name.</p><p>This way, you don't have to create many and many<br/>shortcuts on the desktop.</p></body></html>")
        elif tip_day == 1:
            # ça c'est un peu naze, c'est juste pour l'exemple
            message = _translate('tip of day', "<html><head/><body><p>Do you know <span style=\" font-weight:600;\">ALT+Tab</span> shortcut ?</p><p><br/>This shortcut allows you to switch quickly<br/>between windows.</p></body></html>")
            
        self.ui.labelTipOfTheDay.setText(message)

if __name__ == "__main__":
    force = False
    if len(sys.argv) >= 2 and sys.argv[1] == '-f':
        force = True
    
    #set Qt Application
    app = QApplication(sys.argv)
    app.setApplicationName("Librazik Donate Tip")
    app.setOrganizationName("librazik")
    app.setWindowIcon(QIcon(':/icon_LZK.svg'))
    #app.setWindowIcon(QIcon(':/scalable/raysession.svg'))
    
    settings = QSettings()
    
    not_again = settings.value('not_again', type=bool)
    tip_of_day = settings.value('tip_of_day', type=int)
    
    if not_again and not force:
        sys.exit(0)
    
    ### Translation process
    locale = QLocale.system().name()
    appTranslator = QTranslator()
    if appTranslator.load("%s/locale/lzk_donatetip_%s" % (getCodeRoot(), locale)):
        app.installTranslator(appTranslator)

    sysTranslator = QTranslator()
    pathSysTranslations = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    if sysTranslator.load(QLocale(), 'qt', '_', pathSysTranslations):
        app.installTranslator(sysTranslator)

    _translate = QApplication.translate

    #connect signals
    signal.signal(signal.SIGINT , signalHandler)
    signal.signal(signal.SIGTERM, signalHandler)
    
    #needed for signals SIGINT, SIGTERM
    timer = QTimer()
    timer.start(200)
    timer.timeout.connect(lambda: None)
    
    dialog = DonateDialog()
    dialog.setTipOfTheDay(tip_of_day)
    dialog.show()
    
    app.exec()
    
    settings.setValue('not_again', dialog.notAgainChecked())
    settings.setValue('tip_of_day', tip_of_day+1)
    settings.sync()
    del app
