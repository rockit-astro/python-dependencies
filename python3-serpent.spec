Name:           python3-serpent
Version:        1.41
Release:        1%{dist}
Summary:        Serialization based on ast.literal_eval
License:        MIT
Group:          Development/Languages/Python
BuildArch:      noarch
%description

%install
%{__python3} -m pip install serpent==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
