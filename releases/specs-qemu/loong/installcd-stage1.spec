subarch: loong
version_stamp: @TIMESTAMP@
target: livecd-stage1
rel_type: 23.0-default
profile: default/linux/loong/23.0/la64v100/lp64d
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/stage3-loong-openrc-@TIMESTAMP@
compression_mode: pixz
portage_confdir: @REPO_DIR@/releases/portage/isos-qemu
interpreter: /usr/bin/qemu-loongarch64

livecd/use:
	alsa
	compile-locales
	fbcon
	livecd
	portaudio
	socks5
	unicode
	xml

livecd/packages:
	app-accessibility/brltty
	app-accessibility/espeakup
	app-admin/hddtemp
	app-admin/pwgen
	app-admin/syslog-ng
	app-arch/unzip
	app-crypt/gnupg
	app-editors/mg
	app-editors/nano
	app-editors/vim
	app-misc/livecd-tools
	app-misc/screen
	app-misc/tmux
	#app-portage/cpuid2cpuflags  # not yet relevant on loong
	app-portage/mirrorselect
	app-shells/bash-completion
	app-shells/gentoo-bashcomp
	app-text/wgetpaste
	media-gfx/fbgrab
	media-sound/alsa-utils
	net-analyzer/traceroute
	net-dialup/mingetty
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-fs/cifs-utils
	net-fs/nfs-utils
	net-irc/irssi
	net-misc/chrony
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/ndisc6
	net-misc/openssh
	net-misc/rdate
	net-misc/rsync
	net-misc/vconfig
	net-proxy/dante
	net-proxy/tsocks
	net-wireless/iw
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	sys-apps/arch-chroot
	sys-apps/busybox
	sys-apps/dmidecode
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/gptfdisk
	sys-apps/hdparm
	sys-apps/iproute2
	sys-apps/memtester
	sys-apps/merge-usr
	sys-apps/netplug
	sys-apps/nvme-cli
	sys-apps/pciutils
	sys-apps/pcmciautils
	sys-apps/pv
	sys-apps/sdparm
	sys-apps/usbutils
	sys-auth/ssh-import-id
	sys-block/parted
	sys-block/partimage
	sys-boot/efibootmgr
	sys-devel/bc
	sys-fs/bcache-tools
	sys-fs/btrfs-progs
	sys-fs/cryptsetup
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/f2fs-tools
	sys-fs/genfstab
	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
	sys-fs/mdadm
	sys-fs/multipath-tools
	sys-fs/ntfs3g
	sys-fs/reiserfsprogs
	sys-fs/xfsdump
	sys-fs/xfsprogs
	sys-kernel/linux-firmware
	sys-libs/gpm
	sys-power/acpid
	www-client/links
