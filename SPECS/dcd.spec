%global         source_name         DCD
%global         source_version      0.9.0-alpha.6

Name:           %(echo %{source_name} | tr [:upper:] [:lower:])
Version:        %(echo %{source_version} | tr '-' '_' | sed -r 's/([a-zA-Z])\./\1/')
Release:        1%{?dist}
Summary:        The D Completion Daemon is an auto-complete program for the D programming language

License:        GPLv3
URL:            https://github.com/Hackerpilot/DCD
Source0:        https://github.com/Hackerpilot/DCD/archive/v%{source_version}.tar.gz#/%{source_name}-%{source_version}.tar.gz

BuildRequires:  dub
Requires:       dmd-druntime-devel
Requires:       dmd-phobos-devel

%description
DCD consists of a client and a server.
The client (dcd-client) is almost always used through a text editor script or plugin, though it can be used from the command line.
The server (dcd-server) is responsible for caching imported files, calculating autocomplete information, and sending it back to the client.


%prep
%autosetup -n %{source_name}-%{source_version}


%build
cd $RPM_BUILD_DIR/%{source_name}-%{source_version}
%dub_build --config client
%dub_build --config server


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{%{_bindir},%{_datadir},%{_sysconfdir},%{_mandir}}
cd $RPM_BUILD_DIR/%{source_name}-%{source_version}
cp %{name}-{client,server} $RPM_BUILD_ROOT/%{_bindir}
cp -R bash-completion $RPM_BUILD_ROOT/%{_datadir}
cp -R man1 $RPM_BUILD_ROOT/%{_mandir}
grep -Eo '\-I\S+' %{_sysconfdir}/dmd.conf | tr -d '\-I' | sort | uniq > $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}.conf


%files
%defattr(-,root,root)
%license $RPM_BUILD_DIR/%{source_name}-%{source_version}/License.txt
%doc $RPM_BUILD_DIR/%{source_name}-%{source_version}/README.md
%config(noreplace) %{_sysconfdir}/*
%config %{_datadir}/bash-completion/completions/*
%{_mandir}/*/*
%defattr(755,root,root)
%{_bindir}/*



%changelog
* Mon Apr  3 2017 Laurent Tréguier <laurent@treguier.org> - 0.9.0-alpha.6
- created specfile
