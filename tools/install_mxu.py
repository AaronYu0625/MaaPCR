import shutil
import sys
from pathlib import Path

try:
    import jsonc
except ModuleNotFoundError as e:
    raise ImportError(
        "Missing dependency 'json-with-comments' (imported as 'jsonc').\n"
        f"Install it with:\n  {sys.executable} -m pip install json-with-comments\n"
        "Or add it to your project's requirements."
    ) from e

working_dir = Path(__file__).parent.parent.resolve()
install_path = working_dir / Path("install-mxu")
version = len(sys.argv) > 1 and sys.argv[1] or "v0.0.1"

if len(sys.argv) < 4:
    print("Usage: python install_mxu.py <version> <os> <arch>")
    sys.exit(1)

os_name = sys.argv[2]
arch = sys.argv[3]


def install_mxu_ui():
    mxu_src = working_dir / "MXU"
    if not mxu_src.exists():
        print("MXU folder not found!")
        sys.exit(1)

    # 複製 MXU UI 檔案到 install-mxu
    shutil.copytree(mxu_src, install_path, dirs_exist_ok=True)

    # 讀取 interface.json 的名稱並為 exe 改名
    interface_file = working_dir / "assets" / "interface.json"
    if interface_file.exists():
        with open(interface_file, "r", encoding="utf-8") as f:
            data = jsonc.load(f)
            project_name = data.get("name", "MaaProject")

        exe_ext = ".exe" if os_name == "win" else ""

        # MXU 的主程式可能叫 mxu.exe 或 MXU.exe
        mxu_exe = install_path / f"MXU{exe_ext}"
        if not mxu_exe.exists():
            mxu_exe = install_path / f"mxu{exe_ext}"

        target_exe = install_path / f"{project_name}{exe_ext}"

        if mxu_exe.exists():
            if target_exe.exists():
                target_exe.unlink()
            mxu_exe.rename(target_exe)


def install_deps():
    if not (working_dir / "deps" / "bin").exists():
        print('Please download MaaFramework to "deps" first.')
        sys.exit(1)

    # 直接將 MaaFramework bin 下的所有核心檔案複製到 install-mxu/maafw/
    shutil.copytree(
        working_dir / "deps" / "bin",
        install_path / "maafw",
        dirs_exist_ok=True,
    )


def install_resource():
    shutil.copytree(
        working_dir / "assets" / "resource",
        install_path / "resource",
        dirs_exist_ok=True,
    )
    shutil.copy2(
        working_dir / "assets" / "interface.json",
        install_path,
    )

    with open(install_path / "interface.json", "r", encoding="utf-8") as f:
        interface = jsonc.load(f)

    interface["version"] = version

    with open(install_path / "interface.json", "w", encoding="utf-8") as f:
        jsonc.dump(interface, f, ensure_ascii=False, indent=4)


def install_chores():
    if (working_dir / "README.md").exists():
        shutil.copy2(working_dir / "README.md", install_path)
    if (working_dir / "LICENSE").exists():
        shutil.copy2(working_dir / "LICENSE", install_path)


if __name__ == "__main__":
    install_mxu_ui()
    install_deps()
    install_resource()
    install_chores()
    print(f"MXU Install to {install_path} successfully.")