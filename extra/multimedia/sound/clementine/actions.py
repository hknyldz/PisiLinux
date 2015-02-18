#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure(" \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DBUILD_WERROR=OFF \
                          -DBUNDLE_PROJECTM_PRESETS=OFF \
                          -DENABLE_GIO=ON \
                          -DENABLE_SPOTIFY_BLOB=OFF \
                          -DENABLE_BREAKPAD=OFF \
                          -DUSE_BUILTIN_TAGLIB=OFF \
                          -DUSE_SYSTEM_GMOCK=ON \
                          -Wno-dev")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    for i in ("16","32","64"):
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" % (i,i), "dist/clementine_%s.png" % i, "clementine.png")

    pisitools.insinto("/usr/share/clementine/locale", "src/translations/*.qm")
    pisitools.dosym("/usr/share/icons/hicolor/64x64/apps/clementine.png", "/usr/share/pixmaps/clementine.png")

    pisitools.dodoc("Changelog", "COPYING")