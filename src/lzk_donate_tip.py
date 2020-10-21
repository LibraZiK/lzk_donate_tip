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

        self.ui.toolButtonPrevious.clicked.connect(self.goPrevious)
        self.ui.toolButtonNext.clicked.connect(self.goNext)

        if not isDarkTheme(self):
            self.ui.labelLogo.setText(
                "<html><head/><body><p><img src=\":/logo-LZK3_light.svg\"/></p></body></html>")

        global_tips = [
            _translate('tip of day', "<p>Do you know <span style=\" font-weight:600;\">ALT+F2</span> shortcut ?</p><p><br/>This shortcut allows you to start very quicky<br/>any software by typing its name.</p><p>This way, you don't have to create many and many<br/>shortcuts on the desktop.</p>"),
            _translate('tip of day', "<p>Do you know <span style=\" font-weight:600;\">ALT+Tab</span> shortcut ?</p><p><br/>This shortcut allows you to switch quickly<br/>between windows.</p>")]
        
        mate_tips = []
        kde_tips = [_translate('tip of day', "<p>Do you know <span style=\" font-weight:600;\">Ctrl+Alt+Esc</span> shortcut ?</p><p><br/>This shortcut allows you to kill windows if they are not responding</p>")]
        
        desktop = os.getenv('XDG_CURRENT_DESKTOP')
        if desktop == 'MATE':
            desktop_tips = mate_tips
        elif desktop == 'KDE':
            desktop_tips = kde_tips

        # mixer les messages généraux et les messages d'environnement de bureau
        self.tips = []
        n = 0
        while global_tips or desktop_tips:
            if not global_tips:
                self.tips += desktop_tips
                break
            if not desktop_tips:
                self.tips += global_tips
                break

            if n % 2:
                self.tips.append(desktop_tips.pop(0))
            else:
                self.tips.append(global_tips.pop(0))
            n += 1
        
        self.tip_day = 0
    
    def notAgainChecked(self):
        return bool(self.ui.checkBox.checkState())
    
    def setTipOfTheDay(self, day):
        self.tip_day = day % len(self.tips)
        message = self.tips[self.tip_day]

        self.ui.labelTipOfTheDay.setText(message)
    
    def goPrevious(self):
        day = len(self.tips) - 1
        if self.tip_day:
            day = self.tip_day -1

        self.setTipOfTheDay(day)
        
    def goNext(self):
        self.setTipOfTheDay(self.tip_day + 1)

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
