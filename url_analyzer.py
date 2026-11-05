# Program to display the components of a URL

from urllib.parse import urlsplit, parse_qsl

url = input("Enter a URL: ").strip()

try:
    parts = urlsplit(url)

    if parts.scheme not in ("http", "https") or not parts.hostname:
        print("Please enter a valid HTTP or HTTPS URL.")
    else:
        print("Scheme:", parts.scheme)
        print("Hostname:", parts.hostname)
        print("Port:", parts.port if parts.port is not None else "Default")
        print("Path:", parts.path if parts.path else "/")
        print("Query parameters:")

        parameters = parse_qsl(parts.query)
        if parameters:
            for key, value in parameters:
                print(f"  {key}: {value}")
        else:
            print("  None")

        if parts.username or parts.password:
            print("Warning: URL contains embedded user information.")

except ValueError:
    print("The URL contains an invalid port or format.")
