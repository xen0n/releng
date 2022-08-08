subarch: loong
version_stamp: systemd-20220808
target: stage1
rel_type: default
profile: default/linux/loong/22.0/la64v100/lp64d/systemd

snapshot: 20220808  # hand-generated

source_subpath: default/stage3-loong-systemd-20220707
update_seed: yes
update_seed_command: -uDU @world
compression_mode: pixz_x
#portage_overlay: /var/gentoo/repos/loongson-overlay
