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
    
    Available commands are:
        
        refresh: download all dependencies. When dependencies have been 
                 downloaded before, their repositories will be updated
                 from remote
        init:    alias for 'refresh'
        help:    print the help text and exit
    
    This tool is configured using a configuration file named
    'dependencies.yml' in the root of the directory.
    
    Additional settings from the file named 'dependencies.override.yml'
    placed in the same directory will be read. Settings from this file will
    then be used to override values specified in the 'dependencies.yml' 
    file. The main purpose of this mechanism is changing f.e. URLs during
    deployments without the need to make modification to the version
    controled 'dependencies.yml' file. This override file is optional.
    
    Example dependencies.yml/dependencies.override.yml configuration file:
    
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
      command     The command to execute. Available are init, help, refresh
    
    optional arguments:
      -h, --help  show this help message and exit


This tool is regonized by git itself as a subcommand and may also be called
using git:

    git dependencies -h

