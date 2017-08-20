%global         source_name EvoPop

Name:           %{source_name}-theme
Version:        2.9.94
Release:        1%{?dist}
Summary:        Modern Desktop Theme Suite

License:        GPLv3
URL:            https://github.com/solus-project/evopop-gtk-theme
Source0:        https://github.com/solus-project/evopop-gtk-theme/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make

%description
EvoPop is a modern desktop theme suite. Its design is mostly flat with a
minimal use of shadows for depth. Requires Gtk 3.20 to function properly. The
theme is primarily build for the Solus Project, this means I can only provide
Budgie, Mate and Gnome support.
EvoPop has been developed primarily with modern GTK3 (GNOME-based) desktop
environments in mind, legacy-toolkit and GTK2 environments will not provide an
ideal experience, as much of the visual design relies on modern GTK3+ widgets.


%package -n %{source_name}-Azure-theme
Summary:        Modern Desktop Theme Suite

%description -n %{source_name}-Azure-theme
EvoPop is a modern desktop theme suite. Its design is mostly flat with a
minimal use of shadows for depth. Requires Gtk 3.20 to function properly. The
theme is primarily build for the Solus Project, this means I can only provide
Budgie, Mate and Gnome support.
EvoPop has been developed primarily with modern GTK3 (GNOME-based) desktop
environments in mind, legacy-toolkit and GTK2 environments will not provide an
ideal experience, as much of the visual design relies on modern GTK3+ widgets.


%prep
%autosetup -n evopop-gtk-theme-%{version}


%build
NOCONFIGURE=true ./autogen.sh
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license LICENSE
%doc README.md
%{_datadir}/themes/%{source_name}


%files -n %{source_name}-Azure-theme
%license LICENSE
%doc README.md
%{_datadir}/themes/%{source_name}-Azure



%changelog
* Sun Aug 20 2017 Laurent Tréguier <laurent@treguier.org> - 2.9.94-1
- new version

* Sun Aug 20 2017 Laurent Tréguier <laurent@treguier.org> - 2.9.93-1
- new version

* Fri Jul 28 2017 Laurent Tréguier <laurent@treguier.org> - 2.9.92-1
- new version

* Fri Jul 28 2017 Laurent Tréguier <laurent@treguier.org> - 2.9.91-1
- new version

* Sun Jul 09 2017 Laurent Tréguier <laurent@treguier.org> - 2.9.90-2
- split package between EvoPop and EvoPop-Azure

* Sun Jul 09 2017 Laurent Tréguier <laurent@treguier.org> - 2.9.90-1
- new version

* Sat Jul 01 2017 Laurent Tréguier <laurent@treguier.org> - 2.1.3-1
- new version

* Thu Jun 29 2017 Laurent Tréguier <laurent@treguier.org> 2.1.2-1
- created specfile
