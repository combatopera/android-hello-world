# android-hello-world
Example project for [Cowpox](https://github.com/combatopera/Cowpox)
## Quick start
* Install [Docker](https://docs.docker.com/get-docker/) for your platform
  * Follow the installation instructions up until you can `docker run hello-world`
* Get [Python 3](https://www.python.org/) if you don't already have it
  * Scripts assume at least Python 3.6
* If you're reading this on GitHub, now is the time to clone the repository
* Then `python3 make.py` will make an APK (this will take a while)
  * About a gigabyte of disk space is needed for the Cowpox image that this downloads from Docker Hub
* You can also `python3 launch.py` to test locally without building an APK
