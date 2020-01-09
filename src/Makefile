PKGNAME=comps-extras
VERSION := $(shell awk '/Version:/ { print $$2 }' ${PKGNAME}.spec)
RELEASE := $(shell awk '/Release:/ { print $$2 }' ${PKGNAME}.spec)
TAG=$(PKGNAME)-$(VERSION)

default: all

all:
	echo "Nothing to do"

clean:
	rm -f *~ *.tar.gz

install: all
	mkdir -p $(DESTDIR)/usr/share/pixmaps/comps

	install -m 644 pixmaps/* $(DESTDIR)/usr/share/pixmaps/comps/

tag:
	@git tag -a -m "Tag as $(TAG)" $(TAG)
	@echo "Tagged as $(TAG)"

archive: clean tag
	@git archive --format=tar --prefix=$(PKGNAME)-$(VERSION)/ HEAD > $(PKGNAME)-$(VERSION).tar
	@gzip -f $(PKGNAME)-$(VERSION).tar
	@echo "The archive is in $(PKGNAME)-$(VERSION).tar.gz"

local: clean
	@rm -rf $(PKGNAME)-$(VERSION).tar.gz
	@rm -rf /tmp/$(PKGNAME)-$(VERSION) /tmp/$(PKGNAME)
	@dir=$$PWD; cd /tmp; cp -a $$dir $(PKGNAME)
	@mv /tmp/$(PKGNAME) /tmp/$(PKGNAME)-$(VERSION)
	@dir=$$PWD; cd /tmp; tar cvzf $$dir/$(PKGNAME)-$(VERSION).tar.gz --exclude .git $(PKGNAME)-$(VERSION)
	@rm -rf /tmp/$(PKGNAME)-$(VERSION)
	@echo "The archive is in $(PKGNAME)-$(VERSION).tar.gz"
