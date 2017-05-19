Name:           libblocksruntime
Version:        0.4.1
Release:        1%{?dist}
Summary:        A target-independent implementation of Apple "Blocks" runtime interfaces

License:        NCSA MIT
URL:            https://compiler-rt.llvm.org/
Source0:        http://http.debian.net/debian/pool/main/libb/%{name}/%{name}_%{version}.orig.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  clang

%description
A target-independent implementation of Apple "Blocks" runtime interfaces.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup


%build
%configure --disable-static
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Fri May 19 2017 Laurent Tréguier <laurent@treguier.org> - 0.4.1-1
- created specfile
