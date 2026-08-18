from http.server import HTTPServer, BaseHTTPRequestHandler
import os


class Site(BaseHTTPRequestHandler):

    def do_GET(self):

        
        if self.path == "/music.mp3":
            try:
                with open("music.mp3", "rb") as file:
                    music = file.read()

                self.send_response(200)
                self.send_header("Content-Type", "audio/mpeg")
                self.send_header(
                    "Content-Length",
                    str(len(music))
                )
                self.end_headers()

                self.wfile.write(music)

            except FileNotFoundError:
                self.send_error(404, "Music not found")

            return

        
        html = """<!DOCTYPE html>
<html lang="fa" dir="rtl">

<head>
    <meta charset="UTF-8">

    <title>AZERI 64</title>

    <style>

        body {
            margin: 0;
            padding: 40px 20px;

            text-align: center;

            font-family: Tahoma, Arial, sans-serif;

            background-color: #111;
            color: white;
        }

        .title {
            font-size: 65px;
            margin-bottom: 35px;
        }

        .telegram {
            display: block;

            font-size: 40px;

            color: white;
            text-decoration: none;

            margin-bottom: 70px;
        }

        .music {
            max-width: 1000px;

            margin: 0 auto;

            padding: 35px;

            background-color: #222;

            border-radius: 25px;
        }

        .music h2 {
            font-size: 40px;
            margin-bottom: 30px;
        }

        audio {
            width: 100%;
            height: 100px;
        }

    </style>

</head>

<body>

    <h1 class="title">
        🎵 اهنگ شاد اذری 🎵
    </h1>

    <a
        class="telegram"
        href="https://t.me/Azeri_64"
        target="_blank"
    >
        📢 ما را در کانال تلگرامی‌مان دنبال کنید 📢
    </a>

    <div class="music">

        <h2>
            🎵 موزیک
        </h2>

        <audio controls>
            <source
                src="/music.mp3"
                type="audio/mpeg"
            >

            مرورگر شما از پخش موزیک پشتیبانی نمی‌کند.

        </audio>

    </div>

</body>

</html>"""

        self.send_response(200)

        self.send_header(
            "Content-Type",
            "text/html; charset=utf-8"
        )

        self.end_headers()

        self.wfile.write(
            html.encode("utf-8")
        )


server = HTTPServer(
    (
        "0.0.0.0",
        int(os.environ.get("PORT", 8000))
    ),
    Site
)

print("سایت اجرا شد")

server.serve_forever()
