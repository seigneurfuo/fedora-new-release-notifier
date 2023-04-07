# rpmbuild -bs

Name:           fedora-new-release-notifier
Version:        0.0.1
Release:        1%{?dist}
BuildArch:      noarch
Summary:        .

License:        None
URL:            .
Source0:        %{name}-%{version}.tar

Requires:       python
Requires:       python3-distro
Requires:       python3-gobject-base-noarch


%description
A demo RPM build

%install
mkdir -p %{buildroot}/usr/bin/

install -m 755 src/app.py %{buildroot}/usr/bin/%{name}

%files
/usr/bin/%{name}



