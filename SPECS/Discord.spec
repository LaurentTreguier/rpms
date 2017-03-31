%global         debug_package   %{nil}
%global         lowercase_name  discord

Name:           Discord
Version:        0.0.1
Release:        5%{?dist}
Summary:        It’s time to ditch Skype and TeamSpeak

License:        Custom
URL:            https://discordapp.com/
Source0:        https://dl.discordapp.net/apps/linux/%{version}/%{lowercase_name}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-copyright

BuildArch:      x86_64
Requires:       alsa-lib
Requires:       GConf2
Requires:       glibc
Requires:       libappindicator
Requires:       libnotify
Requires:       libstdc++
Requires:       libXScrnSaver
Requires:       libXtst
Requires:       nspr
Requires:       nss
AutoReqProv:    no

%description
All-in-one voice and text chat for gamers that’s free, secure, and works on both your desktop and phone.
Stop paying for TeamSpeak servers and hassling with Skype.
Simplify your life.


%prep
%autosetup -n %{name}


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/{%{lowercase_name},applications,pixmaps}
mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}
cp -R $RPM_BUILD_DIR/%{name}/* $RPM_BUILD_ROOT/%{_datadir}/%{lowercase_name}
cp $RPM_BUILD_DIR/%{name}/*.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/%{lowercase_name}.png
cp $RPM_BUILD_DIR/%{name}/*.desktop $RPM_BUILD_ROOT/%{_datadir}/applications
cp %{SOURCE1} $RPM_BUILD_ROOT/%{_defaultdocdir}/%{name}/copyright
rm $RPM_BUILD_ROOT/%{_datadir}/%{lowercase_name}/postinst.sh
ln -s %{_datadir}/%{lowercase_name}/%{name} $RPM_BUILD_ROOT/%{_bindir}


%files
%license %{_defaultdocdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{lowercase_name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png



%changelog
* Thu Mar 30 2017 Laurent Tréguier <laurent@treguier.org> - 0.0.1-5
- added dependencies according to the official deb package

* Thu Mar 30 2017 Laurent Tréguier <laurent@treguier.org> - 0.0.1-4
- changed url for consistent downloads
- corrected copyright location

* Thu Mar 30 2017 Laurent Tréguier <laurent@treguier.org> - 0.0.1-3
- removed postinst.sh
- added link to binary in /usr/bin

* Wed Mar 29 2017 Laurent Tréguier <laurent@treguier.org> - 0.0.1-2
- bundle png icon in /usr/share/discord

* Wed Mar 29 2017 Laurent Tréguier <laurent@treguier.org>
- created specfile
