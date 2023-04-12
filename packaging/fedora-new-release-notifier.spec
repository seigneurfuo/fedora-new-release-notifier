Name:           fedora-new-release-notifier
Version:        0.0.1
Release:        %autorelease
BuildArch:      noarch
Summary:        A nsi

License:        None
URL:            .
Source0:        %{name}.tar

Requires:       python
Requires:       python3-distro
Requires:       python3-gobject-base-noarch

%description
A demo RPM build

%prep
%setup -c

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 src/app.py %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

