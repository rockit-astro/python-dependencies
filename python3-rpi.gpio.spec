Name:           python3-rpi.gpio
Version:        0.7.1
Release:        1%{dist}
Url:            http://sourceforge.net/projects/raspberry-gpio-python/
Summary:        A module to control Raspberry Pi GPIO channels
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
BuildArch:      aarch64
%description

%install
%{__python3} -m pip install RPi.GPIO==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*
