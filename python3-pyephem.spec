#
# spec file for package python-pyephem
#
# Copyright (c) 2016 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


Name:           python3-pyephem
Version:        3.7.6.0
Release:        0
License:        LGPL
Summary:        Compute positions of the planets and stars
Url:            http://rhodesmill.org/pyephem/
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/p/pyephem/pyephem-%{version}.tar.gz
BuildRequires:  python3-devel
BuildArch:      noarch

%description
==============
PyEphem README
==============

.. image:: http://bottlepy.org/docs/dev/_static/Gittip.png
   :target: https://www.gittip.com/brandon-rhodes/

.. image:: https://travis-ci.org/brandon-rhodes/pyephem.png
   :target: https://travis-ci.org/brandon-rhodes/pyephem

.. _ephem: http://pypi.python.org/pypi/ephem/
.. _pyephem: http://pypi.python.org/pypi/pyephem/
.. _XEphem: http://www.clearskyinstitute.com/xephem/
.. _Quick Reference: http://rhodesmill.org/pyephem/quick
.. _Tutorial: http://rhodesmill.org/pyephem/tutorial
.. _PyEphem web site: http://rhodesmill.org/pyephem/

PyEphem provides an ``ephem`` Python package
for performing high-precision astronomy computations.
The underlying numeric routines are coded in C
and are the same ones that drive the popular `XEphem`_ astronomy application,
whose author, Elwood Charles Downey,
generously gave permission for their use in PyEphem.
The name *ephem* is short for the word *ephemeris*,
which is the traditional term for a table
giving the position of a planet, asteroid, or comet for a series of dates.

The `PyEphem web site`_ offers documentation
and also links to the project bug tracker, user support forum,
and source code repository.
If you have a C compiler and the
`pip Python installer tool <https://pip.pypa.io/en/latest/installing.html>`_
on your system,
then installing PyEphem should be as easy as::

  pip install ephem

There are also Windows installers in the downloads section below.

The design of PyEphem emphasizes convenience and ease of use.
Both celestial bodies and the observer's location on Earth
are represented by Python objects,
while dates and angles automatically print themselves
in standard astronomical formats::

 >>> import ephem
 >>> mars = ephem.Mars()
 >>> mars.compute('2008/1/1')
 >>> print mars.ra, mars.dec
 5:59:27.35 26:56:27.4

The documentation includes both a `Quick Reference`_ and a `Tutorial`_,
which are included in text files within the module itself
as well as being available on the `PyEphem web site`_.

The features provided by PyEphem include:

* Find where a planet, comet, or asteroid is in the sky.

  * High-precision orbital routines are provdied
    for the Moon, Sun, planets, and the major planet moons.
  * The user can supply the orbital elements of a comet, asteroid,
    or Earth-orbiting satellite, and have its location computed.
  * The positions of 94 bright stars come built-in,
    and the user can create further fixed objects as needed
    for their calculations.

* Determine where in the sky an object appears for a particular observer.

  * The user can supply the longitude, latitude, and altitude
    of the location from which they will be observing.
  * For convenience, a small database of longitudes and latitudes
    for 122 world cities is included.
  * For specified weather conditions (temperature and pressure),
    PyEphem will compensate for atmospheric refraction
    by adjusting the positions of bodies near the horizon.

* Compute when a body will rise, transit overhead, and set
  from a particular location.

* Parse and use orbital data in either the traditional XEphem file format,
  or the standard TLE format used for tracking Earth-orbiting satellites.

* Determine the dates of the equinoxes and solstices.

* Compute the dates of the various phases of the Moon.

* Convert from the Greenwich Time (more precisely, Ephemeris Time)
  which PyEphem uses to the local time of the user.

* Convert positions between the equatorial, ecliptic, and galactic
  coordinate systems.

* Determine on which page of the Uranometria or the Millennium Star Atlas
  a particular star should appear.

* Return the Julian Date corresponding to any calendar date.

%prep
%setup -q -n pyephem-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*

%changelog
