%global         source_name         materia

Name:           %{source_name}-theme
Version:        20171213
Release:        1%{?dist}
Summary:        A Material Design-like theme for GNOME/GTK+ based desktop environments

License:        GPLv2
URL:            https://github.com/nana-4/materia-theme
Source0:        https://github.com/nana-4/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  bash
BuildRequires:  glib2-devel
BuildRequires:  %{_bindir}/gnome-shell
Requires:       gdk-pixbuf2
Requires:       gnome-themes-standard
Requires:       gtk-murrine-engine
Obsoletes:      Flat-Plat-theme         < %{version}
Obsoletes:      Flat-Plat-light-theme   < %{version}
Obsoletes:      Flat-Plat-dark-theme    < %{version}

%description
Materia is a Material Design-like theme for GNOME/GTK+ based desktop
environments. It supports GTK3, GTK2, Metacity, GNOME Shell, Unity, MATE,
LightDM, GDM, Chrome theme, etc.


%prep
%autosetup


%build


%install
rm -rf $RPM_BUILD_ROOT
cd $RPM_BUILD_DIR/%{name}-%{version}
destdir=$RPM_BUILD_ROOT ./install.sh


%files
%license COPYING
%doc README.md
%{_datadir}/themes/Materia*



%changelog
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
