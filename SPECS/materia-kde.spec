Name:           materia-kde
Version:        20190613
Release:        1%{?dist}
Summary:        Materia KDE customization

License:        GPLv3
URL:            https://github.com/PapirusDevelopmentTeam/%{name}
Source0:        https://github.com/PapirusDevelopmentTeam/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
%if 0%{?fedora}%{?mageia}
Recommends:     %{_bindir}/kvantummanager
%endif

%description
This is a port of the popular GTK theme Materia for Plasma 5 desktop with a few
additions and extras.


%prep
%autosetup


%build
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license LICENSE
%doc README.md
%{_datadir}/aurorae/themes/*
%{_datadir}/color-schemes/*
%{_datadir}/konsole/*
%{_datadir}/Kvantum/*
%{_datadir}/plasma/desktoptheme/*
%{_datadir}/plasma/look-and-feel/*
%{_datadir}/yakuake/skins/*



%changelog
* Fri Jun 14 2019 Laurent Tréguier <laurent@treguier.org> - 20190613-1
- new version

* Thu May 23 2019 Laurent Tréguier <laurent@treguier.org> - 20190518-1
- new version

* Sun May 19 2019 Laurent Tréguier <laurent@treguier.org> - 20190506-1
- created specfile