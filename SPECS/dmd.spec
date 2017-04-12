%global         dmd_name        dmd
%global         drt_name        druntime
%global         phb_name        phobos
%global         dto_name        tools
%global         arch_bits       %(getconf LONG_BIT)

%define         make_options    -f posix.mak RELEASE=1 MODEL=%{arch_bits} AUTO_BOOTSTRAP=1
%define         build_dir       $RPM_BUILD_DIR/%{name}-%{version}-build
%define         install_dir     $RPM_BUILD_DIR/%{name}-%{version}-install

Name:           %{dmd_name}
Version:        2.074.0
Release:        7%{?dist}
Summary:        Digital Mars D Compiler

License:        Boost
URL:            http://dlang.org/
Source0:        https://github.com/dlang/%{dmd_name}/archive/v%{version}.tar.gz#/%{name}-%{dmd_name}-%{version}.tar.gz
Source1:        https://github.com/dlang/%{drt_name}/archive/v%{version}.tar.gz#/%{name}-%{drt_name}-%{version}.tar.gz
Source2:        https://github.com/dlang/%{phb_name}/archive/v%{version}.tar.gz#/%{name}-%{phb_name}-%{version}.tar.gz
Source3:        https://github.com/dlang/%{dto_name}/archive/v%{version}.tar.gz#/%{name}-%{dto_name}-%{version}.tar.gz
Source10:       http://www.boost.org/LICENSE_1_0.txt#/%{name}-%{version}-LICENSE

BuildRequires:  curl
Requires:       %{name}-%{drt_name}-devel
Requires:       %{name}-%{phb_name}-devel

%description
D is a systems programming language. Its focus is on combining the power and
high performance of C and C++ with the programmer productivity of modern
languages like Ruby and Python. Special attention is given to the needs of
quality assurance, documentation, management, portability and reliability.

The D language is statically typed and compiles directly to machine code.
It's multiparadigm, supporting many programming styles: imperative,
object oriented, functional, and metaprogramming. It's a member of the C
syntax family, and its appearance is very similar to that of C++.

It is not governed by a corporate agenda or any overarching theory of
programming. The needs and contributions of the D programming community form
the direction it goes.


%package %{drt_name}
Summary:        Runtime library for D

%description %{drt_name}
Druntime is the minimum library required to support the D programming
language. It includes the system code required to support the garbage
collector, associative arrays, exception handling, array vector operations,
startup/shutdown, etc.


%package %{drt_name}-devel
Summary:        Support for developing D application
Requires:       %{name}-%{drt_name}

%description %{drt_name}-devel
The druntime-devel package contains header files for developing D
applications that use druntime.


%package %{phb_name}
Summary:        Standard Runtime Library

%description %{phb_name}
Each module in Phobos conforms as much as possible to the following design
goals. These are goals rather than requirements because D is not a religion,
it's a programming language, and it recognizes that sometimes the goals are
contradictory and counterproductive in certain situations, and programmers have
jobs that need to get done


%package %{phb_name}-devel
Summary:        Support for developing D application
Requires:       %{name}-%{phb_name}

%description %{phb_name}-devel
The phobos-devel package contains header files for developing D
applications that use phobos.


%package %{dto_name}
Summary:        Ancillary tools for the D programming language compiler
BuildRequires:  curl-devel
Requires:       dmd

%description %{dto_name}
This repository hosts various tools redistributed with DMD or used internally
during various build tasks.


%prep
%autosetup -b 0
%autosetup -b 1
%autosetup -b 2
%autosetup -b 3
rm -rf %{build_dir}
mkdir -p %{build_dir}

for component in %{dmd_name} %{drt_name} %{phb_name} %{dto_name}
do
    cp -R $RPM_BUILD_DIR/$component-%{version} %{build_dir}/$component
done

cp %SOURCE10 $RPM_BUILD_DIR/%{dmd_name}-%{version}/LICENSE_1_0.txt


%build
for component in %{dmd_name} %{drt_name} %{phb_name} %{dto_name}
do
    cd %{build_dir}/$component
    %make_build %{make_options}
done


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{%{_bindir},%{_libdir},%{_includedir}/%{name}/{%{drt_name},%{phb_name}},%{_mandir},%{_sysconfdir}}

cd %{build_dir}/%{dmd_name}
cp src/%{dmd_name} $RPM_BUILD_ROOT/%{_bindir}
cp ini/$RPM_OS/bin%(getconf LONG_BIT)/*.conf $RPM_BUILD_ROOT/%{_sysconfdir}
cp -R docs/man/* $RPM_BUILD_ROOT/%{_mandir}
sed -ri 's,-I\S*%{drt_name}\S*,-I%{_includedir}/%{name}/%{drt_name}/import,g' $RPM_BUILD_ROOT/%{_sysconfdir}/%{dmd_name}.conf
sed -ri 's,-I\S*%{phb_name}\S*,-I%{_includedir}/%{name}/%{phb_name},g' $RPM_BUILD_ROOT/%{_sysconfdir}/%{dmd_name}.conf
sed -ri 's,-L-L\S*lib([0-9]+)\S*,-L-L%{_prefix}/lib\1,g' $RPM_BUILD_ROOT/%{_sysconfdir}/%{dmd_name}.conf

cd %{build_dir}/%{drt_name}
cp generated/$RPM_OS/release/%{arch_bits}/lib%{drt_name}.a $RPM_BUILD_ROOT/%{_libdir}
cp -R import $RPM_BUILD_ROOT/%{_includedir}/%{name}/%{drt_name}

cd %{build_dir}/%{phb_name}
cp -R {etc,std} $RPM_BUILD_ROOT/%{_includedir}/%{name}/%{phb_name}
cd generated/$RPM_OS/release/%{arch_bits}
rm *.o
cp lib%{phb_name}2.{a,so.*.*.*} $RPM_BUILD_ROOT/%{_libdir}
ldconfig -N $RPM_BUILD_ROOT/%{_libdir}
ln -sf lib%{phb_name}2.so.*.*.* $RPM_BUILD_ROOT/%{_libdir}/lib%{phb_name}2.so

cd %{build_dir}/%{dto_name}
cp -R man/* $RPM_BUILD_ROOT/%{_mandir}
cd generated/$RPM_OS/%{arch_bits}
cp $(ls -I '*.o') $RPM_BUILD_ROOT/%{_bindir}


%post %{phb_name} -p /sbin/ldconfig


%postun %{phb_name} -p /sbin/ldconfig


%files
%defattr(-,root,root)
%license LICENSE_1_0.txt
%doc README.md
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/*/*
%defattr(755,root,root)
%{_bindir}/%{name}


%files %{drt_name}
%defattr(-,root,root)
%license LICENSE_1_0.txt
%{_libdir}/lib%{drt_name}.*


%files %{drt_name}-devel
%defattr(-,root,root)
%license LICENSE_1_0.txt
%{_includedir}/%{name}/%{drt_name}


%files %{phb_name}
%defattr(-,root,root)
%license LICENSE_1_0.txt
%{_libdir}/lib%{phb_name}2.a
%{_libdir}/lib%{phb_name}2.so.*


%files %{phb_name}-devel
%defattr(-,root,root)
%license LICENSE_1_0.txt
%{_libdir}/lib%{phb_name}2.so
%{_includedir}/%{name}/%{phb_name}


%files %{dto_name}
%defattr(-,root,root)
%{_bindir}/catdoc
%{_bindir}/changed
%{_bindir}/ddemangle
%{_bindir}/detab
%{_bindir}/dget
%{_bindir}/dustmite
%{_bindir}/rdmd
%{_bindir}/tolf
%{_mandir}/*/rdmd.*



%changelog
* Wed Apr 12 2017 Laurent Tréguier <laurent@treguier.org> - 2.074.0-7
- started using ldconfig

* Wed Apr 12 2017 Laurent Tréguier <laurent@treguier.org> - 2.074.0-6
- added %config macro for dmd.conf

* Wed Apr 12 2017 Laurent Tréguier <laurent@treguier.org> - 2.074.0-5
- added more symlinks for libphobos2.so

* Tue Apr 11 2017 Laurent Tréguier <laurent@treguier.org> - 2.074.0-4
- fixed libphobos so files and symlinks

* Tue Apr 11 2017 Laurent Tréguier <laurent@treguier.org> - 2.074.0-3
- added dmd dependency to dmd-tools

* Tue Apr 11 2017 Laurent Tréguier <laurent@treguier.org> - 2.074.0-2
- added curl build dependency
- added tools subpackage

* Tue Apr 11 2017 Laurent Tréguier <laurent@treguier.org> - 2.074.0-1
- created specfile
