Name:           python3-pyvo
Version:        1.7
Release:        1%{dist}
Url:            https://github.com/astropy/pyvo
Summary:        PyVO is a package providing access to remote data and services of the Virtual observatory (VO) using Python.
License:        BSD
Group:          Development/Languages/Python
BuildArch:      noarch

%description

%install
%{__python3} -m pip install pyvo==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
