%global         debug_package   %{nil}
%global         source_name     dart

%ifarch x86_64
%global         source_arch     x64
%global         source_num      1
%else
%global         source_arch     ia32
%global         source_num      0
%endif

%define         release_dir     $RPM_BUILD_DIR/%{name}-%{version}-%{source_arch}/dart-sdk

Name:           dart-bin
Version:        1.24.1
Release:        1%{?dist}
Summary:        The Dart SDK, including the VM, dart2js, core libraries, and more
Conflicts:      %{source_name}

License:        BSD
URL:            https://www.dartlang.org
Source0:        https://storage.googleapis.com/dart-archive/channels/stable/release/%{version}/sdk/dartsdk-linux-ia32-release.zip#/%{name}-%{version}-ia32.zip
Source1:        https://storage.googleapis.com/dart-archive/channels/stable/release/%{version}/sdk/dartsdk-linux-x64-release.zip#/%{name}-%{version}-x64.zip

%description
Dart is an open-source, scalable programming language, with robust libraries and runtimes, for building web, server, and mobile apps.


%prep
%autosetup -b 0 -c -T -n %{name}-%{version}-ia32
%autosetup -b 1 -c -T -n %{name}-%{version}-x64


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{%{_bindir},%{_libdir}/%{source_name}}
cp -R %{release_dir}/* $RPM_BUILD_ROOT/%{_libdir}/%{source_name}
rm $RPM_BUILD_ROOT/%{_libdir}/%{source_name}/{LICENSE,README}

for f in $(ls %{release_dir}/bin)
do
    if [[ -f %{release_dir}/bin/$f ]]
    then
        ln -s %{_libdir}/%{source_name}/bin/$f $RPM_BUILD_ROOT/%{_bindir}/$f
    fi
done


%files
%license %{release_dir}/LICENSE
%doc %{release_dir}/README
%{_libdir}/%{source_name}
%attr(755,root,root) %{_bindir}/*



%changelog
* Wed Jun 14 2017 Laurent Tréguier <laurent@treguier.org> - 1.24.1-1
- new version

* Mon Jun 12 2017 Laurent Tréguier <laurent@treguier.org> - 1.24.0-1
- new version

* Mon May 15 2017 Laurent Tréguier <laurent@treguier.org> - 1.23.0-1
- created specfile
