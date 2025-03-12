Name:           python3-pandas
Version:        1.4
Release:        0
Url:            https://pandas.pydata.org/
Summary:        Powerful Python data analysis toolkit
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
BuildRequires:  python3-pip python3-numpy python3-packaging
Requires:       python3-numpy python3-dateutil python3-pytz
BuildArch:      x86_64 aarch64

%description
pandas is a Python package that provides fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python. Additionally, it has the broader goal of becoming the most powerful and flexible open source data analysis / manipulation tool available in any language. It is already well on its way towards this goal.


%install
pip3 install pandas==%{version} --prefix=%{buildroot}/usr --no-input

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*

%changelog
