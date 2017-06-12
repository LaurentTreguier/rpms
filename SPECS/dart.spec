%global         debug_package   %{nil}
%global         temp_dir        %(mktemp -d)

%ifarch x86_64
%global         out_arch        X64
%else
%global         out_arch        IA32
%endif

%define         release_dir     $RPM_BUILD_DIR/%{name}-%{version}/sdk/out/Release%{out_arch}/%{name}-sdk

Name:           dart
Version:        1.24.0
Release:        1%{?dist}
Summary:        The Dart SDK, including the VM, dart2js, core libraries, and more
Conflicts:      %{name}-bin

License:        BSD
URL:            https://www.dartlang.org
# Fixes 'gcc -dumpversion' with gcc7
Source0:        dart-fake-gcc

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  ninja-build
BuildRequires:  python2

BuildRequires:  ld-linux.so.2
BuildRequires:  %{_libdir}/libtinfo.so.5

%description
Dart is an open-source, scalable programming language, with robust libraries and runtimes, for building web, server, and mobile apps.


%prep
mkdir -p %{temp_dir}/{sdk,depot_tools}

cd %{temp_dir}/sdk
git init .
git remote add origin https://github.com/dart-lang/sdk.git
git fetch --tags
tag_date=$(git log -1 --format=%ai %{version})
version_commit=$(git rev-parse %{version})

cd %{temp_dir}/depot_tools
git init .
git remote add origin https://chromium.googlesource.com/chromium/tools/depot_tools.git
git pull origin master
git checkout $(git rev-list -n 1 --before "$tag_date" master)

cp %SOURCE0 ./c++
chmod +x c++
export PATH="$PWD:$PATH"

mkdir -p $RPM_BUILD_DIR/%{name}-%{version}
cd $RPM_BUILD_DIR/%{name}-%{version}
gclient config https://github.com/dart-lang/sdk
gclient sync --revision=$version_commit


%build
export PATH="%{temp_dir}/depot_tools:$PATH"
cd $RPM_BUILD_DIR/%{name}-%{version}/sdk
./tools/build.py --mode release create_sdk
rm -rf %{temp_dir}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{%{_bindir},%{_libdir}/%{name}}
rm -r %{release_dir}/include
cp -R %{release_dir}/* $RPM_BUILD_ROOT/%{_libdir}/%{name}
rm $RPM_BUILD_ROOT/%{_libdir}/%{name}/{LICENSE,README}

for f in $(ls %{release_dir}/bin)
do
    if [[ -f %{release_dir}/bin/$f ]]
    then
        ln -s %{_libdir}/%{name}/bin/$f $RPM_BUILD_ROOT/%{_bindir}/$f
    fi
done


%files
%license %{release_dir}/LICENSE
%doc %{release_dir}/README
%{_libdir}/%{name}
%attr(755,root,root) %{_bindir}/*



%changelog
* Mon Jun 12 2017 Laurent Tréguier <laurent@treguier.org> - 1.24.0-1
- new version
- removed header files

* Mon May 15 2017 Laurent Tréguier <laurent@treguier.org> - 1.23.0-2
- changed glibc(x86-32) dependency to ld-linux.so.2
- removed include directory from /usr/lib/dart
- fixed ownership of /usr/include (now /usr/include/*)
- added conflict with dart-bin

* Thu Apr 27 2017 Laurent Tréguier <laurent@treguier.org> - 1.23.0-1
- created specfile
