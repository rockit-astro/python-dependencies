Name:           python3-mpmath
Version:        1.2.1
Release:        1%{dist}
Url:            http://mpmath.org
Summary:        Python library for arbitrary-precision floating-point arithmetic
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
BuildArch:      noarch
%description

%install
%{__python3} -m pip install mpmath==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
