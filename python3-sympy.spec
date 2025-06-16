Name:           python3-sympy
Version:        1.10.1
Release:        1%{dist}
Url:            https://sympy.org
Summary:        Computer algebra system (CAS) in Python
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
Requires:       python3-mpmath
BuildArch:      noarch
%description

%install
%{__python3} -m pip install sympy==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{_bindir}/isympy
%{_mandir}/man1/isympy.1.gz
