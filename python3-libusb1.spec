Name:           python3-libusb1
Version:        3.3.1
Release:        1%{dist}
Summary:        Pure-python wrapper for libusb-1.0
License:        LGPL-2.1+
URL:            http://github.com/vpelletier/python-libusb1
BuildArch:      noarch
%description

%install
%{__python3} -m pip install libusb1==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
