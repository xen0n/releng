subarch: loong
version_stamp: systemd-20220416
target: stage1
rel_type: default
profile: loongson:default/linux/loong/22.0/la64v100/lp64d/systemd

snapshot: 20220416  # hand-generated

source_subpath: default/stage3-loong-openrc-20220416
update_seed: yes
update_seed_command: --update --deep --newuse @world
compression_mode: pixz_x
portage_overlay: /var/gentoo/repos/loongson-overlay
