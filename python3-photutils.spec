%define debug_package %{nil}

Name:           python3-photutils
Version:        1.5.0
Release:        0
Url:            https://github.com/astropy/photutils
Summary:        An Astropy package for source detection and photometry
License:        BSD 3-Clause License (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/photutils/photutils-%{version}.tar.gz
BuildRequires:  python3-devel

%description

%prep
%setup -q -n photutils-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*

%changelog
