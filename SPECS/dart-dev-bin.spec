%global         debug_package   %{nil}
%global         source_name     dart

%ifarch x86_64
%global         source_arch     x64
%else
%global         source_arch     ia32
%endif

%define         release_dir     $RPM_BUILD_DIR/%{name}-%{version}-%{dev_version}-%{source_arch}/dart-sdk
%define         dev_version     dev.0.0

Name:           %{source_name}-dev-bin
Epoch:          1
Version:        2.8.0
Release:        0.1.%{dev_version}%{?dist}
Summary:        The Dart SDK, including the VM, dart2js, core libraries, and more
Conflicts:      %{source_name}
Conflicts:      %{source_name}-bin
Obsoletes:      %{source_name}  < %{version}
Provides:       %{source_name}  = %{version}

License:        BSD
URL:            https://www.dartlang.org
Source0:        https://storage.googleapis.com/dart-archive/channels/dev/release/%{version}-%{dev_version}/sdk/dartsdk-linux-ia32-release.zip#/%{name}-%{version}-%{dev_version}-ia32.zip
Source1:        https://storage.googleapis.com/dart-archive/channels/dev/release/%{version}-%{dev_version}/sdk/dartsdk-linux-x64-release.zip#/%{name}-%{version}-%{dev_version}-x64.zip

BuildRequires:  unzip

%description
Dart is an open-source, scalable programming language, with robust libraries and
runtimes, for building web, server, and mobile apps.


%prep
%setup -q -a 0 -T -c -n %{name}-%{version}-%{dev_version}-ia32
%setup -q -a 1 -T -c -n %{name}-%{version}-%{dev_version}-x64


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
* Wed Dec 11 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.8.0-0.1.dev.0.0
- new version

* Tue Dec 03 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.7.0-0.1.dev.2.1
- new release

* Thu Nov 21 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.7.0-0.1.dev.1.0
- new release

* Tue Nov 05 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.7.0-0.1.dev.0.0
- new version

* Thu Oct 24 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.6.0-0.1.dev.8.2
- new release

* Mon Oct 21 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.6.0-0.1.dev.8.1
- new release

* Thu Oct 17 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.6.0-0.1.dev.8.0
- new release

* Fri Oct 11 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.6.0-0.1.dev.7.0
- new release

* Tue Oct 08 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.6.0-0.1.dev.6.0
- new release

* Mon Sep 30 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.6.0-0.1.dev.4.0
- new release

* Thu Sep 26 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.6.0-0.1.dev.3.0
- new release

* Wed Sep 25 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.6.0-0.1.dev.2.0
- new release

* Tue Sep 17 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.6.0-0.1.dev.1.0
- new release

* Wed Sep 11 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.6.0-0.1.dev.0.0
- new version

* Thu Aug 29 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.5.0-0.1.dev.4.0
- new release

* Wed Aug 28 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.5.0-0.1.dev.3.0
- new release

* Fri Aug 16 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.5.0-0.1.dev.2.1
- new release

* Mon Aug 12 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.5.0-0.1.dev.2.0
- new release

* Tue Jul 09 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.5.0-0.1.dev.1.0
- new release

* Fri Jun 21 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.5.0-0.1.dev.0.0
- new version

* Wed Jun 19 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.4.0-0.1.dev.0.1
- new release

* Fri Jun 14 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.4.0-0.1.dev.0.0
- new version

* Wed Jun 12 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.3.3-0.1.dev.0.0
- new version

* Wed Jun 05 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.3.2-0.1.dev.0.1
- new release

* Wed May 22 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.3.2-0.1.dev.0.0
- new version

* Tue May 21 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.3.1-1
- new release

* Wed May 08 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.3.1-0.1.dev.0.0
- new version

* Wed May 01 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.3.0-0.1.dev.0.5
- new release

* Wed Apr 24 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.3.0-0.1.dev.0.3
- new release

* Thu Apr 18 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.3.0-0.1.dev.0.1
- new release

* Wed Apr 17 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.2.1-0.1.dev.4.2
- new release

* Thu Apr 11 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.2.1-0.1.dev.4.0
- new release

* Mon Apr 08 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.2.1-0.1.dev.3.1
- new release

* Tue Apr 02 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.2.1-0.1.dev.3.0
- new release

* Sun Mar 31 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.2.1-0.1.dev.2.0
- new release

* Fri Mar 15 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.2.1-0.1.dev.1.1
- new release

* Wed Feb 27 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.2.1-0.1.dev.0.0
- new version

* Wed Feb 27 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.2.0-1
- new release

* Tue Feb 26 2019 Laurent Tréguier <laurent@treguier.org> - 1:2.2.0-0.1.dev.2.1
- new release

* Fri Dec 14 2018 Laurent Tréguier <laurent@treguier.org> - 1:2.2.0-0.1.dev.1.1
- new release

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
