# Podcast-on-Pages (GitHub Pages)

ابزاری برای استخراج کتاب‌های صوتی از سایت [ایران‌صدا](https://book.iranseda.ir) و تبدیل آن‌ها به فید RSS قابل انتشار روی GitHub Pages.

## ویژگی‌ها
- `scrape_iranseda_env.py` صفحات فهرست کتاب‌ها را پیمایش می‌کند و شناسه و آدرس هر کتاب را در یک فایل CSV ذخیره می‌کند.
- `script_iran_seda_final_STREAM_MERGE_v6_env.py` اطلاعات تکمیلی و لینک فایل‌های MP3 را واکشی می‌کند و یک CSV کامل می‌سازد.
- `tools/csv_to_podcast.py` از CSV نهایی یک فید پادکست (RSS) تولید می‌کند که با GitHub Pages قابل سرو است.

## پیش‌نیازها
- Python 3.10+
- کتابخانه‌های `requests`, `beautifulsoup4`, `pandas`
- اتصال اینترنت برای دریافت داده‌ها

نصب وابستگی‌ها:

```bash
pip install requests beautifulsoup4 pandas
```

## اجرای محلی

### ۱. دریافت فهرست اولیه کتاب‌ها
```bash
export RUN_NAME=myrun
python scrape_iranseda_env.py
```
متغیرهای محیطی مهم:
- `RUN_NAME`: نام اجرا که خروجی‌ها در مسیر `runs/<RUN_NAME>/` ذخیره می‌شوند (پیش‌فرض `latest`)
- `SOURCE_URL`: قالب آدرس صفحات فهرست (در صورت نیاز تغییر دهید)
- `START_PAGE` و `END_PAGE`: محدوده صفحات برای پیمایش

خروجی: `runs/<RUN_NAME>/raw/audiobooks_<RUN_NAME>.csv`

### ۲. واکشی جزئیات و لینک‌های MP3
```bash
export RUN_NAME=myrun
python script_iran_seda_final_STREAM_MERGE_v6_env.py
```
خروجی‌ها:
- `runs/<RUN_NAME>/merged/books_with_attid_<RUN_NAME>.csv`
- `runs/<RUN_NAME>/errors/errors_<RUN_NAME>.csv` (در صورت بروز خطا)

### ۳. ساخت فید پادکست
```bash
python tools/csv_to_podcast.py --csv runs/<RUN_NAME>/merged/books_with_attid_<RUN_NAME>.csv --site https://<username>.github.io/<repo> --run-name <RUN_NAME>
```
گزینه‌های مفید:
- `--channel-title`: عنوان فید
- `--channel-author`: نام تولیدکننده
- `--channel-summary`: توضیح کوتاه

خروجی: `public/feeds/<RUN_NAME>/podcast.xml`

### ۴. انتشار روی GitHub Pages
1. مخزن را در GitHub روی برنچ `main` منتشر کنید.
2. از **Settings → Pages** حالت **Build and deployment: GitHub Actions** را انتخاب کنید.
3. در تب **Actions** ورک‌فلو **Build & Deploy Podcast RSS (GitHub Pages)** را اجرا کنید و مقادیر `run_name`، `source_url`، `start_page` و `end_page` را در صورت نیاز وارد کنید.
4. پس از اتمام اجرا، فید در آدرس زیر در دسترس خواهد بود:

```text
https://<username>.github.io/<repo>/feeds/<RUN_NAME>/podcast.xml
```

## ساختار خروجی‌ها
```text
runs/<RUN_NAME>/raw/audiobooks_<RUN_NAME>.csv
runs/<RUN_NAME>/merged/books_with_attid_<RUN_NAME>.csv
runs/<RUN_NAME>/errors/errors_<RUN_NAME>.csv
public/feeds/<RUN_NAME>/podcast.xml
```

## License
در این مخزن مجوز مشخصی تعریف نشده است.
