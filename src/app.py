#!/bin/env python3

import sys
import time
import urllib.request
import json

import distro

import gi
gi.require_version("Notify", "0.7")
from gi.repository import Notify

APP_NAME = "Fedora New Release Checker"
URL = "https://getfedora.org/releases.json"

ARCH = "x86_64"
CURRENT_VERSION = int(distro.version())
CHECK_EVERY = 3600

def _get_versions_list():
    with urllib.request.urlopen(URL) as req:
        data = req.read()
        if data:
            return json.loads(data)
def get_latest_version():
    versions = _get_versions_list()

    latest_version = 0

    for version in versions:

        # Filters
        if version['arch'] != ARCH and version["version"] and version['variant'].lower() not in ["workstation", "spins", "silverblue"]:
            continue

        # Filtrage des nombres uniquement
        try:
            version['version'] = int(version['version'])
        except ValueError:
            continue

        if int(version['version']) > latest_version:
            latest_version = int(version['version'])

    return latest_version

def _check_for_newer_version():
    latest_version = get_latest_version()
    if not latest_version or latest_version <= CURRENT_VERSION:
        print('Rien')
        exit()

    _send_notification(latest_version)

def _send_notification(latest_version):
    title = f"La version de Fedora {latest_version} est disponible !"
    msg = f"{title}\nVous pouvez lancer la commande suivante pour mettre à jour:\nsudo dnf system-upgrade download --releasever {latest_version}"

    notification = Notify.Notification.new(title, msg, 'fedora-logo-icon')
    notification.show()

def main():
    Notify.init(APP_NAME)

    while True:
        _check_for_newer_version()
        time.sleep(CHECK_EVERY)

if __name__ == "__main__":
    main()