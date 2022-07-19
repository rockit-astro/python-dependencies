Name:           python3-pyerfa
Version:        2.0.0.1
Release:        0
Url:            https://github.com/liberfa/pyerfa
Summary:        PyERFA is the Python wrapper for the ERFA library (Essential Routines for Fundamental Astronomy)
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
Requires:       python3-numpy
BuildRequires:  python3-rpm-macros
BuildArch:      x86_64

%description


%install
pip3 install pyerfa==%{version} --prefix=%{buildroot}/usr --no-input

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*


%changelog
