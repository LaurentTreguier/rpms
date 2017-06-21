%global         nimble_version  0.8.6
%global         koch_options    -d:release -d:useGnuReadline

Name:           nim
Version:        0.17.0
Release:        2%{?dist}
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
%doc doc/*
%{_bindir}/*
%{_datadir}/%{name}



%changelog
* Wed Jun 21 2017 Laurent Tréguier <laurent@treguier.org> - 0.17.0-2
- added nimble provides tag
- added docs

* Sun Jun 18 2017 Laurent Tréguier <laurent@treguier.org> - 0.17.0-1
- created specfile
