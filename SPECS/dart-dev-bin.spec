%global         debug_package   %{nil}
%global         source_name     dart

%ifarch x86_64
%global         source_arch     x64
%else
%global         source_arch     ia32
%endif

%define         release_dir     $RPM_BUILD_DIR/%{name}-%{version}-%{source_arch}/dart-sdk
%define         dev_version     dev.0.0

Name:           %{source_name}-dev-bin
Epoch:          1
Version:        2.2.0
Release:        0.1.%{dev_version}%{?dist}
Summary:        The Dart SDK, including the VM, dart2js, core libraries, and more
Conflicts:      %{source_name}
Conflicts:      %{source_name}-bin
Obsoletes:      %{source_name}  < %{version}
Provides:       %{source_name}  = %{version}

License:        BSD
URL:            https://www.dartlang.org
Source0:        https://storage.googleapis.com/dart-archive/channels/dev/release/%{version}-%{dev_version}/sdk/dartsdk-linux-ia32-release.zip#/%{name}-%{version}-ia32.zip
Source1:        https://storage.googleapis.com/dart-archive/channels/dev/release/%{version}-%{dev_version}/sdk/dartsdk-linux-x64-release.zip#/%{name}-%{version}-x64.zip

BuildRequires:  unzip

%description
Dart is an open-source, scalable programming language, with robust libraries and
runtimes, for building web, server, and mobile apps.


%prep
%setup -q -a 0 -T -c -n %{name}-%{version}-ia32
%setup -q -a 1 -T -c -n %{name}-%{version}-x64


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
%attr(-,root,root) %{_libdir}/%{source_name}
%attr(755,root,root) %{_bindir}/*



%changelog
* Mon Nov 19 2018 Laurent Tréguier <laurent@treguier.org> - 1:2.2.0-0.1.dev.0.0
- new version

* Sun Nov 18 2018 Laurent Tréguier <laurent@treguier.org> - 1:2.1.0-1
- added epoch
- moved dev version to release

* Fri Nov 09 2018 Laurent Tréguier <laurent@treguier.org> - 2.1.0_dev.9.4-1
- new version

* Thu Nov 08 2018 Laurent Tréguier <laurent@treguier.org> - 2.1.0_dev.9.3-1
- new version

* Wed Nov 07 2018 Laurent Tréguier <laurent@treguier.org> - 2.1.0_dev.9.2-1
- new version

* Sun Nov 04 2018 Laurent Tréguier <laurent@treguier.org> - 2.1.0_dev.9.1-1
- new version

* Fri Nov 02 2018 Laurent Tréguier <laurent@treguier.org> - 2.1.0_dev.8.0-2
- fixed build on Opensuse

* Thu Oct 25 2018 Laurent Tréguier <laurent@treguier.org> - 2.1.0_dev.8.0-1
- new version

* Sat Oct 13 2018 Laurent Tréguier <laurent@treguier.org> - 2.1.0_dev.7.1-1
- created specfile
