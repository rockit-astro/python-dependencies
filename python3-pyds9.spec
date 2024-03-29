%define debug_package %{nil}

Name:           python3-pyds9
Version:        1.8.1
Release:        3
License:        GPL2
Summary:        Python connection to ds9 via XPA
Url:            https://github.com/ericmandel/pyds9/
Group:          Development/Languages/Python
Source:         https://github.com/ericmandel/pyds9/archive/v1.8.1.zip
BuildRequires:  python3-devel, libXt-devel
Requires:       python3-six
BuildArch:      x86_64 aarch64

%description
The XPA messaging system provides seamless communication between many kinds of Unix programs, including Tcl/Tk programs such as ds9. The pyds9 module uses a Python interface to XPA to communicate with ds9. It supports communication with all of ds9's XPA access points. See http://hea-www.harvard.edu/saord/ds9/ref/xpa.html for more info.

%prep
%setup -q -n pyds9-1.8.1

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
