Name:           python36-astroplan
Version:        0.4
Release:        0
Url:            https://github.com/astropy/astroplan
Summary:        Observation planning package for astronomers
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/a/astroplan/astroplan-%{version}.tar.gz
BuildRequires:  python36-devel
Requires:       python36-pytz
BuildArch:      noarch

%description
astroplan is an open source (BSD licensed) observation planning package for
astronomers that can help you plan for everything but the clouds.

It is an in-development `Astropy <http://www.astropy.org>`__
`affiliated package <http://www.astropy.org/affiliated/index.html>`__ that
seeks to make your life as an observational astronomer a little less
infuriating.

* Code: https://github.com/astropy/astroplan
* Docs: https://astroplan.readthedocs.io/

%prep
%setup -q -n astroplan-%{version}

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