Name:           python3-jinja2
Version:        3.1.2
Release:        0
Url:            http://jinja.pocoo.org/
Summary:        A small but fast and easy to use stand-alone template engine written in pure python.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/J/Jinja2/Jinja2-%{version}.tar.gz
Requires:       python3-markupsafe
BuildArch:      noarch

%description

%prep
%setup -q -n Jinja2-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
