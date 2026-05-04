class PlaywrightInventoryPage:
    ADD_TO_CART_BUTTONS = ".inventory_item button"
    CART_BADGE = ".shopping_cart_badge"
    TWITTER_LINK = ".social_twitter a"

    def __init__(self, page):
        self.page = page

    def add_item_by_index(self, index):
        self.page.locator(self.ADD_TO_CART_BUTTONS).nth(index).click()

    def get_cart_badge_text(self):
        return self.page.locator(self.CART_BADGE).inner_text()

    def click_twitter(self):
        return self.page.context.expect_page(lambda p: True, timeout=5000)