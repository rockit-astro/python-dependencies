Name:           python3-bibtexparser
Version:        1.4.3
Release:        1%{dist}
Url:            https://github.com/sciunto-org/python-bibtexparser
Summary:        Bibtex parser for python 2.7 and 3.3 and newer
License:        LGPLv3 or BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
BuildArch:      noarch

%description

%install
%{__python3} -m pip install bibtexparser==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
