Name:           python3-astropy-iers-data
Version:        0.2025.6.16.0.38.47
Release:        1%{dist}
Url:            http://astropy.org
Summary:        Community-developed python astronomy tools
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
BuildArch:      noarch

%description

%install
%{__python3} -m pip install astropy-iers-data==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
