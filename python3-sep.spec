Name:           python3-sep
Version:        1.4.1
Release:        1%{dist}
License:        LGPL-3.0+
Summary:        Astronomical source extraction and photometry library
Url:            https://github.com/sep-developers/sep
Group:          Development/Languages/Python
# generated from https://pypi.org/pypi/sep/1.4.1/json
Requires:       python3-numpy
BuildArch:      x86_64 aarch64
%description

%install
%{__python3} -m pip install sep==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*
