from http.server import HTTPServer, BaseHTTPRequestHandler
import os


MUSIC_COUNT = 11


class Site(BaseHTTPRequestHandler):

    def do_GET(self):

       
        if self.path.endswith(".mp3"):

            filename = self.path[1:]

            try:
                with open(filename, "rb") as file:
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

        
        music_list = ""

        for number in range(MUSIC_COUNT):

            
            if number == 0:
                filename = "music.mp3"
            else:
                filename = f"music{number}.mp3"

            music_list += f"""
            <div class="music">

                <h2>🎵 موزیک {number + 1}</h2>

                <audio controls>
                    <source
                        src="/{filename}"
                        type="audio/mpeg"
                    >
                    مرورگر شما از پخش موزیک پشتیبانی نمی‌کند.
                </audio>

            </div>
            """

        
        html = f"""<!DOCTYPE html>

<html lang="fa" dir="rtl">

<head>

    <meta charset="UTF-8">

    <title>AZERI 64</title>

    <style>

        * {{
            box-sizing: border-box;
        }}

        body {{
            margin: 0;
            padding: 50px 20px;

            text-align: center;

            font-family: Tahoma, Arial, sans-serif;

            background-color: #111;
            color: white;
        }}

        .title {{
            font-size: 70px;
            margin-bottom: 35px;
        }}

        .telegram {{
            display: block;

            font-size: 45px;
            font-weight: bold;

            color: white;
            text-decoration: none;

            margin-bottom: 80px;
        }}

        .music {{
            width: 98%;
            max-width: 1400px;

            margin: 0 auto 60px auto;

            padding: 45px 50px;

            background-color: #222;

            border-radius: 30px;
        }}

        .music h2 {{
            font-size: 45px;
            margin: 0 0 35px 0;
        }}

        audio {{
            width: 100%;
            transfrom: caleY(2):
            margin: 40px 0;
        }}

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

    {music_list}

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
