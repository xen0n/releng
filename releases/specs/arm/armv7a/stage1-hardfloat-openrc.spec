subarch: armv7a_hardfp
version_stamp: openrc-@TIMESTAMP@
target: stage1
rel_type: default
profile: default/linux/arm/17.0/armv7a
snapshot: @TIMESTAMP@
source_subpath: default/stage3-armv7a_hardfp-openrc-latest
compression_mode: pixz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
