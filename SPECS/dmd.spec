%global         debug_package   %{nil}

%global         dmd_name        dmd
%global         drt_name        druntime
%global         phb_name        phobos
%global         dto_name        tools
%global         arch_bits       %(getconf LONG_BIT)
%global         make_options    RELEASE=1 MODEL=%{arch_bits}

%define         build_dir       $RPM_BUILD_DIR/%{name}-%{version}-build
%define         install_dir     $RPM_BUILD_DIR/%{name}-%{version}-install

Name:           %{dmd_name}
Version:        2.079.1
Release:        1%{?dist}
Summary:        Digital Mars D Compiler

License:        Boost
URL:            http://dlang.org/
Source0:        https://github.com/dlang/%{dmd_name}/archive/v%{version}.tar.gz#/%{name}-%{dmd_name}-%{version}.tar.gz
Source1:        https://github.com/dlang/%{drt_name}/archive/v%{version}.tar.gz#/%{name}-%{drt_name}-%{version}.tar.gz
Source2:        https://github.com/dlang/%{phb_name}/archive/v%{version}.tar.gz#/%{name}-%{phb_name}-%{version}.tar.gz
Source3:        https://github.com/dlang/%{dto_name}/archive/v%{version}.tar.gz#/%{name}-%{dto_name}-%{version}.tar.gz
Source10:       http://www.boost.org/LICENSE_1_0.txt#/%{name}-%{version}-LICENSE
Source20:       macros.%{name}

%if 0%{?_with_bootstrap}
BuildRequires:  curl
%else
BuildRequires:  %{name}
%endif

Requires:       %{name}-%{phb_name}-devel%{?_isa}   = %{version}-%{release}
Obsoletes:      %{name}-%{drt_name}                 < %{version}-%{release}
Obsoletes:      %{name}-%{drt_name}-devel           < %{version}-%{release}
Obsoletes:      %{name}-config                      < %{version}-%{release}

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
Provides:       %{name}-%{phb_name}-static%{?_isa} = %{version}-%{release}

%description %{phb_name}-devel
The phobos-devel package contains header files for developing D
applications that use phobos.


%package %{dto_name}
Summary:        Ancillary tools for the D programming language compiler
BuildRequires:  curl-devel
Requires:       %{dmd_name}%{?_isa} = %{version}-%{release}

%description %{dto_name}
This repository hosts various tools redistributed with DMD or used internally
during various build tasks.


%prep
%setup -q -b 0
%setup -q -b 1
%setup -q -b 2
%setup -q -b 3

rm -rf %{build_dir}
mkdir -p %{build_dir}

for component in %{dmd_name} %{drt_name} %{phb_name} %{dto_name}
do
    cp -R $RPM_BUILD_DIR/$component-%{version} %{build_dir}/$component
done

cp %SOURCE10 $RPM_BUILD_DIR/%{dmd_name}-%{version}/LICENSE_1_0.txt


%build
cd %{build_dir}/%{dmd_name}
%make_build %{?_with_bootstrap: AUTO_BOOTSTRAP=1} \
            %{make_options} -f posix.mak

for component in %{drt_name} %{phb_name} %{dto_name}
do
    cd %{build_dir}/$component
    %make_build %{?_with_bootstrap: HOST_DMD=ldmd2} \
                %{!?_with_bootstrap: DMD=../%{dmd_name}/generated/$RPM_OS/release/%{arch_bits}/%{name}} \
                %{make_options} -f posix.mak
done


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{%{_bindir},%{_libdir},%{_includedir}/%{name}/{%{drt_name},%{phb_name}},%{_sysconfdir},%{_mandir},%{_rpmconfigdir}/macros.d}

# dmd
cd %{build_dir}/%{dmd_name}
cp generated/$RPM_OS/release/%{arch_bits}/%{dmd_name} $RPM_BUILD_ROOT/%{_bindir}
cp ini/$RPM_OS/bin%{arch_bits}/*.conf $RPM_BUILD_ROOT/%{_sysconfdir}
cp -R docs/man/* $RPM_BUILD_ROOT/%{_mandir}
sed -ri 's,-I\S*%{drt_name}\S*,-I%{_includedir}/%{name}/%{drt_name}/import,g' $RPM_BUILD_ROOT/%{_sysconfdir}/%{dmd_name}.conf
sed -ri 's,-I\S*%{phb_name}\S*,-I%{_includedir}/%{name}/%{phb_name},g' $RPM_BUILD_ROOT/%{_sysconfdir}/%{dmd_name}.conf
sed -ri 's,-L-L\S*lib([0-9]+)\S*,-L-L%{_prefix}/lib\1,g' $RPM_BUILD_ROOT/%{_sysconfdir}/%{dmd_name}.conf

# druntime
cd %{build_dir}/%{drt_name}
cp generated/$RPM_OS/release/%{arch_bits}/lib%{drt_name}.a $RPM_BUILD_ROOT/%{_libdir}
cp -R import $RPM_BUILD_ROOT/%{_includedir}/%{name}/%{drt_name}

# phobos
cd %{build_dir}/%{phb_name}
cp -R {etc,std} $RPM_BUILD_ROOT/%{_includedir}/%{name}/%{phb_name}
cd generated/$RPM_OS/release/%{arch_bits}
rm *.o
cp lib%{phb_name}2.{a,so.*.*.*} $RPM_BUILD_ROOT/%{_libdir}
ldconfig -N $RPM_BUILD_ROOT/%{_libdir}
ln -sf lib%{phb_name}2.so.*.*.* $RPM_BUILD_ROOT/%{_libdir}/lib%{phb_name}2.so

# tools
cd %{build_dir}/%{dto_name}
cp -R man/* $RPM_BUILD_ROOT/%{_mandir}
cd generated/$RPM_OS/%{arch_bits}
cp ddemangle dustmite rdmd $RPM_BUILD_ROOT/%{_bindir}

# macros
cp %{SOURCE20} $RPM_BUILD_ROOT/%{_rpmconfigdir}/macros.d


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post %{phb_name} -p /sbin/ldconfig

%postun %{phb_name} -p /sbin/ldconfig


%files
%license LICENSE_1_0.txt
%doc README.md
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config %{_rpmconfigdir}/macros.d/*
%attr(755,root,root) %{_bindir}/%{name}
%{_libdir}/lib%{drt_name}.a
%{_includedir}/%{name}/%{drt_name}
%{_mandir}/*/%{name}.*
%{_mandir}/*/dumpobj.*
%{_mandir}/*/obj2asm.*


%files %{phb_name}
%license LICENSE_1_0.txt
%{_libdir}/lib%{phb_name}2.so.*


%files %{phb_name}-devel
%license LICENSE_1_0.txt
%{_libdir}/lib%{phb_name}2.a
%{_libdir}/lib%{phb_name}2.so
%{_includedir}/%{name}/%{phb_name}


%files %{dto_name}
%{_mandir}/*/rdmd.*
%defattr(755,root,root)
%{_bindir}/ddemangle
%{_bindir}/dustmite
%{_bindir}/rdmd



%changelog
* Sun Apr 15 2018 Laurent Tréguier <laurent@treguier.org> - 2.079.1-1
- new version

* Sat Mar 03 2018 Laurent Tréguier <laurent@treguier.org> - 2.079.0-1
- new version

* Fri Feb 16 2018 Laurent Tréguier <laurent@treguier.org> - 2.078.3-1
- new version

* Thu Feb 08 2018 Laurent Tréguier <laurent@treguier.org> - 2.078.2-1
- new version

* Mon Jan 22 2018 Laurent Tréguier <laurent@treguier.org> - 2.078.1-1
- new version

* Wed Jan 03 2018 Laurent Tréguier <laurent@treguier.org> - 2.078.0-1
- new version

* Fri Dec 01 2017 Laurent Tréguier <laurent@treguier.org> - 2.077.1-1
- new version

* Thu Nov 02 2017 Laurent Tréguier <laurent@treguier.org> - 2.077.0-1
- new version

* Mon Oct 09 2017 Laurent Tréguier <laurent@treguier.org> - 2.076.1-1
- new version

* Fri Sep 01 2017 Laurent Tréguier <laurent@treguier.org> - 2.076.0-1
- new version

* Wed Aug 16 2017 Laurent Tréguier <laurent@treguier.org> - 2.075.1-2
- removed debuginfo package the proper way

* Tue Aug 15 2017 Laurent Tréguier <laurent@treguier.org> - 2.075.1-1
- new version

* Thu Jul 20 2017 Laurent Tréguier <laurent@treguier.org> - 2.075.0-2
- added obsolotes for dmd-config to fix upgrading

* Wed Jul 19 2017 Laurent Tréguier <laurent@treguier.org> - 2.075.0-1
- new version
- merged dmd-config into dmd

* Thu Jun 15 2017 Laurent Tréguier <laurent@treguier.org> - 2.074.1-5
- dropped bootstrapping

* Thu Jun 15 2017 Laurent Tréguier <laurent@treguier.org> - 2.074.1-4
- added patch to fix segfault when compiling druntime with gcc7
- fixed bootstrapping
- enabled bootstrapping for Fedora versions that didn't build dmd

* Sun Jun 04 2017 Laurent Tréguier <laurent@treguier.org> - 2.074.1-3
- switched to using ldc for bootstrapping process
- fixed build using host dmd instead of just compiled dmd for compiling other components

* Sat Jun 03 2017 Laurent Tréguier <laurent@treguier.org>
- merged druntime packages into dmd

* Fri Jun 02 2017 Laurent Tréguier <laurent@treguier.org> - 2.074.1-1
- new version
- added togglable bootstrapping

* Fri Apr 21 2017 Laurent Tréguier <laurent@treguier.org> - 2.074.0-13
- switched to using ldconfig again to ensure a single libphobos2.so file exists
- removed unnecessary defattr macros for standard permissions

* Sun Apr 16 2017 Laurent Tréguier <laurent@treguier.org> - 2.074.0-12
- removed references to _dmd_includedir to fix EPEL 6 build

* Sun Apr 16 2017 Laurent Tréguier <laurent@treguier.org> - 2.074.0-11
- moved *.a static libs to *-devel subpackages

* Fri Apr 14 2017 Laurent Tréguier <laurent@treguier.org> - 2.074.0-10
- removed debuginfo package
- removed explicit *-devel dependencies on their library counterparts
- removed curl dependency since package isn't bootstrapped anymore
- made *-devel provide *-static
- replaced _includedir/dmd with _dmd_includedir

* Fri Apr 14 2017 Laurent Tréguier <laurent@treguier.org> - 2.074.0-9
- dropped bootstrapping

* Wed Apr 12 2017 Laurent Tréguier <laurent@treguier.org> - 2.074.0-8
- added macros.dmd
- added config subpackage
- added ldconfig run for druntime post and postun
- ensured tools are marked as executable

* Wed Apr 12 2017 Laurent Tréguier <laurent@treguier.org> - 2.074.0-7
- started using ldconfig

* Wed Apr 12 2017 Laurent Tréguier <laurent@treguier.org> - 2.074.0-6
- added config macro for dmd.conf

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
