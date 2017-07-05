%global         debug_package   %{nil}

Name:           fsharp
Version:        4.1.21
Release:        1%{?dist}
Summary:        The Open Edition of the F# compiler, core library and tools

License:        Apache-2.0
URL:            http://fsharp.org/
Source0:        https://github.com/fsharp/fsharp/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

ExclusiveArch:  %{mono_arches}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  ca-certificates
BuildRequires:  nuget
BuildRequires:  make
BuildRequires:  mono-devel      >=  4.4.0
BuildRequires:  mono-wcf        >=  4.4.0
Requires:       gdb
Requires:       valgrind

%description
F# is a mature, open source, cross-platform, functional-first programming
language. It empowers users and organizations to tackle complex computing
problems with simple, maintainable and robust code.


%prep
%autosetup
cert-sync --user /etc/pki/tls/certs/ca-bundle.crt


%build
autoreconf
%configure --libexecdir=%{_monodir}/.. --libdir=%{_monodir}/..
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install
cd $RPM_BUILD_DIR/%{name}-%{version}/packages/System.ValueTuple.4.3.1/lib/netstandard1.0
chmod +x System.ValueTuple.dll
cp System.ValueTuple.dll $RPM_BUILD_ROOT/%{_monodir}/%{name}


%files
%license LICENSE
%doc README.md
%doc CHANGELOG-fsharp.md
%attr(755,root,root) %{_bindir}/*
%{_monodir}/*/FSharp*
%{_monodir}/fsharp
%{_monodir}/xbuild/Microsoft/VisualStudio/*/FSharp
"%{_monodir}/Microsoft F#"
"%{_monodir}/Microsoft SDKs/F#"
%{_monogacdir}/*



%changelog
* Wed Jul 05 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.21-1
- new version

* Wed Jul 05 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.20-1
- new version

* Thu Jun 29 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.19-3
- fixed permissions on System.ValueTuple.dll

* Thu Jun 29 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.19-2
- added System.ValueTuple.dll to package to fix missing dependency error

* Thu Jun 29 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.19-1
- new version

* Sat Jun 24 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.18-3
- changed architecture from noarch to mono_arches
- added ca-certificates as explicit build dependency
- added CHANGLOG as doc

* Wed Jun 14 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.18-2
- explicited make build dependency
- added redhat-rpm-config build dependency
- added mono macros for CentOS 6

* Sat Apr 29 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.18-1
- new version

* Sat Apr 29 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.17-1
- new version

* Tue Apr 25 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.15-1
- new version
- removed hack instroduced in 4.1.5-1

* Thu Apr 20 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.14-1
- new version

* Thu Apr 20 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.13-1
- new version
- moved file dependencies to package dependencies

* Thu Apr 13 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.12-1
- new version

* Thu Apr 13 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.11-1
- new version

* Thu Apr 13 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.10-1
- new version

* Tue Apr 11 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.9-1
- new version
- ensured executables are marked as much

* Wed Apr 05 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.8-2
- added license and doc files

* Wed Apr 05 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.8-1
- new version

* Thu Mar 30 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.7-1
- new version

* Thu Mar 30 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.6-1
- new version

* Wed Mar 29 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.5-1
- new version
- added Provides for mono(System.Collections.Immutable) = 1.2.0.0 (hack)

* Wed Mar 29 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.4-1
- new version

* Wed Mar 29 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.3-1
- new version

* Tue Mar 28 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.2-1
- new version

* Fri Mar 17 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.1-1
- new version

* Sun Mar 12 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.0.2-2
- rebuilt

* Fri Mar 10 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.0.2-1
- new version

* Thu Mar  9 2017 Laurent Tréguier <laurent@treguier.org> - 4.1.0.1-1
- rewrite entire specfile
