%global         source_name arc-icon-theme

Name:           arc-paper-icon-theme
Version:        20161122
Release:        8%{?dist}
Summary:        The Arc icon theme patched to use Paper as secondary theme

License:        GPLv3
URL:            https://github.com/horst3180/%{source_name}
Source0:        https://github.com/horst3180/%{source_name}/archive/%{version}.tar.gz#/%{source_name}-%{version}.tar.gz

Patch0:         arc-paper-icon-theme-makefile.patch
Patch1:         arc-paper-icon-theme-index.patch

BuildArch:      noarch
BuildRequires:  autoconf
BuildRequires:  automake
Requires:       hicolor-icon-theme
Requires:       gnome-icon-theme
Requires:       gtk-murrine-engine
%if "0%{?epel}" == "0"
Recommends:     paper-icon-theme
%endif

%description
Icon theme for the Arc-Gtk-theme, patched to use Paper as secondary icon theme.


%prep
%setup -q -n %{source_name}-%{version}
%patch0
%patch1


%build
NOCONFIGURE=yes ./autogen.sh
%configure
%make_build
mv Arc 'Arc Paper'


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license COPYING
%doc README.md
"%{_datadir}/icons/Arc Paper/"



%changelog
* Thu Sep 14 2017 Laurent Tréguier <laurent@treguier.org> - 20161122-8
- fixed building on EPEL
- removed useless gtk3-devel build dependency

* Thu Apr 20 2017 Laurent Tréguier <laurent@treguier.org> - 20161122-7
- synced build dependencies with upstream

* Fri Mar 31 2017 Laurent Tréguier <laurent@treguier.org> - 20161122-6
- added condition to only recommend paper-icon-theme with rpm >= 4.12

* Fri Mar 31 2017 Laurent Tréguier <laurent@treguier.org> - 20161122-5
- added paper-icon-theme as weak dependency

* Wed Mar 15 2017 Laurent Tréguier <laurent@treguier.org> - 20161122-4
- clean up build root before install

* Sun Mar 12 2017 Laurent Tréguier <laurent@treguier.org> - 20161122-3
- updated specfile

* Thu Mar  9 2017 Laurent Tréguier <laurent@treguier.org> - 20161122-2
- rewrite specfile
