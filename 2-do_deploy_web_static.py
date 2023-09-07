#!/usr/bin/python3
"""
sets up server for deployment
"""
from fabric.api import env, run, put
from os.path import exists, isdir
from fabric.operations import local
from datetime import datetime
env.hosts = ["54.227.128.86", "54.237.40.109"]


def do_pack():
    """
    compresses a version of a file and creates a directory if missing
    """
    # check if directory is present
    if not isdir("versions"):
        if local("mkdir -p versions").failed:
            return None
    # create the name of file with current time
    location = 'versions/web_static_{}.tgz'.format(
        datetime.utcnow().strftime("%Y%m%d%H%M%S"))

    # compress the file
    if local("tar -cvzf {} web_static".format(location)).failed:
        return None
    return location


def do_deploy(archive_path):
    """
    deploys a version of the file to the server
    """
    if not exists(archive_path):
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True
