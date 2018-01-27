%global         debug_package   %{nil}

Name:           libcxxabi
Version:        5.0.1
Release:        2%{?dist}
Summary:        Low level support for a standard C++ library

License:        MIT or NCSA
URL:            http://libcxxabi.llvm.org/
Source0:        http://llvm.org/releases/%{version}/%{name}-%{version}.src.tar.xz

BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  llvm-devel
BuildRequires:  llvm-static
BuildRequires:  libcxx-devel    >= %{version}

%description
libcxxabi provides low level support for a standard C++ library.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        static
Summary:        Static libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    static
The %{name}-devel package contains static libraries for developing
applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}.src


%build
export LDFLAGS="-Wl,--build-id"
%cmake .. \
    -DCMAKE_C_COMPILER=%{_bindir}/clang \
    -DCMAKE_CXX_COMPILER=%{_bindir}/clang++ \
    -DLLVM_CONFIG=%{_bindir}/llvm-config \
    -DCMAKE_CXX_FLAGS="-std=c++11" \
    -DLIBCXXABI_LIBCXX_INCLUDES=%{_includedir}/c++/v1/ \
    -DLLVM_LIBDIR_SUFFIX:STRING=64 \
%if 0%{?__isa_bits} == 64
    -DLIBCXXABI_LIBDIR_SUFFIX:STRING=64 \
%endif
    -DCMAKE_BUILD_TYPE=RelWithDebInfo
%make_build


%install
rm -rf $RPM_BUILD_ROOT
cd build
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
mkdir -p $RPM_BUILD_ROOT/%{_includedir}
cd ..
cp -a include/* $RPM_BUILD_ROOT/%{_includedir}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license LICENSE.TXT
%doc CREDITS.TXT
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so

%files static
%license LICENSE.TXT
%{_libdir}/*.a


%changelog
* Sat Jan 27 2018 Laurent Tréguier <laurent@treguier.org> - 5.0.1-2
- remove debug package

* Thu Dec 21 2017 Laurent Tréguier <laurent@treguier.org> - 5.0.1-1
- new version

* Sat Sep 09 2017 Laurent Tréguier <laurent@treguier.org> - 5.0.0-1
- new version
- added debuginfo again

* Tue Aug 08 2017 Laurent Tréguier <laurent@treguier.org> - 4.0.1-3
- fixed debuginfo generation

* Sat Aug 05 2017 Laurent Tréguier <laurent@treguier.org> - 4.0.1-2
- stop producing debuginfo on Mageia

* Thu Aug  3 2017 Laurent Tréguier <laurent@treguier.org> - 4.0.1-1
- created specfile
