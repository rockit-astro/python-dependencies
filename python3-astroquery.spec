Name:           python3-astroquery
Version:        0.4.10
Release:        1%{dist}
Url:            http://astropy.org/astroquery
Summary:        Functions and classes to access online astronomical data resources
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
Requires:       python3-astropy, python3-requests, python3-keyring, python3-beautifulsoup4, python3-html5lib, python3-six
BuildArch:      noarch


%description

%install
%{__python3} -m pip install astroquery==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*