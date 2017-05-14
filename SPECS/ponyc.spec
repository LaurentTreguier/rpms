Name:           ponyc
Version:        0.14.0
Release:        4%{?dist}
Summary:        An open-source, actor-model, capabilities-secure, high performance programming language

License:        BSD
URL:            http://www.ponylang.org
Source0:        https://github.com/ponylang/ponyc/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        ponyc.sh
# https://github.com/ponylang/ponyc/issues/1225#issuecomment-300753325
Patch0:         %{name}-compilation-segfault.patch

BuildRequires:  clang                   >= 3.3
BuildRequires:  gcc                     >= 4.7
BuildRequires:  gcc-c++                 >= 4.7
BuildRequires:  llvm-devel-ponyc-compat
BuildRequires:  ncurses-devel
BuildRequires:  pcre2-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
Requires:       gcc

%description
Pony is an open-source, object-oriented, actor-model, capabilities-secure, high performance programming language.


%prep
%autosetup -N
%patch0
sed -i 's,$(prefix)/lib,$(libdir),' Makefile


%build
%make_build LLVM_CONFIG=$(rpm -ql $(rpm -qa --qf '%%{NAME}\n' | grep -E 'llvm.+devel$' | sort -r | head -1) | grep 'bin/llvm-config')


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall LLVM_CONFIG=$(rpm -ql $(rpm -qa --qf '%%{NAME}\n' | grep -E 'llvm.+devel$' | sort -r | head -1) | grep 'bin/llvm-config') destdir=$RPM_BUILD_ROOT/%{_libdir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d
cp %SOURCE1 $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d
echo %{llvm_config}


%files
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%config %{_sysconfdir}/*
%{_includedir}/*
%{_libdir}/*
%defattr(755,root,root)
%{_bindir}/*



%changelog
* Sun May 14 2017 Laurent Tréguier <laurent@treguier.org> - 0.14.0-4
- ensured binary is executable

* Fri May 12 2017 Laurent Tréguier <laurent@treguier.org> - 0.14.0-3
- added gcc dependency
- added /etc/profile.d/ponyc.sh to set default $CC variable

* Thu May 11 2017 Laurent Tréguier <laurent@treguier.org> - 0.14.0-2
- fixed llvm-devel handling with llvm-devel-ponyc-compat

* Tue Apr 25 2017 Laurent Tréguier <laurent@treguier.org> - 0.14.0-1
- created specfile
