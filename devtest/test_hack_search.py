""" Testing the "self.set_attribute()" and "self.set_attributes()" methods
    to modify a Google search into becoming a Bing search.
    set_attribute() -> Modifies the attribute of the first matching element.
    set_attributes() -> Modifies the attribute of all matching elements. """

from seleniumbase import BaseCase


class HackingTests(BaseCase):
    def test_hack_search(self):
        self.open("https://google.com/ncr")
        self.assert_element('input[title="Search"]')
        self.set_attribute('[action="/search"]', "action", "//bing.com/search")
        self.set_attributes('[value="Google Search"]', "value", "Bing Search")
        self.type('input[title="Search"]', "SeleniumBase GitHub Docs Install")
        self.sleep(0.5)
        self.js_click('[value="Bing Search"]')
        self.highlight("h1.b_logo")
        help_docs_install_link = 'a[href*="seleniumbase.io/help_docs/install"]'
        if self.is_element_visible(help_docs_install_link):
            self.highlight_click(help_docs_install_link)
            self.assert_text("Install SeleniumBase", "h1")
            self.click_link_text("GitHub branch")
        self.highlight_click('a[href*="/seleniumbase/SeleniumBase"]')
        self.assert_element('[href="/seleniumbase/SeleniumBase"]')
        self.assert_true("seleniumbase/SeleniumBase" in self.get_current_url())
        self.highlight_click('a[title="examples"]')
        self.assert_text("examples", "strong.final-path")
        self.highlight_click('[title="test_hack_search.py"]')
        self.assert_text("test_hack_search.py", "strong.final-path")
