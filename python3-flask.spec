Name:           python3-flask
Version:        2.1.3
Release:        0
Url:            https://www.palletsprojects.com/p/flask/
Summary:        A simple framework for building complex web applications.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/F/Flask/Flask-%{version}.tar.gz
Requires:       python3-werkzeug, python3-jinja2, python3-itsdangerous, python3-click
BuildArch:      noarch

%description

%prep
%setup -q -n Flask-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{_bindir}/flask

%changelog
