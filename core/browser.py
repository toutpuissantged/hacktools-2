import asyncio
from pyppeteer import launch
import sys

class Browser():
    def __init__(self) -> None:
        pass

    @staticmethod
    def pup():
        async def main():
            url = sys.argv[1]
            browser = await launch()
            page = await browser.newPage()
            await page.goto(url)
            await page.screenshot({'path': 'example.png'})
            await browser.close()
        asyncio.get_event_loop().run_until_complete(main())
