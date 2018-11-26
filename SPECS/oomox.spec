%global         __python                %{__python3}
%global         numix_version           1.9.2
%global         materia_version         20181125
%global         arc_commit              e97206cf0772da5b07b982da67cc65d91884d48d
%global         archdroid_version       1.0.2
%global         gnome_colors_version    5.5.3
%global         oomoxify_version        1.1
%global         base16_commit           d022b9daa5c233a08a8d3b94fd534a3041e3a8c1

Name:           oomox
Version:        1.7.2.1
Release:        3%{?dist}
Summary:        GUI for generating variations of Numix/Materia/Arc themes, gnome-colors and ArchDroid icon themes

License:        GPLv3
URL:            https://github.com/themix-project/oomox
Source0:        https://github.com/themix-project/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/themix-project/%{name}-gtk-theme/archive/%{numix_version}.tar.gz#/%{name}-gtk-theme-%{numix_version}.tar.gz
Source2:        https://github.com/nana-4/materia-theme/archive/v%{materia_version}.tar.gz#/%{name}-materia-theme-%{materia_version}.tar.gz
Source3:        https://github.com/NicoHood/arc-theme/archive/%{arc_commit}.tar.gz#/%{name}-arc-theme-%{arc_commit}.tar.gz
Source4:        https://github.com/themix-project/%{name}-archdroid-icon-theme/archive/%{archdroid_version}.tar.gz#/%{name}-archdroid-icon-theme-%{archdroid_version}.tar.gz
Source5:        https://github.com/themix-project/%{name}-gnome-colors-icon-theme/archive/%{gnome_colors_version}.tar.gz#/%{name}-gnome-colors-icon-theme-%{gnome_colors_version}.tar.gz
Source6:        https://github.com/themix-project/oomoxify/archive/%{oomoxify_version}.tar.gz#/%{name}-oomoxify-%{oomoxify_version}.tar.gz
Source7:        https://github.com/base16-builder/base16-builder/archive/%{base16_commit}.tar.gz#/%{name}-oomoxify-%{base16_commit}.tar.gz

BuildArch:      noarch
BuildRequires:  bash
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
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
Requires:       python3-imaging
Requires:       sed
Requires:       zip
Requires:       %{_bindir}/gdk-pixbuf-pixdata
Requires:       %{_bindir}/parallel
Requires:       %{_bindir}/xrdb
Requires:       %{_libdir}/libglib-2.0.so.0
Requires:       %{_libdir}/libgtk-3.so
Requires:       %{_datadir}/gtk-engines/murrine.xml

%if 0%{?mageia}
Requires:       gtk2-theme-engines
Requires:       python3-gobject3
Requires:       ruby-sass
%else
Requires:       gtk2-engines
Requires:       sassc
%if 0%{?fedora}
Requires:       python3-gobject
%else
Requires:       python34-gobject
%endif
%endif

%if 0%{?fedora}%{?mageia}
Recommends:     python3-colorthief
Recommends:     python3-colorz
Recommends:     python3-haishoku
%endif

AutoReq:        no

%description
Graphical application for generating different color variations of a
Numix-based, Materia and Arc themes (GTK2, GTK3), Gnome-Colors and Archdroid
icons.


%prep
%setup -q -b 0
%setup -q -b 1
%setup -q -b 2
%setup -q -b 3
%setup -q -b 4
%setup -q -b 5
%setup -q -b 6
%setup -q -b 7
cd $RPM_BUILD_DIR
cp -pr %{name}-gtk-theme-%{numix_version}/* %{name}-%{version}/plugins/theme_oomox/gtk-theme
cp -pr materia-theme-%{materia_version}/* %{name}-%{version}/plugins/theme_materia/materia-theme
cp -pr arc-theme-%{arc_commit}/* %{name}-%{version}/plugins/theme_arc/arc-theme
cp -pr archdroid-icon-theme-%{archdroid_version}/* %{name}-%{version}/plugins/icons_archdroid/archdroid-icon-theme
cp -pr gnome-colors-icon-theme-%{gnome_colors_version}/* %{name}-%{version}/plugins/icons_gnomecolors/gnome-colors-icon-theme
cp -pr oomoxify-%{oomoxify_version}/* %{name}-%{version}/plugins/oomoxify
cp -pr base16-builder-%{base16_commit}/* %{name}-%{version}/plugins/import_base16/base16-data


%build


%install
rm -rf $RPM_BUILD_ROOT/*
install -d $RPM_BUILD_ROOT/%{_bindir}
%make_install APPDIR=/opt/%{name} PREFIX=%{_prefix} . $RPM_BUILD_ROOT
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
%{_datadir}/icons/hicolor/*/apps/*
/opt/%{name}



%changelog
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
