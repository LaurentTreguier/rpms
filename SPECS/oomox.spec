%global         __python %{__python3}

Name:           oomox
Version:        1.2.6
Release:        1%{?dist}
Summary:        GUI for generating variations of Numix theme, gnome-colors and ArchDroid icon themes

License:        GPLv3
URL:            https://github.com/actionless/oomox
Source0:        https://github.com/actionless/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source10:       oomox-archdroid-icons-cli
Source11:       oomox-cli
Source12:       oomox-gnome-colors-icons-cli
Source13:       oomoxify-cli
Source14:       oomox-gui
Source20:       oomox.desktop

BuildArch:      noarch
BuildRequires:  bash
BuildRequires:  bc
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
Requires:       gdk-pixbuf2-devel
Requires:       glib2
Requires:       gtk-murrine-engine
Requires:       gtk2-engines
Requires:       python3-gobject
Requires:       sassc

%description
Graphical application for generating different color variations of Numix theme (GTK2, GTK3), Gnome-Colors and Archdroid icon themes.


%prep
%autosetup


%build
make -C $RPM_BUILD_DIR/%{name}-%{version} -f po.mk install


%install
rm -rf $RPM_BUILD_ROOT/*
mkdir -p $RPM_BUILD_ROOT/opt/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications
cp -R $RPM_BUILD_DIR/%{name}-%{version}/* $RPM_BUILD_ROOT/opt/%{name}
cp                              \
    %{SOURCE10}                 \
    %{SOURCE11}                 \
    %{SOURCE12}                 \
    %{SOURCE13}                 \
    %{SOURCE14}                 \
    $RPM_BUILD_ROOT/%{_bindir}
desktop-file-install --dir $RPM_BUILD_ROOT/%{_datadir}/applications %{SOURCE20}
rm $RPM_BUILD_ROOT/opt/%{name}/{CHANGES,CREDITS,PKGBUILD,circle.yml,screenshot*}


%files
%defattr(-,root,root)
%license LICENSE
%license CREDITS
%doc README.md
%doc CHANGES
/opt/%{name}
%{_datadir}/applications/%{name}.desktop
%defattr(755,root,root)
%{_bindir}/*



%changelog
* Sat May 06 2017 Laurent Tréguier <laurent@treguier.org> - 1.2.6-1
- new version

* Fri May 05 2017 Laurent Tréguier <laurent@treguier.org> - 1.2.5-1
- new version

* Fri Apr 14 2017 Laurent Tréguier <laurent@treguier.org> - 1.2.4-2
- replaced file dependencies with package dependencies
- removed RPM_SOURCE_DIR references
- changed .desktop file installation to use desktop-file-install
- added CREDITS to licenses
- added CHANGES to docs

* Sun Apr 09 2017 Laurent Tréguier <laurent@treguier.org> - 1.2.4-1
- new version
- simplified install and files sections

* Sun Apr 02 2017 Laurent Tréguier <laurent@treguier.org> - 1.2.3-1
- new version

* Sun Apr 02 2017 Laurent Tréguier <laurent@treguier.org> - 1.2.2-1
- new version

* Thu Mar 30 2017 Laurent Tréguier <laurent@treguier.org> - 1.2.1-7
- cleaned up specfile a bit

* Thu Mar 16 2017 Laurent Tréguier <laurent@treguier.org> - 1.2.1-6
- attempt to fix EPEL build

* Wed Mar 15 2017 Laurent Tréguier <laurent@treguier.org> - 1.2.1-5
- replaced macros with $RPM_*

* Sun Mar 12 2017 Laurent Tréguier <laurent@treguier.org> - 1.2.1-4
- updated specfile

* Thu Mar 09 2017 Laurent Tréguier <laurent@treguier.org> - 1.2.1-3
- rebuilt
