%global         bootstrap       0

Name:           libcxx
Version:        4.0.1
Release:        5%{?dist}
Summary:        C++ standard library targeting C++11

License:        MIT or NCSA
URL:            http://libcxx.llvm.org/
Source0:        http://llvm.org/releases/%{version}/%{name}-%{version}.src.tar.xz

BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  llvm-devel
BuildRequires:  llvm-static
%if %{bootstrap} < 1
BuildRequires:  libcxxabi-devel
BuildRequires:  python3
%endif

%description
libc++ is a new implementation of the C++ standard library, targeting C++11.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if %{bootstrap} < 1
Requires:       libcxxabi-devel
%endif

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
%if %{bootstrap} < 1
    -DLIBCXX_CXX_ABI=libcxxabi \
    -DLIBCXX_CXX_ABI_INCLUDE_PATHS=%{_includedir} \
    -DPYTHONINTERP_FOUND=ON \
    -DPYTHON_EXECUTABLE=%{_bindir}/python3 \
    -DLIBCXX_ENABLE_ABI_LINKER_SCRIPT=ON \
%endif
%if 0%{?__isa_bits} == 64
    -DLIBCXX_LIBDIR_SUFFIX:STRING=64 \
%endif
    -DCMAKE_BUILD_TYPE=RelWithDebInfo
%make_build


%install
rm -rf $RPM_BUILD_ROOT
cd build
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license LICENSE.TXT
%doc CREDITS.TXT
%doc TODO.TXT
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so

%files static
%license LICENSE.TXT
%{_libdir}/*.a


%changelog
* Mon Aug 14 2017 Laurent Tréguier <laurent@treguier.org> - 4.0.1-5
- added debuginfo again

* Tue Aug 08 2017 Laurent Tréguier <laurent@treguier.org> - 4.0.1-4
- fixed debuginfo generation

* Sat Aug 05 2017 Laurent Tréguier <laurent@treguier.org> - 4.0.1-3
- stop producing debuginfo on Mageia

* Thu Aug 03 2017 Laurent Tréguier <laurent@treguier.org> - 4.0.1-2
- drop bootstrapping

* Thu Aug  3 2017 Laurent Tréguier <laurent@treguier.org> - 4.0.1-1
- created specfile
