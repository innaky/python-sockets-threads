# python-sockets-threads
Generic and practic examples for python with sockets and threads

## socket_with_http.py
### usage
For usage open the browser and write 127.0.0.1:8001, with this request the server send the string "hell-o", but if you send 127.0.0.1:8001/?foo/4, the server send 24, this is the factorial of 4. 

### Explanation
The number 4 is an example you can change this for any number and you can change "/?foo" for any other path, this is only an example over http and using a function to process the input. You can use any other function, capture the input and send the result.

If you have a LAN you can executed the server in a machine and open the explorer in other, but the input is the ip number of the server not 127.0.0.1

Happy Hacking 
