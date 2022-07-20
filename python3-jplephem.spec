Name:           python3-jplephem
Version:        2.17
Release:        0
Url:            https://github.com/brandon-rhodes/python-jplephem
Summary:        Use a JPL ephemeris to predict planet positions.
License:        MIT
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/j/jplephem/jplephem-%{version}.tar.gz
BuildRequires:  python3-numpy
Requires:       python3-numpy
BuildArch:      noarch

%description

%prep
%setup -q -n jplephem-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
