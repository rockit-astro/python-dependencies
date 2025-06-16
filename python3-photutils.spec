Name:           python3-photutils
Version:        2.2.0
Release:        1%{dist}
Url:            https://github.com/astropy/photutils
Summary:        An Astropy package for source detection and photometry
License:        BSD 3-Clause License (FIXME:No SPDX)
Group:          Development/Languages/Python
# generated from https://pypi.org/pypi/photutils/2.2.0/json
Requires:       python3-numpy python3-scipy python3-astropy
BuildArch:      x86_64 aarch64
%description

%install
%{__python3} -m pip install photutils==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*
