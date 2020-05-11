# Created by pyp2rpm-3.3.4
%global         pypi_name pystache

Name:           python-%{pypi_name}
Version:        0.5.4
Release:        13%{?dist}
Summary:        Mustache for Python

License:        MIT
URL:            http://github.com/defunkt/pystache
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
A Python implementation of Mustache


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(setuptools)

%description -n python3-%{pypi_name}
A Python implementation of Mustache


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build


%install
%py3_install


%check
# See https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=python-pystache
mkdir -p temp_dir
%{__python3} %{py_setup} %{?py_setup_args} install -O1 --root temp_dir
PYTHONPATH=$(readlink -e temp_dir/%{python3_sitelib}) temp_dir/%{_bindir}/pystache-test .


%files -n python3-%{pypi_name}
%license LICENSE
%doc pystache/tests/examples/readme.py README.md
%{_bindir}/pystache
%{_bindir}/pystache-test
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon May 11 2020 Laurent Tréguier <laurent@treguier.org> - 0.5.4-13
- Initial package