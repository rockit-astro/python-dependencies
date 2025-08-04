Name:           python3-jeepney
Version:        0.9.0
Release:        1%{dist}
Url:            https://github.com/mitya57/secretstorage
Summary:        Low-level, pure Python DBus protocol wrapper.
License:        MIT
Group:          Development/Languages/Python
BuildArch:      noarch

%description

%install
%{__python3} -m pip install jeepney==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*