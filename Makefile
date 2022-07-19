# HACK: Expand the _topdir path to work around "Dest dir longer than base dir is not supported" errors from rpmbuild
RPMBUILD = rpmbuild --define "_topdir %(pwd)/build/../build/../build/../build/" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)" \
        --undefine=_disable_source_fetch

# Generate spec files for new packages using:
# py2pack generate -t fedora.spec <package name> <package version>
# then rename and modify spec file to use match the others in the repository
web: flask werkzeug jinja2 github-flask bibtexparser biplist itsdangerous
general: pyerfa astropy astroquery keyring skyfield sgp4 jplephem sep pyds9 pyro4 photutils strict-rfc3339 demjson mpmath sympy sip_tpv pcomfortcloud libusb1

astropy:
	mkdir -p build
	${RPMBUILD} -ba python3-astropy.spec
	mv build/x86_64/*.rpm .
	rm -rf build

pyerfa:
	mkdir -p build
	${RPMBUILD} -ba python3-pyerfa.spec
	mv build/x86_64/*.rpm .
	rm -rf build

pyds9:
	mkdir -p build
	${RPMBUILD} -ba python3-pyds9.spec
	mv build/x86_64/*.rpm .
	rm -rf x86_64

serpent:
	mkdir -p build
	${RPMBUILD} -ba python3-serpent.spec
	mv build/noarch/*.rpm .
	rm -rf build

pyro4:
	mkdir -p build
	${RPMBUILD} -ba python3-Pyro4.spec
	mv build/noarch/*.rpm .
	rm -rf build

sep:
	mkdir -p build
	${RPMBUILD} -ba python3-sep.spec
	mv build/x86_64/*.rpm .
	rm -rf build

demjson:
	mkdir -p build
	${RPMBUILD} -ba python3-demjson.spec
	mv build/noarch/*.rpm .
	rm -rf build

strict-rfc3339:
	mkdir -p build
	${RPMBUILD} -ba python3-strict-rfc3339.spec
	mv build/noarch/*.rpm .
	rm -rf build

skyfield:
	mkdir -p build
	${RPMBUILD} -ba python3-skyfield.spec
	mv build/noarch/*.rpm .
	rm -rf build

sgp4:
	mkdir -p build
	${RPMBUILD} -ba python3-sgp4.spec
	mv build/x86_64/*.rpm .
	rm -rf build

jplephem:
	mkdir -p build
	${RPMBUILD} -ba python3-jplephem.spec
	mv build/noarch/*.rpm .
	rm -rf build

astroquery:
	mkdir -p build
	${RPMBUILD} -ba python3-astroquery.spec
	mv build/noarch/*.rpm .
	rm -rf build

keyring:
	mkdir -p build
	${RPMBUILD} -ba python3-keyring.spec
	mv build/noarch/*.rpm .
	rm -rf build

bibtexparser:
	mkdir -p build
	${RPMBUILD} -ba python3-bibtexparser.spec
	mv build/noarch/*.rpm .
	rm -rf build

biplist:
	mkdir -p build
	${RPMBUILD} -ba python3-biplist.spec
	mv build/noarch/*.rpm .
	rm -rf build

photutils:
	mkdir -p build
	${RPMBUILD} -ba python3-photutils.spec
	mv build/x86_64/*.rpm .
	rm -rf build

flask:
	mkdir -p build
	${RPMBUILD} -ba python3-flask.spec
	mv build/noarch/*.rpm .
	rm -rf build

jinja2:
	mkdir -p build
	${RPMBUILD} -ba python3-jinja2.spec
	mv build/noarch/*.rpm .
	rm -rf build

werkzeug:
	mkdir -p build
	${RPMBUILD} -ba python3-werkzeug.spec
	mv build/noarch/*.rpm .
	rm -rf build

github-flask:
	mkdir -p build
	${RPMBUILD} -ba python3-github-flask.spec
	mv build/noarch/*.rpm .
	rm -rf build

mpmath:
	mkdir -p build
	${RPMBUILD} -ba python3-mpmath.spec
	mv build/noarch/*.rpm .
	rm -rf build

sympy:
	mkdir -p build
	${RPMBUILD} -ba python3-sympy.spec
	mv build/noarch/*.rpm .
	rm -rf build

sip_tpv:
	mkdir -p build
	${RPMBUILD} -ba python3-sip_tpv.spec
	mv build/noarch/*.rpm .
	rm -rf build

itsdangerous:
	mkdir -p build
	${RPMBUILD} -ba python3-itsdangerous.spec
	mv build/noarch/*.rpm .
	rm -rf build

pcomfortcloud:
	mkdir -p build
	${RPMBUILD} -ba python3-pcomfortcloud.spec
	mv build/noarch/*.rpm .
	rm -rf build

libusb1:
	mkdir -p build
	${RPMBUILD} -ba python3-libusb1.spec
	mv build/x86_64/*.rpm .
	rm -rf build
