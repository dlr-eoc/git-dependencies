Fetch external dependencies from their git repositories and integrate
them in the working tree.

Installation
============

    python setup.py install

Usage
=====

See "git-dependencies -h":


    git dependencies -h

    usage: git-dependencies [-h] command [subcommand [subcommand ...]]

    Fetch external dependencies from their git repositories and integrate
    them in the working tree.

    Available commands are:
        
        refresh:  download all dependencies. When dependencies have been 
                  downloaded before, their repositories will be updated
                  from remote
        init:     alias for 'refresh'
        help:     print the help text and exit
        status:   show the git status all dependencies. 
        version:  Display the version number of git-dependencies
        for-each: Execute a git command in each of the repositories of 
                  the dependencies.
                  When passing options to git using this function you 
                  need to seperate the command from the subcommand using
                  "--", so git-dependencies does not interpret the options
                  itself. Example:

                      git dependencies for-each -- remote -v


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
            use_target_as_remote_path: no

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

    The remotes.?.use_target_as_remote_path directive is useful when cloning
    a directory already managed by git-dependencies. When the directive is
    true, the target of a dependency will be used as the remote_path setting.
    This directive defaults to False and is optional.

    positional arguments:
      command     The command to execute. Available are status, init, help,
                  refresh
      subcommand  Command-specific subcommands

    optional arguments:
      -h, --help  show this help message and exit


This tool is regonized by git itself as a subcommand and may also be called
using git:
