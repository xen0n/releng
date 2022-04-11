subarch: loong
version_stamp: systemd-20220411
target: stage1
rel_type: default
profile: loongson:default/linux/loong/21.0/la64v100/lp64d/systemd

snapshot: 20220411  # hand-generated

source_subpath: default/stage3-loong-systemd-20220326
update_seed: yes
update_seed_command: --update --deep --newuse @world
compression_mode: pixz_x
portage_overlay: /var/gentoo/repos/loongson-overlay
