import sys
import os

# apne project ka path add karo
path = '/home/premrahi/jarvis_with_genAI'
if path not in sys.path:
    sys.path.append(path)

from app import app as application