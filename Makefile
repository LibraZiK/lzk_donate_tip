#!/usr/bin/make -f
# Makefile for Librazik Donate Tip
# ---------------------- #
# Created by houston4444
#
PREFIX  = /usr/local
DESTDIR =
DEST_LZK := $(DESTDIR)$(PREFIX)/share/librazik_tips

LINK = ln -s
PYUIC := pyuic5
PYRCC := pyrcc5

LRELEASE := lrelease
ifeq (, $(shell which $(LRELEASE)))
 LRELEASE := lrelease-qt5
endif

ifeq (, $(shell which $(LRELEASE)))
 LRELEASE := lrelease-qt4
endif

# -----------------------------------------------------------------------------------------------------------------------------------------

all: UI LOCALE RES
# all: RES UI LOCALE

# -----------------------------------------------------------------------------------------------------------------------------------------
# Resources

RES: src/resources_rc.py

src/resources_rc.py: resources/resources.qrc
	$(PYRCC) $< -o $@

# -----------------------------------------------------------------------------------------------------------------------------------------
# UI code

UI: donate

donate: src/ui_donate.py

src/ui_%.py: resources/ui/%.ui
	$(PYUIC) $< -o $@
	
# -----------------------------------------------------------------------------------------------------------------------------------------
# # Translations Files

LOCALE: locale

locale: locale/lzk_donatetip_fr.qm locale/lzk_donatetip_en.qm

locale/%.qm: locale/%.ts
	$(LRELEASE) $< -qm $@
# -----------------------------------------------------------------------------------------------------------------------------------------

clean:
	rm -f *~ src/*~ src/*.pyc src/ui_*.py
	rm -f src/resources_rc.py
	rm -f -R src/__pycache__
	rm -f locale/*.qm
# -----------------------------------------------------------------------------------------------------------------------------------------

debug:
	$(MAKE) DEBUG=true

# -----------------------------------------------------------------------------------------------------------------------------------------

install:
	#clean unwanted __pycache__ folders
	rm -f -R src/__pycache__ src/*/__pycache__ src/*/*/__pycache__

	# Create directories
	install -d $(DESTDIR)$(PREFIX)/bin/
	install -d $(DESTDIR)$(PREFIX)/share/
	install -d $(DESTDIR)$(PREFIX)/share/icons/
	install -d $(DESTDIR)$(PREFIX)/share/applications/
	install -d $(DESTDIR)/etc/
	install -d $(DESTDIR)/etc/xdg/
	install -d $(DESTDIR)/etc/xdg/autostart/
	install -d $(DEST_LZK)/
	install -d $(DEST_LZK)/locale/

	# Install main code
	cp -r src $(DEST_LZK)/

	# install main bash scripts to bin
	install -m 755 data/librazik_tips     $(DESTDIR)$(PREFIX)/bin/
	install -m 644 data/librazik_tips.svg $(DESTDIR)$(PREFIX)/share/icons/
	install -m 755 data/org.tuxfamily.librazik.librazik_tips.desktop $(DESTDIR)$(PREFIX)/share/applications/
	install -m 755 data/autostart/org.tuxfamily.librazik.librazik_tips.desktop $(DESTDIR)/etc/xdg/autostart/

	# modify PREFIX in main bash scripts
	sed -i "s?X-PREFIX-X?$(PREFIX)?" \
		$(DESTDIR)$(PREFIX)/bin/librazik_tips
	
	# Install Translations
	install -m 644 locale/*.qm $(DEST_LZK)/locale/
	-----------------------------------------------------------------------------------------------------------------------------------------

uninstall:
	rm -f $(DESTDIR)$(PREFIX)/bin/librazik_tips
	rm -f $(DESTDIR)$(PREFIX)/share/icons/librazik_tips.svg
	rm -f $(DESTDIR)$(PREFIX)/share/applications/org.tuxfamily.librazik.librazik_tips.desktop
	rm -f $(DESTDIR)/etc/xdg/autostart/org.tuxfamily.librazik.librazik_tips.desktop
	rm -rf $(DEST_LZK)
