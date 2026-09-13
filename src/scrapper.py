import os
import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = (
    "https://www.imdb.com/search/title/"
    "?title_type=feature"
    "&release_date=2024-01-01,2024-12-31"
)

OUTPUT_FILE = "data/imdb_movies_2024.csv"


def scrape_batch(start_page, end_page):

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 30)

    try:
        driver.get(BASE_URL)

        # Wait for first set of movies
        wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")
            )
        )

        for page in range(1, end_page + 1):

            print(f"\nCurrently processing page {page}...")

            # Get all currently loaded movie cards
            cards = driver.find_elements(
                By.CSS_SELECTOR,
                "li.ipc-metadata-list-summary-item"
            )

            # print(f"Movies currently loaded: {len(cards)}")

            if page >= start_page:

                start_index = (page - 1) * 50
                end_index = page * 50
                page_cards = cards[start_index:end_index]

                page_data = []

                for card in page_cards:
                    # Movie title
                    try:
                        title = card.find_element(
                            By.CSS_SELECTOR,
                            "h4.ipc-title__text"
                        ).text.strip()
                    except Exception:
                        title = ""

                    # Storyline / description
                    try:
                        description = card.find_element(
                            By.CSS_SELECTOR,
                            "div.ipc-html-content-inner-div"
                        ).text.strip()
                    except Exception:
                        description = ""

                    if title:
                        # Remove ranking number if present
                        if ". " in title:
                            title = title.split(". ", 1)[1]

                        page_data.append({
                            "Movie Name": title,
                            "Storyline": description
                        })

                page_df = pd.DataFrame(page_data)

                if os.path.exists(OUTPUT_FILE):
                    page_df.to_csv(
                        OUTPUT_FILE,
                        mode="a",
                        header=False,
                        index=False
                    )
                    print(f"Page {page} appended ({len(page_df)} movies)")
                else:
                    page_df.to_csv(OUTPUT_FILE, index=False)
                    print(f"Page {page} saved ({len(page_df)} movies)")

            if page == end_page:
                break

            # Click "50 more"
            old_count = len(cards)
            more_button = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button.ipc-see-more__button")
                )
            )
            driver.execute_script("arguments[0].click();", more_button)

            # Wait until new movies load
            wait.until(
                lambda d: len(
                    d.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")
                ) > old_count
            )
            time.sleep(2)

    finally:
        driver.quit()

scrape_batch(88, 100)
