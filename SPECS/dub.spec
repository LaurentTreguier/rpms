Name:           dub
Version:        1.3.0
Release:        2%{?dist}
Summary:        Package and build management system for D

License:        MIT
URL:            http://dlang.org/
Source0:        https://github.com/dlang/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tr.gz

BuildRequires:  dmd
Requires:       dmd

%description
DUB emerged as a more general replacement for vibe.d's package manager.
It does not imply a dependency to vibe.d for packages and was extended to not only directly build projects,
but also to generate project files (currently VisualD).
Mono-D also supports the use of dub.json (dub's package description) as the project file.

The project's philosophy is to keep things as simple as possible.
All that is needed to make a project a dub package is to write a short dub.json file and put the source code into a source subfolder.
It can then be registered on the public package registry to be made available for everyone.
Any dependencies specified in dub.json are automatically downloaded and made available to the project during the build process.


%prep
%autosetup


%build
./build.sh


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{%{_bindir},%{_datadir}/{bash-completion,fish}/completions}
cp bin/%{name} $RPM_BUILD_ROOT/%{_bindir}
cp scripts/bash-completion/* $RPM_BUILD_ROOT/%{_datadir}/bash-completion/completions
cp scripts/fish-completion/* $RPM_BUILD_ROOT/%{_datadir}/fish/completions


%files
%defattr(-,root,root)
%config %{_datadir}/bash-completion/completions/*
%config %{_datadir}/fish/completions/*
%defattr(755,root,root)
%{_bindir}/%{name}



%changelog
* Wed Apr 12 2017 Laurent Tréguier <laurent@treguier.org> - 1.3.0-2
- fixed file permissions and attributes

* Tue Apr 11 2017 Laurent Tréguier <laurent@treguier.org> - 1.3.0-1
- created specfile
