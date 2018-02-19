%global         __python                %{__python3}
%global         numix_version           1.6.1
%global         materia_version         20180110
%global         archdroid_version       1.0.2
%global         gnome_colors_version    5.5.3
%global         oomoxify_version        675fedce9a47745212b062e13a7e51b01f2bb581

Name:           oomox
Version:        1.5.0.5
Release:        1%{?dist}
Summary:        GUI for generating variations of Numix/Materia themes, gnome-colors and ArchDroid icon themes

License:        GPLv3
URL:            https://github.com/actionless/oomox
Source0:        https://github.com/actionless/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/actionless/%{name}-gtk-theme/archive/%{numix_version}.tar.gz#/%{name}-gtk-theme-%{numix_version}.tar.gz
Source2:        https://github.com/nana-4/materia-theme/archive/v%{materia_version}.tar.gz#/%{name}-materia-theme-%{materia_version}.tar.gz
Source3:        https://github.com/actionless/%{name}-archdroid-icon-theme/archive/%{archdroid_version}.tar.gz#/%{name}-archdroid-icon-theme-%{archdroid_version}.tar.gz
Source4:        https://github.com/actionless/%{name}-gnome-colors-icon-theme/archive/%{gnome_colors_version}.tar.gz#/%{name}-gnome-colors-icon-theme-%{gnome_colors_version}.tar.gz
Source5:        https://github.com/actionless/oomoxify/archive/%{oomoxify_version}.zip#/%{name}-oomoxify-%{oomoxify_version}.zip

BuildArch:      noarch
BuildRequires:  bash
BuildRequires:  bc
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
Requires:       coreutils
Requires:       grep
Requires:       glib2
Requires:       gtk-murrine-engine
Requires:       ImageMagick
Requires:       inkscape
Requires:       librsvg2
Requires:       optipng
Requires:       parallel
Requires:       polkit
Requires:       sed
Requires:       %{_bindir}/gdk-pixbuf-pixdata
Requires:       %{_bindir}/xrdb
Requires:       %{_libdir}/libgtk-3.so
%if 0%{?mageia}
Requires:       gtk2-theme-engines
Requires:       python3-gobject3
Requires:       ruby-sass
%else
Requires:       gtk2-engines
Requires:       python3-gobject
Requires:       sassc
%endif

%description
Graphical application for generating different color variations of a
Numix-based and Materia themes (GTK2, GTK3), Gnome-Colors and Archdroid icons.


%prep
%setup -q -b 0
%setup -q -b 1
%setup -q -b 2
%setup -q -b 3
%setup -q -b 4
%setup -q -b 5
cd $RPM_BUILD_DIR
cp -pr %{name}-gtk-theme-%{numix_version}/* %{name}-%{version}/plugins/theme_oomox/gtk-theme
cp -pr materia-theme-%{materia_version}/* %{name}-%{version}/plugins/theme_materia/materia-theme
cp -pr %{name}-archdroid-icon-theme-%{archdroid_version}/* %{name}-%{version}/plugins/icons_archdroid/archdroid-icon-theme
cp -pr %{name}-gnome-colors-icon-theme-%{gnome_colors_version}/* %{name}-%{version}/plugins/icons_gnomecolors/gnome-colors-icon-theme
cp -pr oomoxify-%{oomoxify_version}/* %{name}-%{version}/plugins/oomoxify


%build


%install
rm -rf $RPM_BUILD_ROOT/*
./packaging/install.sh . $RPM_BUILD_ROOT
%if 0%{?mageia}
ln -s sass $RPM_BUILD_ROOT/%{_bindir}/sassc
%endif


%files
%license LICENSE
%doc CREDITS
%doc README.md
%attr(755,root,root) %{_bindir}/*
%{_datadir}/appdata/*.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
/opt/%{name}



%changelog
* Mon Feb 19 2018 Laurent Tréguier <laurent@treguier.org> - 1.5.0.5-1
- new version

* Sat Feb 17 2018 Laurent Tréguier <laurent@treguier.org> - 1.5.0.4-1
- new version

* Fri Feb 16 2018 Laurent Tréguier <laurent@treguier.org> - 1.5.0.1-1
- new version

* Wed Feb 14 2018 Laurent Tréguier <laurent@treguier.org> - 1.5.0-2
- updated oomox-gtk-theme

* Wed Feb 14 2018 Laurent Tréguier <laurent@treguier.org> - 1.5.0-1
- new version
- fixed Mageia compatibility

* Sat Jan 06 2018 Laurent Tréguier <laurent@treguier.org> - 1.4.99-1
- new version
- removed version numbers from release

* Wed Jan 03 2018 Laurent Tréguier <laurent@treguier.org> - 1.4.5.2-1_1.4.0.1.1_20171213.1
- new version

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
