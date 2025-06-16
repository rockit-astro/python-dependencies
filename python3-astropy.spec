Name:           python3-astropy
Version:        7.1.0
Release:        1%{dist}
Url:            http://astropy.org
Summary:        Community-developed python astronomy tools
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# generated from https://pypi.org/pypi/astropy/7.1.0/json
Requires:       python3-numpy python3-pyerfa python3-astropy-iers-data python3-PyYAML python3-packaging python3-scipy
BuildArch:      x86_64 aarch64

%description

%install
%{__python3} -m pip install astropy==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*
%{_bindir}/*
