"""Testing the About Page"""

def test_about_page(client):
    """This makes the about page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b'Arcu felis bibendum ut tristique et egestas quis ipsum.' in response.data
    assert b'<h6 class="card-title">Sagittis purus</h6>' in response.data
    assert b'<p class="card-text"></p>' in response.data
