Name:           fedora-new-release-notifier
Version:        0.0.1
Release:        %autorelease
BuildArch:      noarch
Summary:        Indicateur de nouvelle version de Fedora

License:        None
URL:            .

Requires:       python
Requires:       python3-distro
Requires:       python3-gobject-base-noarch

%description
Un petit script qui affiche une notification (par défaut toutes les heures) quand une nouvelle version de Fedora est disponible.

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 ../src/app.py %{buildroot}/%{_bindir}/%{name}

mkdir -p %{buildroot}/etc/xdg/autostart/
install -m 644 ./%{name}-autostart.desktop %{buildroot}/etc/xdg/autostart/%{name}.desktop

%files
%{_bindir}/%{name}
/etc/xdg/autostart/%{name}.desktop
