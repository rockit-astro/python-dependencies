Name:           python3-sysv_ipc
Version:        1.1.0
Release:        1%{dist}
License:        BSD (FIXME:No SPDX)
Summary:        System V IPC primitives (semaphores, shared memory and message queues) for Python
Url:            http://semanchuk.com/philip/sysv_ipc/
Group:          Development/Languages/Python
BuildArch:      x86_64 aarch64

%description

%install
%{__python3} -m pip install sysv_ipc==%{version} --prefix=%{buildroot}/usr --no-input --no-deps --ignore-installed
echo rpm | tee %{buildroot}/usr/lib*/*/site-packages/*.dist-info/INSTALLER

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*
