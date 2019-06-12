%bcond_without check 

Name:           pew 
Version:        1.1.2
Release:        4%{?dist}
Summary:        Tool to manage multiple virtualenvs written in pure Python

License:        MIT
URL:            https://github.com/berdario/pew
Source0:        https://github.com/berdario/%{name}/archive/%{version}/%{name}-%{version}.tar.gz 

# Add pytest marker to test requiring connection
Patch0:         0001-tests-connection-marker-fix.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(virtualenv) >= 1.11
BuildRequires:  python3dist(virtualenv-clone) >= 0.2.5
BuildRequires:  python3dist(pythonz-bd) >= 1.10.2

%if %{with check}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pip)
%endif

%{?python_provide:%python_provide python3-%{name}}
Requires:       python3dist(setuptools) >= 17.1
Requires:       python3dist(virtualenv) >= 1.11
Requires:       python3dist(virtualenv-clone) >= 0.2.5
Requires:       python3dist(pythonz-bd) >= 1.10.2

%description
Python Env Wrapper is a set of commands to manage multiple virtual
environments. Pew can create, delete and copy your environments, using a
single command to switch to them wherever you are, while keeping them in a
single (configurable) location.

%prep
%autosetup -p1 -n %{name}-%{version}

# This script for shell completion can't be used for Fedora package
rm -rf %{name}/shell_config/complete_deploy

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
export PATH=$PATH:%{buildroot}%{_bindir}
export PYTHONPATH=$PYTHONPATH:%{buildroot}%{python3_sitelib}
py.test-3 -vv tests
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/pew
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py?.?.egg-info

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 13 2017 Michal Cyprian <mcyprian@redhat.com> - 1.1.2-1
- Initial package.
