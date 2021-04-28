Name:           python3-extension-helpers
Version:        0.1
Release:        0
Summary:        Utilities for building and installing packages in the Astropy ecosystem
License:        BSD 3-Clause License (FIXME:No SPDX)
URL:            https://github.com/astropy/astropy-helpers
Source:         https://files.pythonhosted.org/packages/source/e/extension-helpers/extension-helpers-%{version}.tar.gz
BuildRequires:  python3-devel
Requires:       python3-jinja2
BuildArch:      noarch

%description
extension-helpers
=================

.. image:: https://dev.azure.com/astropy-project/extension-helpers/_apis/build/status/astropy.extension-helpers?branchName=master
  :target: https://dev.azure.com/astropy-project/extension-helpers/_build/latest?definitionId=4&branchName=master

.. image:: https://codecov.io/gh/astropy/extension-helpers/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/astropy/extension-helpers

The **extension-helpers** package includes convenience helpers to assist with
building Python packages with compiled C/Cython extensions. It is developed by
the Astropy project but is intended to be general and usable by any Python
package.

For more information, see the documentation at http://extension-helpers.readthedocs.io




%prep
%setup -q -n extension-helpers-%{version}

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
