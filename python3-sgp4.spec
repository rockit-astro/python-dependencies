Name:           python3-sgp4
Version:        2.24
Release:        1%{dist}
Url:            https://github.com/brandon-rhodes/python-sgp4
Summary:        Track earth satellite TLE orbits using up-to-date 2010 version of SGP4
License:        MIT
Group:          Development/Languages/Python
BuildArch:      x86_64 aarch64
%description

%install
%{__python3} -m pip install sgp4==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*
