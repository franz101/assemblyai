import sys
sys.path.insert(1, "./")
from tube2blog.worker import Worker
w = Worker().start("https://www.youtube.com/watch?v=5GorMC2lPpk")