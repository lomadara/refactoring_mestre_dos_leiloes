import sys
import os

sys.path.append(os.path.abspath(__file__))
from app import app as application
application.run(debug=False, port=5001)