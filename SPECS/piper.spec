Name:           piper
Version:        0.2.900
Release:        1%{?dist}
Summary:        GTK application to configure gaming mice

License:        GPLv2
URL:            https://github.com/libratbag/piper
Source0:        https://github.com/libratbag/piper/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  gtk-update-icon-cache
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(pygobject-3.0)
Requires:       ratbagd
Requires:       python3dist(evdev)
Requires:       python3dist(lxml)
Requires:       python3dist(pygobject)

%description
Piper is a GTK+ application to configure gaming mice, using libratbag via
ratbagd. For the design mockups, see the Redesign Wiki.


%prep
%autosetup


%build
%meson
%meson_build


%install
rm -rf $RPM_BUILD_ROOT
%meson_install
rm -f $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/icon-theme.cache


%files
%license COPYING
%doc README.md
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/locale/*/LC_MESSAGES/*
%{python3_sitelib}/*



%changelog
* Fri Aug 25 2017 Laurent Tréguier <laurent@treguier.org> - 0.2.900-1
- created specfile
