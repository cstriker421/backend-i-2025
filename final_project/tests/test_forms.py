import pytest
from books.forms import BookForm

@pytest.mark.parametrize("data,is_valid", [
    ({"title": "Test", "author": "Author", "genre": "Genre", "status": "to_read", "rating": 3}, True),
    ({"title": "", "author": "", "status": "to_read"}, False),
])
def test_book_form_validation(data, is_valid):
    form = BookForm(data=data)
    assert form.is_valid() is is_valid
