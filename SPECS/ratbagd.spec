Name:           ratbagd
Version:        0.4
Release:        1%{?dist}
Summary:        D-Bus daemon to export libratbag

License:        MIT
URL:            https://github.com/libratbag/ratbagd/
Source0:        https://github.com/libratbag/ratbagd/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(libratbag)    >= 0.6
BuildRequires:  pkgconfig(libsystemd)   >= 227
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(python3)
%if 0%{?systemd_requires}
%systemd_requires
%endif

%description
ratbagd is a system daemon to introspect and modify configurable mice.

ratbagd uses libratbag to access mice and exports the features over a DBus API
to unprivileged proceses. ratbagd needs permissions to access device nodes
(primarily /dev/hidraw nodes) and usually needs to run as root.

ratbagd is a relatively thin wrapper arond libratbag. If a device is not
detected or does not function as expected, the issue is usually in libratbag.
libratbag can be found at https://github.com/libratbag/libratbag.


%prep
%autosetup


%build
%meson -Dsystemd-unit-dir=%{_unitdir}
%meson_build


%install
rm -rf $RPM_BUILD_ROOT
%meson_install


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service


%files
%license COPYING
%doc README.md
%{_bindir}/*
%{_datadir}/dbus-1/*/*
%{_mandir}/*
%{_unitdir}/*
%{python3_sitelib}/*


%changelog
* Sun Aug 13 2017 Laurent Tréguier <laurent@treguier.org> - 0.4-1
- created specfile
