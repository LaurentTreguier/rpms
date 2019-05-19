%global         source_name materia-theme

Name:           materia-gtk-theme
Version:        20190315
Release:        2%{?dist}
Summary:        A Material Design-like theme for GNOME/GTK+ based desktop environments

License:        GPLv2
URL:            https://github.com/nana-4/%{source_name}
Source0:        https://github.com/nana-4/%{source_name}/archive/v%{version}.tar.gz#/%{source_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  bash
BuildRequires:  bc
Requires:       %{_bindir}/glib-compile-resources
Requires:       %{_datadir}/gtk-engines/murrine.xml
%if 0%{?suse_version}
Requires:       gnome-themes-extras
%else
Requires:       gnome-themes-extra
%endif
Obsoletes:      materia-theme   < %{version}-%{release}

%description
Materia is a Material Design-like theme for GNOME/GTK+ based desktop
environments. It supports GTK3, GTK2, Metacity, GNOME Shell, Unity, MATE,
LightDM, GDM, Chrome theme, etc.


%prep
%autosetup -n %{source_name}-%{version}


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/themes
cd $RPM_BUILD_DIR/%{source_name}-%{version}
./install.sh --dest $RPM_BUILD_ROOT/%{_datadir}/themes


%files
%license COPYING
%doc README.md
%{_datadir}/themes/*



%changelog
* Sun May 19 2019 Laurent Tréguier <laurent@treguier.org> - 20190315-2
- changed name to materia-gtk-theme for consistency with other distros

* Sat Mar 16 2019 Laurent Tréguier <laurent@treguier.org> - 20190315-1
- new version

* Sat Feb 02 2019 Laurent Tréguier <laurent@treguier.org> - 20190201-1
- new version

* Sun Nov 25 2018 Laurent Tréguier <laurent@treguier.org> - 20181125-2
- fixed murrine engine dependency

* Sun Nov 25 2018 Laurent Tréguier <laurent@treguier.org> - 20181125-1
- new version

* Thu Nov 15 2018 Laurent Tréguier <laurent@treguier.org> - 20181115-1
- new version

* Sun Sep 30 2018 Laurent Tréguier <laurent@treguier.org> - 20180928-1
- new version

* Sun Sep 23 2018 Laurent Tréguier <laurent@treguier.org> - 20180922-1
- new version

* Sat May 19 2018 Laurent Tréguier <laurent@treguier.org> - 20180519-1
- new version

* Wed Mar 21 2018 Laurent Tréguier <laurent@treguier.org> - 20180321-1
- new version

* Sun Mar 11 2018 Laurent Tréguier <laurent@treguier.org> - 20180311-1
- new version

* Wed Jan 10 2018 Laurent Tréguier <laurent@treguier.org> - 20180110-1
- new version

* Wed Dec 13 2017 Laurent Tréguier <laurent@treguier.org> - 20171213-1
- new version

* Mon Nov 13 2017 Laurent Tréguier <laurent@treguier.org> - 20171112-1
- new version

* Thu Oct 05 2017 Laurent Tréguier <laurent@treguier.org> - 20171005-1
- new version
- renamed package to materia-theme
- merged all variants of the theme

* Sun Sep 17 2017 Laurent Tréguier <laurent@treguier.org> - 20170917-1
- new version

* Sat Sep 16 2017 Laurent Tréguier <laurent@treguier.org> - 20170916-1
- new version
- added gnome-shell build dependency

* Mon Jun 05 2017 Laurent Tréguier <laurent@treguier.org> - 20170605-1
- new version

* Mon May 15 2017 Laurent Tréguier <laurent@treguier.org> - 20170515-1
- new version

* Fri Apr 21 2017 Laurent Tréguier <laurent@treguier.org> - 20170323-4
- split normal, light and dark themes into subpackages

* Thu Apr 20 2017 Laurent Tréguier <laurent@treguier.org> - 20170323-3
- moved file dependencies to package dependencies
- added license and doc

* Sat Mar 25 2017 Laurent Tréguier <laurent@treguier.org> - 20170323-2
- added glib-compile-resources dependency to fix .gresource files not being built

* Thu Mar 23 2017 Laurent Tréguier <laurent@treguier.org> - 20170323-1
- new version

* Wed Mar 22 2017 Laurent Tréguier <laurent@treguier.org> - 20170307-1
- created specfile
