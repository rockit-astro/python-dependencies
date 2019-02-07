Name:           python36-Pyro4
Version:        4.75
Release:        0
Url:            http://pyro4.readthedocs.io
Summary:        distributed object middleware for Python (RPC)
License:        MIT
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/P/Pyro4/Pyro4-%{version}.tar.gz
BuildRequires:  python36-devel
BuildRequires:  python36-serpent
Requires:       python36-serpent
BuildArch:      noarch

%description
Pyro means PYthon Remote Objects.
It is a library that enables you to build applications in which
objects can talk to eachother over the network, with minimal programming effort.
You can just use normal Python method calls, with almost every possible parameter
and return value type, and Pyro takes care of locating the right object on the right
computer to execute the method. It is designed to be very easy to use, and to
generally stay out of your way. But it also provides a set of powerful features that
enables you to build distributed applications rapidly and effortlessly.
Pyro is a pure Python library and runs on many different platforms and Python versions.

The source code repository is on Github: https://github.com/irmen/Pyro4

The documentation can be found here: http://pyro4.readthedocs.io


%prep
%setup -q -n Pyro4-%{version}

%build
%{__python3_other} setup.py build

%install
%{__python3_other} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%doc LICENSE
%defattr(-,root,root,-)
%{python3_other_sitelib}/*
%{_bindir}/*

%changelog