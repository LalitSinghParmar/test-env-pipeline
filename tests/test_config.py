import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from app import config

def test_get_env():
    assert config.get_env() in ["production", "staging"]