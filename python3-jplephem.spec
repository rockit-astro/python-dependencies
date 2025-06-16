Name:           python3-jplephem
Version:        2.22
Release:        1%{dist}
Url:            https://github.com/brandon-rhodes/python-jplephem
Summary:        Use a JPL ephemeris to predict planet positions.
License:        MIT
Group:          Development/Languages/Python
# generated from https://pypi.org/pypi/jplephem/2.22/json
Requires:       python3-numpy
BuildArch:      noarch

%description

%install
%{__python3} -m pip install jplephem==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
