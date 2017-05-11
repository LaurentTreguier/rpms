Name:           llvm-devel-ponyc-compat
Version:        3.9
Release:        1%{?dist}
Summary:        Compatibility package to build ponyc

License:        MIT
URL:            http://llvm.org/

BuildArch:      noarch
BuildRequires:  llvm-devel
Requires:       %(if [[ "$(rpm -q --qf '%%{VERSION}' llvm-devel)" = %{version}* ]]; \
                    then echo 'llvm-devel'; \
                    else echo 'llvm%{version}-devel'; \
                    fi)
%description
Compatibility package to build ponyc


%prep


%build


%install


%files



%changelog
* Thu May 11 2017 Laurent Tréguier <laurent@treguier.org> - 3.9-1
- created specfile
