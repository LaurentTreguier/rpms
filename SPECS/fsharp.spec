Name:           fsharp
Version:        4.1.9
Release:        1%{?dist}
Summary:        The Open Edition of the F# compiler, core library and tools

License:        Apache-2.0
URL:            http://fsharp.org/
Source0:        https://github.com/fsharp/fsharp/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  %{_bindir}/autoreconf
BuildRequires:  %{_bindir}/automake
BuildRequires:  %{_bindir}/nuget
BuildRequires:  mono-devel >= 4.4.0
BuildRequires:  mono-wcf   >= 4.4.0
Requires:       %{_bindir}/gdb
Requires:       %{_bindir}/valgrind
# Hack ! (see https://github.com/fsharp/fsharp/issues/699)
Provides:       mono(System.Collections.Immutable) = 1.2.0.0

%description
F# is a mature, open source, cross-platform, functional-first programming language.
It empowers users and organizations to tackle complex computing problems with simple, maintainable and robust code.


%prep
%autosetup
cert-sync --user /etc/pki/tls/certs/ca-bundle.crt


%build
autoreconf
%configure --libexecdir=%{_monodir}/.. --libdir=%{_monodir}/..
make


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%defattr(-,root,root)
%license LICENSE
%doc README.md
%{_monodir}/*/FSharp.*
%{_monodir}/fsharp
%{_monogacdir}/FSharp.*
%{_monogacdir}/*.FSharp.Core
"%{_monodir}/Microsoft F#"
"%{_monodir}/Microsoft SDKs/F#"
%{_monodir}/xbuild/Microsoft/VisualStudio/*/FSharp
%defattr(755,root,root)
%{_bindir}/fsharp*



%changelog
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

* Thu Mar  9 2017 Laurent Tréguier <laurent@treguier.org>
- rewrite entire specfile
