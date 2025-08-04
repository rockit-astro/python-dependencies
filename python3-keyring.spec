Name:           python3-keyring
Version:        25.6.0
Release:        1%{dist}
Url:            https://github.com/jaraco/keyring
Summary:        Store and access your passwords safely.
License:        MIT
Group:          Development/Languages/Python
BuildArch:      noarch

%description

%install
%{__python3} -m pip install keyring==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{_bindir}/*