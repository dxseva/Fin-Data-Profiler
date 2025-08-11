import sys
import httpx

def main():
    if len(sys.argv) != 3:
        raise Exception("Usage: python3 financial_enhanced.py TICKER 'Field Name'")

    ticker = sys.argv[1]
    field_name = sys.argv[2]

    url = f"https://query1.finance.yahoo.com/v10/finance/quoteSummary/{ticker}?modules=incomeStatementHistory"

    try:
        response = httpx.get(url, timeout=10)
        response.raise_for_status()
    except httpx.RequestError as e:
        raise Exception(f"HTTP request failed: {e}")
    except httpx.HTTPStatusError as e:
        raise Exception(f"Non-200 response: {e}")

    try:
        data = response.json()
        income_data = data["quoteSummary"]["result"][0]["incomeStatementHistory"]["incomeStatementHistory"]

        for entry in income_data:
            if field_name in entry:
                value = entry[field_name]["raw"]
                print((field_name, value))
                return

        raise Exception(f"Field '{field_name}' not found in income statement.")
    except Exception as e:
        raise Exception(f"Failed to parse response: {e}")

if __name__ == "__main__":
    main()
