#!/usr/bin/python3

import os
import signal
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import (QLocale, QTranslator, QTimer, QSettings,
                          QLibraryInfo, QDate)
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
            _translate('tip of day', "<html><head/><body><p>Do you know <span style=\" font-weight:600;\">ALT + F2</span> shortcut ?</p><p><br/>This shortcut allows you to start very quicky<br/>any software by typing its name.</p><p>This way, you don't have to create many and many<br/>shortcuts on the desktop.</p></body></html>"),
            _translate('tip of day', "<html><head/><body><p>Do you know <span style=\" font-weight:600;\">ALT + Tab</span> shortcut ?</p><p><br/>This shortcut allows you to switch quickly<br/>between windows.</p></body></html>"),
            _translate('tip of day', "<html><head/><body><p>Do you know that you can come and chat live with other LibraZiK users?</p><p></br>Come on the <span style=\" font-weight:600;\">#librazik IRC channel.</p><p>More information about that <a href=\"https://librazik.tuxfamily.org/base-site-LZK/english.php#help\"><span style=\" font-weight:600; text-decoration: underline; color:#2980b9;\">here</span></a>.</p></body></html>"),
            _translate('tip of day', "<html><head/><body><p>Pretty sure you don't know <a href=\"https://github.com/deufrai/Qrest\"><span style=\" font-weight:600; text-decoration: underline; color:#2980b9;\">Qrest</span></a>.</p><p></br>Do you?</p></body></html>")
                      ]
        mate_tips = [
            _translate('tip of day', "<html><head/><body><p>Do you know <span style=\" font-weight:600;\">Alt + left-click + move</span> shortcut ?</p><p><br/>This shortcut allows you to move a window. Very useful if a window is too big for your screen!</p><p>More information about MATE <a href=\"https://mate-desktop.org/\"><span style=\" font-weight:600; text-decoration: underline; color:#2980b9;\">here</span></a>.</p></body></html>"),
                    ]
        kde_tips = [
            _translate('tip of day', "<html><head/><body><p>Do you know <span style=\" font-weight:600;\">Ctrl + Alt + Esc</span> shortcut ?</p><p><br/>This shortcut allows you to kill windows if they are not responding</p></body></html>"),
            _translate('tip of day', "<html><head/><body><p>Do you know <span style=\" font-weight:600;\">Alt + left-click + move</span> shortcut ?</p><p><br/>This shortcut allows you to move a window. Very useful if a window is too big for your screen!</p></body></html>")
                   ]

        self.bottom_texts = [
            _translate('bottom_texts', "<html><head/><body><p align=\"center\">Creating and maintaining this distribution is<br/>a hard and constant work that takes time.<br/><br/>That is why donations (even modest ones) are very much appreciated<br/>to help keep the motivation alive.</p><p align=\"center\">You can make a donation <a href=\"https://liberapay.com/LibraZiK/donate\"><span style=\" text-decoration: underline; color:#2980b9;\">here</span></a>.<br/>More information and alternatives about donation can be found <a href=\"https://librazik.tuxfamily.org/base-site-LZK/english.php#donation\"><span style=\" text-decoration: underline; color:#0986d3;\">here</span></a>.</p><p align=\"center\">Now, go make some music!</p></body></html>"),
            _translate('bottom_texts', "<html><head/><body><p align=\"center\">LibraZiK takes many hours each week to be what it is.<br/>LibraZiK is free (as a free speech), but not really free (as a free drink).<br/>If you don't donate, the project will eventually stop.</p><p align=\"center\">You can make a donation <a href=\"https://liberapay.com/LibraZiK/donate\"><span style=\" text-decoration: underline; color:#2980b9;\">here</span></a>.<br/>So, if you're able to finance the project, please donate! If you're not able, that's ok, keep using it, we don't want money to be a blocker.</p><p align=\"center\"></br>More information and alternatives about donation can be found <a href=\"https://librazik.tuxfamily.org/base-site-LZK/english.php#donation\"><span style=\" text-decoration: underline; color:#0986d3;\">here</span></a>.</p></body></html>")
                            ]

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

    def setNotAgain(self, not_again: bool):
        self.ui.checkBox.setChecked(not_again)
    
    def setTipOfTheDay(self, day):
        self.tip_day = day % len(self.tips)
        message = self.tips[self.tip_day]

        self.ui.labelTipOfTheDay.setText(message)
        
    def setBottomText(self, day):
        self.ui.labelDonate.setText(
            self.bottom_texts[day % len(self.bottom_texts)])
    
    def goPrevious(self):
        day = len(self.tips) - 1
        if self.tip_day:
            day = self.tip_day -1

        self.setTipOfTheDay(day)
        
    def goNext(self):
        self.setTipOfTheDay(self.tip_day + 1)

if __name__ == "__main__":
    #set Qt Application
    app = QApplication(sys.argv)
    app.setApplicationName("Librazik Tips")
    app.setOrganizationName("librazik")
    app.setWindowIcon(QIcon(':/icon_LZK.svg'))
    app.setDesktopFileName('org.tuxfamily.librazik.librazik_tips')

    settings = QSettings()

    not_again = settings.value('not_again', type=bool)
    tip_of_day = settings.value('tip_of_day', type=int)

    ### Translation process
    locale = QLocale.system().name()
    appTranslator = QTranslator()
    if appTranslator.load(QLocale(), 'lzk_donatetip', '_', getCodeRoot() + '/locale'):
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
    dialog.setNotAgain(not_again)
    dialog.setTipOfTheDay(tip_of_day)
    dialog.setBottomText(tip_of_day)
    dialog.show()
    
    app.exec()
    
    settings.setValue('not_again', dialog.notAgainChecked())
    settings.setValue('tip_of_day', tip_of_day+1)
    settings.setValue('month', QDate.currentDate().month())
    settings.sync()
    del app
