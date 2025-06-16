Name:           python3-skyfield
Version:        1.53
Release:        1%{dist}
Url:            http://github.com/brandon-rhodes/python-skyfield/
Summary:        Elegant astronomy for Python
License:        MIT
Group:          Development/Languages/Python
# generated from https://pypi.org/pypi/skyfield/1.53/json
Requires:       python3-certifi python3-sgp4 python3-jplephem python3-numpy
BuildArch:      noarch
%description

%install
%{__python3} -m pip install skyfield==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
