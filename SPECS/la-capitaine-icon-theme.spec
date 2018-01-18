%global         git_date        20180117
%global         git_commit      b473b39d12e83571be1eb684c3dfecd48d95afbb
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
