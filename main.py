from http.server import HTTPServer, BaseHTTPRequestHandler
import os


class Site(BaseHTTPRequestHandler):

    def do_GET(self):

       
        if self.path.startswith("/music"):
            filename = self.path[1:]

             music1.mp3  music50.mp3
            if (
                filename.startswith("music")
                and filename.endswith(".mp3")
            ):
                try:
                    number = int(
                        filename.replace("music", "").replace(".mp3", "")
                    )

                    if number < 1 or number > 50:
                        self.send_error(404)
                        return

                    with open(filename, "rb") as file:
                        music = file.read()

                    self.send_response(200)
                    self.send_header(
                        "Content-Type",
                        "audio/mpeg"
                    )
                    self.send_header(
                        "Content-Length",
                        str(len(music))
                    )
                    self.end_headers()

                    self.wfile.write(music)

                except (FileNotFoundError, ValueError):
                    self.send_error(404, "Music not found")

                return

  
        music_list = ""

        for number in range(1, 2):
            music_list += f"""
            <div class="music">

                <h2>🎵 موزیک {number}</h2>

                <audio controls>
                    <source
                        src="/music{number}.mp3"
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

    <title>TASDIGHI MUSIC</title>

    <style>

        body {{
            margin: 0;
            padding: 40px 20px;

            text-align: center;

            font-family: Tahoma, Arial, sans-serif;

            background-color: #111;
            color: white;
        }}

        .title {{
            font-size: 65px;
            margin-bottom: 35px;
        }}

        .telegram {{
            display: block;

            font-size: 40px;

            color: white;

            text-decoration: none;

            margin-bottom: 80px;
        }}

        .music {{
            max-width: 1000px;

            margin: 0 auto 50px auto;

            padding: 35px;

            background-color: #222;

            border-radius: 25px;
        }}

        .music h2 {{
            font-size: 40px;

            margin-bottom: 30px;
        }}

        audio {{
            width: 100%;
            height: 100px;
        }}

    </style>

</head>

<body>

    <h1 class="title">
        🎵 TASDIGHI MUSIC 🎵
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

</html>
"""

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