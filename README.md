Initially, just a python script for scraping my nginx logs.  

Later I might add in some other one off scripts, experimental scripts where I am just testing stuff out, etc.


#### Regarding the access log scraping file:

The original files are on my ubuntu server, and I was having trouble copying them to my computer due to permissions errors.

I created a sample file here, to test the script (rather than having to write it with nano on the server).

I copied an access file into a text file (.txt format), and compressed it with gzip (Note: the -k tells gzip to keep the original file):

$ gzip -k exampleFile.txt

