Name:           python3-werkzeug
Version:        2.1.2
Release:        0
Url:            https://www.palletsprojects.org/p/werkzeug/
Summary:        The comprehensive WSGI web application library.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/W/Werkzeug/Werkzeug-%{version}.tar.gz
BuildArch:      noarch


%description

%prep
%setup -q -n Werkzeug-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
