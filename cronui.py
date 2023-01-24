from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Header, Footer, Static, ListView, ListItem, Label
from tools.cronmod import get_cron_jobs


class crons(Static):
    def __init__(self):
        self.crons = get_cron_jobs()
        super().__init__()

    def compose(self) -> ComposeResult:
        options = [f"{self.crons[cron]['next_exec']} | {self.crons[cron]['command']}" for cron in self.crons]
        arguments = [ListItem(Label(option)) for option in options]

        yield ListView(
            *arguments
        )

class buttons(Static):
    def compose(self) -> ComposeResult:
        yield Button("Delete", id="delete", variant="error")
        yield Button("New", id="new", variant="success")


class CronUi(App):
    """A Textual app to manage stopwatches."""

    CSS_PATH = "cron_ui.css"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield Container(crons())
        yield Container(buttons())
        

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = CronUi()
    app.run()