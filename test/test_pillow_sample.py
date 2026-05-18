import os

import pytest

from pillow_sample import PillowSample


@pytest.fixture
def pillow_sample() -> PillowSample:
    return PillowSample('./imgs/bird.jpg')


def test_image_size(pillow_sample: PillowSample) -> None:
    assert pillow_sample.image.size == (1200, 798)


def test_resize_image(pillow_sample: PillowSample) -> None:
    assert pillow_sample.resize_image((1024, 768)) == (1024, 768)


def test_save_image(pillow_sample: PillowSample, tmp_dir: str) -> None:
    pillow_sample.resize_image((1024, 768))
    filename = 'bird_resized.jpg'
    pillow_sample.save_image(tmp_dir, filename)
    assert os.path.exists(os.path.join(tmp_dir, filename))
