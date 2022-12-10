import sys
sys.path.insert(1, "./")
from tube2blog.worker import Woker
w = Woker().start("https://www.youtube.com/watch?v=5GorMC2lPpk")