%global         __python %{__python3}

Name:           oomox
Version:        1.2.3
Release:        1%{?dist}
Summary:        GUI for generating variations of Numix theme, gnome-colors and ArchDroid icon themes

License:        GPLv3
URL:            https://github.com/actionless/oomox
Source0:        https://github.com/actionless/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        oomox-archdroid-icons-cli
Source2:        oomox-cli
Source3:        oomox-gnome-colors-icons-cli
Source4:        oomoxify-cli
Source5:        oomox-gui
Source6:        oomox.desktop

BuildArch:      noarch
BuildRequires:  %{_bindir}/bash
BuildRequires:  %{_bindir}/bc
BuildRequires:  %{_bindir}/xgettext
Requires:       %{_bindir}/gdk-pixbuf-pixdata
Requires:       %{_bindir}/glib-compile-schemas
Requires:       rubygem(sass)
Requires:       gtk-murrine-engine
Requires:       gtk2-engines
Requires:       python3-gobject

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
cp $RPM_SOURCE_DIR/*-{cli,gui} $RPM_BUILD_ROOT/%{_bindir}
cp $RPM_SOURCE_DIR/%{name}.desktop $RPM_BUILD_ROOT/%{_datadir}/applications
rm $RPM_BUILD_ROOT/opt/%{name}/CHANGES
rm $RPM_BUILD_ROOT/opt/%{name}/CREDITS
rm $RPM_BUILD_ROOT/opt/%{name}/PKGBUILD
rm $RPM_BUILD_ROOT/opt/%{name}/circle.yml
rm $RPM_BUILD_ROOT/opt/%{name}/screenshot*


%files
%defattr(-,root,root)
%license /opt/%{name}/LICENSE
%doc /opt/%{name}/README.md
/opt/%{name}
%{_datadir}/applications/%{name}.desktop
%defattr(755,root,root)
%{_bindir}/*-cli
%{_bindir}/%{name}-gui



%changelog
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

