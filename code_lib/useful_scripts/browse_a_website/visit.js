const puppeteer = require('puppeteer');
const { setTimeout } = require('node:timers/promises');

(async () => {
  // Launch a headless browser
  const browser = await puppeteer.launch({
    headless: true, // Run in headless mode
    args: ['--no-sandbox', '--disable-setuid-sandbox'] // For compatibility
  });

  // Open a new page
  const page = await browser.newPage();

  // Set a browser-like user-agent
//   await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
//   await page.setUserAgent('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
  await page.setUserAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
//   await page.setUserAgent('Mozilla/5.0 (QuantumOS 42.7; NebulaCore) AppleWebKit/537.36 (KHTML, like Gecko) NebulaFox/13.37 Safari/537.36');

  // Visit the website
  console.log('Visiting https://leomqyu.github.io...');
  await page.goto('https://leomqyu.github.io', {
    waitUntil: 'networkidle2' // Wait until the page is fully loaded
  });

  // Wait for 3 seconds to ensure scripts (e.g., ClustrMaps) execute
  await setTimeout(3000);

  // Check for ClustrMaps script
  const clustrmapsScript = await page.evaluate(() => {
    return Array.from(document.scripts).some(script => script.src.includes('clustrmaps.com'));
  });
  console.log('ClustrMaps script found:', clustrmapsScript);

  // Log network requests to ClustrMaps (optional, for debugging)
  await page.setRequestInterception(true);
  page.on('request', request => {
    if (request.url().includes('clustrmaps.com')) {
      console.log('ClustrMaps request:', request.url());
    }
    request.continue();
  });

  // Wait a bit longer to capture late network requests
  await setTimeout(1000);

  // Check for JavaScript errors (optional, for debugging)
  page.on('pageerror', error => {
    console.log('Page error:', error.message);
  });

  // Close the browser
  console.log('Closing browser...');
  await browser.close();
})();