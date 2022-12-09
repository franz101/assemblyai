from tube2blog.downloader import Downloader
import os

def test_assembly_downloader():
    d = Downloader()
    url = d()
    assert url is not None
    