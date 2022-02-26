# uploading_platform
This is a very simple flask app that allows you to upload your files, I needed this app multple time when I have a machine that don't have the permission to open an http server to serve files, or in the case that it doesn't the permission to touch ports. To resolve this problem, I host this application in my machine then go to the other one and upload the files, without any serving or opening http server.

Here's the `curl` command to upload multiple files:
```bash
curl -X POST http://127.0.0.1:5000/upload -F 'files=@file1' -F 'files=@file2'
```
