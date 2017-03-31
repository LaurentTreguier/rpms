%global         source_name Flat-Plat

Name:           %{source_name}-theme
Version:        20170323
Release:        2%{?dist}
Summary:        A Material Design-like theme for GNOME/GTK+ based desktop environments

License:        GPLv2
URL:            https://github.com/nana-4/Flat-Plat
Source0:        https://github.com/nana-4/%{source_name}/archive/v%{version}.tar.gz#/%{source_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  %{_bindir}/bash
BuildRequires:  %{_bindir}/glib-compile-resources
Requires:       gdk-pixbuf2
Requires:       gnome-themes-standard
Requires:       gtk-murrine-engine

%description
Flat-Plat is a Material Design-like theme for GNOME/GTK+ based desktop environments.
It supports GTK3, GTK2, Metacity, GNOME Shell, Unity, MATE, LightDM, GDM, Chrome theme, etc.


%prep
%autosetup -n %{source_name}-%{version}


%build


%install
rm -rf $RPM_BUILD_ROOT
cd $RPM_BUILD_DIR/%{source_name}-%{version}
destdir=$RPM_BUILD_ROOT ./install.sh


%files
%{_datadir}/themes/%{source_name}*



%changelog
* Sat Mar 25 2017 Laurent Tréguier <laurent@treguier.org> - 20170323-2
- added glib-compile-resources dependency to fix .gresource files not being built

* Thu Mar 23 2017 Laurent Tréguier <laurent@treguier.org> - 20170323-1
- new version

* Wed Mar 22 2017 Laurent Tréguier <laurent@treguier.org>
- created specfile
