Name:           ponyc
Version:        0.14.0
Release:        1%{?dist}
Summary:        An open-source, actor-model, capabilities-secure, high performance programming language

License:        BSD
URL:            http://www.ponylang.org
Source0:        https://github.com/ponylang/ponyc/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/ponylang/ponyc/issues/1225#issuecomment-300753325
Patch0:         %{name}-compilation-segfault.patch

BuildRequires:  clang           >= 3.3
BuildRequires:  gcc             >= 4.7
BuildRequires:  gcc-c++         >= 4.7
BuildRequires:  llvm-devel
BuildRequires:  ncurses-devel
BuildRequires:  pcre2-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel

%description
Pony is an open-source, object-oriented, actor-model, capabilities-secure, high performance programming language.


%prep
%autosetup -N
%patch0
sed -i 's,$(prefix)/lib,$(libdir),' Makefile


%build
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall destdir=$RPM_BUILD_ROOT/%{_libdir}/%{name}


%files
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*



%changelog
* Tue Apr 25 2017 Laurent Tréguier <laurent@treguier.org> - 0.14.0-1
- created specfile
