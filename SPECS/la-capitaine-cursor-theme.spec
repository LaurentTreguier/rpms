%global         git_date    20171126
%global         git_commit  46c3ffd3d818bce8094712f38577dc5f3a7e810a
%global         source_name capitaine-cursors

Name:           la-capitaine-cursor-theme
Version:        2.1.%{git_date}
Release:        1%{?dist}
Summary:        An x-cursor theme inspired by macOS and based on KDE Breeze

License:        LGPLv3
URL:            https://krourke.org/projects/art/capitaine-cursors
Source0:        https://github.com/keeferrourke/capitaine-cursors/archive/%{git_commit}.tar.gz#/%{name}-%{git_commit}.tar.gz

BuildArch:      noarch
BuildRequires:  inkscape
BuildRequires:  %{_bindir}/xcursorgen

%description
An x-cursor theme inspired by macOS and based on KDE Breeze.
Designed to pair well with the associated icon pack, La Capitaine.


%prep
%autosetup -n %{source_name}-%{git_commit}


%build
./build.sh


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p "$RPM_BUILD_ROOT/%{_datadir}/icons/La Capitaine"
cp -R $RPM_BUILD_DIR/%{source_name}-%{git_commit}/dist/cursors "$RPM_BUILD_ROOT/%{_datadir}/icons/La Capitaine"


%files
%license COPYING
%doc README.md
"%{_datadir}/icons/La Capitaine/cursors"



%changelog
* Wed Jan 17 2018 Laurent Tréguier <laurent@treguier.org> - 2.1.20171126-1
- new version
- fixed missing inkscape dependency (I never noticed the package was never working...)

* Wed Oct 18 2017 Laurent Tréguier <laurent@treguier.org> - 2.1-1
- new version

* Wed Mar 15 2017 Laurent Tréguier <laurent@treguier.org> - 2-1
- created specfile
