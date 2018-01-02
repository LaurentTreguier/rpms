%global         __python                %{__python3}
%global         numix_version           1.4.0.1
%global         materia_version         20171213
%global         archdroid_version       1bf91f49f76112d48415bfa997aabc2cea84f01d
%global         gnome_colors_version    3c8596ea630b8255b9cf5d5bf90a69658dd32b79
%global         oomoxify_version        5640e1c2323a319ede50b24b2d2f45b49e76e112

Name:           oomox
Version:        1.4.5.1
Release:        1_%{numix_version}.1_%{materia_version}.1%{?dist}
Summary:        GUI for generating variations of Numix/Materia themes, gnome-colors and ArchDroid icon themes

License:        GPLv3
URL:            https://github.com/actionless/oomox
Source0:        https://github.com/actionless/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/actionless/%{name}-gtk-theme/archive/%{numix_version}.tar.gz#/%{name}-gtk-theme-%{numix_version}.tar.gz
Source2:        https://github.com/nana-4/materia-theme/archive/v%{materia_version}.tar.gz#/%{name}-materia-theme-%{materia_version}.tar.gz
Source3:        https://github.com/actionless/%{name}-archdroid-icon-theme/archive/%{archdroid_version}.zip#/%{name}-archdroid-icon-theme-%{archdroid_version}.zip
Source4:        https://github.com/actionless/%{name}-gnome-colors-icon-theme/archive/%{gnome_colors_version}.zip#/%{name}-gnome-colors-icon-theme-%{gnome_colors_version}.zip
Source5:        https://github.com/actionless/oomoxify/archive/%{oomoxify_version}.zip#/%{name}-oomoxify-%{oomoxify_version}.zip

BuildArch:      noarch
BuildRequires:  bash
BuildRequires:  bc
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
Requires:       coreutils
Requires:       grep
Requires:       gdk-pixbuf2-devel
Requires:       glib2
Requires:       gtk-murrine-engine
Requires:       gtk2-engines
Requires:       ImageMagick
Requires:       inkscape
Requires:       optipng
Requires:       parallel
Requires:       polkit
Requires:       python3-gobject
Requires:       sassc
Requires:       sed
Requires:       xorg-x11-server-utils

%description
Graphical application for generating different color variations of a
Numix-based and Materia themes (GTK2, GTK3), Gnome-Colors and Archdroid icons.


%prep
%autosetup -b 0
%autosetup -b 1
%autosetup -b 2
%autosetup -b 3
%autosetup -b 4
%autosetup -b 5
cp -pr $RPM_BUILD_DIR/%{name}-gtk-theme-%{numix_version}/* $RPM_BUILD_DIR/%{name}-%{version}/gtk-theme
cp -pr $RPM_BUILD_DIR/materia-theme-%{materia_version}/* $RPM_BUILD_DIR/%{name}-%{version}/materia-theme
cp -pr $RPM_BUILD_DIR/%{name}-archdroid-icon-theme-%{archdroid_version}/* $RPM_BUILD_DIR/%{name}-%{version}/archdroid-icon-theme
cp -pr $RPM_BUILD_DIR/%{name}-gnome-colors-icon-theme-%{gnome_colors_version}/* $RPM_BUILD_DIR/%{name}-%{version}/gnome-colors-icon-theme
cp -pr $RPM_BUILD_DIR/oomoxify-%{oomoxify_version}/* $RPM_BUILD_DIR/%{name}-%{version}/oomoxify


%build


%install
rm -rf $RPM_BUILD_ROOT/*
./packaging/install.sh . $RPM_BUILD_ROOT


%files
%license LICENSE
%doc CREDITS
%doc README.md
%attr(755,root,root) %{_bindir}/*
%{_datadir}/applications/%{name}.desktop
/opt/%{name}



%changelog
* Tue Jan 02 2018 Laurent Tréguier <laurent@treguier.org> - 1.4.5.1-1_1.4.0.1.1_20171213.1
- new version

* Mon Jan 01 2018 Laurent Tréguier <laurent@treguier.org> - 1.4.5-1_1.3.1.1.1_20171213.1
- new version

* Sat Dec 23 2017 Laurent Tréguier <laurent@treguier.org> - 1.4.4.1-2_1.3.1.1.1_20171213.1
- fixed missing oomoxify submodule

* Sat Dec 23 2017 Laurent Tréguier <laurent@treguier.org> - 1.4.4.1-1_1.3.1.1.1_20171213.1
- new version

* Sat Dec 16 2017 Laurent Tréguier <laurent@treguier.org> - 1.4.3-1_1.3.0.1_20171213.1
- updated Numix and Materia

* Sun Dec 03 2017 Laurent Tréguier <laurent@treguier.org> - 1.4.3-1_1.2.9.1_20171112.1
- updated Numix

* Mon Nov 13 2017 Laurent Tréguier <laurent@treguier.org> - 1.4.2-1_1.2.8.1.1_20171112.1
- updated Materia

* Sun Nov 05 2017 Laurent Tréguier <laurent@treguier.org> - 1.4.2-1_1.2.8.1.1_20171005.1
- new version

* Sun Oct 01 2017 Laurent Tréguier <laurent@treguier.org> - 1.4.1-1_1.2.8.1.1_20170917.1
- new version

* Fri Sep 29 2017 Laurent Tréguier <laurent@treguier.org> - 1.4.0-1_1.2.8.1.1_20170917.1
- new version

* Sun Sep 17 2017 Laurent Tréguier <laurent@treguier.org> - 1.3.1-1_1.2.8.1.1_20170917.1
- updated Flat-Plat

* Sat Sep 16 2017 Laurent Tréguier <laurent@treguier.org> - 1.3.1-1_1.2.8.1.1_20170916.2
- fixed Flat-Plat source

* Sat Sep 16 2017 Laurent Tréguier <laurent@treguier.org> - 1.3.1-1_1.2.8.1.1_20170916.1
- updated Flat-Plat

* Sat Sep 16 2017 Laurent Tréguier <laurent@treguier.org> - 1.3.1-1_1.2.8.1.1_20170916gitbb04ec9.1
- updated Flat-Plat

* Thu Sep 14 2017 Laurent Tréguier <laurent@treguier.org> - 1.3.1-1_1.2.8.1.1_20170913git0c915c2.1
- updated Flat-Plat

* Sat Sep 09 2017 Laurent Tréguier <laurent@treguier.org> - 1.3.1-1_1.2.8.1.1_20170909gita96196d.1
- new version
- updated Flat-Plat

* Sat Sep 02 2017 Laurent Tréguier <laurent@treguier.org> - 1.3.0-1_1.2.8.1.1_20170902git0ed1caf.1
- updated Flat-Plat

* Mon Aug 28 2017 Laurent Tréguier <laurent@treguier.org> - 1.3.0-1_1.2.8.1.1_20170827git96bffc0.1
- updated Flat-Plat to a functional version

* Mon Aug 28 2017 Laurent Tréguier <laurent@treguier.org> - 1.3.0-1_1.2.8.1.1_20170605.1
- new version

* Sun Aug 20 2017 Laurent Tréguier <laurent@treguier.org> - 1.2.8.1-1
- new version

* Sat Jul 22 2017 Laurent Tréguier <laurent@treguier.org> - 1.2.8-2
- fixed ImageMagick dependency

* Wed Jul 19 2017 Laurent Tréguier <laurent@treguier.org> - 1.2.8-1
- new version

* Tue Jul 18 2017 Laurent Tréguier <laurent@treguier.org> - 1.2.7-1
- new version
- added some dependencies

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
