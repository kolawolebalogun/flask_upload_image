import unittest

import io
import re

import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        print("[x] Setting up the test environment")
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def tearDown(self):
        print("[x] Tearing down the test environment")

    # Test to check if file posted is a photo
    def test_post_file_OK(self):
        image = io.BytesIO(b"image_file")
        resp = self.app.post('/', content_type='multipart/form-data', data={"image": (image, 'image.jpg')},
                             follow_redirects=True)
        assert "200 OK" == resp.status

    # Test to check if file posted isn't a photo
    def test_post_file_FAIL(self):
        image = io.BytesIO(b"image_file")
        resp = self.app.post('/', content_type='multipart/form-data', data={"image": (image, 'image.pdf')},
                             follow_redirects=True)
        assert "403 FORBIDDEN" == resp.status

    # Test to check if response body is a photo
    def test_post_file_response_OK(self):
        image = io.BytesIO(b"image_file")
        resp = self.app.post('/', content_type='multipart/form-data', data={"image": (image, 'image.jpg')},
                             follow_redirects=True)
        assert resp.data == b"image_file"
        assert resp.headers["Content-Type"] == "image/jpg"


if __name__ == "__main__":
    unittest.main()
