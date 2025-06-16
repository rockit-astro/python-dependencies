Name:           python3-pcomfortcloud
Version:        0.1.2
Release:        1%{dist}
Url:            http://github.com/lostfields/python-panasonic-comfort-cloud
Summary:        Read and change status of Panasonic Comfort Cloud devices
License:        MIT
Group:          Development/Languages/Python
# from https://github.com/lostfields/python-panasonic-comfort-cloud/blob/master/requirements.txt
Requires:       python3-requests python3-urllib3 python3-beautifulsoup4
BuildArch:      noarch
%description

%install
%{__python3} -m pip install pcomfortcloud==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{_bindir}/pcomfortcloud
