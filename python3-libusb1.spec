%define debug_package %{nil}

Name:           python3-libusb1
Version:        3.0.0
Release:        0
Summary:        Pure-python wrapper for libusb-1.0
License:        LGPL-2.1+
URL:            http://github.com/vpelletier/python-libusb1
Source:         https://files.pythonhosted.org/packages/source/l/libusb1/libusb1-%{version}.tar.gz
BuildArch:      x86_64 aarch64

%description


%prep
%setup -q -n libusb1-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
