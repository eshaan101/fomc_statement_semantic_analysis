import os
from dotenv import load_dotenv
from statement_getter import get_text_from_one_site

# Load env variables from .env file
load_dotenv()

def main():
    # Retrieve link for past FOMC statement
    try:
        # Get the Slack webhook URL
        TEST_STATEMENT_URL_PREV = os.environ.get("TEST_STATEMENT_URL_PREV", None)
        if TEST_STATEMENT_URL_PREV is None:
            print("TEST_STATEMENT_URL_PREV environment variable is not set")
            return
    except Exception as e:
        print(f"Error in getting TEST_STATEMENT_URL_PREV: {e}")

    # Retrieve link for current FOMC statement
    try:
        # Get the Slack webhook URL
        TEST_STATEMENT_URL_CURR = os.environ.get("TEST_STATEMENT_URL_CURR", None)
        if TEST_STATEMENT_URL_CURR is None:
            print("TEST_STATEMENT_URL_CURR environment variable is not set")
            return
    except Exception as e:
        print(f"Error in getting TEST_STATEMENT_URL_CURR: {e}")

    print('FOMC Statement 1:')
    print()
    print(get_text_from_one_site(TEST_STATEMENT_URL_PREV))

    print()
    print()

    print('FOMC Statement 2:')
    print()
    print(get_text_from_one_site(TEST_STATEMENT_URL_CURR))

main()
