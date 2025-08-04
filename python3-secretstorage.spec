Name:           python3-secretstorage
Version:        3.3.3
Release:        1%{dist}
Url:            https://github.com/mitya57/secretstorage
Summary:        Python bindings to FreeDesktop.org Secret Service API
License:        BSD
Group:          Development/Languages/Python
BuildArch:      noarch

%description

%install
%{__python3} -m pip install secretstorage==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*