subarch: armv7a_hardfp_musl
version_stamp: musl-@TIMESTAMP@
target: stage1
rel_type: musl
profile: default/linux/arm/17.0/musl/armv7a
snapshot: @TIMESTAMP@
source_subpath: musl/stage3-armv7a_hardfp-musl-latest
compression_mode: pixz_x
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-musl
portage_prefix: releng
repos: /root/musl
