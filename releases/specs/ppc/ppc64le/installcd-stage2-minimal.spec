subarch: ppc64le
version_stamp: @TIMESTAMP@
target: livecd-stage2
rel_type: default
profile: default/linux/ppc64le/17.0
snapshot: @TIMESTAMP@
source_subpath: default/livecd-stage1-ppc64le-@TIMESTAMP@
compression_mode: pixz_x
portage_confdir: @REPO_DIR@/releases/portage/isos

livecd/bootargs: dokeymap
livecd/fstype: squashfs 
livecd/gk_mainargs: --makeopts=-j12
livecd/iso: install-ppc64le-minimal-@TIMESTAMP@.iso
livecd/type: gentoo-release-minimal
livecd/volid: Gentoo ppc64le @TIMESTAMP@

boot/kernel: 4K_PAGESZ 64K_PAGESZ

# OpenPower hardware primary, but kernel also supports pseries and qemu.
# We neet to ship both 4K and 64K page kernels, as some filesystems
# can't be mounted on 4K if created on 64K kernels (btrfs is known to do that and some others)
boot/kernel/4K_PAGESZ/sources: sys-kernel/gentoo-sources
boot/kernel/4K_PAGESZ/config: ../../../kconfig/powerpc/installcd-ppc64le-4K-5.10.config
boot/kernel/4K_PAGESZ/console: hvc0 tty0
boot/kernel/4K_PAGESZ/extraversion: 4K_PAGESZ
boot/kernel/4K_PAGESZ/gk_kernargs: --all-ramdisk-modules --firmware

boot/kernel/64K_PAGESZ/sources: sys-kernel/gentoo-sources
boot/kernel/64K_PAGESZ/config: ../../../kconfig/powerpc/installcd-ppc64le-64K-5.10.config
boot/kernel/64K_PAGESZ/console: hvc0 tty0
boot/kernel/64K_PAGESZ/extraversion: 64K_PAGESZ
boot/kernel/64K_PAGESZ/gk_kernargs: --all-ramdisk-modules --firmware

livecd/unmerge:
	app-admin/eselect
	app-admin/eselect-ctags
	app-admin/eselect-vi
	app-admin/perl-cleaner
	app-admin/python-updater
	app-arch/cpio
	dev-libs/gmp
	dev-libs/libxml2
	dev-libs/mpfr
	dev-python/pycrypto
	dev-util/pkgconfig
	perl-core/PodParser
	perl-core/Test-Harness
	sys-apps/debianutils
	sys-apps/diffutils
	sys-apps/groff
	sys-apps/man-db
	sys-apps/man-pages
	sys-apps/miscfiles
	sys-apps/sandbox
	sys-apps/texinfo
	sys-devel/autoconf
	sys-devel/autoconf-wrapper
	sys-devel/automake
	sys-devel/automake-wrapper
	sys-devel/binutils
	sys-devel/binutils-config
	sys-devel/bison
	sys-devel/flex
	sys-devel/gcc
	sys-devel/gcc-config
	sys-devel/gettext
	sys-devel/gnuconfig
	sys-devel/libtool
	sys-devel/m4
	sys-devel/make
	sys-devel/patch
	sys-libs/db
	sys-libs/gdbm
	sys-kernel/genkernel
	sys-kernel/linux-headers

livecd/empty:
	/boot
	/etc/cron.daily
	/etc/cron.hourly
	/etc/cron.monthly
	/etc/cron.weekly
	/etc/logrotate.d
	/etc/modules.autoload.d
	/etc/rsync
	/etc/runlevels/single
	/etc/skel
	/lib/dev-state
	/lib/udev-state
	/lib64/dev-state
	/lib64/udev-state
	/root/.ccache
	/tmp
	/usr/include
	/usr/lib64/X11/config
	/usr/lib64/X11/doc
	/usr/lib64/X11/etc
	/usr/lib64/awk
	/usr/lib64/ccache
	/usr/lib64/gcc-config
	/usr/lib64/nfs
	/usr/lib64/perl5/site_perl
	/usr/lib64/portage
	/usr/local
	/usr/portage
	/usr/powerpc64*-unknown-linux-gnu
	/usr/share/aclocal
	/usr/share/baselayout
	/usr/share/binutils-data
	/usr/share/consolefonts/partialfonts
	/usr/share/consoletrans
	/usr/share/dict
	/usr/share/doc
	/usr/share/emacs
	/usr/share/et
	/usr/share/gcc-data
	/usr/share/genkernel
	/usr/share/gettext
	/usr/share/glib-2.0
	/usr/share/gnuconfig
	/usr/share/gtk-doc
	/usr/share/i18n
	/usr/share/info
	/usr/share/lcms
	/usr/share/libtool
	/usr/share/locale
	/usr/share/man
	/usr/share/rfc
	/usr/share/ss
	/usr/share/state
	/usr/share/texinfo
	/usr/share/unimaps
	/usr/share/zoneinfo
	/usr/src
	/var/cache
	/var/empty
	/var/lib/portage
	/var/log
	/var/spool
	/var/state
	/var/tmp

livecd/rm:
	/boot/System*
	/boot/initr*
	/boot/kernel*
	/etc/*-
	/etc/*.old
	/etc/default/audioctl
	/etc/dispatch-conf.conf
	/etc/env.d/05binutils
	/etc/env.d/05gcc
	/etc/etc-update.conf
	/etc/hosts.bck
	/etc/issue*
	/etc/genkernel.conf
	/etc/make.conf*
	/etc/make.globals
	/etc/make.profile
	/etc/man.conf
	/etc/resolv.conf
	/lib*/*.a
	/lib*/*.la
	/lib*/cpp
	/root/.bash_history
	/root/.viminfo
	/sbin/*.static
	/sbin/fsck.cramfs
	/sbin/fsck.minix
	/sbin/mkfs.bfs
	/sbin/mkfs.cramfs
	/sbin/mkfs.minix
	/usr/bin/addr2line
	/usr/bin/ar
	/usr/bin/as
	/usr/bin/audioctl
	/usr/bin/c++*
	/usr/bin/cc
	/usr/bin/cjpeg
	/usr/bin/cpp
	/usr/bin/djpeg
	/usr/bin/ebuild
	/usr/bin/egencache
	/usr/bin/emerge
	/usr/bin/emerge-webrsync
	/usr/bin/emirrordist
	/usr/bin/elftoaout
	/usr/bin/f77
	/usr/bin/g++*
	/usr/bin/g77
	/usr/bin/gcc*
	/usr/bin/genkernel
	/usr/bin/gprof
	/usr/bin/jpegtran
	/usr/bin/ld
	/usr/bin/libpng*
	/usr/bin/nm
	/usr/bin/objcopy
	/usr/bin/objdump
	/usr/bin/piggyback*
	/usr/bin/portageq
	/usr/bin/ranlib
	/usr/bin/readelf
	/usr/bin/repoman
	/usr/bin/size
	/usr/bin/powerpc64*-unknown-linux-gnu-*
	/usr/bin/strings
	/usr/bin/strip
	/usr/bin/tbz2tool
	/usr/bin/xpak
	/usr/bin/yacc
	/usr/lib*/*.a
	/usr/lib*/*.la
	/usr/lib*/perl5/site_perl
	/usr/lib*/gcc-lib/*/*/libgcj*
	/usr/sbin/archive-conf
	/usr/sbin/dispatch-conf
	/usr/sbin/emaint
	/usr/sbin/env-update
	/usr/sbin/etc-update
	/usr/sbin/fb*
	/usr/sbin/fixpackages
	/usr/sbin/quickpkg
	/usr/sbin/regenworld
	/usr/share/consolefonts/1*
	/usr/share/consolefonts/7*
	/usr/share/consolefonts/8*
	/usr/share/consolefonts/9*
	/usr/share/consolefonts/A*
	/usr/share/consolefonts/C*
	/usr/share/consolefonts/E*
	/usr/share/consolefonts/G*
	/usr/share/consolefonts/L*
	/usr/share/consolefonts/M*
	/usr/share/consolefonts/R*
	/usr/share/consolefonts/a*
	/usr/share/consolefonts/c*
	/usr/share/consolefonts/dr*
	/usr/share/consolefonts/g*
	/usr/share/consolefonts/i*
	/usr/share/consolefonts/k*
	/usr/share/consolefonts/l*
	/usr/share/consolefonts/r*
	/usr/share/consolefonts/s*
	/usr/share/consolefonts/t*
	/usr/share/consolefonts/v*
	/usr/share/misc/*.old