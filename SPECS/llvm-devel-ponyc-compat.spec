Name:           llvm-devel-ponyc-compat
Version:        3.9
Release:        2%{?dist}
Summary:        Compatibility package to build ponyc

License:        MIT
URL:            http://llvm.org/

BuildArch:      noarch
BuildRequires:  rpmdevtools
BuildRequires:  llvm-devel
Requires:       %(if [[ "$(rpm -q --qf '%%{VERSION}' llvm-devel)" = %{version}* ]]; \
                    then echo 'llvm-devel'; \
                    elif [[ '%{dist}' = .el* ]] || [[ -z $(rpmdev-vercmp %{version} $(rpm -q --qf '%%{VERSION}' llvm-devel | grep -Eo '[0-9]\\.[0-9]') | grep '>') ]];
                    then echo 'llvm%{version}-devel'; \
                    else echo '(llvm%{version}-devel or llvm-devel)'; \
                    fi)
%description
Compatibility package to build ponyc


%prep


%build


%install


%files



%changelog
* Thu May 11 2017 Laurent Tréguier <laurent@treguier.org> - 3.9-2
- fixed behavior with llvm-devel version lower than package version

* Thu May 11 2017 Laurent Tréguier <laurent@treguier.org> - 3.9-1
- created specfile
