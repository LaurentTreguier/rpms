%global         source_name capitaine-cursors
%global         git_date    20200223
%global         git_commit  f6281e892772b115cb7492d55979d80ee8df6952

Name:           la-capitaine-cursor-theme
Version:        4
Release:        2.%{git_date}%{?dist}
Summary:        An x-cursor theme inspired by macOS and based on KDE Breeze

License:        LGPLv3
URL:            https://krourke.org/projects/art/%{source_name}
Source0:        https://github.com/keeferrourke/%{source_name}/archive/%{git_commit}.tar.gz#/%{name}-%{git_commit}.tar.gz

BuildArch:      noarch
BuildRequires:  bc
BuildRequires:  inkscape
BuildRequires:  %{_bindir}/xcursorgen

%description
An x-cursor theme inspired by macOS and based on KDE Breeze.
Designed to pair well with the associated icon pack, La Capitaine.


%prep
%autosetup -n %{source_name}-%{git_commit}


%build
for theme in light dark
do
    ./build.sh --max-dpi xxxhd --type $theme
done


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p "$RPM_BUILD_ROOT/%{_datadir}/icons"
cp -R $RPM_BUILD_DIR/%{source_name}-%{git_commit}/dist/light "$RPM_BUILD_ROOT/%{_datadir}/icons/La Capitaine Cursors"
cp -R $RPM_BUILD_DIR/%{source_name}-%{git_commit}/dist/dark "$RPM_BUILD_ROOT/%{_datadir}/icons/La Capitaine Cursors (Dark)"


%files
%license COPYING
%doc README.md
"%{_datadir}/icons/La Capitaine Cursors"
"%{_datadir}/icons/La Capitaine Cursors (Dark)"



%changelog
* Sun Feb 23 2020 Laurent Tréguier <laurent@treguier.org> - 4-2.20200223
- new release

* Fri Feb 21 2020 Laurent Tréguier <laurent@treguier.org> - 4-1
- new version

* Thu Mar 07 2019 Laurent Tréguier <laurent@treguier.org> - 3-1
- new version

* Wed Jan 17 2018 Laurent Tréguier <laurent@treguier.org> - 2.1.20171126-1
- new version
- fixed missing inkscape dependency (I never noticed the package was never working...)

* Wed Oct 18 2017 Laurent Tréguier <laurent@treguier.org> - 2.1-1
- new version

* Wed Mar 15 2017 Laurent Tréguier <laurent@treguier.org> - 2-1
- created specfile
