Name:           python3-bibtexparser
Version:        1.2.0
Release:        0
Url:            https://github.com/sciunto-org/python-bibtexparser
Summary:        Bibtex parser for python 2.7 and 3.3 and newer
License:        LGPLv3 or BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/b/bibtexparser/bibtexparser-%{version}.tar.gz
BuildRequires:  python3-devel
Requires:       python3-pyparsing
BuildArch:      noarch

%description

%prep
%setup -q -n bibtexparser-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
