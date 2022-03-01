"""Testing the About Page"""

def test_about_page(client):
    """This makes the about page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b'Arcu felis bibendum ut tristique et egestas quis ipsum.' in response.data
