from playwright.sync_api import sync_playwright, Page, expect


class Browser():

    def __init__(self):
        # 1. Pornim manual motorul Playwright sincron
        self.playwright = sync_playwright().start()
        # 2. Configurația pentru browser (argumentele --no-sandbox și --disable-dev-shm-usage sunt incluse implicit)
        self.browser = self.playwright.chromium.launch(headless=True)

        # 3. Creăm contextul browserului (echivalentul setărilor de sesiune)
        # viewport=None + args: maximizează fereastra la pornire
        self.context = self.browser.new_context(viewport=None)

        # 4. Creăm pagina principală și o adnotăm cu tipul Page importat de tine
        self.page: Page = self.context.new_page()

        # 5. Echivalentul lui self.driver.implicitly_wait(5)
        self.page.set_default_timeout(5000)


    def close(self):
        # Închidem resursele în ordine inversă, exact ca driver.quit()
        self.browser.close()
        self.playwright.stop()
