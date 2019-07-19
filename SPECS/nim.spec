%global         debug_package   %{nil}
%global         nimble_version  0.10.2
%global         koch_options    -d:release -d:useGnuReadline

Name:           nim
Version:        0.20.2
Release:        1%{?dist}
Summary:        A compiled, garbage-collected systems programming language

License:        MIT and BSD
URL:            http://nim-lang.org/
Source0:        https://nim-lang.org/download/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc
Requires:       gcc
Requires:       gcc-c++
Provides:       nimble  = %{nimble_version}

%description
Nim is a compiled, garbage-collected systems programming language with a design
that focuses on efficiency, expressiveness, and elegance (in the order of
priority).


%prep
%autosetup


%build
./build.sh
./bin/%{name} c -d:release koch
./koch boot         %{koch_options}
./koch tools        %{koch_options}
./koch nimble       %{koch_options}
./koch geninstall


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{%{_bindir},%{_datadir}}
./install.sh $RPM_BUILD_ROOT/%{_datadir}
chmod +x bin/*
cp -u bin/* $RPM_BUILD_ROOT/%{_datadir}/%{name}/bin

for binary in $(ls bin)
do
    ln -s %{_datadir}/%{name}/bin/$binary $RPM_BUILD_ROOT/%{_bindir}
done


%files
%license copying.txt
%doc doc
%doc examples
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}



%changelog
* Fri Jul 19 2019 Laurent Tréguier <laurent@treguier.org> - 0.20.2-1
- new version

* Thu Jun 06 2019 Laurent Tréguier <laurent@treguier.org> - 0.20.0-1
- new version

* Sat May 11 2019 Laurent Tréguier <laurent@treguier.org> - 0.19.6-1
- new version

* Sat Feb 02 2019 Laurent Tréguier <laurent@treguier.org> - 0.19.4-1
- new version

* Tue Jan 01 2019 Laurent Tréguier <laurent@treguier.org> - 0.19.2-1
- new version

* Thu Sep 27 2018 Laurent Tréguier <laurent@treguier.org> - 0.19.0-1
- new version

* Fri Mar 02 2018 Laurent Tréguier <laurent@treguier.org> - 0.18.0-1
- new version

* Thu Sep 07 2017 Laurent Tréguier <laurent@treguier.org> - 0.17.2-2
- removed debuginfo

* Thu Sep 07 2017 Laurent Tréguier <laurent@treguier.org> - 0.17.2-1
- new version
- forced executable bit on binaries
- added examples to doc

* Wed Jun 21 2017 Laurent Tréguier <laurent@treguier.org> - 0.17.0-2
- added nimble provides tag
- added docs

* Sun Jun 18 2017 Laurent Tréguier <laurent@treguier.org> - 0.17.0-1
- created specfile
