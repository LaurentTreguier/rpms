Name:           libkqueue
Version:        2.1.0
Release:        2%{?dist}
Summary:        kqueue(2) compatibility library

License:        BSD
URL:            https://github.com/mheily/libkqueue
Source0:        https://github.com/mheily/libkqueue/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libtool

%description
A user space implementation of the kqueue(2) kernel event notification
mechanism libkqueue acts as a translator between the kevent structure and the
native kernel facilities on Linux, Android, Solaris, and Windows.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup


%build
autoreconf -i
%configure --disable-static --disable-dependency-tracking
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license LICENSE
%doc README.md
%{_libdir}/*.so.*

%files devel
%doc %{_mandir}/*/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*


%changelog
* Sat Jul 08 2017 Laurent Tréguier <laurent@treguier.org> - 2.1.0-2
- ensured --disable-dependency-tracking option is used

* Fri May 19 2017 Laurent Tréguier <laurent@treguier.org> - 2.1.0-1
- created specfile
