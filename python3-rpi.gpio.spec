Name:           python3-rpi.gpio
Version:        0.7.1
Release:        0
Url:            http://sourceforge.net/projects/raspberry-gpio-python/
Summary:        A module to control Raspberry Pi GPIO channels
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
BuildRequires:  python3-pip
BuildArch:      aarch64

%description
This package provides a class to control the GPIO on a Raspberry Pi.

%install
pip3 install RPi.GPIO==%{version} --prefix=%{buildroot}/usr --no-input

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*

%changelog
