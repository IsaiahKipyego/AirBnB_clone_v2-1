#!/usr/bin/python3
"""
sets up server for deployment
"""
from fabric.api import env
from fabric.operations import run, local, put
from fabric.context_managers import settings
from os import path


env.hosts = ["54.227.128.86", "54.237.40.109"]

def do_deploy(archive_path):
    """
    deploys a version of the file to the server
    """
    if not path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        folder = archive_path.replace('versions/', '')
        folder = folder.replace('.tgz', '')
        run("mkdir -p /data/web_static/releases/{}/".format(folder))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(folder, folder))
        run("rm /tmp/{}.tgz".format(folder))
        run("mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}/".format(folder, folder))
        run("rm -rf /data/web_static/releases/{}/web_static".format(folder))
        run("rm -rf /data/web_static/current")
        run("ln -sfn /data/web_static/releases/{}/ /data/web_static/current"
            .format(folder))

    except Exception as e:
        return False
    return True
