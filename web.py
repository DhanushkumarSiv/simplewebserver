from http.server import HTTPServer, BaseHTTPRequestHand
<html>
    <title>
        Thalapathy web
    </title>
        <h1 align="center">Device Specifications  (DHANUSH KUMAR   [24901013])  
            <ol type="1" start="1">
                <li align="left">   Device Name    :  DhanushPC</li>
                <li align="left">   Processor      :  13th Gen Intel(R) Core(TM) i5-1335U   1.30 GHz</li>
                <li align="left">   Installed RAM  :  16.0 GB (15.7 GB usable)</li>
                <li align="left">   Device ID      :  15EEA3B2-7EF5-4DEC-903D-577382C3C005</li>
                <li align="left">   Product ID     :  00342-42708-92761-AAOEM</li>
                <li align="left">   System Type    :  64-bit operating system, x64-based processor</li>
                <li align="left">   Pen and Touch  :  No pen or touch input is available for this display</li>
            </ol>    
            </h1>



        
        </h1>
        
    </body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()