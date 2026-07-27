import yt_dlp
import os

# ضع رابط فيديو ok.ru هنا
url = "https://ok.ru/video/1234567890"

print("جاري استخراج رابط البث من ok.ru...")

ydl_opts = {
    'quiet': True,
    'skip_download': True,
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        m3u8_url = info.get('url')

    print("\nتم استخراج الرابط بنجاح:")
    print(m3u8_url)

    # فتح الرابط في مشغل فيديو خارجي على أندرويد (مثل VLC)
    os.system(f'am start -a android.intent.action.VIEW -d "{m3u8_url}" -t "video/*"')

except Exception as e:
    print(f"حدث خطأ أثناء الاستخراج: {e}")
  
