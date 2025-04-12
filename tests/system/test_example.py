from playwright.sync_api import sync_playwright, expect

def test_slider_updates_displayed_value_after_arrow_keys_pressed_twice():
    # GIVEN a user opens the horizontal slider page
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("http://127.0.0.1/horizontal_slider")

        # WHEN the user focuses the slider and presses the right arrow key twice
        slider = page.get_by_role("slider")
        slider.focus()
        page.keyboard.press("ArrowRight")  # should increase to 0.5
        page.keyboard.press("ArrowRight")  # should increase to 1.0

        # THEN the value next to the slider should update to show 1
        value_display = page.locator("#range")
        expect(value_display).to_have_text("1")

        browser.close()