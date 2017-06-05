%global         debug_package       %{nil}
%global         source_name         swift
%global         build_script_flags  %{?_smp_mflags} --install-prefix=%{_prefix} --release --lldb --llbuild --swiftpm --xctest true --foundation true --libdispatch true

Name:           %{source_name}-language
Version:        3.1.1
Release:        3%{?dist}
Summary:        The Swift programming language

License:        Apache-2.0
URL:            https://swift.org/
Source0:        https://github.com/apple/%{source_name}/archive/%{source_name}-%{version}-RELEASE.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/apple/%{source_name}-clang/archive/%{source_name}-%{version}-RELEASE.tar.gz#/%{name}-clang-%{version}.tar.gz
Source2:        https://github.com/apple/%{source_name}-cmark/archive/%{source_name}-%{version}-RELEASE.tar.gz#/%{name}-cmark-%{version}.tar.gz
Source3:        https://github.com/apple/%{source_name}-corelibs-foundation/archive/%{source_name}-%{version}-RELEASE.tar.gz#/%{name}-corelibs-foundation-%{version}.tar.gz
Source4:        https://github.com/apple/%{source_name}-corelibs-libdispatch/archive/%{source_name}-%{version}-RELEASE.tar.gz#/%{name}-corelibs-libdispatch-%{version}.tar.gz
Source5:        https://github.com/apple/%{source_name}-corelibs-xctest/archive/%{source_name}-%{version}-RELEASE.tar.gz#/#/%{name}-corelibs-xctest-%{version}.tar.gz
Source6:        https://github.com/apple/%{source_name}-llbuild/archive/%{source_name}-%{version}-RELEASE.tar.gz#/%{name}-llbuild-%{version}.tar.gz
Source7:        https://github.com/apple/%{source_name}-lldb/archive/%{source_name}-%{version}-RELEASE.tar.gz#/%{name}-lldb-%{version}.tar.gz
Source8:        https://github.com/apple/%{source_name}-llvm/archive/%{source_name}-%{version}-RELEASE.tar.gz#/%{name}-llvm-%{version}.tar.gz
Source9:        https://github.com/apple/%{source_name}-package-manager/archive/%{source_name}-%{version}-RELEASE.tar.gz#/%{name}-package-manager-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  libtool
BuildRequires:  ninja-build
BuildRequires:  python2
BuildRequires:  rsync
BuildRequires:  swig
BuildRequires:  pkgconfig
BuildRequires:  python2-sphinx
BuildRequires:  libblocksruntime-devel
BuildRequires:  libbsd-devel
BuildRequires:  libcurl-devel
BuildRequires:  libedit-devel
BuildRequires:  libicu-devel
BuildRequires:  libkqueue-devel
BuildRequires:  libsqlite3x-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxml2-devel
BuildRequires:  ncurses-devel
BuildRequires:  python2-devel
BuildRequires:  systemtap-sdt-devel

%description
Swift is a high-performance system programming language.
It has a clean and modern syntax, offers seamless access to existing C and Objective-C code and frameworks, and is memory safe by default.


%package lldb
Summary:        Next generation high-performance debugger (swift version)
Conflicts:      lldb
Provides:       lldb

%description lldb
LLDB is a next generation, high-performance debugger. It is built as a set
of reusable components which highly leverage existing libraries in the
larger LLVM Project, such as the Clang expression parser and LLVM
disassembler.


%package lldb-devel
Summary:        Development files for %{name}-lldb
Requires:       %{name}-lldb%{?_isa} = %{version}-%{release}

%description lldb-devel
The %{name}-lldb-devel package contains libraries and header files for
developing applications that use %{name}-lldb.


%prep
%autosetup -b 0 -n %{source_name}-%{source_name}-%{version}-RELEASE
%autosetup -b 1 -n %{source_name}-clang-%{source_name}-%{version}-RELEASE
%autosetup -b 2 -n %{source_name}-cmark-%{source_name}-%{version}-RELEASE
%autosetup -b 3 -n %{source_name}-corelibs-foundation-%{source_name}-%{version}-RELEASE
%autosetup -b 4 -n %{source_name}-corelibs-libdispatch-%{source_name}-%{version}-RELEASE
%autosetup -b 5 -n %{source_name}-corelibs-xctest-%{source_name}-%{version}-RELEASE
%autosetup -b 6 -n %{source_name}-llbuild-%{source_name}-%{version}-RELEASE
%autosetup -b 7 -n %{source_name}-lldb-%{source_name}-%{version}-RELEASE
%autosetup -b 8 -n %{source_name}-llvm-%{source_name}-%{version}-RELEASE
%autosetup -b 9 -n %{source_name}-package-manager-%{source_name}-%{version}-RELEASE

cd $RPM_BUILD_DIR

for sdir in llvm clang lldb cmark llbuild
do
    ln -sf %{source_name}-${sdir}-%{source_name}-%{version}-RELEASE ${sdir}
done

for sdir in corelibs-xctest corelibs-foundation corelibs-libdispatch integration-tests
do
    ln -sf %{source_name}-${sdir}-%{source_name}-%{version}-RELEASE %{source_name}-${sdir}
done

ln -sf %{source_name}-%{source_name}-%{version}-RELEASE %{source_name}
ln -sf %{source_name}-package-manager-%{source_name}-%{version}-RELEASE swiftpm


%build
export SWIFT_SOURCE_ROOT="$RPM_BUILD_DIR"
cd $RPM_BUILD_DIR/%{source_name}
./utils/build-script %{build_script_flags}
./utils/build-script %{build_script_flags} \
    --extra-cmake-options="-DSWIFT_BUILD_SOURCEKIT=TRUE" \
    --reconfigure


%install
rm -rf $RPM_BUILD_ROOT
export SWIFT_SOURCE_ROOT="$RPM_BUILD_DIR"

cd $RPM_BUILD_DIR/build/Ninja-ReleaseAssert/lldb-linux-*/scripts
find . -type f -exec sed -ri 's,lib/python2\.7,%{_lib}/python2.7,g' {} ';'

cd $RPM_BUILD_DIR/%{source_name}
./utils/build-script %{build_script_flags} \
    --install-destdir $RPM_BUILD_ROOT \
    --install-lldb \
    --install-llbuild \
    --install-swiftpm \
    --install-xctest \
    --install-foundation

cd $RPM_BUILD_DIR/build/Ninja-ReleaseAssert

pushd %{source_name}-linux-*
mkdir -p $RPM_BUILD_ROOT/{%{_libdir}/%{source_name},%{_mandir}/man1}

cp bin/%{source_name} $RPM_BUILD_ROOT/%{_bindir}
cp lib/libsourcekitdInProc.so $RPM_BUILD_ROOT/%{_libdir}
cp -RL lib/%{source_name}/{clang,linux,shims} $RPM_BUILD_ROOT/%{_libdir}/%{source_name}
cp docs/tools/%{source_name}.1 $RPM_BUILD_ROOT/%{_mandir}/man1

ln -s %{source_name} $RPM_BUILD_ROOT/%{_bindir}/swiftc
ln -s %{source_name} $RPM_BUILD_ROOT/%{_bindir}/swift-autolink-extract
popd

cd libdispatch-linux-*
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

cd $RPM_BUILD_ROOT/%{_prefix}
rmdir -p local/include

for part in $(ls lib)
do
    if [[ $part != %{source_name} ]]
    then
        cp -R lib/$part %{_lib}
        rm -r lib/$part
    fi
done

cp -R %{_lib}/%{source_name}/* lib/%{source_name}
rm -r %{_lib}/%{source_name}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post lldb -p /sbin/ldconfig

%postun lldb -p /sbin/ldconfig


%files
%license $RPM_BUILD_DIR/%{source_name}/LICENSE.txt
%doc %{_mandir}/*/*
%attr(755,root,root) %{_bindir}/%{source_name}*
%{_prefix}/*/%{source_name}
%{_libdir}/libsourcekitdInProc.so
%{_libexecdir}/*


%files lldb
%{_libdir}/liblldb.so.*
%{_libdir}/lldb
%{_libdir}/python2.7/*
%defattr(755,root,root)
%{_bindir}/lldb*
%{_bindir}/repl_swift


%files lldb-devel
%{_includedir}/lldb
%{_libdir}/liblldb.so



%changelog
* Sat Jun 03 2017 Laurent Tréguier <laurent@treguier.org> - 3.1.1-3
- made swift directory always go to /usr/lib
- changed python related dependencies to python2*
- fixed lldb being provided by swift-language-lldb-devel

* Thu Jun 01 2017 Laurent Tréguier <laurent@treguier.org> - 3.1.1-2
- added libraries symlinks

* Tue May 23 2017 Laurent Tréguier <laurent@treguier.org> - 3.1.1-1
- created specfile
