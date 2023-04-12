#!/bin/bash
#rpmbuild --define "_topdir `pwd`/packaging/" -bs packaging/fedora-new-release-notifier.spec

APP_NAME=fedora-new-release-notifier
FEDORA_TARGET_VERSION=37

# Create sources archive
#tar --create --file="rpmbuild/SOURCES/$APP_NAME-$APP_VERSION.tar" "../src"
cd ..
git archive master -o packaging/$APP_NAME.tar
cd packaging

#fedpkg --release f$FEDORA_TARGET_VERSION mockbuild --no-clean-all
fedpkg --release f$FEDORA_TARGET_VERSION local