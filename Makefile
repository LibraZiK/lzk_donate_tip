#!/usr/bin/make -f
# Makefile for Librazik Donate Tip
# ---------------------- #
# Created by houston4444
#
PREFIX  = /usr/local
DESTDIR =
DEST_LZK := $(DESTDIR)$(PREFIX)/share/librazik-donatetip

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

locale: locale/lzk_donatetip_fr_FR.qm locale/lzk_donatetip_en_US.qm

locale/%.qm: locale/%.ts
	$(LRELEASE) $< -qm $@
# -----------------------------------------------------------------------------------------------------------------------------------------

clean:
	rm -f *~ src/*~ src/*.pyc src/ui_*.py
	rm -f -R src/__pycache__
# -----------------------------------------------------------------------------------------------------------------------------------------

debug:
	$(MAKE) DEBUG=true

# -----------------------------------------------------------------------------------------------------------------------------------------

install:
	#clean unwanted __pycache__ folders
	rm -f -R src/__pycache__ src/*/__pycache__ src/*/*/__pycache__
	
	# Create directories
	install -d $(DESTDIR)$(PREFIX)/bin/
	install -d $(DEST_LZK)/
	install -d $(DEST_LZK)/locale/

	# Install main code
	cp -r src $(DEST_LZK)/
	
	# install main bash scripts to bin
	install -m 755 data/librazik_donatetip $(DESTDIR)$(PREFIX)/bin/
	
	# modify PREFIX in main bash scripts
	sed -i "s?X-PREFIX-X?$(PREFIX)?" \
		$(DESTDIR)$(PREFIX)/bin/librazik_donatetip
	
	# Install Translations
	install -m 644 locale/*.qm $(DEST_LZK)/locale/
	-----------------------------------------------------------------------------------------------------------------------------------------

uninstall:
	rm -f $(DESTDIR)$(PREFIX)/bin/librazik_donatetip
	rm -rf $(DEST_LZK)
