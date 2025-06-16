Name:           python3-Pyro4
Version:        4.82
Release:        1%{dist}
Url:            http://pyro4.readthedocs.io
Summary:        distributed object middleware for Python (RPC)
License:        MIT
Group:          Development/Languages/Python
# generated from https://pypi.org/pypi/Pyro4/4.82/json
Requires:       python3-serpent
BuildArch:      noarch
%description

%install
%{__python3} -m pip install Pyro4==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{_bindir}/*
