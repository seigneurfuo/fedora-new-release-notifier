#!/bin/bash
#rpmbuild --define "_topdir `pwd`/packaging/" -bs packaging/fedora-new-release-notifier.spec

APP_NAME=fedora-new-release-notifier
APP_VERSION=0.0.1

RPMBUILD_PATH="$(pwd)/rpmbuild"

#
# TODO IF EXISTS
mkdir -p "$RPMBUILD_PATH/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}"

# Create sources archive
tar --create --file="rpmbuild/SOURCES/$APP_NAME-$APP_VERSION.tar" "../src"

rpmbuild --define "_topdir $RPMBUILD_PATH" -bb fedora-new-release-notifier.spec
