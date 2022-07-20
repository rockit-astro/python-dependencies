Name:           python3-Pyro4
Version:        4.82
Release:        0
Url:            http://pyro4.readthedocs.io
Summary:        distributed object middleware for Python (RPC)
License:        MIT
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/P/Pyro4/Pyro4-%{version}.tar.gz
Requires:       python3-serpent
BuildArch:      noarch

%description

%prep
%setup -q -n Pyro4-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%doc LICENSE
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{_bindir}/*

%changelog
