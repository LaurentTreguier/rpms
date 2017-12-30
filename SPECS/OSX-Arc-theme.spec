%global         source_name         OSX-Arc
%global         source_white        White
%global         source_plus         Plus
%global         source_darker       Darker
%global         source_shadow       Shadow
%global         source_name_white   %{source_name}-%{source_white}
%global         source_name_darker  %{source_name}-%{source_darker}
%global         source_name_shadow  %{source_name}-%{source_shadow}

Name:           %{source_name}-theme
Version:        1.4.7
Release:        1%{?dist}
Summary:        A flat theme collection based on arc with transparent elements for GTK 3, GTK 2 and GTK based desktops

License:        GPLv3
URL:            https://github.com/LinxGem33/
Source0:        https://github.com/LinxGem33/%{source_name_white}/archive/v%{version}.tar.gz#/%{source_name_white}-%{version}.tar.gz
Source1:        https://github.com/LinxGem33/%{source_name_darker}/archive/v%{version}.tar.gz#/%{source_name_darker}-%{version}.tar.gz
Source2:        https://github.com/LinxGem33/%{source_name_shadow}/archive/v%{version}.tar.gz#/%{source_name_shadow}-%{version}.tar.gz

BuildArch:      noarch
Requires:       gnome-themes-standard

%description
OSX-Arc theme collection is a flat theme collection based on arc with transparent elements OSX-Arc Collection is available in three variants, it also supports GTK 3, GTK 2 and Gnome-Shell which integrates with GTK 3 and GTK 2 based desktop environments like Gnome, Unity, Budgie, Pantheon, XFCE, Mate, etc.


%package -n %{source_name_white}-theme
Summary:        A flat theme collection based on arc with transparent elements for GTK 3, GTK 2 and GTK based desktops

%description -n %{source_name_white}-theme
OSX-Arc theme collection is a flat theme collection based on arc with transparent elements OSX-Arc Collection is available in three variants, it also supports GTK 3, GTK 2 and Gnome-Shell which integrates with GTK 3 and GTK 2 based desktop environments like Gnome, Unity, Budgie, Pantheon, XFCE, Mate, etc.


%package -n %{source_name_darker}-theme
Summary:        A flat theme collection based on arc with transparent elements for GTK 3, GTK 2 and GTK based desktops

%description -n %{source_name_darker}-theme
OSX-Arc theme collection is a flat theme collection based on arc with transparent elements OSX-Arc Collection is available in three variants, it also supports GTK 3, GTK 2 and Gnome-Shell which integrates with GTK 3 and GTK 2 based desktop environments like Gnome, Unity, Budgie, Pantheon, XFCE, Mate, etc.


%package -n %{source_name_shadow}-theme
Summary:        A flat theme collection based on arc with transparent elements for GTK 3, GTK 2 and GTK based desktops

%description -n %{source_name_shadow}-theme
OSX-Arc theme collection is a flat theme collection based on arc with transparent elements OSX-Arc Collection is available in three variants, it also supports GTK 3, GTK 2 and Gnome-Shell which integrates with GTK 3 and GTK 2 based desktop environments like Gnome, Unity, Budgie, Pantheon, XFCE, Mate, etc.


%package -n %{source_name}-plank-theme
Summary:        A flat theme collection based on arc with transparent elements for GTK 3, GTK 2 and GTK based desktops

%description -n %{source_name}-plank-theme
OSX-Arc theme collection is a flat theme collection based on arc with transparent elements OSX-Arc Collection is available in three variants, it also supports GTK 3, GTK 2 and Gnome-Shell which integrates with GTK 3 and GTK 2 based desktop environments like Gnome, Unity, Budgie, Pantheon, XFCE, Mate, etc.


%prep
%autosetup -b 0 -n %{source_name_white}-%{version}
%autosetup -b 1 -n %{source_name_darker}-%{version}
%autosetup -b 2 -n %{source_name_shadow}-%{version}


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/{,plank}/themes

for theme in {%{source_name_white},%{source_name_darker},%{source_name_shadow}}
do
    mkdir -p $RPM_BUILD_ROOT/%{_datadir}/themes/$theme
    cp -R $RPM_BUILD_DIR/$theme-%{version}/* $RPM_BUILD_ROOT/%{_datadir}/themes/$theme
done

cp -R $RPM_BUILD_ROOT/%{_datadir}/themes/%{source_name_white}/extra/Arc-Plank \
    $RPM_BUILD_ROOT/%{_datadir}/plank/themes


%files -n %{source_name_white}-theme
%license AUTHORS
%license COPYING
%doc README.md
%{_datadir}/themes/%{source_name_white}


%files -n %{source_name_darker}-theme
%license AUTHORS
%license COPYING
%doc README.md
%{_datadir}/themes/%{source_name_darker}


%files -n %{source_name_shadow}-theme
%license AUTHORS
%license COPYING
%doc README.md
%{_datadir}/themes/%{source_name_shadow}


%files -n %{source_name}-plank-theme
%license AUTHORS
%license COPYING
%doc README.md
%{_datadir}/plank/themes/*



%changelog
* Sat Dec 30 2017 Laurent Tréguier <laurent@treguier.org> - 1.4.7-1
- new version

* Fri Nov 24 2017 Laurent Tréguier <laurent@treguier.org> - 1.4.5-1
- new version

* Tue May 30 2017 Laurent Tréguier <laurent@treguier.org> - 1.4.3-1
- new version
- OSX-Arc-plus was removed from specfile as upstream removed it

* Thu Apr 20 2017 Laurent Tréguier <laurent@treguier.org> - 1.4.1-1
- created specfile
