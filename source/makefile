SHELL = bash
all: kern donemsg
kern: prepperms kerncomp
install: kern rootfs donemsg
compiletest: prepperms ctest
debug: prepperms kerncompd
test: compiletest blacktest

donemsg:
	@echo -e "\nSyncing changes.."
	@sync
	@echo -e "\n   ---Operation completed successfully---\n\nTry running make connection"
rootfs:
	@echo -e "\nUpdating the board's rootfs:\n"
	@sync
	@../scripts/copy_rootfs.sh
prepperms:
	@echo -e "Preparing script permissions..\n"
	@chmod +x ../scripts/*.sh
	@chmod +x ../scripts/mpy*
	@echo -e "OK"
kerncomp:
	@echo -e "\nCommencing kernel compilation.."
	@sync
	@python3 ../scripts/make_kernel.py
kerncompd:
	@echo -e "\nCommencing debug kernel compilation.."
	@sync
	@python3 ../scripts/make_kernel_debug.py
ctest:
	@echo -e "\nCommencing kernel compile test\nNote: This does not update any board files."
	@python3 ../scripts/make_kernel_test.py
connection:
	@echo -n "Ensuring GNU/Screen is installed.."
	@command -v screen >/dev/null && echo "Found" || (echo -e "Not found\nInstalling.." && ./scripts/installscreen.sh)
	@echo -n "Ensuring user is in dialout group.."
	@../scripts/groupadd.sh
	@echo -e "\nRunning screen connection.."
	@../scripts/screenningg.sh
blacktest:
	@echo -n "Commencing black compatibility test.."
	@command -v black >/dev/null && echo -e "Found black\n" || (echo -e "Not found\nInstalling.." && ./scripts/installblack.sh)
	@black --check .
	@../scripts/returncheck.sh
ccon:
	@echo -n "Ensuring GNU/Screen is installed.."
	@command -v screen >/dev/null && echo "Found" || (echo -e "Not found\nInstalling.." && ./scripts/installscreen.sh)
	@echo -n "Ensuring user is in dialout group.."
	@../scripts/groupadd.sh
	@echo "Installing ccon to the machine.."
	@python3 ../scripts/ccon.py
	@echo -e "\nDone, now try running ccon\n"
