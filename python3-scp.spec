Name:           python3-scp
Version:        0.15.0
Release:        1%{dist}
License:        LGPLv2+
Summary:        Scp module for paramiko
Url:            https://github.com/jbardin/scp.py
Group:          Development/Languages/Python
Requires:       python3-numpy
BuildArch:      noarch

%description
The scp.py module uses a paramiko transport to send and receive files via the
scp1 protocol. This is the protocol as referenced from the openssh scp program,
and has only been tested with this implementation.

%install
%{__python3} -m pip install scp==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
