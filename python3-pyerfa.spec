Name:           python3-pyerfa
Version:        2.0.1.5
Release:        1%{dist}
Url:            https://github.com/liberfa/pyerfa
Summary:        PyERFA is the Python wrapper for the ERFA library (Essential Routines for Fundamental Astronomy)
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
Requires:       python3-numpy
BuildArch:      x86_64 aarch64
%description

%install
%{__python3} -m pip install pyerfa==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*