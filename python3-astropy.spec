Name:           python3-astropy
Version:        5.2.2
Release:        0
Url:            http://astropy.org
Summary:        Community-developed python astronomy tools
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
BuildRequires:  python3-pip python3-numpy python3-pyparsing python3-pyyaml python3-packaging
Requires:       python3-numpy python3-pyparsing python3-pyyaml python3-pyerfa python3-packaging
BuildArch:      x86_64 aarch64

%description
Astropy is a package intended to contain core functionality and some
common tools needed for performing astronomy and astrophysics research with
Python. It also provides an index for other astronomy packages and tools for
managing them.


%install
pip3 install astropy==%{version} --prefix=%{buildroot}/usr --no-input

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*
%{_bindir}/*

%changelog
