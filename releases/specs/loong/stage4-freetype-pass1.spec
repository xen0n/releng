subarch: loong
target: stage4
version_stamp: systemd-ft-pass1-20211001
rel_type: default
profile: loongson:default/linux/loong/21.0/la64v100/lp64d/desktop/systemd
snapshot: 20211001
compression_mode: pixz_x
source_subpath: default/stage3-loong-systemd-20211001
portage_overlay: /var/gentoo/repos/loongson-overlay
portage_confdir: /opt/la-releng/portage/stages

stage4/use:
	bindist
	bzip2
	idm
	ipv6
	urandom

stage4/packages:
	media-libs/freetype

stage4/empty:
	/root/.ccache
	/tmp
	/usr/portage/distfiles
	/usr/src
	/var/cache/edb/dep
	/var/cache/genkernel
	/var/cache/portage/distfiles
	/var/empty
	/var/run
	/var/state
	/var/tmp

stage4/rm:
	/etc/*-
	/etc/*.old
	/etc/ssh/ssh_host_*
	/root/.*history
	/root/.lesshst
	/root/.ssh/known_hosts
	/root/.viminfo
	# Remove any generated stuff by genkernel
	/usr/share/genkernel
	# This is 3MB of crap for each copy
	/usr/lib64/python*/site-packages/gentoolkit/test/eclean/testdistfiles.tar.gz
