# Podcast-on-Pages (GitHub Pages)

ساخت خودکار RSS از CSV و انتشار روی **GitHub Pages**. هر اجرا با `RUN_NAME` جداگانه ساخته می‌شود.

## استفاده
1. این پروژه را روی GitHub آپلود کنید (برنچ `main`).
2. به **Settings → Pages** بروید و حالت **Build and deployment: GitHub Actions** را انتخاب کنید.
3. در تب **Actions**، ورک‌فلو **Build & Deploy Podcast RSS (GitHub Pages)** را **Run workflow** کنید و ورودی‌ها را بدهید:
   - `run_name` (مثلاً `iranseda-1404-05-29`)
   - `source_url` (اختیاری؛ قالب با `{page}`)
   - `start_page` و `end_page` (اختیاری)
4. پس از اجرا، فید در مسیر زیر در دسترس خواهد بود:
   ```
   https://<username>.github.io/<repo>/feeds/<RUN_NAME>/podcast.xml
   ```

## مسیر خروجی‌ها
```
runs/<RUN_NAME>/raw/audiobooks_<RUN_NAME>.csv
runs/<RUN_NAME>/merged/books_with_attid_<RUN_NAME>.csv
runs/<RUN_NAME>/errors/errors_<RUN_NAME>.csv
public/feeds/<RUN_NAME>/podcast.xml
```
