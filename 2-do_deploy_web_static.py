#!/usr/bin/python3
"""
sets up server for deployment
"""
from fabric.api import env
from fabric.operations import run, put
from os.path import exists
env.hosts = ["54.227.128.86", "54.237.40.109"]


def do_deploy(archive_path):
    """
    deploys a version of the file to the server
    """
    if not exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        name = archive_path.split("/")[-1]
        no_ext = name.split('.')[0]
        path = "/data/web_static/releases/"
        # upload the contents
        put(archive_path, '/tmp/')
        # setup the directories
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(name, path, no_ext))
        run('rm /tmp/{}'.format(name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True

    except Exception as e:
        return False
