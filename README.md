### Chunk-loader demo for the Monocle

There is a limitation in [Monocle](https://www.brilliantmonocle.com/) now that does not allow to store files, longer than 128 characters long. 
This demo shows how can you dynamically load a long python file, that was split into small chunks and execute it.
The chunk loading logic is also split into multiple modules (l1, l2, l3) to fit into 128 chars limit.

## Running the demo

Using the VSCode Monocle plugin upload `main.py`, `l1.py`, `l2.py`, `l3.py` and the `chunks` directory to your monocle. 
Possibly you will have to create the `chunks` directory manually and upload the chunk files one by one (for me bulk upload didn't work).
After restarting the Monocle it will execute `main.py` automatically and you will see the `Hello World` message on the screen.

## Using your own file

You can use the `splitter.py` python script to split your own custom code into chunks, to run them on Monocle.
