Name:           python3-biplist
Version:        1.0.3
Release:        1%{dist}
Url:            https://bitbucket.org/wooster/biplist
Summary:        biplist is a library for reading/writing binary plists.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
BuildArch:      noarch

%description

%install
%{__python3} -m pip install biplist==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
