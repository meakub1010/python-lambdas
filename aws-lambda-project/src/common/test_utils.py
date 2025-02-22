from common.utils import log_message

def test_log_message(capfd):  # capfd is a pytest fixture to capture print output
    message = "Test message"

    # Call the utility function
    log_message(message)

    # Capture the printed output
    captured = capfd.readouterr()

    # Assert the output contains the expected message
    assert f"[INFO] {message}" in captured.out
