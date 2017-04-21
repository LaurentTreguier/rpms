%global         source_name         Flat-Plat
%global         source_name_light   %{source_name}-light
%global         source_name_dark    %{source_name}-dark

Name:           %{source_name}-theme
Version:        20170323
Release:        4%{?dist}
Summary:        A Material Design-like theme for GNOME/GTK+ based desktop environments

License:        GPLv2
URL:            https://github.com/nana-4/Flat-Plat
Source0:        https://github.com/nana-4/%{source_name}/archive/v%{version}.tar.gz#/%{source_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  bash
BuildRequires:  glib2-devel
Requires:       gdk-pixbuf2
Requires:       gnome-themes-standard
Requires:       gtk-murrine-engine

%description
Flat-Plat is a Material Design-like theme for GNOME/GTK+ based desktop environments.
It supports GTK3, GTK2, Metacity, GNOME Shell, Unity, MATE, LightDM, GDM, Chrome theme, etc.


%package -n %{source_name_light}-theme
Summary:        A Material Design-like theme for GNOME/GTK+ based desktop environments

%description -n %{source_name_light}-theme
Flat-Plat is a Material Design-like theme for GNOME/GTK+ based desktop environments.
It supports GTK3, GTK2, Metacity, GNOME Shell, Unity, MATE, LightDM, GDM, Chrome theme, etc.


%package -n %{source_name_dark}-theme
Summary:        A Material Design-like theme for GNOME/GTK+ based desktop environments

%description -n %{source_name_dark}-theme
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
%license COPYING
%doc README.md
%{_datadir}/themes/%{source_name}
%{_datadir}/themes/%{source_name}-compact


%files -n %{source_name_light}-theme
%license COPYING
%doc README.md
%{_datadir}/themes/%{source_name_light}
%{_datadir}/themes/%{source_name_light}-compact


%files -n %{source_name_dark}-theme
%license COPYING
%doc README.md
%{_datadir}/themes/%{source_name_dark}
%{_datadir}/themes/%{source_name_dark}-compact



%changelog
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
