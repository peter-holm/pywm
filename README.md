pywm
----
it is a cli tool that can monitor the file system event and execute correspond commands.

there are 4 kind of event can be monitor:
* `-s`: IN_ACCESS
* `-c`: IN_CREATE
* `-d`: IN_DELETE
* `-m`: IN_MODIFY

and `-a` for all of the above.

there are 2 placeholder can be use in the `run` command
* `%file%` : indicate the file that trigger the event.
* `%event%` : indicate what event occur.

basic usage
----------
following is a simple exmaple that watch any file system event under current folder and echo.
```sh
$ pywm -a --run='echo %event%: %file%'
```
