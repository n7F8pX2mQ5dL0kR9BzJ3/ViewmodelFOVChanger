from src.ReadWriteMemory import ReadWriteMemory
from src.colors import Colors
from os import system


def hr(char='━', length=None):
    try:
        if length is None:
            import shutil
            length = shutil.get_terminal_size().columns
    except Exception:
        length = 80  # Fallback
    print(char * length)

def clear():
    system('cls')

def main() -> None:
    c = Colors()
    banner = f"""
{c.cyan} __          __                            ______ ______      __
 \\ \\        / /                           |  ____/ __ \\ \\    / /
  \\ \\  /\\  / /__  __ _ _ __   ___  _ __   | |__ | |  | \\ \\  / / 
   \\ \\/  \\/ / _ \\/ _` | '_ \\ / _ \\| '_ \\  |  __|| |  | |\\ \\/ /  
    \\  /\\  /  __/ (_| | |_) | (_) | | | | | |   | |__| | \\  /   
     \\/  \\/ \\___|\\__,_| .__/ \\___/|_| |_| |_|    \\____/   \\/    
                      | |                                       
                      |_|                                       
{c.reset}{c.green}By: {c.italic}Spunky ♥{c.reset}"""


    VIEWMODEL_FOV_OFFSET = int("623AC4", 16)
    rwm = ReadWriteMemory()
    # rwm.set_privileges()
    process = rwm.get_process_by_name("hl2mp_win64.exe")
    process.open()
    modules = process.get_modules()

    client_dll_base_address = None
    for module in modules:
        if "client.dll" in module[1]:
            client_dll_base_address = module[0]
    
    if not client_dll_base_address:
        print("Could not find client.dll offset.")
        return

    while True:
        clear()
        print(banner)
        hr()
        viewmodel_fov: float = float(input("Enter Viewmodel FOV > "))
        process.writeFloat(client_dll_base_address + VIEWMODEL_FOV_OFFSET, viewmodel_fov)
        clear()

if __name__ == "__main__":
    main()