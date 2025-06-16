Name:           python3-sip_tpv
Version:        1.1
Release:        1%{dist}
Url:            https://github.com/stargaser/sip_tpv
Summary:        Conversion of distortion representations in FITS headers between SIP and TPV formats.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# from https://github.com/stargaser/sip_tpv/blob/master/setup.py
Requires:       python3-numpy python3-astropy python3-sympy
BuildArch:      noarch
%description

%install
%{__python3} -m pip install sip_tpv==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
