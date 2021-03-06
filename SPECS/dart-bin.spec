%global         debug_package   %{nil}
%global         source_name     dart

%ifarch x86_64
%global         source_arch     x64
%else
%global         source_arch     ia32
%endif

%define         release_dir     $RPM_BUILD_DIR/%{name}-%{version}-%{source_arch}/dart-sdk

Name:           dart-bin
Epoch:          1
Version:        2.10.3
Release:        1%{?dist}
Summary:        The Dart SDK, including the VM, dart2js, core libraries, and more
Conflicts:      %{source_name}
Conflicts:      %{source_name}-dev-bin
Obsoletes:      %{source_name}  < %{version}
Provides:       %{source_name}  = %{version}

License:        BSD
URL:            https://www.dartlang.org
Source0:        https://storage.googleapis.com/dart-archive/channels/stable/release/%{version}/sdk/dartsdk-linux-ia32-release.zip#/%{name}-%{version}-ia32.zip
Source1:        https://storage.googleapis.com/dart-archive/channels/stable/release/%{version}/sdk/dartsdk-linux-x64-release.zip#/%{name}-%{version}-x64.zip

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
* Tue Nov  3 19:49:14 CET 2020 Laurent Tréguier <laurent@treguier.org> - 1:2.10.3-1
- new version

* Thu Oct 15 2020 Laurent Tréguier <laurent@treguier.org> - 1:2.10.2-1
- new version

* Tue Oct 06 2020 Laurent Tréguier <laurent@treguier.org> - 1:2.10.1-1
- new version

* Sat Oct 03 2020 Laurent Tréguier <laurent@treguier.org> - 1:2.10.0-1
- new version

* Thu Aug 13 2020 Laurent Tréguier <laurent@treguier.org> - 1:2.9.1-1
- new version

* Thu Aug 06 2020 Laurent Tréguier <laurent@treguier.org> - 1:2.9.0-1
- new version

* Fri Jun 05 2020 Laurent Tréguier <laurent@treguier.org> - 1:2.8.4-1
- new version

* Sat May 16 2020 Laurent Tréguier <laurent@treguier.org> - 1:2.8.2-1
- new version

* Thu May 07 2020 Laurent Tréguier <laurent@treguier.org> - 1:2.8.1-1
- new version

* Tue Mar 24 2020 Laurent Tréguier <laurent@treguier.org> - 1:2.7.2-1
- new version

* Thu Jan 23 2020 Laurent Tréguier <laurent@treguier.org> - 1:2.7.1-1
- new version

* Wed Dec 11 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.7.0-1
- new version

* Tue Nov 12 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.6.1-1
- new version

* Tue Nov 05 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.6.0-1
- new version

* Tue Oct 08 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.5.2-1
- new version

* Fri Sep 27 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.5.1-1
- new version

* Wed Sep 11 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.5.0-1
- new version

* Wed Aug 07 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.4.1-1
- new version

* Thu Jun 27 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.4.0-1
- new version

* Wed Jun 12 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.3.2-1
- new version

* Tue May 21 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.3.1-1
- new version

* Wed May 08 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.3.0-1
- new version

* Wed Feb 27 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.2.0-1
- new version

* Wed Feb 20 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.1.1-1
- new version

* Sun Nov 18 2018 Laurent Tréguier <laurent@treguier.org> - 1:2.1.0-1
- added epoch

* Thu Nov 15 2018 Laurent Tréguier <laurent@treguier.org> - 2.1.0-1
- new version

* Fri Nov 02 2018 Laurent Tréguier <laurent@treguier.org> - 2.0.0-2
- added Conflicts and Provides clauses
- fixed build on Opensuse

* Mon Aug 06 2018 Laurent Tréguier <laurent@treguier.org> - 2.0.0-1
- new version

* Sun Dec 17 2017 Laurent Tréguier <laurent@treguier.org> - 1.24.3-1
- new version

* Fri Jul 14 2017 Laurent Tréguier <laurent@treguier.org> - 1.24.2-2
- fixed permission issue

* Fri Jun 23 2017 Laurent Tréguier <laurent@treguier.org> - 1.24.2-1
- new version

* Wed Jun 14 2017 Laurent Tréguier <laurent@treguier.org> - 1.24.1-1
- new version

* Mon Jun 12 2017 Laurent Tréguier <laurent@treguier.org> - 1.24.0-1
- new version

* Mon May 15 2017 Laurent Tréguier <laurent@treguier.org> - 1.23.0-1
- created specfile
