%global         debug_package   %{nil}

Name:           dub
Version:        1.6.0
Release:        1%{?dist}
Summary:        Package and build management system for D

License:        MIT
URL:            http://dlang.org/
Source0:        https://github.com/dlang/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tr.gz
Source10:       macros.%{name}

BuildRequires:  dmd
Requires:       dmd

%description
DUB emerged as a more general replacement for vibe.d's package manager.
It does not imply a dependency to vibe.d for packages and was extended to not
only directly build projects, but also to generate project files (currently
VisualD). Mono-D also supports the use of dub.json (dub's package description)
as the project file.
The project's philosophy is to keep things as simple as possible. All that is
needed to make a project a dub package is to write a short dub.json file and put
the source code into a source subfolder. It can then be registered on the public
package registry to be made available for everyone. Any dependencies specified
in dub.json are automatically downloaded and made available to the project
during the build process.


%prep
%autosetup


%build
./build.sh


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{%{_bindir},%{_datadir}/{bash-completion,fish}/completions,%{_rpmconfigdir}/macros.d}
cp bin/%{name} $RPM_BUILD_ROOT/%{_bindir}
cp scripts/bash-completion/* $RPM_BUILD_ROOT/%{_datadir}/bash-completion/completions
cp scripts/fish-completion/* $RPM_BUILD_ROOT/%{_datadir}/fish/completions
cp %{SOURCE10} $RPM_BUILD_ROOT/%{_rpmconfigdir}/macros.d


%files
%config %{_datadir}/bash-completion/completions/*
%config %{_datadir}/fish/completions/*
%config %{_rpmconfigdir}/macros.d/*
%attr(755,root,root) %{_bindir}/*



%changelog
* Thu Nov 02 2017 Laurent Tréguier <laurent@treguier.org> - 1.6.0-1
- new version

* Mon Oct 09 2017 Laurent Tréguier <laurent@treguier.org> - 1.5.0-2
- rebuilt

* Fri Sep 01 2017 Laurent Tréguier <laurent@treguier.org> - 1.5.0-1
- new version

* Tue Aug 15 2017 Laurent Tréguier <laurent@treguier.org> - 1.4.1-1
- new version

* Wed Jul 19 2017 Laurent Tréguier <laurent@treguier.org> - 1.4.0-1
- new version

* Wed Apr 26 2017 Laurent Tréguier <laurent@treguier.org> - 1.3.0-5
- removed debuginfo subpackage

* Fri Apr 14 2017 Laurent Tréguier <laurent@treguier.org> - 1.3.0-4
- rebuilt with dmd that is not bootstrapped anymore

* Wed Apr 12 2017 Laurent Tréguier <laurent@treguier.org> - 1.3.0-3
- added dub macros

* Wed Apr 12 2017 Laurent Tréguier <laurent@treguier.org> - 1.3.0-2
- fixed file permissions and attributes

* Tue Apr 11 2017 Laurent Tréguier <laurent@treguier.org> - 1.3.0-1
- created specfile
