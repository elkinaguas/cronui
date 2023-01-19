from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Header, Footer, Static, ListView, ListItem, Label

class crons(Static):
    def compose(self) -> ComposeResult:
        options = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
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