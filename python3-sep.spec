%define debug_package %{nil}

Name:           python3-sep
Version:        1.1.1
Release:        0
License:        LGPL-3.0+
Summary:        Astronomical source extraction and photometry library
Url:            https://github.com/kbarbary/sep
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/s/sep/sep-%{version}.tar.gz
BuildRequires:  python36-devel
BuildArch:      x86_64

%description
http://sep.readthedocs.org

%prep
%setup -q -n sep-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*

%changelog
