"""Testing the homepage"""


def test_home_page(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    # Check name in header
    assert b'<span class="fs-4">Prem Kumar\'s Bootstrap Page</span>' in response.data
    # Check Navigation Links
    assert b'<li class="nav-item"><a href="/" class="nav-link active" ' \
           b'aria-current="page">Home</a></li>'\
           in response.data
    assert b'<li class="nav-item"><a href="/about" class="nav-link">About</a></li>' in response.data
    # Check content
    assert b'<h1>Facilisi Morbi.</h1>' in response.data
