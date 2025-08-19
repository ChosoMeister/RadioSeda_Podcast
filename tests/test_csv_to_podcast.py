import sys
import pathlib
import pytest
from unittest.mock import patch, MagicMock

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from tools.csv_to_podcast import build_item


def _mock_response(headers):
    resp = MagicMock()
    resp.headers = headers
    resp.raise_for_status = lambda: None
    return resp


@patch("tools.csv_to_podcast.requests.head")
def test_build_item_includes_content_length(mock_head):
    headers = {
        "Content-Type": "audio/mpeg",
        "Content-Length": "321"
    }
    mock_head.return_value = _mock_response(headers)
    row = {"Book_Title": "T", "FullBook_MP3_URL": "http://example.com/a.mp3"}
    item = build_item(row, "Wed, 01 Jan 2024 00:00:00 +0000")
    assert 'enclosure url="http://example.com/a.mp3" length="321" type="audio/mpeg"' in item


@patch("tools.csv_to_podcast.requests.head")
def test_accept_ranges_not_bytes_is_ignored(mock_head):
    headers = {
        "Content-Type": "audio/mpeg",
        "Accept-Ranges": "none",
        "Content-Length": "77",
    }
    mock_head.return_value = _mock_response(headers)
    row = {"Book_Title": "T", "FullBook_MP3_URL": "http://example.com/a.mp3"}
    item = build_item(row, "Wed, 01 Jan 2024 00:00:00 +0000")
    assert 'length="77"' in item


@patch("tools.csv_to_podcast.requests.head")
def test_build_item_raises_for_missing_content_length(mock_head):
    headers = {"Content-Type": "audio/mpeg"}  # missing Content-Length
    mock_head.return_value = _mock_response(headers)
    row = {"Book_Title": "T", "FullBook_MP3_URL": "http://example.com/a.mp3"}
    with pytest.raises(RuntimeError):
        build_item(row, "Wed, 01 Jan 2024 00:00:00 +0000")
