%global         __python            %{__python3}
%global         numix_version       1.2.8.1
%global         flatplat_version    20170605
%global         flatplat_commit     96bffc0b13c81a0a608e036da5b1c720e647a11a
%global         flatplat_githash    %(c=%{flatplat_commit}; echo ${c:0:7})
%global         flatplat_gitdate    20170827

Name:           oomox
Version:        1.3.0
Release:        1_%{numix_version}.1_%{flatplat_gitdate}git%{flatplat_githash}.1%{?dist}
Summary:        GUI for generating variations of Numix/Flat-Plat themes, gnome-colors and ArchDroid icon themes

License:        GPLv3
URL:            https://github.com/actionless/oomox
Source0:        https://github.com/actionless/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/actionless/%{name}-gtk-theme/archive/%{numix_version}.tar.gz#/%{name}-gtk-theme-%{numix_version}.tar.gz
Source2:        https://github.com/nana-4/Flat-Plat/archive/%{flatplat_commit}.zip#/Flat-Plat-%{flatplat_commit}.zip
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
Graphical application for generating different color variations of Numix and
Flat-Plat themes (GTK2, GTK3), gnome-colors and ArchDroid icon themes. Have a
hack for HiDPI in gtk2.


%prep
%autosetup -b 0
%autosetup -b 1
%autosetup -b 2
cp -pr $RPM_BUILD_DIR/%{name}-gtk-theme-%{numix_version}/* $RPM_BUILD_DIR/%{name}-%{version}/gtk-theme
cp -pr $RPM_BUILD_DIR/Flat-Plat-%{flatplat_commit}/* $RPM_BUILD_DIR/%{name}-%{version}/flat-plat-theme


%build
%{__make} -C $RPM_BUILD_DIR/%{name}-%{version} -f po.mk install


%install
rm -rf $RPM_BUILD_ROOT/*
mkdir -p $RPM_BUILD_ROOT/opt/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications
cp -pr $RPM_BUILD_DIR/%{name}-%{version}/* $RPM_BUILD_ROOT/opt/%{name}
cp                              \
    %{SOURCE10}                 \
    %{SOURCE11}                 \
    %{SOURCE12}                 \
    %{SOURCE13}                 \
    %{SOURCE14}                 \
    $RPM_BUILD_ROOT/%{_bindir}
desktop-file-install --dir $RPM_BUILD_ROOT/%{_datadir}/applications %{SOURCE20}
rm $RPM_BUILD_ROOT/opt/%{name}/{CREDITS,PKGBUILD,screenshot*}


%files
%license LICENSE
%doc CREDITS
%doc README.md
%attr(755,root,root) %{_bindir}/*
%{_datadir}/applications/%{name}.desktop
/opt/%{name}



%changelog
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
