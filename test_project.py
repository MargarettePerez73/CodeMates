import pytest
from unittest.mock import Mock, patch
import csv
from io import StringIO
from project import QuizApp

@pytest.fixture
def app_instance():
    with patch("project.tk.Tk", Mock()):
        root = Mock()
        app = QuizApp(root)
        return app

def test_load_questions_from_csv(app_instance, mock_questions_csv):
    # Simulate reading CSV questions
    with patch("builtins.open", mock_open(read_data=mock_questions_csv)) as mock_file:
        app_instance.load_questions_from_csv("mock_questions.csv")

    assert len(app_instance.questions) == 2
    assert app_instance.questions[0]["question"] == "What is 2+2?"
    assert app_instance.questions[1]["options"] == ["Berlin", "Madrid", "Paris", "London"]

def test_is_name_taken(app_instance):
    app_instance.leaderboard = [
        {"name": "Player1", "score": 10},
        {"name": "Player2", "score": 8},
    ]
    assert app_instance.is_name_taken("Player1") is True
    assert app_instance.is_name_taken("Player3") is False

def test_update_leaderboard(app_instance):
    app_instance.leaderboard = [
        {"name": "Player1", "score": 10},
        {"name": "Player2", "score": 8},
    ]

    app_instance.update_leaderboard("Player3", 12)

    assert len(app_instance.leaderboard) == 3
    assert app_instance.leaderboard[0]["name"] == "Player3"
    assert app_instance.leaderboard[0]["score"] == 12

def test_save_leaderboard(app_instance):
    app_instance.leaderboard = [
        {"name": "Player1", "score": 10},
        {"name": "Player2", "score": 8},
    ]

    with patch("builtins.open", mock_open()) as mock_file:
        app_instance.save_leaderboard()

        mock_file.assert_called_once_with("leaderboard.csv", mode="w", newline="", encoding="utf-8")
        handle = mock_file()
        handle.write.assert_any_call("name,score\n")
        handle.write.assert_any_call("Player1,10\n")
        handle.write.assert_any_call("Player2,8\n")

def test_load_leaderboard(app_instance):
    mock_csv = """name,score
    Player1,10
    Player2,8
    """
    with patch("builtins.open", mock_open(read_data=mock_csv)) as mock_file:
        app_instance.load_leaderboard()

    assert len(app_instance.leaderboard) == 2
    assert app_instance.leaderboard[0]["name"] == "Player1"
    assert app_instance.leaderboard[1]["score"] == 8

@patch("project.messagebox.showinfo")
def test_end_quiz(mock_messagebox, app_instance):
    app_instance.player_name = "PlayerTest"
    app_instance.total_score = 8
    app_instance.questions = ["Question1", "Question2"]

    app_instance.end_quiz()

    mock_messagebox.assert_called_once_with("Quiz Finished", "PlayerTest, your total score: 8/2")