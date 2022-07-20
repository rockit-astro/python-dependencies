Name:           python3-skyfield
Version:        1.43.1
Release:        0
Url:            http://github.com/brandon-rhodes/python-skyfield/
Summary:        Elegant astronomy for Python
License:        MIT
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/s/skyfield/skyfield-%{version}.tar.gz
Requires:       python3-certifi >= 2017.4.17
Requires:       python3-sgp4 >= 2.2
Requires:       python3-jplephem >= 2.13
Requires:       python3-numpy
BuildRequires:  python3-setuptools
BuildArch: noarch

%description


%prep
%setup -q -n skyfield-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
