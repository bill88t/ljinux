global sdcard_fs
try:
    if not sdcard_fs:
        remount("/", False)
    src = ljinux.based.fn.betterpath(ljinux.based.user_vars["argj"].split()[1])
    srcisd = ljinux.based.fn.isdir(src)
    dst = ljinux.based.fn.betterpath(ljinux.based.user_vars["argj"].split()[2])
    dstisd = ljinux.based.fn.isdir(dst)

    if srcisd == 2 or (dstisd == 2 and dst.endswith("/")):
        raise OSError
    elif srcisd == 0 and dstisd in [0, 2]:  # both files / dst non existent
        with open(src, "rb") as srcf:
            srcd = srcf.read()
            with open(dst, "wb") as dstf:
                dstf.write(srcd)
            del srcd
    elif srcisd == 1:
        if dstisd == 2:
            ljinux.based.user_vars["argj"] = f"mkdir {dst}"
            ljinux.based.command.fpexecc([None, "-n", "/bin/mkdir.py"])
            if not sdcard_fs:
                remount("/", False)
            gc.collect()
            gc.collect()
            for i in listdir(src):
                print(f"{src}/{i} -> {dst}/{i}")
                if ljinux.based.fn.isdir(f"{src}/{i}"):
                    ljinux.based.user_vars["argj"] = f"cp {src}/{i} {dst}/{i}"
                    ljinux.based.command.fpexecc([None, "-n", "/bin/cp.py"])
                    if not sdcard_fs:
                        remount("/", False)
                    src = src[: src.rfind("/")]
                    dst = dst[: dst.rfind("/")]
                    srcisd = ljinux.based.fn.isdir(src)
                    dstisd = ljinux.based.fn.isdir(dst)
                else:
                    with open(f"{src}/{i}", "rb") as srcf:
                        srcd = srcf.read()
                        with open(f"{dst}/{i}", "wb") as dstf:
                            dstf.write(srcd)
                gc.collect()
                gc.collect()

    if not sdcard_fs:
        remount("/", True)
    ljinux.based.user_vars["return"] = "0"

except IndexError:
    ljinux.based.error(1)
    ljinux.based.user_vars["return"] = "1"
    if not sdcard_fs:
        remount("/", True)

except RuntimeError:
    ljinux.based.error(7)
    ljinux.based.user_vars["return"] = "1"
