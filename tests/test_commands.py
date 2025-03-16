import pytest
from app.commands import CommandHandler, Command

class MockCommand(Command):
    """Mock command for testing."""
    def execute(self):
        return "Mock Command Executed"

@pytest.fixture
def command_handler():
    """Fixture for CommandHandler."""
    return CommandHandler()

def test_register_command(command_handler):
    """Test registering a command."""
    command_handler.register_command("mock", MockCommand())
    assert "mock" in command_handler.commands

def test_execute_command(command_handler):
    """Test executing a registered command."""
    command_handler.register_command("mock", MockCommand())
    assert command_handler.execute_command("mock") == "Mock Command Executed"

def test_execute_unknown_command(command_handler):
    """Test executing an unknown command."""
    assert command_handler.execute_command("unknown") == "Unknown command: unknown"