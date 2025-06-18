# List the packages that should be built under each recipe
x86_64 = astropy pyerfa sep sgp4 photutils
noarch = flask github-flask bibtexparser biplist libusb1 astropy-iers-data skyfield sgp4 jplephem sep serpent Pyro4 photutils mpmath sympy scp sip_tpv pcomfortcloud
aarch64 = astropy pyerfa sep sgp4 photutils rpi.gpio

# Generate recipes for each of the listed packages
all = $(x86_64) $(noarch) $(aarch64)

all: $(all)
noarch: $(noarch)
x86_64: $(x86_64)
aarch64: $(aarch64)

define GENERATE_RECIPE
ifndef $(1)_DEFINED
$(1)_DEFINED = 1
$(1):
	@mkdir -p build
	rpmbuild --define "_topdir %(pwd)/build/" \
         --define "_builddir %{_topdir}" \
         --define "_rpmdir %{_topdir}" \
         --define "_srcrpmdir %{_topdir}" \
         --define "_sourcedir %{_topdir}" \
         -ba python3-$(1).spec
	@mv build/*/*.rpm .
	@rm -rf build
endif
endef
$(foreach package,$(all),$(eval $(call GENERATE_RECIPE,$(package))))
