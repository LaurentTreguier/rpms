%if el6
%global         debug_package   %{nil}
%endif

Name:           libblocksruntime
Version:        0.4.1
Release:        4%{?dist}
Summary:        A target-independent implementation of Apple "Blocks" runtime interfaces

License:        NCSA and MIT
URL:            https://compiler-rt.llvm.org/
Source0:        https://github.com/mheily/blocks-runtime/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  clang
BuildRequires:  libtool
BuildRequires:  make

%description
A target-independent implementation of Apple "Blocks" runtime interfaces.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n blocks-runtime-%{version}


%build
export CFLAGS="%{optflags}"

if [[ -z $(clang --help | grep '\-fstack-protector-strong') ]]
then
    export CFLAGS=${CFLAGS/-fstack-protector-strong/}
fi

export CXXFLAGS="$CFLAGS"
autoreconf -i
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
* Thu Jun 29 2017 Laurent Tréguier <laurent@treguier.org> - 0.4.1-4
- fixed compilation on CentOS 6

* Thu Jun 29 2017 Laurent Tréguier <laurent@treguier.org> - 0.4.1-3
- fixed compilation on CentOS

* Tue May 23 2017 Laurent Tréguier <laurent@treguier.org> - 0.4.1-2
- fixed licenses
- changed source from debian pool to github

* Fri May 19 2017 Laurent Tréguier <laurent@treguier.org> - 0.4.1-1
- created specfile
