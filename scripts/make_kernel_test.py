from os import system, mkdir, listdir, uname

mpyn = f"../scripts/mpy-cross-{uname().machine}"

print(f"\nUsing mpycross: {mpyn}")

print("[1/1] Compiling source files and pin allocation tabs\n")
for filee in listdir():
    if filee.endswith(".py"):
        print(f"-> {filee[:-3]}")
        a = system(f"{mpyn} ./{filee} -s {filee[:-3]} -v -O4 -o /dev/null")
        if a != 0:
            print("Compilation error, exiting")
            exit(1)
        del a

print()
del mpyn
