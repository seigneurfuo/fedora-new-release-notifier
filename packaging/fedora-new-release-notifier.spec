Name:           fedora-new-release-notifier
Version:        0.0.1
Release:        %autorelease
BuildArch:      noarch
Summary:        A nsi

License:        None
URL:            .

Requires:       python
Requires:       python3-distro
Requires:       python3-gobject-base-noarch

%description
A demo RPM build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 ../src/app.py %{buildroot}/%{_bindir}/%{name}

mkdir -p %{buildroot}/usr/xdg/autostart/
install -m 644 ./%{name}-autostart.desktop %{buildroot}/usr/xdg/autostart/%{name}.desktop

%files
%{_bindir}/%{name}
/usr/xdg/autostart/%{name}.desktop
