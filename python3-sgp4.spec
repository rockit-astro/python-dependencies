%define debug_package %{nil}

Name:           python3-sgp4
Version:        2.21
Release:        0
Url:            https://github.com/brandon-rhodes/python-sgp4
Summary:        Track earth satellite TLE orbits using up-to-date 2010 version of SGP4
License:        MIT
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/s/sgp4/sgp4-%{version}.tar.gz
BuildRequires:  python3-setuptools
BuildArch:      x86_64

%description

%prep
%setup -q -n sgp4-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*

%changelog
