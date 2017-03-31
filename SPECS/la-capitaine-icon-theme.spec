Name:           la-capitaine-icon-theme
Version:        0.4.0
Release:        2%{?dist}
Summary:        A set of icons that takes inspiration from macOS and Google's Material Design

License:        GPLv3
URL:            https://krourke.org/projects/art/la-capitaine-icon-theme
Source0:        https://github.com/keeferrourke/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  %{_bindir}/lsb_release

%description
La Capitaine is an icon pack designed to integrate with most desktop environments.
The set of icons takes inspiration from the latest iterations of macOS and Google's Material Design through the use of visually pleasing gradients, shadowing, and simple icon geometry.
Every image in this theme is a scalable vector graphic so it will look great at any size, on any screen.

%prep
%autosetup


%build
cd $RPM_BUILD_DIR/%{name}-%{version}
chmod +x configure
echo no | ./configure


%install
%define icon_dir "$RPM_BUILD_ROOT/%{_datadir}/icons/La Capitaine"
rm -rf $RPM_BUILD_ROOT
rm *.{svg,png}
mkdir -p %{icon_dir}
cp -R $RPM_BUILD_DIR/%{name}-%{version}/* %{icon_dir}


%files
%license LICENSE
%doc README.md
"%{_datadir}/icons/La Capitaine"



%changelog
* Wed Mar 15 2017 Laurent Tréguier <laurent@treguier.org> - 0.4.0-2
- replaced macros with $RPM_*

* Tue Mar 14 2017 Laurent Tréguier <laurent@treguier.org>
- created specfile
