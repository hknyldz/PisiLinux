#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("./bootstrap.sh")
    autotools.configure("--sbindir=/usr/bin")

def build():
    autotools.make()

def install():
     autotools.rawInstall("DESTDIR=%s" % get.installDIR())
