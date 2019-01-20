%global         debug_package   %{nil}

Name:           gnome-builder-dlang
Version:        0.1.0
Release:        1%{?dist}
Summary:        D language support for GNOME Builder

License:        MIT
URL:            https://github.com/d-language-server/%{name}
Source0:        https://github.com/d-language-server/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Requires:       gnome-builder
Requires:       dmd
Requires:       dub

%description
A GNOME Builder plugin for Dlang. Provides dub project and build integration,
and editing features using the Language Server protocol.


%prep
%autosetup


%build


%install
rm -rf $RPM_BUILD_ROOT
plugins_dir="$RPM_BUILD_ROOT/%{_libdir}/gnome-builder/plugins"
mkdir -p $plugins_dir
mv dlang* $plugins_dir


%files
%license LICENSE.txt
%doc README.md
%{_libdir}/gnome-builder/*



%changelog
* Sun Jan 20 2019 Laurent Tréguier <laurent@treguier.org> - 0.1.0-1
- created specfile
