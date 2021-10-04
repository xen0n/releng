subarch: loong
target: stage4
version_stamp: systemd-qemu-20211001
rel_type: default
profile: loongson:desktop/3a5000/systemd
snapshot: 20211001
compression_mode: pixz_x
source_subpath: default/stage4-systemd-ft-pass1-20211001
portage_overlay: /var/gentoo/repos/loongson-overlay
portage_confdir: /opt/la-releng/portage/stages

stage4/use:
	bindist
	bzip2
	gtk
	gtk3
	harfbuzz
	idm
	ipv6
	policykit
	qemu_softmmu_targets_aarch64
	qemu_softmmu_targets_alpha
	qemu_softmmu_targets_arm
	qemu_softmmu_targets_avr
	qemu_softmmu_targets_cris
	qemu_softmmu_targets_hppa
	qemu_softmmu_targets_i386
	qemu_softmmu_targets_m68k
	qemu_softmmu_targets_microblaze
	qemu_softmmu_targets_microblazeel
	qemu_softmmu_targets_mips
	qemu_softmmu_targets_mips64
	qemu_softmmu_targets_mips64el
	qemu_softmmu_targets_mipsel
	qemu_softmmu_targets_nios2
	qemu_softmmu_targets_or1k
	qemu_softmmu_targets_ppc
	qemu_softmmu_targets_ppc64
	qemu_softmmu_targets_riscv32
	qemu_softmmu_targets_riscv64
	qemu_softmmu_targets_rx
	qemu_softmmu_targets_s390x
	qemu_softmmu_targets_sh4
	qemu_softmmu_targets_sh4eb
	qemu_softmmu_targets_sparc
	qemu_softmmu_targets_sparc64
	qemu_softmmu_targets_tricore
	qemu_softmmu_targets_x86_64
	qemu_softmmu_targets_xtensa
	qemu_softmmu_targets_xtensaeb
	qemu_user_targets_aarch64
	qemu_user_targets_aarch64_be
	qemu_user_targets_alpha
	qemu_user_targets_arm
	qemu_user_targets_armeb
	qemu_user_targets_cris
	qemu_user_targets_hexagon
	qemu_user_targets_hppa
	qemu_user_targets_i386
	qemu_user_targets_m68k
	qemu_user_targets_microblaze
	qemu_user_targets_microblazeel
	qemu_user_targets_mips
	qemu_user_targets_mips64
	qemu_user_targets_mips64el
	qemu_user_targets_mipsel
	qemu_user_targets_mipsn32
	qemu_user_targets_mipsn32el
	qemu_user_targets_nios2
	qemu_user_targets_or1k
	qemu_user_targets_ppc
	qemu_user_targets_ppc64
	qemu_user_targets_ppc64abi32
	qemu_user_targets_ppc64le
	qemu_user_targets_riscv32
	qemu_user_targets_riscv64
	qemu_user_targets_s390x
	qemu_user_targets_sh4
	qemu_user_targets_sh4eb
	qemu_user_targets_sparc
	qemu_user_targets_sparc32plus
	qemu_user_targets_sparc64
	qemu_user_targets_x86_64
	qemu_user_targets_xtensa
	qemu_user_targets_xtensaeb
	udisks
	unicode
	urandom
	X

stage4/packages:
	app-emulation/qemu

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
