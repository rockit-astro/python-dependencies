Name:           python36-urllib3
Version:        1.24.1
Release:        0
Url:            https://urllib3.readthedocs.io/
Summary:        HTTP library with thread-safe connection pooling, file post, and more.
License:        MIT
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/u/urllib3/urllib3-%{version}.tar.gz
BuildRequires:  python36-devel
BuildArch:      noarch

%description
urllib3
=======

.. image:: https://travis-ci.org/urllib3/urllib3.svg?branch=master
        :alt: Build status on Travis
        :target: https://travis-ci.org/urllib3/urllib3

.. image:: https://img.shields.io/appveyor/ci/urllib3/urllib3/master.svg
        :alt: Build status on AppVeyor
        :target: https://ci.appveyor.com/project/urllib3/urllib3

.. image:: https://readthedocs.org/projects/urllib3/badge/?version=latest
        :alt: Documentation Status
        :target: https://urllib3.readthedocs.io/en/latest/

.. image:: https://img.shields.io/codecov/c/github/urllib3/urllib3.svg
        :alt: Coverage Status
        :target: https://codecov.io/gh/urllib3/urllib3

.. image:: https://img.shields.io/pypi/v/urllib3.svg?maxAge=86400
        :alt: PyPI version
        :target: https://pypi.org/project/urllib3/

.. image:: https://www.bountysource.com/badge/tracker?tracker_id=192525
        :alt: Bountysource
        :target: https://www.bountysource.com/trackers/192525-urllib3?utm_source=192525&utm_medium=shield&utm_campaign=TRACKER_BADGE

.. image:: https://badges.gitter.im/python-urllib3/Lobby.svg
        :alt: Gitter
        :target: https://gitter.im/python-urllib3/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

urllib3 is a powerful, *sanity-friendly* HTTP client for Python. Much of the
Python ecosystem already uses urllib3 and you should too.
urllib3 brings many critical features that are missing from the Python
standard libraries:

- Thread safety.
- Connection pooling.
- Client-side SSL/TLS verification.
- File uploads with multipart encoding.
- Helpers for retrying requests and dealing with HTTP redirects.
- Support for gzip and deflate encoding.
- Proxy support for HTTP and SOCKS.
- 100% test coverage.

urllib3 is powerful and easy to use::

    >>> import urllib3
    >>> http = urllib3.PoolManager()
    >>> r = http.request('GET', 'http://httpbin.org/robots.txt')
    >>> r.status
    200
    >>> r.data
    'User-agent: *\nDisallow: /deny\n'


Installing
----------

urllib3 can be installed with `pip <https://pip.pypa.io>`_::

    $ pip install urllib3

Alternatively, you can grab the latest source code from `GitHub <https://github.com/urllib3/urllib3>`_::

    $ git clone git://github.com/urllib3/urllib3.git
    $ python setup.py install


Documentation
-------------

urllib3 has usage and reference documentation at `urllib3.readthedocs.io <https://urllib3.readthedocs.io>`_.


Contributing
------------

urllib3 happily accepts contributions. Please see our
`contributing documentation <https://urllib3.readthedocs.io/en/latest/contributing.html>`_
for some tips on getting started.


Maintainers
-----------

- `@theacodes <https://github.com/theacodes>`_ (Thea Flowers)
- `@SethMichaelLarson <https://github.com/SethMichaelLarson>`_ (Seth M. Larson)
- `@haikuginger <https://github.com/haikuginger>`_ (Jesse Shapiro)
- `@lukasa <https://github.com/lukasa>`_ (Cory Benfield)
- `@sigmavirus24 <https://github.com/sigmavirus24>`_ (Ian Cordasco)
- `@shazow <https://github.com/shazow>`_ (Andrey Petrov)

&#128075;


Sponsorship
-----------

If your company benefits from this library, please consider `sponsoring its
development <https://urllib3.readthedocs.io/en/latest/contributing.html#sponsorship>`_.

Sponsors include:

- Google Cloud Platform (2018-present), sponsors `@theacodes <https://github.com/theacodes>`_'s work on an ongoing basis
- Abbott (2018-present), sponsors `@SethMichaelLarson <https://github.com/SethMichaelLarson>`_'s work on an ongoing basis
- Akamai (2017-present), sponsors `@haikuginger <https://github.com/haikuginger>`_'s work on an ongoing basis
- Hewlett Packard Enterprise (2016-2017), sponsored `@Lukasa&#8217;s <https://github.com/Lukasa>`_ work on urllib3


Changes
=======

1.24.1 (2018-11-02)
-------------------

* Remove quadratic behavior within ``GzipDecoder.decompress()`` (Issue #1467)

* Restored functionality of `ciphers` parameter for `create_urllib3_context()`. (Issue #1462)


1.24 (2018-10-16)
-----------------

* Allow key_server_hostname to be specified when initializing a PoolManager to allow custom SNI to be overridden. (Pull #1449)

* Test against Python 3.7 on AppVeyor. (Pull #1453)

* Early-out ipv6 checks when running on App Engine. (Pull #1450)

* Change ambiguous description of backoff_factor (Pull #1436)

* Add ability to handle multiple Content-Encodings (Issue #1441 and Pull #1442)

* Skip DNS names that can't be idna-decoded when using pyOpenSSL (Issue #1405).

* Add a server_hostname parameter to HTTPSConnection which allows for
  overriding the SNI hostname sent in the handshake. (Pull #1397)

* Drop support for EOL Python 2.6 (Pull #1429 and Pull #1430)

* Fixed bug where responses with header Content-Type: message/* erroneously
  raised HeaderParsingError, resulting in a warning being logged. (Pull #1439)

* Move urllib3 to src/urllib3 (Pull #1409)


1.23 (2018-06-04)
-----------------

* Allow providing a list of headers to strip from requests when redirecting
  to a different host. Defaults to the ``Authorization`` header. Different
  headers can be set via ``Retry.remove_headers_on_redirect``. (Issue #1316)

* Fix ``util.selectors._fileobj_to_fd`` to accept ``long`` (Issue #1247).

* Dropped Python 3.3 support. (Pull #1242)

* Put the connection back in the pool when calling stream() or read_chunked() on
  a chunked HEAD response. (Issue #1234)

* Fixed pyOpenSSL-specific ssl client authentication issue when clients
  attempted to auth via certificate + chain (Issue #1060)

* Add the port to the connectionpool connect print (Pull #1251)

* Don't use the ``uuid`` module to create multipart data boundaries. (Pull #1380)

* ``read_chunked()`` on a closed response returns no chunks. (Issue #1088)

* Add Python 2.6 support to ``contrib.securetransport`` (Pull #1359)

* Added support for auth info in url for SOCKS proxy (Pull #1363)


1.22 (2017-07-20)
-----------------

* Fixed missing brackets in ``HTTP CONNECT`` when connecting to IPv6 address via
  IPv6 proxy. (Issue #1222)

* Made the connection pool retry on ``SSLError``.  The original ``SSLError``
  is available on ``MaxRetryError.reason``. (Issue #1112)

* Drain and release connection before recursing on retry/redirect.  Fixes
  deadlocks with a blocking connectionpool. (Issue #1167)

* Fixed compatibility for cookiejar. (Issue #1229)

* pyopenssl: Use vendored version of ``six``. (Issue #1231)


1.21.1 (2017-05-02)
-------------------

* Fixed SecureTransport issue that would cause long delays in response body
  delivery. (Pull #1154)

* Fixed regression in 1.21 that threw exceptions when users passed the
  ``socket_options`` flag to the ``PoolManager``.  (Issue #1165)

* Fixed regression in 1.21 that threw exceptions when users passed the
  ``assert_hostname`` or ``assert_fingerprint`` flag to the ``PoolManager``.
  (Pull #1157)


1.21 (2017-04-25)
-----------------

* Improved performance of certain selector system calls on Python 3.5 and
  later. (Pull #1095)

* Resolved issue where the PyOpenSSL backend would not wrap SysCallError
  exceptions appropriately when sending data. (Pull #1125)

* Selectors now detects a monkey-patched select module after import for modules
  that patch the select module like eventlet, greenlet. (Pull #1128)

* Reduced memory consumption when streaming zlib-compressed responses
  (as opposed to raw deflate streams). (Pull #1129)

* Connection pools now use the entire request context when constructing the
  pool key. (Pull #1016)

* ``PoolManager.connection_from_*`` methods now accept a new keyword argument,
  ``pool_kwargs``, which are merged with the existing ``connection_pool_kw``.
  (Pull #1016)

* Add retry counter for ``status_forcelist``. (Issue #1147)

* Added ``contrib`` module for using SecureTransport on macOS:
  ``urllib3.contrib.securetransport``.  (Pull #1122)

* urllib3 now only normalizes the case of ``http://`` and ``https://`` schemes:
  for schemes it does not recognise, it assumes they are case-sensitive and
  leaves them unchanged.
  (Issue #1080)


1.20 (2017-01-19)
-----------------

* Added support for waiting for I/O using selectors other than select,
  improving urllib3's behaviour with large numbers of concurrent connections.
  (Pull #1001)

* Updated the date for the system clock check. (Issue #1005)

* ConnectionPools now correctly consider hostnames to be case-insensitive.
  (Issue #1032)

* Outdated versions of PyOpenSSL now cause the PyOpenSSL contrib module
  to fail when it is injected, rather than at first use. (Pull #1063)

* Outdated versions of cryptography now cause the PyOpenSSL contrib module
  to fail when it is injected, rather than at first use. (Issue #1044)

* Automatically attempt to rewind a file-like body object when a request is
  retried or redirected. (Pull #1039)

* Fix some bugs that occur when modules incautiously patch the queue module.
  (Pull #1061)

* Prevent retries from occurring on read timeouts for which the request method
  was not in the method whitelist. (Issue #1059)

* Changed the PyOpenSSL contrib module to lazily load idna to avoid
  unnecessarily bloating the memory of programs that don't need it. (Pull
  #1076)

* Add support for IPv6 literals with zone identifiers. (Pull #1013)

* Added support for socks5h:// and socks4a:// schemes when working with SOCKS
  proxies, and controlled remote DNS appropriately. (Issue #1035)


1.19.1 (2016-11-16)
-------------------

* Fixed AppEngine import that didn't function on Python 3.5. (Pull #1025)


1.19 (2016-11-03)
-----------------

* urllib3 now respects Retry-After headers on 413, 429, and 503 responses when
  using the default retry logic. (Pull #955)

* Remove markers from setup.py to assist ancient setuptools versions. (Issue
  #986)

* Disallow superscripts and other integerish things in URL ports. (Issue #989)

* Allow urllib3's HTTPResponse.stream() method to continue to work with
  non-httplib underlying FPs. (Pull #990)

* Empty filenames in multipart headers are now emitted as such, rather than
  being suppressed. (Issue #1015)

* Prefer user-supplied Host headers on chunked uploads. (Issue #1009)


1.18.1 (2016-10-27)
-------------------

* CVE-2016-9015. Users who are using urllib3 version 1.17 or 1.18 along with
  PyOpenSSL injection and OpenSSL 1.1.0 *must* upgrade to this version. This
  release fixes a vulnerability whereby urllib3 in the above configuration
  would silently fail to validate TLS certificates due to erroneously setting
  invalid flags in OpenSSL's ``SSL_CTX_set_verify`` function. These erroneous
  flags do not cause a problem in OpenSSL versions before 1.1.0, which
  interprets the presence of any flag as requesting certificate validation.

  There is no PR for this patch, as it was prepared for simultaneous disclosure
  and release. The master branch received the same fix in PR #1010.


1.18 (2016-09-26)
-----------------

* Fixed incorrect message for IncompleteRead exception. (PR #973)

* Accept ``iPAddress`` subject alternative name fields in TLS certificates.
  (Issue #258)

* Fixed consistency of ``HTTPResponse.closed`` between Python 2 and 3.
  (Issue #977)

* Fixed handling of wildcard certificates when using PyOpenSSL. (Issue #979)


1.17 (2016-09-06)
-----------------

* Accept ``SSLContext`` objects for use in SSL/TLS negotiation. (Issue #835)

* ConnectionPool debug log now includes scheme, host, and port. (Issue #897)

* Substantially refactored documentation. (Issue #887)

* Used URLFetch default timeout on AppEngine, rather than hardcoding our own.
  (Issue #858)

* Normalize the scheme and host in the URL parser (Issue #833)

* ``HTTPResponse`` contains the last ``Retry`` object, which now also
  contains retries history. (Issue #848)

* Timeout can no longer be set as boolean, and must be greater than zero.
  (PR #924)

* Removed pyasn1 and ndg-httpsclient from dependencies used for PyOpenSSL. We
  now use cryptography and idna, both of which are already dependencies of
  PyOpenSSL. (PR #930)

* Fixed infinite loop in ``stream`` when amt=None. (Issue #928)

* Try to use the operating system's certificates when we are using an
  ``SSLContext``. (PR #941)

* Updated cipher suite list to allow ChaCha20+Poly1305. AES-GCM is preferred to
  ChaCha20, but ChaCha20 is then preferred to everything else. (PR #947)

* Updated cipher suite list to remove 3DES-based cipher suites. (PR #958)

* Removed the cipher suite fallback to allow HIGH ciphers. (PR #958)

* Implemented ``length_remaining`` to determine remaining content
  to be read. (PR #949)

* Implemented ``enforce_content_length`` to enable exceptions when
  incomplete data chunks are received. (PR #949)

* Dropped connection start, dropped connection reset, redirect, forced retry,
  and new HTTPS connection log levels to DEBUG, from INFO. (PR #967)


1.16 (2016-06-11)
-----------------

* Disable IPv6 DNS when IPv6 connections are not possible. (Issue #840)

* Provide ``key_fn_by_scheme`` pool keying mechanism that can be
  overridden. (Issue #830)

* Normalize scheme and host to lowercase for pool keys, and include
  ``source_address``. (Issue #830)

* Cleaner exception chain in Python 3 for ``_make_request``.
  (Issue #861)

* Fixed installing ``urllib3[socks]`` extra. (Issue #864)

* Fixed signature of ``ConnectionPool.close`` so it can actually safely be
  called by subclasses. (Issue #873)

* Retain ``release_conn`` state across retries. (Issues #651, #866)

* Add customizable ``HTTPConnectionPool.ResponseCls``, which defaults to
  ``HTTPResponse`` but can be replaced with a subclass. (Issue #879)


1.15.1 (2016-04-11)
-------------------

* Fix packaging to include backports module. (Issue #841)


1.15 (2016-04-06)
-----------------

* Added Retry(raise_on_status=False). (Issue #720)

* Always use setuptools, no more distutils fallback. (Issue #785)

* Dropped support for Python 3.2. (Issue #786)

* Chunked transfer encoding when requesting with ``chunked=True``.
  (Issue #790)

* Fixed regression with IPv6 port parsing. (Issue #801)

* Append SNIMissingWarning messages to allow users to specify it in
  the PYTHONWARNINGS environment variable. (Issue #816)

* Handle unicode headers in Py2. (Issue #818)

* Log certificate when there is a hostname mismatch. (Issue #820)

* Preserve order of request/response headers. (Issue #821)


1.14 (2015-12-29)
-----------------

* contrib: SOCKS proxy support! (Issue #762)

* Fixed AppEngine handling of transfer-encoding header and bug
  in Timeout defaults checking. (Issue #763)


1.13.1 (2015-12-18)
-------------------

* Fixed regression in IPv6 + SSL for match_hostname. (Issue #761)


1.13 (2015-12-14)
-----------------

* Fixed ``pip install urllib3[secure]`` on modern pip. (Issue #706)

* pyopenssl: Fixed SSL3_WRITE_PENDING error. (Issue #717)

* pyopenssl: Support for TLSv1.1 and TLSv1.2. (Issue #696)

* Close connections more defensively on exception. (Issue #734)

* Adjusted ``read_chunked`` to handle gzipped, chunk-encoded bodies without
  repeatedly flushing the decoder, to function better on Jython. (Issue #743)

* Accept ``ca_cert_dir`` for SSL-related PoolManager configuration. (Issue #758)


1.12 (2015-09-03)
-----------------

* Rely on ``six`` for importing ``httplib`` to work around
  conflicts with other Python 3 shims. (Issue #688)

* Add support for directories of certificate authorities, as supported by
  OpenSSL. (Issue #701)

* New exception: ``NewConnectionError``, raised when we fail to establish
  a new connection, usually ``ECONNREFUSED`` socket error.


1.11 (2015-07-21)
-----------------

* When ``ca_certs`` is given, ``cert_reqs`` defaults to
  ``'CERT_REQUIRED'``. (Issue #650)

* ``pip install urllib3[secure]`` will install Certifi and
  PyOpenSSL as dependencies. (Issue #678)

* Made ``HTTPHeaderDict`` usable as a ``headers`` input value
  (Issues #632, #679)

* Added `urllib3.contrib.appengine <https://urllib3.readthedocs.io/en/latest/contrib.html#google-app-engine>`_
  which has an ``AppEngineManager`` for using ``URLFetch`` in a
  Google AppEngine environment. (Issue #664)

* Dev: Added test suite for AppEngine. (Issue #631)

* Fix performance regression when using PyOpenSSL. (Issue #626)

* Passing incorrect scheme (e.g. ``foo://``) will raise
  ``ValueError`` instead of ``AssertionError`` (backwards
  compatible for now, but please migrate). (Issue #640)

* Fix pools not getting replenished when an error occurs during a
  request using ``release_conn=False``. (Issue #644)

* Fix pool-default headers not applying for url-encoded requests
  like GET. (Issue #657)

* log.warning in Python 3 when headers are skipped due to parsing
  errors. (Issue #642)

* Close and discard connections if an error occurs during read.
  (Issue #660)

* Fix host parsing for IPv6 proxies. (Issue #668)

* Separate warning type SubjectAltNameWarning, now issued once
  per host. (Issue #671)

* Fix ``httplib.IncompleteRead`` not getting converted to
  ``ProtocolError`` when using ``HTTPResponse.stream()``
  (Issue #674)

1.10.4 (2015-05-03)
-------------------

* Migrate tests to Tornado 4. (Issue #594)

* Append default warning configuration rather than overwrite.
  (Issue #603)

* Fix streaming decoding regression. (Issue #595)

* Fix chunked requests losing state across keep-alive connections.
  (Issue #599)

* Fix hanging when chunked HEAD response has no body. (Issue #605)


1.10.3 (2015-04-21)
-------------------

* Emit ``InsecurePlatformWarning`` when SSLContext object is missing.
  (Issue #558)

* Fix regression of duplicate header keys being discarded.
  (Issue #563)

* ``Response.stream()`` returns a generator for chunked responses.
  (Issue #560)

* Set upper-bound timeout when waiting for a socket in PyOpenSSL.
  (Issue #585)

* Work on platforms without `ssl` module for plain HTTP requests.
  (Issue #587)

* Stop relying on the stdlib's default cipher list. (Issue #588)


1.10.2 (2015-02-25)
-------------------

* Fix file descriptor leakage on retries. (Issue #548)

* Removed RC4 from default cipher list. (Issue #551)

* Header performance improvements. (Issue #544)

* Fix PoolManager not obeying redirect retry settings. (Issue #553)


1.10.1 (2015-02-10)
-------------------

* Pools can be used as context managers. (Issue #545)

* Don't re-use connections which experienced an SSLError. (Issue #529)

* Don't fail when gzip decoding an empty stream. (Issue #535)

* Add sha256 support for fingerprint verification. (Issue #540)

* Fixed handling of header values containing commas. (Issue #533)


1.10 (2014-12-14)
-----------------

* Disabled SSLv3. (Issue #473)

* Add ``Url.url`` property to return the composed url string. (Issue #394)

* Fixed PyOpenSSL + gevent ``WantWriteError``. (Issue #412)

* ``MaxRetryError.reason`` will always be an exception, not string.
  (Issue #481)

* Fixed SSL-related timeouts not being detected as timeouts. (Issue #492)

* Py3: Use ``ssl.create_default_context()`` when available. (Issue #473)

* Emit ``InsecureRequestWarning`` for *every* insecure HTTPS request.
  (Issue #496)

* Emit ``SecurityWarning`` when certificate has no ``subjectAltName``.
  (Issue #499)

* Close and discard sockets which experienced SSL-related errors.
  (Issue #501)

* Handle ``body`` param in ``.request(...)``. (Issue #513)

* Respect timeout with HTTPS proxy. (Issue #505)

* PyOpenSSL: Handle ZeroReturnError exception. (Issue #520)


1.9.1 (2014-09-13)
------------------

* Apply socket arguments before binding. (Issue #427)

* More careful checks if fp-like object is closed. (Issue #435)

* Fixed packaging issues of some development-related files not
  getting included. (Issue #440)

* Allow performing *only* fingerprint verification. (Issue #444)

* Emit ``SecurityWarning`` if system clock is waaay off. (Issue #445)

* Fixed PyOpenSSL compatibility with PyPy. (Issue #450)

* Fixed ``BrokenPipeError`` and ``ConnectionError`` handling in Py3.
  (Issue #443)



1.9 (2014-07-04)
----------------

* Shuffled around development-related files. If you're maintaining a distro
  package of urllib3, you may need to tweak things. (Issue #415)

* Unverified HTTPS requests will trigger a warning on the first request. See
  our new `security documentation
  <https://urllib3.readthedocs.io/en/latest/security.html>`_ for details.
  (Issue #426)

* New retry logic and ``urllib3.util.retry.Retry`` configuration object.
  (Issue #326)

* All raised exceptions should now wrapped in a
  ``urllib3.exceptions.HTTPException``-extending exception. (Issue #326)

* All errors during a retry-enabled request should be wrapped in
  ``urllib3.exceptions.MaxRetryError``, including timeout-related exceptions
  which were previously exempt. Underlying error is accessible from the
  ``.reason`` property. (Issue #326)

* ``urllib3.exceptions.ConnectionError`` renamed to
  ``urllib3.exceptions.ProtocolError``. (Issue #326)

* Errors during response read (such as IncompleteRead) are now wrapped in
  ``urllib3.exceptions.ProtocolError``. (Issue #418)

* Requesting an empty host will raise ``urllib3.exceptions.LocationValueError``.
  (Issue #417)

* Catch read timeouts over SSL connections as
  ``urllib3.exceptions.ReadTimeoutError``. (Issue #419)

* Apply socket arguments before connecting. (Issue #427)


1.8.3 (2014-06-23)
------------------

* Fix TLS verification when using a proxy in Python 3.4.1. (Issue #385)

* Add ``disable_cache`` option to ``urllib3.util.make_headers``. (Issue #393)

* Wrap ``socket.timeout`` exception with
  ``urllib3.exceptions.ReadTimeoutError``. (Issue #399)

* Fixed proxy-related bug where connections were being reused incorrectly.
  (Issues #366, #369)

* Added ``socket_options`` keyword parameter which allows to define
  ``setsockopt`` configuration of new sockets. (Issue #397)

* Removed ``HTTPConnection.tcp_nodelay`` in favor of
  ``HTTPConnection.default_socket_options``. (Issue #397)

* Fixed ``TypeError`` bug in Python 2.6.4. (Issue #411)


1.8.2 (2014-04-17)
------------------

* Fix ``urllib3.util`` not being included in the package.


1.8.1 (2014-04-17)
------------------

* Fix AppEngine bug of HTTPS requests going out as HTTP. (Issue #356)

* Don't install ``dummyserver`` into ``site-packages`` as it's only needed
  for the test suite. (Issue #362)

* Added support for specifying ``source_address``. (Issue #352)


1.8 (2014-03-04)
----------------

* Improved url parsing in ``urllib3.util.parse_url`` (properly parse '@' in
  username, and blank ports like 'hostname:').

* New ``urllib3.connection`` module which contains all the HTTPConnection
  objects.

* Several ``urllib3.util.Timeout``-related fixes. Also changed constructor
  signature to a more sensible order. [Backwards incompatible]
  (Issues #252, #262, #263)

* Use ``backports.ssl_match_hostname`` if it's installed. (Issue #274)

* Added ``.tell()`` method to ``urllib3.response.HTTPResponse`` which
  returns the number of bytes read so far. (Issue #277)

* Support for platforms without threading. (Issue #289)

* Expand default-port comparison in ``HTTPConnectionPool.is_same_host``
  to allow a pool with no specified port to be considered equal to to an
  HTTP/HTTPS url with port 80/443 explicitly provided. (Issue #305)

* Improved default SSL/TLS settings to avoid vulnerabilities.
  (Issue #309)

* Fixed ``urllib3.poolmanager.ProxyManager`` not retrying on connect errors.
  (Issue #310)

* Disable Nagle's Algorithm on the socket for non-proxies. A subset of requests
  will send the entire HTTP request ~200 milliseconds faster; however, some of
  the resulting TCP packets will be smaller. (Issue #254)

* Increased maximum number of SubjectAltNames in ``urllib3.contrib.pyopenssl``
  from the default 64 to 1024 in a single certificate. (Issue #318)

* Headers are now passed and stored as a custom
  ``urllib3.collections_.HTTPHeaderDict`` object rather than a plain ``dict``.
  (Issue #329, #333)

* Headers no longer lose their case on Python 3. (Issue #236)

* ``urllib3.contrib.pyopenssl`` now uses the operating system's default CA
  certificates on inject. (Issue #332)

* Requests with ``retries=False`` will immediately raise any exceptions without
  wrapping them in ``MaxRetryError``. (Issue #348)

* Fixed open socket leak with SSL-related failures. (Issue #344, #348)


1.7.1 (2013-09-25)
------------------

* Added granular timeout support with new ``urllib3.util.Timeout`` class.
  (Issue #231)

* Fixed Python 3.4 support. (Issue #238)


1.7 (2013-08-14)
----------------

* More exceptions are now pickle-able, with tests. (Issue #174)

* Fixed redirecting with relative URLs in Location header. (Issue #178)

* Support for relative urls in ``Location: ...`` header. (Issue #179)

* ``urllib3.response.HTTPResponse`` now inherits from ``io.IOBase`` for bonus
  file-like functionality. (Issue #187)

* Passing ``assert_hostname=False`` when creating a HTTPSConnectionPool will
  skip hostname verification for SSL connections. (Issue #194)

* New method ``urllib3.response.HTTPResponse.stream(...)`` which acts as a
  generator wrapped around ``.read(...)``. (Issue #198)

* IPv6 url parsing enforces brackets around the hostname. (Issue #199)

* Fixed thread race condition in
  ``urllib3.poolmanager.PoolManager.connection_from_host(...)`` (Issue #204)

* ``ProxyManager`` requests now include non-default port in ``Host: ...``
  header. (Issue #217)

* Added HTTPS proxy support in ``ProxyManager``. (Issue #170 #139)

* New ``RequestField`` object can be passed to the ``fields=...`` param which
  can specify headers. (Issue #220)

* Raise ``urllib3.exceptions.ProxyError`` when connecting to proxy fails.
  (Issue #221)

* Use international headers when posting file names. (Issue #119)

* Improved IPv6 support. (Issue #203)


1.6 (2013-04-25)
----------------

* Contrib: Optional SNI support for Py2 using PyOpenSSL. (Issue #156)

* ``ProxyManager`` automatically adds ``Host: ...`` header if not given.

* Improved SSL-related code. ``cert_req`` now optionally takes a string like
  "REQUIRED" or "NONE". Same with ``ssl_version`` takes strings like "SSLv23"
  The string values reflect the suffix of the respective constant variable.
  (Issue #130)

* Vendored ``socksipy`` now based on Anorov's fork which handles unexpectedly
  closed proxy connections and larger read buffers. (Issue #135)

* Ensure the connection is closed if no data is received, fixes connection leak
  on some platforms. (Issue #133)

* Added SNI support for SSL/TLS connections on Py32+. (Issue #89)

* Tests fixed to be compatible with Py26 again. (Issue #125)

* Added ability to choose SSL version by passing an ``ssl.PROTOCOL_*`` constant
  to the ``ssl_version`` parameter of ``HTTPSConnectionPool``. (Issue #109)

* Allow an explicit content type to be specified when encoding file fields.
  (Issue #126)

* Exceptions are now pickleable, with tests. (Issue #101)

* Fixed default headers not getting passed in some cases. (Issue #99)

* Treat "content-encoding" header value as case-insensitive, per RFC 2616
  Section 3.5. (Issue #110)

* "Connection Refused" SocketErrors will get retried rather than raised.
  (Issue #92)

* Updated vendored ``six``, no longer overrides the global ``six`` module
  namespace. (Issue #113)

* ``urllib3.exceptions.MaxRetryError`` contains a ``reason`` property holding
  the exception that prompted the final retry. If ``reason is None`` then it
  was due to a redirect. (Issue #92, #114)

* Fixed ``PoolManager.urlopen()`` from not redirecting more than once.
  (Issue #149)

* Don't assume ``Content-Type: text/plain`` for multi-part encoding parameters
  that are not files. (Issue #111)

* Pass `strict` param down to ``httplib.HTTPConnection``. (Issue #122)

* Added mechanism to verify SSL certificates by fingerprint (md5, sha1) or
  against an arbitrary hostname (when connecting by IP or for misconfigured
  servers). (Issue #140)

* Streaming decompression support. (Issue #159)


1.5 (2012-08-02)
----------------

* Added ``urllib3.add_stderr_logger()`` for quickly enabling STDERR debug
  logging in urllib3.

* Native full URL parsing (including auth, path, query, fragment) available in
  ``urllib3.util.parse_url(url)``.

* Built-in redirect will switch method to 'GET' if status code is 303.
  (Issue #11)

* ``urllib3.PoolManager`` strips the scheme and host before sending the request
  uri. (Issue #8)

* New ``urllib3.exceptions.DecodeError`` exception for when automatic decoding,
  based on the Content-Type header, fails.

* Fixed bug with pool depletion and leaking connections (Issue #76). Added
  explicit connection closing on pool eviction. Added
  ``urllib3.PoolManager.clear()``.

* 99% -> 100% unit test coverage.


1.4 (2012-06-16)
----------------

* Minor AppEngine-related fixes.

* Switched from ``mimetools.choose_boundary`` to ``uuid.uuid4()``.

* Improved url parsing. (Issue #73)

* IPv6 url support. (Issue #72)


1.3 (2012-03-25)
----------------

* Removed pre-1.0 deprecated API.

* Refactored helpers into a ``urllib3.util`` submodule.

* Fixed multipart encoding to support list-of-tuples for keys with multiple
  values. (Issue #48)

* Fixed multiple Set-Cookie headers in response not getting merged properly in
  Python 3. (Issue #53)

* AppEngine support with Py27. (Issue #61)

* Minor ``encode_multipart_formdata`` fixes related to Python 3 strings vs
  bytes.


1.2.2 (2012-02-06)
------------------

* Fixed packaging bug of not shipping ``test-requirements.txt``. (Issue #47)


1.2.1 (2012-02-05)
------------------

* Fixed another bug related to when ``ssl`` module is not available. (Issue #41)

* Location parsing errors now raise ``urllib3.exceptions.LocationParseError``
  which inherits from ``ValueError``.


1.2 (2012-01-29)
----------------

* Added Python 3 support (tested on 3.2.2)

* Dropped Python 2.5 support (tested on 2.6.7, 2.7.2)

* Use ``select.poll`` instead of ``select.select`` for platforms that support
  it.

* Use ``Queue.LifoQueue`` instead of ``Queue.Queue`` for more aggressive
  connection reusing. Configurable by overriding ``ConnectionPool.QueueCls``.

* Fixed ``ImportError`` during install when ``ssl`` module is not available.
  (Issue #41)

* Fixed ``PoolManager`` redirects between schemes (such as HTTP -> HTTPS) not
  completing properly. (Issue #28, uncovered by Issue #10 in v1.1)

* Ported ``dummyserver`` to use ``tornado`` instead of ``webob`` +
  ``eventlet``. Removed extraneous unsupported dummyserver testing backends.
  Added socket-level tests.

* More tests. Achievement Unlocked: 99% Coverage.


1.1 (2012-01-07)
----------------

* Refactored ``dummyserver`` to its own root namespace module (used for
  testing).

* Added hostname verification for ``VerifiedHTTPSConnection`` by vendoring in
  Py32's ``ssl_match_hostname``. (Issue #25)

* Fixed cross-host HTTP redirects when using ``PoolManager``. (Issue #10)

* Fixed ``decode_content`` being ignored when set through ``urlopen``. (Issue
  #27)

* Fixed timeout-related bugs. (Issues #17, #23)


1.0.2 (2011-11-04)
------------------

* Fixed typo in ``VerifiedHTTPSConnection`` which would only present as a bug if
  you're using the object manually. (Thanks pyos)

* Made RecentlyUsedContainer (and consequently PoolManager) more thread-safe by
  wrapping the access log in a mutex. (Thanks @christer)

* Made RecentlyUsedContainer more dict-like (corrected ``__delitem__`` and
  ``__getitem__`` behaviour), with tests. Shouldn't affect core urllib3 code.


1.0.1 (2011-10-10)
------------------

* Fixed a bug where the same connection would get returned into the pool twice,
  causing extraneous "HttpConnectionPool is full" log warnings.


1.0 (2011-10-08)
----------------

* Added ``PoolManager`` with LRU expiration of connections (tested and
  documented).
* Added ``ProxyManager`` (needs tests, docs, and confirmation that it works
  with HTTPS proxies).
* Added optional partial-read support for responses when
  ``preload_content=False``. You can now make requests and just read the headers
  without loading the content.
* Made response decoding optional (default on, same as before).
* Added optional explicit boundary string for ``encode_multipart_formdata``.
* Convenience request methods are now inherited from ``RequestMethods``. Old
  helpers like ``get_url`` and ``post_url`` should be abandoned in favour of
  the new ``request(method, url, ...)``.
* Refactored code to be even more decoupled, reusable, and extendable.
* License header added to ``.py`` files.
* Embiggened the documentation: Lots of Sphinx-friendly docstrings in the code
  and docs in ``docs/`` and on https://urllib3.readthedocs.io/.
* Embettered all the things!
* Started writing this file.


0.4.1 (2011-07-17)
------------------

* Minor bug fixes, code cleanup.


0.4 (2011-03-01)
----------------

* Better unicode support.
* Added ``VerifiedHTTPSConnection``.
* Added ``NTLMConnectionPool`` in contrib.
* Minor improvements.


0.3.1 (2010-07-13)
------------------

* Added ``assert_host_name`` optional parameter. Now compatible with proxies.


0.3 (2009-12-10)
----------------

* Added HTTPS support.
* Minor bug fixes.
* Refactored, broken backwards compatibility with 0.2.
* API to be treated as stable from this version forward.


0.2 (2008-11-17)
----------------

* Added unit tests.
* Bug fixes.


0.1 (2008-11-16)
----------------

* First release.




%prep
%setup -q -n urllib3-%{version}

%build
%{__python3_other} setup.py build

%install
%{__python3_other} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python3_other_sitelib}/*

%changelog
