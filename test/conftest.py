import pytest
import glob
import os
import shutil
import sys
from collections.abc import Iterator

sys.path.append('./src')
sys.path.append('./src/lib')


@pytest.fixture(autouse=True)
def __cleanup_caches__() -> Iterator[None]:
    before = set(
        glob.glob(
            os.path.join(
                '.',
                '**',
                '__pycache__'),
            recursive=True))
    yield
    for pycache in before:
        if os.path.exists(pycache):
            shutil.rmtree(pycache)


@pytest.fixture
def tmp_dir() -> Iterator[str]:
    dirname = os.path.join('.', 'test', 'tmp')
    os.makedirs(dirname, exist_ok=True)
    yield dirname
    if os.path.exists(dirname):
        shutil.rmtree(dirname)
