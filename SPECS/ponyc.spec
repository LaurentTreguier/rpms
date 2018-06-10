%global         debug_package       %{nil}

Name:           ponyc
Version:        0.23.0
Release:        1%{?dist}
Summary:        An open-source, actor-model, capabilities-secure, high performance programming language

License:        BSD
URL:            http://www.ponylang.org
Source0:        https://github.com/ponylang/ponyc/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        ponyc.sh

BuildRequires:  gcc-c++                     >=  4.7
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
%if 0%{?mageia}
BuildRequires:  llvm-devel                  >=  3.9.1
BuildRequires:  %{_libdir}/libatomic.so
%else
BuildRequires:  cmake(LLVM)                 >=  3.9.1
BuildRequires:  cmake(LLVM)                 <   4.0
BuildRequires:  %{_libdir}/libatomic.so.1
%endif
Requires:       gcc

%description
Pony is an open-source, object-oriented, actor-model, capabilities-secure, high
performance programming language.


%prep
%autosetup


%build
%if %{?mageia:0}%{!?mageia:1}
export LLVM_CONFIG=%{_libdir}/llvm*.*/bin/llvm-config
%endif
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%if %{?mageia:0}%{!?mageia:1}
export LLVM_CONFIG=%{_libdir}/llvm*.*/bin/llvm-config
%endif
%makeinstall destdir=$RPM_BUILD_ROOT/%{_libdir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d
cp %SOURCE1 $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d


%files
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%config %{_sysconfdir}/*
%{_includedir}/*
%{_libdir}/*
%attr(755,root,root) %{_bindir}/*



%changelog
* Sun Jun 10 2018 Laurent Tréguier <laurent@treguier.org> - 0.23.0-1
- new version

* Thu Jun 07 2018 Laurent Tréguier <laurent@treguier.org> - 0.22.6-1
- new version

* Tue Jun 05 2018 Laurent Tréguier <laurent@treguier.org> - 0.22.5-1
- new version

* Fri Jun 01 2018 Laurent Tréguier <laurent@treguier.org> - 0.22.3-1
- new version

* Sun May 27 2018 Laurent Tréguier <laurent@treguier.org> - 0.22.2-1
- new version

* Wed Jan 17 2018 Laurent Tréguier <laurent@treguier.org> - 0.21.3-3
- update dependencies

* Tue Jan 16 2018 Laurent Tréguier <laurent@treguier.org> - 0.21.3-2
- update dependencies

* Mon Jan 15 2018 Laurent Tréguier <laurent@treguier.org> - 0.21.3-1
- new version

* Tue Dec 26 2017 Laurent Tréguier <laurent@treguier.org> - 0.21.2-1
- new version

* Sat Dec 23 2017 Laurent Tréguier <laurent@treguier.org> - 0.21.1-1
- new version

* Mon Dec 18 2017 Laurent Tréguier <laurent@treguier.org> - 0.21.0-1
- new version

* Wed Oct 18 2017 Laurent Tréguier <laurent@treguier.org> - 0.20.0-1
- new version
- removed patch for fallthrough errors

* Mon Sep 25 2017 Laurent Tréguier <laurent@treguier.org> - 0.19.2-1
- new version

* Thu Sep 14 2017 Laurent Tréguier <laurent@treguier.org> - 0.19.1-2
- changed LLVM devel dependency to cmake(LLVM) < 4.0.0 to fix building on EPEL

* Thu Sep 14 2017 Laurent Tréguier <laurent@treguier.org> - 0.19.1-1
- new version
- added patch for fallthrough error

* Sat Sep 02 2017 Laurent Tréguier <laurent@treguier.org> - 0.19.0-1
- new version

* Fri Aug 25 2017 Laurent Tréguier <laurent@treguier.org> - 0.18.1-1
- new version

* Sat Aug 19 2017 Laurent Tréguier <laurent@treguier.org> - 0.18.0-1
- new version

* Sun Aug 06 2017 Laurent Tréguier <laurent@treguier.org> - 0.17.0-2
- fixed build on Mageia

* Sun Aug 06 2017 Laurent Tréguier <laurent@treguier.org> - 0.17.0-1
- new version

* Sat Aug 05 2017 Laurent Tréguier <laurent@treguier.org> - 0.16.1-2
- remove useless pcre2-devel build dependency
- change dependency names to pkgconfig()

* Sun Jul 30 2017 Laurent Tréguier <laurent@treguier.org> - 0.16.1-1
- new version

* Fri Jul 28 2017 Laurent Tréguier <laurent@treguier.org> - 0.16.0-2
- fixed mageia build failing because of debuginfo

* Fri Jul 28 2017 Laurent Tréguier <laurent@treguier.org> - 0.16.0-1
- new version

* Sat Jul 08 2017 Laurent Tréguier <laurent@treguier.org> - 0.15.0-1
- new version
- changed libatomic build dependency to libatomic.so.1
- removed patch for compilation segfault
- added patch for fallthrough error with gcc7

* Thu Jun 29 2017 Laurent Tréguier <laurent@treguier.org> - 0.14.0-6
- cleaned up specfile

* Thu Jun 15 2017 Laurent Tréguier <laurent@treguier.org> - 0.14.0-5
- cleaned up specfile
- removed llvm-devel-ponyc-compat build dependency
- added patch for gcc7

* Sun May 14 2017 Laurent Tréguier <laurent@treguier.org> - 0.14.0-4
- ensured binary is executable

* Fri May 12 2017 Laurent Tréguier <laurent@treguier.org> - 0.14.0-3
- added gcc dependency
- added /etc/profile.d/ponyc.sh to set default $CC variable

* Thu May 11 2017 Laurent Tréguier <laurent@treguier.org> - 0.14.0-2
- fixed llvm-devel handling with llvm-devel-ponyc-compat

* Tue Apr 25 2017 Laurent Tréguier <laurent@treguier.org> - 0.14.0-1
- created specfile
