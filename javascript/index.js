const puppeteer = require('puppeteer')

const main = async () => {
    const url = process.argv[2]
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(url)
    await page.waitForResponse()
    await page.screenshot({ path: 'example.png' });
    await browser.close();
}

main()
