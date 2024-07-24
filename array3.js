const puppeteer = require('puppeteer');
const seedrandom = require('seedrandom');

const searchQueries = [
  "cidade perdida de ratanaba memes",
  "nove lendas urbanas famosas na Amazônia",
  "proprietário tenta recuperar revólver 357 Magnum",
  "festa das novinhas Vilhena",
  "plantio sem solo primeira produção hidropônica de Rondônia",
  "Desafios e perspectivas da exploração de petróleo na bacia do Amapá",
  "menor morre baleada em cujubim",
  "lenda da mulher árvore",
  "lenda do Uirapuru misticismo folclore",
  "Mini Atlas Marajoara",
  "livro imagens raras da Amazônia",
  "lendas esquecidas do folclore amazonico",
  "quem são as 4 musas no Musas do Teatro Amazonas",
  "meme apocalíptico o que significa e como surgiu",
  "Cinema Brasileiro filmes inspirados nos Estados da Região Norte",
  "Sítio arqueológico Boliviano Puma Punku",
  "cachoeira do rio Mandi Rondônia",
  "cine Super K o último cinema de rua de Boa Vista",
  "\"descubra de quem é o whatsapp\"",
  "\"Conheça a versatilidade culinária da ora-pro-nóbis amazônica\"",
  "\"Memórias Curiosas de Porto Velho\"",
  "\"Como preparar um autêntico Pato no Tucupi\"",
  "\"Café Robusta Amazônico Recebe Título de Patrimônio Cultural em Rondônia\"",
  "mari-mari fruta benefícios"
];
const navigatedUrls = [];

async function main() {
  while (true) {
    const seed = Math.random().toString();
    const rng = seedrandom(seed);
    const randomQueryIndex = Math.floor(rng() * searchQueries.length);
    const randomQuery = searchQueries[randomQueryIndex];

    const browser = await puppeteer.launch({
      headless: "new",
      args: ['--disable-web-security', '--disable-features=IsolateOrigins,site-per-process', '--lang-pt-BR'],
    });

    const page = await browser.newPage();

    const motoG4 = {
      name: 'Moto G4',
      userAgent: 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Mobile Safari/537.36',
      viewport: {
        width: 360,
        height: 640,
        deviceScaleFactor: 2,
        isMobile: true,
        hasTouch: true,
        isLandscape: false
      }
    };

    await page.emulate(motoG4);

    await Promise.all([
      page.waitForNavigation({ waitUntil: 'networkidle0' }),
      page.goto('https://www.google.com.br')
    ]);

    const searchInput = await page.waitForSelector('textarea[name="q"]', { visible: true });

    if (searchInput) {
      console.log('Search field found!');

      for (let char of randomQuery) {
        const delay = Math.floor(Math.random() * (150 - 50 + 1)) + 50;
        await new Promise(resolve => setTimeout(resolve, delay));
        await searchInput.type(char, { delay });
      }

      await searchInput.press('Enter');

      console.log(randomQuery);

      await page.waitForNavigation({ waitUntil: 'networkidle2' });

      const scrollSteps = Math.floor(Math.random() * 5) + 1;

      for (let i = 0; i < scrollSteps; i++) {
        await page.evaluate(() => {
          window.scrollBy(0, window.innerHeight / 4);
        });

        const delay = Math.floor(Math.random() * (1500 - 500 + 1)) + 500;
        await new Promise(resolve => setTimeout(resolve, delay));
      }

      const linkHandler = await page.evaluateHandle(() => {
        const links = document.querySelectorAll('a');
        for (const link of links) {
          if (link.href.includes('madeiraoweb') || link.textContent.includes('madeiraoweb')) {
            return link;
          }
        }
        return null;
      });

      if (linkHandler) {
        const linkUrl = await page.evaluate((link) => link.href, linkHandler);
        console.log('Link found!', linkUrl);
        await page.evaluate((link) => link.click(), linkHandler);

        await page.waitForNavigation({ waitUntil: 'networkidle2' });

        navigatedUrls.push(await page.url());

        const madeiraoscrollSteps = Math.floor(Math.random() * 10) + 1;

        for (let i = 0; i < madeiraoscrollSteps; i++) {
          await page.evaluate(() => {
            window.scrollBy(0, window.innerHeight / 5);
          });

          const delay = Math.floor(Math.random() * (1500 - 500 + 1)) + 500;
          await new Promise(resolve => setTimeout(resolve, delay));
        }

        const tabsToNavigate = Math.floor(Math.random() * 35) + 1;

        for (let i = 0; i < tabsToNavigate; i++) {
          await page.keyboard.press('Tab');

          const delay = Math.floor(Math.random() * (300 - 100 + 1)) + 100;
          await new Promise(resolve => setTimeout(resolve, delay));
        }

        await page.keyboard.press('Enter');
        console.log('Navigated URLs:', navigatedUrls);

        const minDelay = 8000;
        const maxDelay = 31000;
        const delay = Math.floor(Math.random() * (maxDelay - minDelay + 1)) + minDelay;
        await new Promise(resolve => setTimeout(resolve, delay));
      } else {
        console.error(`Link not found for search input: ${randomQuery}`);
      }
    } else {
      console.error('Search field not found');
    }

    await browser.close();
  }
}

main();
