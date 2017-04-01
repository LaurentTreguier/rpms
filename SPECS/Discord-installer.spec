%global         debug_package   %{nil}

Name:           Discord-installer
Version:        1.0.2
Release:        1%{?dist}
Summary:        Some systemd services to install Discord on Redhat based systems

License:        MIT
URL:            https://github.com/LaurentTreguier/Discord-installer
Source0:        https://github.com/LaurentTreguier/Discord-installer/archive/%{version}.tar.gz#/%{name}-%{version}.zip

BuildArch:      x86_64
BuildRequires:  make
BuildRequires:  systemd
Requires:       dos2unix
Requires:       rpm-build
Requires:       rpmdevtools
Requires:       systemd
Obsoletes:      Discord         = 0:0.0.1
Obsoletes:      DiscordCanary   = 0:0.0.15

%description
Some systemd services to install Discord on Redhat based systems.


%prep
%autosetup


%build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%post
touch %{_var}/lib/discord-installer-rebuild-Discord
touch %{_var}/lib/discord-installer-rebuild-DiscordCanary

if [[ $1 = 1 ]]
then
    systemctl enable --now --no-block discord-installer.service
fi


%preun
rm -f %{_var}/lib/discord-installer/discord-installer-rebuild-Discord
rm -f %{_var}/lib/discord-installer/discord-installer-rebuild-DiscordCanary

if [[ $1 = 0 ]]
then
    systemctl disable discord-installer.service
    systemctl disable discord-canary-installer.service
fi


%files
%{_unitdir}/discord*.service
%{_libexecdir}/discord-installer
%{_datadir}/discord-installer



%changelog
* Sat Apr 01 2017 Laurent Tréguier <laurent@treguier.org> - 1.0.2-1
- new version

* Sat Apr 01 2017 Laurent Tréguier <laurent@treguier.org> - 1.0.1-1
- new version

* Sat Apr  1 2017 Laurent Tréguier <laurent@treguier.org>
- created specfile
