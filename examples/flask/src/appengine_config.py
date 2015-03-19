import os
import sys

# Inject 3rd party libraries into sys.path
src_path = os.path.dirname(__file__)
distlib_path = os.path.join(src_path, 'libs')
if src_path not in sys.path:
    sys.path.insert(0, src_path)
if distlib_path not in sys.path:
    sys.path.insert(0, distlib_path)
