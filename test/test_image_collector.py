import os

from image_collector import ImageCollector


def test_save_images(tmp_dir: str) -> None:
    filename = 'image_{i:02}.jpg'
    ImageCollector().save_images(tmp_dir, filename)
    filepath = os.path.join(tmp_dir, filename)
    for i in range(1, 25):
        assert os.path.exists(filepath.format(i=i))
