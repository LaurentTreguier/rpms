Name:           rust-src-installer
Version:        1.0.0
Release:        1%{?dist}
Summary:        The rust sources

License:        (ASL 2.0 or MIT) and (BSD and ISC and MIT)
URL:            http://rust-lang.org/
Source0:        %{name}-profile.sh

BuildArch:      noarch
Requires:       curl
Requires:       gzip
Requires:       rust

%description
An automatic installer for rust source files.


%prep
mkdir -p $RPM_BUILD_DIR/%{name}-%{version}
cd $RPM_BUILD_DIR/%{name}-%{version}


%build
rpm --eval "$(cat %SOURCE0)" > $RPM_BUILD_DIR/%{name}-%{version}/%{name}.sh


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{%{_sysconfdir}/profile.d,%{_usrsrc}/rust}
cp $RPM_BUILD_DIR/%{name}-%{version}/%{name}.sh \
    $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d


%preun
rm -rf "%{_usrsrc}"/rust/*


%triggerin -- rust
temp=$(mktemp -d)
cd $temp
curl -sL https://github.com/rust-lang/rust/archive/$(rpm -q --qf '%%{VERSION}' rust).tar.gz \
    | tar -xzC . --strip-components 1
rm -rf "%{_usrsrc}"/rust
mv src %{_usrsrc}/rust
rm -rf "$temp"


%files
%config %{_sysconfdir}/profile.d/*
%{_usrsrc}/rust



%changelog
* Sun May 28 2017 Laurent Tréguier <laurent@treguier.org> - 1.0.0-1
- created specfile
