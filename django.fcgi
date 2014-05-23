#!/www/virtual/g/gore/python26
import sys, os

# Add a custom Python path.
sys.path.insert(0, "/www/virtual/g/gore/")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "bombardier.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(["method=threaded", "maxspare=1", "maxchildren=1", "daemonize=false"])

