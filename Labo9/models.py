from rich.console import Console
from rich.table import Table

from checks import Check


class Server:
    def __init__(self, naam, check_type, target, interval):
        self.naam = naam
        self.target = target
        self.type = check_type
        self.interval = interval
        self.check = Check.create_check(check_type, target)


class ServerMonitor:
    def __init__(self, console: Console):
        self.servers = []
        self.console = console

    def add_server(self):
        naam = self.console.input("Naam: ")
        check_type = self.console.input("Type: ")
        target = self.console.input("Target: ")
        interval = int(self.console.input("Interval: "))

        try:
            server = Server(naam, check_type, target, interval)
        except ValueError as e:
            self.console.print(f"Error: {e}")
        else:
            if server not in self.servers:
                self.servers.append(server)
            self.console.print("Server toegevoegd.")

    def remove_server(self):
        self.print_servers(True)
        id = int(self.console.input("Keuze (ID): "))

        try:
            server = self.servers[id - 1]
        except IndexError:
            self.console.print("Server niet in lijst.")
        else:
            self.servers.remove(server)
            self.console.print("Server verwijderd.")

    def print_servers(self, with_id=False):
        table = Table()
        if with_id:
            table.add_column("ID")
        table.add_column("Naam")
        table.add_column("Type")
        table.add_column("Target")

        if len(self.servers) > 0:
            for index, server in enumerate(self.servers, start=1):
                if with_id:
                    table.add_row(f"{index}", server.naam, server.type, server.target)
                else:
                    table.add_row(server.naam, server.type, server.target)
            self.console.print(table)
        else:
            self.console.print("Geen servers.")

    def run_checks(self):
        for server in self.servers:
            server.check.execute()

        # TODO: Print check resultaten

        # TODO: Genereer HTML rapport
