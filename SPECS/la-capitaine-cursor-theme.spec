%global         source_name capitaine-cursors

Name:           la-capitaine-cursor-theme
Version:        3
Release:        1%{?dist}
Summary:        An x-cursor theme inspired by macOS and based on KDE Breeze

License:        LGPLv3
URL:            https://krourke.org/projects/art/%{source_name}
Source0:        https://github.com/keeferrourke/%{source_name}/archive/r%{version}.tar.gz#/%{name}-r%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  inkscape
BuildRequires:  %{_bindir}/xcursorgen

%description
An x-cursor theme inspired by macOS and based on KDE Breeze.
Designed to pair well with the associated icon pack, La Capitaine.


%prep
%autosetup -n %{source_name}-r%{version}


%build
./build.sh


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p "$RPM_BUILD_ROOT/%{_datadir}/icons/La Capitaine"
cp -R $RPM_BUILD_DIR/%{source_name}-r%{version}/dist/cursors "$RPM_BUILD_ROOT/%{_datadir}/icons/La Capitaine"


%files
%license COPYING
%doc README.md
"%{_datadir}/icons/La Capitaine/cursors"



%changelog
* Thu Mar 07 2019 Laurent Tréguier <laurent@treguier.org> - 3-1
- new version

* Wed Jan 17 2018 Laurent Tréguier <laurent@treguier.org> - 2.1.20171126-1
- new version
- fixed missing inkscape dependency (I never noticed the package was never working...)

* Wed Oct 18 2017 Laurent Tréguier <laurent@treguier.org> - 2.1-1
- new version

* Wed Mar 15 2017 Laurent Tréguier <laurent@treguier.org> - 2-1
- created specfile
