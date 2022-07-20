Name:           python3-itsdangerous
Version:        2.1.2
Release:        0
Url:            https://palletsprojects.com/p/itsdangerous/
Summary:        Various helpers to pass data to untrusted environments and back.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/i/itsdangerous/itsdangerous-%{version}.tar.gz
BuildArch:      noarch

%description

%prep
%setup -q -n itsdangerous-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
