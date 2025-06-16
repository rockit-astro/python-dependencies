Name:           python3-github-flask
Version:        3.2.0
Release:        1%{dist}
Url:            http://github.com/cenkalti/github-flask
Summary:        GitHub extension for Flask microframework
License:        MIT
Group:          Development/Languages/Python
Requires:       python3-flask, python3-requests
BuildArch:      noarch

%description

%install
%{__python3} -m pip install github-flask==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
