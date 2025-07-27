from django.core.management.base import BaseCommand
from django.conf import settings
from helpers.downloaders import download_files_to_local


STATICFILES_VENDOR_DIR = getattr(settings, 'STATICFILES_VENDOR_DIR')
STATIC_VENDOR_RESOURCES = {
    'flowbite.min.js': 'https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js',
    'flowbite.min.css': 'https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.css'
}


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Downloading static files...")
        completed_urls = []
        for filename, url in STATIC_VENDOR_RESOURCES.items():
            is_downloaded = download_files_to_local(url, STATICFILES_VENDOR_DIR / filename)
            if is_downloaded:
                completed_urls.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f'file {filename} not downloaded')
                )
            
        if (set(completed_urls) == set(STATIC_VENDOR_RESOURCES.values())):
            self.stdout.write(
                self.style.SUCCESS("vendor files downloaded successfully.")
            )