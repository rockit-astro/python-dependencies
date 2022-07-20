Name:           python3-serpent
Version:        1.41
Release:        0
Summary:        Serialization based on ast.literal_eval
License:        MIT
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/s/serpent/serpent-%{version}.tar.gz
BuildRequires:  python3-devel
BuildArch:      noarch

%description

%prep
%setup -q -n serpent-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
