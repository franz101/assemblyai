from tube2blog.downloader import Downloader
import os

def test_assembly_downloader():
    url = Downloader()
    assert url is not None
    