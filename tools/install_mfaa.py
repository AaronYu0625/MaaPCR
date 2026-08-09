import shutil
import sys
from pathlib import Path

try:
    import jsonc
except ModuleNotFoundError as e:
    raise ImportError(
        "Missing dependency 'json-with-comments' (imported as 'jsonc').\n"
        f"Install it with:\n  {sys.executable} -m pip install json-with-comments\n"
    ) from e

working_dir = Path(__file__).parent.parent.resolve()
install_path = working_dir / Path("install-mfaa")
version = len(sys.argv) > 1 and sys.argv[1] or "v0.0.1"

if len(sys.argv) < 4:
    print("Usage: python install_mfaa.py <version> <os> <arch>")
    sys.exit(1)

os_name = sys.argv[2]
arch = sys.argv[3]


def get_dotnet_platform_tag():
    if os_name == "win" and arch == "x86_64":
        return "win-x64"
    elif os_name == "win" and arch == "aarch64":
        return "win-arm64"
    elif os_name == "macos" and arch == "x86_64":
        return "osx-x64"
    elif os_name == "macos" and arch == "aarch64":
        return "osx-arm64"
    elif os_name == "linux" and arch == "x86_64":
        return "linux-x64"
    elif os_name == "linux" and arch == "aarch64":
        return "linux-arm64"
    sys.exit(1)


def install_mfaa_ui():
    mfaa_src = working_dir / "MFAA"
    if not mfaa_src.exists():
        print("MFAA folder not found!")
        sys.exit(1)

    # 複製 MFAA UI 檔案到 install-mfaa
    shutil.copytree(mfaa_src, install_path, dirs_exist_ok=True)

    # 讀取 interface.json 的名稱並為 exe 改名
    interface_file = working_dir / "assets" / "interface.json"
    if interface_file.exists():
        with open(interface_file, "r", encoding="utf-8") as f:
            data = jsonc.load(f)
            project_name = data.get("name", "MaaProject")

        exe_ext = ".exe" if os_name == "win" else ""
        mfa_exe = install_path / f"MFAAvalonia{exe_ext}"
        target_exe = install_path / f"{project_name}{exe_ext}"

        if mfa_exe.exists():
            if target_exe.exists():
                target_exe.unlink()
            mfa_exe.rename(target_exe)


def install_deps():
    if not (working_dir / "deps" / "bin").exists():
        sys.exit(1)

    if os_name == "android":
        shutil.copytree(
            working_dir / "deps" / "bin", install_path, dirs_exist_ok=True
        )
    else:
        shutil.copytree(
            working_dir / "deps" / "bin",
            install_path / "runtimes" / get_dotnet_platform_tag() / "native",
            ignore=shutil.ignore_patterns(
                "*MaaDbgControlUnit*",
                "*MaaThriftControlUnit*",
                "*MaaRpc*",
                "*MaaHttp*",
                "plugins",
                "*.node",
                "*MaaPiCli*",
            ),
            dirs_exist_ok=True,
        )
        shutil.copytree(
            working_dir / "deps" / "share" / "MaaAgentBinary",
            install_path / "libs" / "MaaAgentBinary",
            dirs_exist_ok=True,
        )
        shutil.copytree(
            working_dir / "deps" / "bin" / "plugins",
            install_path / "plugins" / get_dotnet_platform_tag(),
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
    install_mfaa_ui()
    install_deps()
    install_resource()
    install_chores()
    print(f"MFAA Install to {install_path} successfully.")