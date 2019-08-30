%global         git_date        20190829
%global         git_commit      284bce94e9921290bb9140819b6bacc9624f9e33
%global         configure       ./configure
%global         conflict_files  actions/22x22 \\\
                                devices/scalable \\\
                                status/scalable \\\
                                panel/16 \\\
                                panel/24 \\\
                                places/16x16

Name:           la-capitaine-icon-theme
Version:        0.6.1.%{git_date}
Release:        2%{?dist}
Summary:        A set of icons that takes inspiration from macOS and Google's Material Design

License:        GPLv3
URL:            https://krourke.org/projects/art/la-capitaine-icon-theme
Source0:        https://github.com/keeferrourke/%{name}/archive/%{git_commit}.tar.gz#/%{name}-%{git_commit}.tar.gz

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
%license Credits.md
%license LICENSE
%license Thanks.md
%doc README.md
%{_datadir}/icons/*



%changelog
* Fri Aug 30 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190829-1
- new version

* Wed Aug 28 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190827-1
- new version

* Fri Aug 16 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190815-1
- new version

* Mon Jul 22 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190720-1
- new version

* Sun Jul 14 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190713-1
- new version

* Thu Jun 20 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190619-1
- new version

* Sat Jun 01 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190530-1
- new version

* Sat May 11 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190510-1
- new version

* Sat Apr 27 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190426-1
- new version

* Fri Apr 19 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190418-1
- new version

* Mon Apr 15 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190414-1
- new version

* Fri Apr 12 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190411-1
- new version

* Tue Apr 09 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190408-1
- new version

* Thu Apr 04 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190402-1
- new version

* Fri Mar 29 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190328-1
- new version

* Tue Mar 19 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190318-1
- new version

* Fri Mar 15 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190314-1
- new version

* Wed Mar 13 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190313-1
- new version

* Sat Mar 02 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190301-1
- new version

* Tue Feb 26 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190225-1
- new version

* Sat Feb 16 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190215-1
- new version

* Wed Feb 13 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190212-1
- new version

* Mon Jan 28 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190127-1
- new version

* Wed Jan 23 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190122-1
- new version

* Sat Jan 12 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190111-1
- new version

* Sun Jan 06 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20190105-1
- new version

* Tue Jan 01 2019 Laurent Tréguier <laurent@treguier.org> - 0.6.1.20181230-1
- new version

* Thu Nov 15 2018 Laurent Tréguier <laurent@treguier.org> - 0.6.1-1
- new version

* Sun Nov 04 2018 Laurent Tréguier <laurent@treguier.org> - 0.6.0.20181103-1
- new version

* Thu Oct 25 2018 Laurent Tréguier <laurent@treguier.org> - 0.6.0.20181024-1
- new version

* Tue Oct 23 2018 Laurent Tréguier <laurent@treguier.org> - 0.6.0.20181022-1
- new version

* Tue Oct 16 2018 Laurent Tréguier <laurent@treguier.org> - 0.6.0.20181014-1
- new version

* Thu Sep 20 2018 Laurent Tréguier <laurent@treguier.org> - 0.6.0.20180919-1
- new version

* Tue Sep 18 2018 Laurent Tréguier <laurent@treguier.org> - 0.6.0.20180916-1
- new version

* Wed Sep 12 2018 Laurent Tréguier <laurent@treguier.org> - 0.6.0.20180911-1
- new version

* Fri Sep 07 2018 Laurent Tréguier <laurent@treguier.org> - 0.6.0.20180906-1
- new version

* Wed Sep 05 2018 Laurent Tréguier <laurent@treguier.org> - 0.6.0.20180904-1
- new version

* Sat Sep 01 2018 Laurent Tréguier <laurent@treguier.org> - 0.6.0.20180829-1
- new version

* Mon Aug 27 2018 Laurent Tréguier <laurent@treguier.org> - 0.6.0.20180825-1
- new version

* Thu Aug 23 2018 Laurent Tréguier <laurent@treguier.org> - 0.6.0.20180822-1
- new version

* Wed Aug 01 2018 Laurent Tréguier <laurent@treguier.org> - 0.6.0.20180731-1
- new version

* Mon Jul 30 2018 Laurent Tréguier <laurent@treguier.org> - 0.6.0-1
- new version

* Fri Jul 27 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180723-1
- new version

* Tue Jun 26 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180624-1
- new version

* Tue Jun 05 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180604-1
- new version

* Mon May 28 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180527-1
- new version

* Sun May 13 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180512-1
- new version

* Thu May 10 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180508-1
- new version

* Tue May 08 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180507-1
- new version

* Wed May 02 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180501-1
- new version

* Thu Mar 15 2018 Laurent Tréguier <laurent@treguier.org> - 0.5.0.20180314-1
- new version

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
