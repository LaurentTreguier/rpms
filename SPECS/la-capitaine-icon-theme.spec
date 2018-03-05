%global         git_date        20180304
%global         git_commit      db69f4e063c9831e8e93b23999ac815f044bb999
%global         configure       ./configure
%global         conflict_files  actions/22x22 \\\
                                devices/scalable \\\
                                status/scalable \\\
                                panel/16 \\\
                                panel/24 \\\
                                places/16x16

Name:           la-capitaine-icon-theme
Version:        0.5.0.%{git_date}
Release:        1%{?dist}
Summary:        A set of icons that takes inspiration from macOS and Google's Material Design

License:        GPLv3
URL:            https://krourke.org/projects/art/la-capitaine-icon-theme
Source0:        https://github.com/keeferrourke/%{name}/archive/%{git_commit}.zip#/%{name}-%{git_commit}.zip

BuildArch:      noarch
BuildRequires:  %{_bindir}/lsb_release

%description
La Capitaine is an icon pack designed to integrate with most desktop
environments. The set of icons takes inspiration from the latest iterations of
macOS and Google's Material Design through the use of visually pleasing
gradients, shadowing, and simple icon geometry. Every image in this theme is a
scalable vector graphic so it will look great at any size, on any screen.


%prep
%autosetup -n %{name}-%{git_commit}
sed -ri 's/ln \-sf /ln -sfr /g' configure


%build
mkdir -p $RPM_BUILD_DIR/%{name}-build{,-darkgtk}{,-darkpanel}

for d in $(ls -d $RPM_BUILD_DIR/%{name}-build*)
do
    cp -R * $d
done

pushd $RPM_BUILD_DIR
pushd %{name}-build
echo $'n\nn\nn' | %configure
sed -ri 's/Name=(.*)/Name=\1/' index.theme
popd
pushd %{name}-build-darkgtk
echo $'y\nn\nn' | %configure
sed -ri 's/Name=(.*)/Name=\1 (Dark GTK)/' index.theme
popd
pushd %{name}-build-darkpanel
echo $'n\ny\nn' | %configure
sed -ri 's/Name=(.*)/Name=\1 (Dark Panel)/' index.theme
popd
pushd %{name}-build-darkgtk-darkpanel
echo $'y\ny\nn' | %configure
sed -ri 's/Name=(.*)/Name=\1 (Dark GTK, Dark panel)/' index.theme
popd
popd


%install
rm -rf $RPM_BUILD_ROOT
icon_dir=$RPM_BUILD_ROOT/%{_datadir}/icons
mkdir -p $icon_dir
cd $icon_dir
cp -R $RPM_BUILD_DIR/%{name}-build                      "$icon_dir/La Capitaine"
cp -R $RPM_BUILD_DIR/%{name}-build-darkgtk              "$icon_dir/La Capitaine (Dark GTK)"
cp -R $RPM_BUILD_DIR/%{name}-build-darkpanel            "$icon_dir/La Capitaine (Dark Panel)"
cp -R $RPM_BUILD_DIR/%{name}-build-darkgtk-darkpanel    "$icon_dir/La Capitaine (Dark GTK, Dark Panel)"


%pretrans
icon_dir="%{_datadir}/icons/La Capitaine"

for conflict in %{conflict_files}
do
    if [[ -d "$icon_dir/$conflict" ]] && [[ ! -L "$icon_dir/$conflict" ]]
    then
        rm -rf "$icon_dir/$conflict"
        ln -sf unicorn "$icon_dir/$conflict"
    fi
done



%files
%license COPYING
%license LICENSE
%doc Credits.md
%doc README.md
%doc Thanks.md
%{_datadir}/icons/*



%changelog
* Mon Mar 05 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180304-1
- new version

* Fri Feb 23 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180222-1
- new version

* Wed Feb 21 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180220-1
- new version

* Tue Feb 13 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180212-1
- new version

* Mon Feb 12 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180211-1
- new version

* Sun Feb 11 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180210-1
- new version

* Fri Feb 09 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180208-1
- new version

* Thu Feb 08 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180207-1
- new version

* Wed Feb 07 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180206-1
- new version

* Tue Feb 06 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180205-1
- new version

* Mon Feb 05 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180204-1
- new version

* Sun Feb 04 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180203-1
- new version

* Sat Feb 03 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180202-1
- new version

* Fri Feb 02 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180131-1
- new version

* Wed Jan 31 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180130-1
- new version

* Tue Jan 30 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180129-1
- new version

* Mon Jan 29 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180128-1
- new version

* Sat Jan 27 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180126-1
- new version

* Fri Jan 26 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180125-1
- new version

* Wed Jan 24 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180123-1
- new version

* Tue Jan 23 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180122-1
- new version

* Mon Jan 22 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180121-1
- new version

* Sat Jan 20 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180119-1
- new version

* Thu Jan 18 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180117-1
- new version

* Wed Jan 17 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180116-1
- new version

* Thu Jan 11 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180111-1
- new version

* Mon Jan 08 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180108-1
- new version

* Thu Jan 04 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180103-1
- new version

* Sun Sep 03 2017 Laurent Tréguier <laurent@treguier.org> - 0.5.0-1
- new version
- added hack to allow migration from files to symlinks

* Wed Mar 15 2017 Laurent Tréguier <laurent@treguier.org> - 0.4.0-2
- replaced macros with $RPM_*

* Tue Mar 14 2017 Laurent Tréguier <laurent@treguier.org> - 0.4.0-1
- created specfile
