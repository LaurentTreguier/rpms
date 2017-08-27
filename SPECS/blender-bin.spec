%global         debug_package   %{nil}
%global         __python        %{_bindir}/python3
%global         source_name     blender
%global         glibc_version   2.19

Name:           %{source_name}-bin
Version:        2.78c
Release:        4%{?dist}
Summary:        3D modeling, animation, rendering and post-production

%global         filename        blender-%{version}-linux-glibc%(echo %{glibc_version} | tr -d '.')-%{_arch}

License:        GPLv2+
URL:            https://www.blender.org
Source0:        http://download.blender.org/release/Blender%(echo %{version} | tr -d [:alpha:])/%{filename}.tar.bz2#/%{name}-%{version}.tar.bz2

ExclusiveArch:  x86_64
Requires:       glibc >= %{glibc_version}
Requires:       blender-fonts
Requires:       fontpackages-filesystem
Requires:       google-droid-sans-fonts
Requires:       python3-numpy
Requires:       python3-requests
Conflicts:      blender

%description
Blender is the essential software solution you need for 3D, from modeling, animation, rendering and post-production to interactive creation and playback.
Professionals and novices can easily and inexpensively publish stand-alone, secure, multi-platform content to the web, CD-ROMs, and other media.


%prep
%autosetup -n %{filename}


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/%{source_name}
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/{applications,icons/scalable}
cp -R $RPM_BUILD_DIR/%{filename}/* $RPM_BUILD_ROOT/opt/%{source_name}
ln -s /opt/%{source_name}/%{source_name} $RPM_BUILD_ROOT/%{_bindir}/%{source_name}
ln -s /opt/%{source_name}/%{source_name}-softwaregl $RPM_BUILD_ROOT/%{_bindir}/%{source_name}-softwaregl
ln -s /opt/%{source_name}/%{source_name}-thumbnailer.py $RPM_BUILD_ROOT/%{_bindir}/%{source_name}-thumbnailer.py
ln -s /opt/%{source_name}/%{source_name}player $RPM_BUILD_ROOT/%{_bindir}/%{source_name}player
mv $RPM_BUILD_ROOT/opt/%{source_name}/%{source_name}.desktop $RPM_BUILD_ROOT/%{_datadir}/applications
mv $RPM_BUILD_ROOT/opt/%{source_name}/%{source_name}.svg $RPM_BUILD_ROOT/%{_datadir}/icons/scalable


%files
%license LICENSE*
%license *-license.txt
%license copyright.txt
%doc readme.html
/opt/%{source_name}
%{_datadir}/applications/%{source_name}.desktop
%{_datadir}/icons/scalable/%{source_name}.svg
%attr(755,root,root) %{_bindir}/%{source_name}*



%changelog
* Sun Aug 27 2017 Laurent Tréguier <laurent@treguier.org> - 2.78c-4
- changed BuildArch to ExclusiveArch

* Sun May 14 2017 Laurent Tréguier <laurent@treguier.org> - 2.78c-3
- ensured binaries are executable

* Wed Apr 05 2017 Laurent Tréguier <laurent@treguier.org> - 2.78c-2
- force x86_64

* Wed Apr  5 2017 Laurent Tréguier <laurent@treguier.org> - 2.78c-1
- created specfile
