import sys
from rich.console import Console

from models import ServerMonitor


def show_help():
    print("""
Usage: python monitor.py <command> [options]

Available commands:
    check         Run monitoring of servers
    manage        Manage servers

Available options:
    --help        Show this menu

""")


def main():
    console = Console()
    console.clear()
    monitor = ServerMonitor(console)
    try:
        mode = sys.argv[1]
    except IndexError:
        show_help()
    else:
        match mode:
            case "check":
                console.print("""
╔═══════════════════════════════════════╗
║       SERVER MONITOR - CHECKING       ║
╚═══════════════════════════════════════╝
""")
                monitor.run_checks()
            case "manage":
                while True:
                    console.print("""
╔═══════════════════════════════════════╗
║       SERVER MONITOR - MANAGEMENT     ║
╚═══════════════════════════════════════╝
1. Servers tonen
2. Server toevoegen
3. Server verwijderen
4. Afsluiten
""")
                    choice = int(console.input("Keuze: "))
                    match choice:
                        case 1:
                            monitor.print_servers()
                        case 2:
                            naam = console.input("Naam: ")
                            check_type = console.input("Type: ")
                            target = console.input("Target: ")
                            interval = int(console.input("Interval: "))
                            monitor.add_server(naam, check_type, target, interval)
                            monitor.write_file()
                        case 3:
                            monitor.remove_server()
                            monitor.write_file()
                        case _:
                            break

            case _:
                show_help()


if __name__ == "__main__":
    main()
