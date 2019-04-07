%global         __python                            %{__python3}
%global         numix_theme_version                 1.10
%global         materia_theme_version               20190315
%global         arc_theme_version                   20190330
%global         archdroid_icons_version             1.0.2
%global         gnome_colors_icons_version          5.5.5
%global         oomoxify_version                    1.1.2
%global         base16_commit                       2e4112fe859ed5d33f67c177f11d369d360db9ae
%global         numix_icons_commit                  88ba3654506c73f77a28629d863d1e23a553bff7
%global         numix_folders_icons_commit          24e5f6c6603e7f798553d2f24a00de107713c333
%global         papirus_icons_version               20190331
%global         suru_plus_icons_version             25.3
%global         suru_plus_aspromauros_icons_version 2.1

Name:           oomox
Version:        1.12.2
Release:        4%{?dist}
Summary:        GUI and command line tool for generating variations of various GTK and icon themes

License:        GPLv3
URL:            https://github.com/themix-project/oomox
Source0:        https://github.com/themix-project/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/themix-project/%{name}-gtk-theme/archive/%{numix_theme_version}.tar.gz#/%{name}-gtk-theme-%{numix_theme_version}.tar.gz
Source2:        https://github.com/nana-4/materia-theme/archive/v%{materia_theme_version}.tar.gz#/%{name}-materia-theme-%{materia_theme_version}.tar.gz
Source3:        https://github.com/NicoHood/arc-theme/archive/%{arc_theme_version}.tar.gz#/%{name}-arc-theme-%{arc_theme_version}.tar.gz
Source4:        https://github.com/themix-project/%{name}-archdroid-icon-theme/archive/%{archdroid_icons_version}.tar.gz#/%{name}-archdroid-icon-theme-%{archdroid_icons_version}.tar.gz
Source5:        https://github.com/themix-project/%{name}-gnome-colors-icon-theme/archive/%{gnome_colors_icons_version}.tar.gz#/%{name}-gnome-colors-icon-theme-%{gnome_colors_icons_version}.tar.gz
Source6:        https://github.com/themix-project/oomoxify/archive/%{oomoxify_version}.tar.gz#/%{name}-oomoxify-%{oomoxify_version}.tar.gz
Source7:        https://github.com/themix-project/base16_mirror/archive/%{base16_commit}.tar.gz#/%{name}-base16_mirror-%{base16_commit}.tar.gz
Source8:        https://github.com/numixproject/numix-icon-theme/archive/%{numix_icons_commit}.tar.gz#/%{name}-numix-icon-theme-%{numix_icons_commit}.tar.gz
Source9:        https://github.com/numixproject/numix-folders/archive/%{numix_folders_icons_commit}.tar.gz#/%{name}-numix-folders-%{numix_folders_icons_commit}.tar.gz
Source10:       https://github.com/PapirusDevelopmentTeam/papirus-icon-theme/archive/%{papirus_icons_version}.tar.gz#/%{name}-papirus-icon-theme-%{papirus_icons_version}.tar.gz
Source11:       https://github.com/gusbemacbe/suru-plus/archive/v%{suru_plus_icons_version}.tar.gz#/%{name}-suru-plus-icon-theme-%{suru_plus_icons_version}.tar.gz
Source12:       https://github.com/gusbemacbe/suru-plus-aspromauros/archive/v%{suru_plus_aspromauros_icons_version}.tar.gz#/%{name}-suru-plus-aspromauros-icon-theme-%{suru_plus_icons_version}.tar.gz

BuildArch:      noarch
BuildRequires:  bash
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  pkgconfig(python3)
Requires:       bc
Requires:       bash
Requires:       coreutils
Requires:       findutils
Requires:       grep
Requires:       ImageMagick
Requires:       inkscape
Requires:       librsvg2
Requires:       make
Requires:       optipng
Requires:       polkit
Requires:       sed
Requires:       zip
Requires:       /%{python3_sitearch}/gi
Requires:       /%{python3_sitearch}/PIL
Requires:       /%{python3_sitearch}/yaml
Requires:       /%{python3_sitelib}/pystache
Requires:       %{_bindir}/gdk-pixbuf-pixdata
Requires:       %{_bindir}/parallel
Requires:       %{_bindir}/xrdb
Requires:       %{_libdir}/libglib-2.0.so.0
Requires:       %{_libdir}/libgtk-3.so
Requires:       %{_datadir}/gtk-engines/murrine.xml
Requires:       %{name}-theme-arc
Requires:       %{name}-theme-materia
Requires:       %{name}-theme-oomox
Requires:       %{name}-icons-archdroid
Requires:       %{name}-icons-gnome-colors
Requires:       %{name}-icons-numix
Requires:       %{name}-icons-papirus
Requires:       %{name}-icons-suru-plus
Requires:       %{name}-icons-suru-plus-aspromauros

%if 0%{?mageia}
Requires:       gtk2-theme-engines
Requires:       ruby-sass
%else
Requires:       gtk2-engines
Requires:       sassc
%endif

%if 0%{?fedora}%{?mageia}
Recommends:     python3-colorthief
Recommends:     python3-colorz
Recommends:     python3-haishoku
%endif

AutoReq:        no

%description
Themix: GUI for generating different color variations of Arc, Materia, Oomox
themes (GTK2, GTK3, Cinnamon, GNOME, MATE, Openbox, Xfwm), ArchDroid,
Gnome-Colors, Numix, Papirus icon themes, and terminal palettes.


%package theme-arc
Summary:        Arc theme plugin for Oomox
Requires:       %{name}

%description theme-arc
Sources of Arc theme used by Oomox


%package theme-materia
Summary:        Materia theme plugin for Oomox
Requires:       %{name}

%description theme-materia
Sources of Materia theme used by Oomox


%package theme-oomox
Summary:        Oomox theme plugin for Oomox
Requires:       %{name}

%description theme-oomox
Sources of Oomox theme used by Oomox


%package icons-archdroid
Summary:        Archdroid icon theme plugins for Oomox
Requires:       %{name}

%description icons-archdroid
Sources of Archdroid icon theme used by Oomox


%package icons-gnome-colors
Summary:        Gnome Colors icon theme plugins for Oomox
Requires:       %{name}

%description icons-gnome-colors
Sources of Gnome Colors icon theme used by Oomox


%package icons-numix
Summary:        Numix icon theme plugins for Oomox
Requires:       %{name}

%description icons-numix
Sources of Numix icon theme used by Oomox


%package icons-papirus
Summary:        Papirus icon theme plugins for Oomox
Requires:       %{name}

%description icons-papirus
Sources of Papirus icon theme used by Oomox


%package icons-suru-plus
Summary:        Suru Plus icon theme plugins for Oomox
Requires:       %{name}

%description icons-suru-plus
Sources of Suru Plus icon theme used by Oomox


%package icons-suru-plus-aspromauros
Summary:        Suru Plus Aspromauros icon theme plugins for Oomox
Requires:       %{name}

%description icons-suru-plus-aspromauros
Sources of Suru Plus Aspromauros icon theme used by Oomox


%prep
%setup -q -b 0
%setup -q -b 1
%setup -q -b 2
%setup -q -b 3
%setup -q -b 4
%setup -q -b 5
%setup -q -b 6
%setup -q -b 7
%setup -q -b 8
%setup -q -b 9
%setup -q -b 10
%setup -q -b 11
%setup -q -b 12
cd $RPM_BUILD_DIR
cp -pr %{name}-gtk-theme-%{numix_theme_version}/* %{name}-%{version}/plugins/theme_oomox/gtk-theme
cp -pr materia-theme-%{materia_theme_version}/* %{name}-%{version}/plugins/theme_materia/materia-theme
cp -pr arc-theme-%{arc_theme_version}/* %{name}-%{version}/plugins/theme_arc/arc-theme
cp -pr archdroid-icon-theme-%{archdroid_icons_version}/* %{name}-%{version}/plugins/icons_archdroid/archdroid-icon-theme
cp -pr gnome-colors-icon-theme-%{gnome_colors_icons_version}/* %{name}-%{version}/plugins/icons_gnomecolors/gnome-colors-icon-theme
cp -pr oomoxify-%{oomoxify_version}/* %{name}-%{version}/plugins/oomoxify
cp -pr base16_mirror-%{base16_commit}/* %{name}-%{version}/plugins/base16/base16_mirror
cp -pr numix-icon-theme-%{numix_icons_commit}/* %{name}-%{version}/plugins/icons_numix/numix-icon-theme
cp -pr numix-folders-%{numix_folders_icons_commit}/* %{name}-%{version}/plugins/icons_numix/numix-folders
cp -pr papirus-icon-theme-%{papirus_icons_version}/* %{name}-%{version}/plugins/icons_papirus/papirus-icon-theme
cp -pr suru-plus-%{suru_plus_icons_version}/* %{name}-%{version}/plugins/icons_suruplus/suru-plus
cp -pr suru-plus-aspromauros-%{suru_plus_aspromauros_icons_version}/* %{name}-%{version}/plugins/icons_suruplus_aspromauros/suru-plus-aspromauros


%build


%install
rm -rf $RPM_BUILD_ROOT/*
install -d $RPM_BUILD_ROOT/%{_bindir}
%make_install APPDIR=/opt/%{name} PREFIX=%{_prefix} . $RPM_BUILD_ROOT
%if 0%{?mageia}
ln -s sass $RPM_BUILD_ROOT/%{_bindir}/sassc
%endif


%files
%license /opt/%{name}/LICENSE
%license /opt/%{name}/CREDITS
%doc /opt/%{name}/README.md
%attr(755,root,root) %{_bindir}/oomox*
%if 0%{?mageia}
%{_bindir}/sassc
%endif
%{_datadir}/appdata/*.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
/opt/%{name}/colors
/opt/%{name}/locale
/opt/%{name}/oomox_gui
/opt/%{name}/po
/opt/%{name}/scripted_colors
/opt/%{name}/terminal_templates
/opt/%{name}/gui.sh
/opt/%{name}/plugins/base16
/opt/%{name}/plugins/import_pil
/opt/%{name}/plugins/import_random
/opt/%{name}/plugins/oomoxify


%files theme-arc
/opt/%{name}/plugins/theme_arc


%files theme-materia
/opt/%{name}/plugins/theme_materia


%files theme-oomox
/opt/%{name}/plugins/theme_oomox


%files icons-archdroid
/opt/%{name}/plugins/icons_archdroid


%files icons-gnome-colors
/opt/%{name}/plugins/icons_gnomecolors


%files icons-numix
/opt/%{name}/plugins/icons_numix


%files icons-papirus
/opt/%{name}/plugins/icons_papirus


%files icons-suru-plus
/opt/%{name}/plugins/icons_suruplus


%files icons-suru-plus-aspromauros
/opt/%{name}/plugins/icons_suruplus_aspromauros



%changelog
* Sun Apr 07 2019 Laurent Tréguier <laurent@treguier.org> - 1.12.2-4
- split into multiple subpackages

* Sun Apr 07 2019 Laurent Tréguier <laurent@treguier.org>
- updated suru-plus-icon-theme
- added suru-plus-aspromauros-icon plugin

* Sun Apr 07 2019 Laurent Tréguier <laurent@treguier.org> - 1.12.2-2
- Fixed build on Mageia and EPEL

* Sun Apr 07 2019 Laurent Tréguier <laurent@treguier.org> - 1.12.2-1
- new version

* Mon Apr 01 2019 Laurent Tréguier <laurent@treguier.org> - 1.12.1-3
- updated papirus-icon-theme

* Sat Mar 30 2019 Laurent Tréguier <laurent@treguier.org> - 1.12.1-2
- updated arc-theme

* Thu Mar 21 2019 Laurent Tréguier <laurent@treguier.org> - 1.12.1-1
- new version

* Sat Mar 16 2019 Laurent Tréguier <laurent@treguier.org> - 1.12-2
- updated materia-theme

* Mon Mar 11 2019 Laurent Tréguier <laurent@treguier.org> - 1.12-1
- new version
- updated numix-icon-theme

* Sat Mar 02 2019 Laurent Tréguier <laurent@treguier.org> - 1.11-5
- updated papirus-icon-theme

* Thu Feb 14 2019 Laurent Tréguier <laurent@treguier.org> - 1.11-4
- updated arc-theme

* Wed Feb 13 2019 Laurent Tréguier <laurent@treguier.org> - 1.11-3
- updated arc-theme

* Sun Feb 10 2019 Laurent Tréguier <laurent@treguier.org> - 1.11-2
- updated materia-theme
- updated arc-theme
- updated papirus-icon-theme

* Mon Jan 28 2019 Laurent Tréguier <laurent@treguier.org> - 1.11-1
- new version

* Wed Jan 09 2019 Laurent Tréguier <laurent@treguier.org> - 1.10-3
- updated gnome-colors-icon-theme

* Fri Jan 04 2019 Laurent Tréguier <laurent@treguier.org> - 1.10-2
- fixed build on EPEL

* Fri Jan 04 2019 Laurent Tréguier <laurent@treguier.org> - 1.10-1
- new version
- updated oomoxify

* Wed Jan 02 2019 Laurent Tréguier <laurent@treguier.org> - 1.9.0.2-4
- updated oomox-gtk-theme
- updated materia-theme

* Sat Dec 29 2018 Laurent Tréguier <laurent@treguier.org> - 1.9.0.2-3
- updated oomox-gtk-theme
- updated oomoxify

* Thu Dec 27 2018 Laurent Tréguier <laurent@treguier.org> - 1.9.0.2-2
- added numix plugin

* Wed Dec 26 2018 Laurent Tréguier <laurent@treguier.org> - 1.9.0.2-1
- new version

* Sun Dec 23 2018 Laurent Tréguier <laurent@treguier.org> - 1.8.0.3-1
- new version
- updated oomox-gtk-theme
- updated arc-theme
- updated gnome-colors-icon-theme

* Sun Dec 09 2018 Laurent Tréguier <laurent@treguier.org> - 1.7.2.3-1
- new version
- updated materia-theme

* Fri Dec 07 2018 Laurent Tréguier <laurent@treguier.org> - 1.7.2.2-1
- new version

* Mon Nov 26 2018 Laurent Tréguier <laurent@treguier.org> - 1.7.2.1-3
- fixed murrine engine dependency

* Mon Nov 26 2018 Laurent Tréguier <laurent@treguier.org> - 1.7.2.1-2
- added new optional dependencies

* Mon Nov 26 2018 Laurent Tréguier <laurent@treguier.org> - 1.7.2.1-1
- new version

* Sun Nov 25 2018 Laurent Tréguier <laurent@treguier.org> - 1.7.1.3-2
- updated materia-theme

* Wed Nov 21 2018 Laurent Tréguier <laurent@treguier.org> - 1.7.1.3-1
- new version

* Sun Nov 18 2018 Laurent Tréguier <laurent@treguier.org> - 1.7.1.1-1
- new version

* Sun Nov 18 2018 Laurent Tréguier <laurent@treguier.org> - 1.7.1-1
- new version

* Thu Oct 18 2018 Laurent Tréguier <laurent@treguier.org> - 1.7.0.6-1
- new version

* Wed Oct 10 2018 Laurent Tréguier <laurent@treguier.org> - 1.7.0.5-2
- updated oomox-gtk-theme

* Wed Oct 03 2018 Laurent Tréguier <laurent@treguier.org> - 1.7.0.5-1
- new version

* Wed Sep 26 2018 Laurent Tréguier <laurent@treguier.org> - 1.7.0.4-1
- new version

* Sun Sep 23 2018 Laurent Tréguier <laurent@treguier.org> - 1.7.0.3-1
- new version
- switched to upstream repos for materia and arc themes

* Sun Aug 26 2018 Laurent Tréguier <laurent@treguier.org> - 1.7.0.2-5
- added base16 submodule

* Fri Aug 24 2018 Laurent Tréguier <laurent@treguier.org> - 1.7.0.2-4
- downgraded oomoxify

* Fri Aug 17 2018 Laurent Tréguier <laurent@treguier.org> - 1.7.0.2-3
- updated oomoxify

* Tue Aug 14 2018 Laurent Tréguier <laurent@treguier.org> - 1.7.0.2-2
- updated numix

* Sun Aug 12 2018 Laurent Tréguier <laurent@treguier.org> - 1.7.0.2-1
- new version

* Fri Aug 10 2018 Laurent Tréguier <laurent@treguier.org> - 1.7.0.1-1
- new version

* Wed Aug 01 2018 Laurent Tréguier <laurent@treguier.org> - 1.6.2.1-1
- new version

* Mon Jul 30 2018 Laurent Tréguier <laurent@treguier.org> - 1.6.2-2
- fixed build on EPEL 6

* Mon Jul 30 2018 Laurent Tréguier <laurent@treguier.org> - 1.6.2-1
- new version

* Tue May 08 2018 Laurent Tréguier <laurent@treguier.org> - 1.6.1-2
- fixed Fedora 28 compatibility

* Fri Mar 30 2018 Laurent Tréguier <laurent@treguier.org> - 1.6.1-1
- new version
- updated dependencies to match upstream better

* Fri Mar 16 2018 Laurent Tréguier <laurent@treguier.org> - 1.6.0-2
- switched to tagged oomoxify

* Fri Mar 16 2018 Laurent Tréguier <laurent@treguier.org> - 1.6.0-1
- new version

* Mon Feb 19 2018 Laurent Tréguier <laurent@treguier.org> - 1.5.0.5-2
- fixed build on EPEL 7

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
