Fetch external dependencies from their git repositories and integrate
them in the working tree.

Installation
============

    python setup.py install

Usage
=====

See "git-dependencies -h":

    usage: git-dependencies [-h] command

    Fetch external dependencies from their git repositories and integrate
    them in the working tree.

    This tool is configured using a configuration file named
    'dependencies.yml' in the root of the directory.

    Available commands are:
        
        refresh: download all dependencies. When dependencies have been 
                 downloaded before, their repositories will be updated
                 from remote

        init:    alias for 'refresh'

    Example dependencies.yml configuration file:

    ----------------------------------------------------------
    ---
    remotes:
        stash:
            url: http://git.ukis.eoc.dlr.de/scm/

    dependencies:
        /configuration:
            remote: stash
            version: master
            remote_path: mri/configuration-djangoapp
        /minimal_rest_webhooks:
            remote: stash
            version: master
            remote_path: mri/minimal_rest_webhooks-djangoapp
    ----------------------------------------------------------

    positional arguments:
      command     The command to execute. Available are init, refresh

    optional arguments:
      -h, --help  show this help message and exit


This tool is regonized by git itself as a subcommand and may also be called
using git:

    git dependencies -h

