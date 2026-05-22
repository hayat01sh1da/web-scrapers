import os
import sys

from invoke import Context, task

_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_ROOT, 'src'))


@task
def collect_images(c: Context) -> None:
    """Collect and save images by web scraping"""
    from image_collector import ImageCollector

    image_collector = ImageCollector()
    dirname = os.path.join('.', 'imgs')
    filename = 'image_{i:02}.jpg'
    image_collector.save_images(dirname, filename)


@task
def collect_info(c: Context) -> None:
    """Collect tour review info and save as CSV"""
    from info_collector import InfoCollector

    info_collector = InfoCollector()
    dirname = os.path.join('.', 'csv')
    filename = 'tour_reviews.csv'
    for _ in range(1, 4):
        info_collector.save_csv(dirname, filename)


@task
def run_pillow_sample(c: Context) -> None:
    """Resize a sample image with Pillow"""
    from pillow_sample import PillowSample

    dirname = os.path.join('.', 'imgs')
    original_filename = 'bird.jpg'
    resized_filename = 'bird_resized.jpg'
    original_filepath = os.path.join(dirname, original_filename)
    pillow_sample = PillowSample(original_filepath)
    pillow_sample.resize_image((1024, 768))
    pillow_sample.save_image(dirname, resized_filename)


@task
def extract_text(c: Context) -> None:
    """Extract lecturer info text and save as CSV"""
    from text_extractor import TextExtractor

    text_extractor = TextExtractor()
    text_extractor.login('imanishi', 'kohei')
    dirname = os.path.join('.', 'csv')
    filename = 'lecturer_info.csv'
    text_extractor.save_csv(dirname, filename)


@task(default=True)
def test(c: Context) -> None:
    """Run all tests"""
    c.run('pytest .')
