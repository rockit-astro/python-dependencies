Name:           python3-flask
Version:        3.1.1
Release:        1%{dist}
Url:            https://www.palletsprojects.com/p/flask/
Summary:        A simple framework for building complex web applications.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# generated from https://pypi.org/pypi/flask/3.1.1/json
Requires:       python3-blinker python3-click python3-itsdangerous python3-jinja2 python3-markupsafe python3-werkzeug
BuildArch:      noarch

%description

%install
%{__python3} -m pip install flask==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{_bindir}/flask

