Name:           python3-six
Version:        1.12.0
Release:        0
Url:            https://github.com/benjaminp/six
Summary:        Python 2 and 3 compatibility utilities
License:        MIT
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/s/six/six-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildArch: noarch

%description
.. image:: https://img.shields.io/pypi/v/six.svg
   :target: https://pypi.org/project/six/
   :alt: six on PyPI

.. image:: https://travis-ci.org/benjaminp/six.svg?branch=master
   :target: https://travis-ci.org/benjaminp/six
   :alt: six on TravisCI

.. image:: https://readthedocs.org/projects/six/badge/?version=latest
   :target: https://six.readthedocs.io/
   :alt: six's documentation on Read the Docs

.. image:: https://img.shields.io/badge/license-MIT-green.svg
   :target: https://github.com/benjaminp/six/blob/master/LICENSE
   :alt: MIT License badge

Six is a Python 2 and 3 compatibility library.  It provides utility functions
for smoothing over the differences between the Python versions with the goal of
writing Python code that is compatible on both Python versions.  See the
documentation for more information on what is provided.

Six supports every Python version since 2.6.  It is contained in only one Python
file, so it can be easily copied into your project. (The copyright and license
notice must be retained.)

Online documentation is at https://six.readthedocs.io/.

Bugs can be reported to https://github.com/benjaminp/six.  The code can also
be found there.

For questions about six or porting in general, email the python-porting mailing
list: https://mail.python.org/mailman/listinfo/python-porting


%prep
%setup -q -n six-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
