from datetime import datetime
from json import dump, load

from jinja2 import Environment, FileSystemLoader
from rich.console import Console
from rich.progress import BarColumn, Progress, TaskProgressColumn, TextColumn
from rich.table import Table

from checks import Check

SERVERS_FILE = "./servers.json"
RESULTS_FILE = "./check_results.json"
REPORT_FILE = "./report.html"
REPORT_TEMPLATE_FILE = "report_template.html.jinja"


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

        try:
            with open(SERVERS_FILE, "r", encoding="utf-8") as f:
                open_file = load(f)
                for server in open_file.get("servers"):
                    s = Server(
                        server.get("naam"),
                        server.get("type"),
                        server.get("target"),
                        server.get("interval"),
                    )
                    self.servers.append(s)
        except FileNotFoundError:
            pass

    def add_server(self, naam, check_type, target, interval):
        try:
            server = Server(naam, check_type, target, interval)
        except ValueError as e:
            self.console.print(f"Error: {e}")
        else:
            if server not in self.servers:
                self.servers.append(server)
                self.console.print("Server toegevoegd.")
            else:
                self.console.print("Server bestaat al.")

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

    def write_file(self):
        s = []
        try:
            with open(SERVERS_FILE, "w", encoding="utf-8") as f:
                for server in self.servers:
                    s.append(
                        {
                            "naam": server.naam,
                            "type": server.type,
                            "target": server.target,
                            "interval": server.interval,
                        }
                    )
                dump({"servers": s}, f, indent=2, ensure_ascii=False)
        except Exception as e:
            self.console.print(f"Error: {e}")

    def run_checks(self):
        progress = Progress(
            TextColumn("{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
        )
        results = []
        with progress:
            for server in progress.track(
                self.servers, description="Uitvoeren checks..."
            ):
                status = server.check.execute()
                results.append(
                    {
                        "server": server.naam,
                        "type": server.type,
                        "success": status,
                        "timestamp": datetime.isoformat(
                            datetime.now(), " ", timespec="seconds"
                        ),
                    }
                )

        table = Table()
        table.add_column("Server")
        table.add_column("Status")
        table.add_column("Timestamp")
        for result in results:
            status = result.get("success")
            s = ""
            if status:
                s = "[green]✓ OK[/green]"
            else:
                s = "[red]✗ Failed[/red]"
            table.add_row(result.get("server"), s, result.get("timestamp"))

        self.console.print(table)

        self.write_results(results)
        self.generate_html_report(results)

    def write_results(self, results):
        try:
            with open(RESULTS_FILE, "w", encoding="utf-8") as f:
                dump({"results": results}, f, indent=2)
        except Exception as e:
            self.console.print(f"Error: {e}")

    def generate_html_report(self, results):
        env = Environment(loader=FileSystemLoader("templates"))
        template = env.get_template(REPORT_TEMPLATE_FILE)
        html = template.render(results=results)
        with open(REPORT_FILE, "w", encoding="utf-8") as f:
            f.write(html)
