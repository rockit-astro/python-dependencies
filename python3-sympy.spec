Name:           python3-sympy
Version:        1.10.1
Release:        0
Url:            https://sympy.org
Summary:        Computer algebra system (CAS) in Python
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/s/sympy/sympy-%{version}.tar.gz
Requires:       python3-mpmath
BuildArch:      noarch

%description

%prep
%setup -q -n sympy-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{_bindir}/isympy
%{_mandir}/man1/isympy.1.gz

%changelog
