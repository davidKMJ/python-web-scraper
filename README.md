# python-web-scraper

A Flask web application that aggregates job listings from multiple sources including RemoteOK, We Work Remotely, Berlin Startup Jobs, and Web3 job boards.

## How to Start

### Prerequisites

-   Python 3.11+ installed
-   Pipenv for dependency management
-   Git for version control

### Quick Start

```bash
# Clone the repository
git clone https://github.com/davidKMJ/python-web-scraper.git
cd python-web-scraper

# Install dependencies
pipenv install

# Start the Flask development server
pipenv run python main.py

# Open in browser
# Navigate to http://localhost:5500
```

### Available Scripts

-   `pipenv run python main.py` - Start Flask development server
-   `pipenv install` - Install project dependencies
-   `pipenv shell` - Activate virtual environment

---

## Project Structure

```
python-web-scraper/
├── main.py                       # Flask web application entry point
├── file.py                       # CSV export functionality
├── Pipfile                       # Pipenv dependencies configuration
├── Pipfile.lock                  # Locked dependency versions
├── extractors/                   # Job scraping modules
│   ├── job.py                    # Job data model class
│   ├── berlinstartupjobs.py     # Berlin Startup Jobs scraper
│   ├── remoteok.py              # RemoteOK scraper
│   ├── weworkremotely.py        # We Work Remotely scraper
│   └── web3.py                  # Web3 jobs scraper
├── templates/                    # HTML templates
│   ├── home.html                # Search form interface
│   └── search.html              # Job results display
├── practice/                     # Learning and practice files
│   ├── crawling.py              # Web crawling practice
│   └── oop.py                   # Object-oriented programming practice
└── README.md                    # Project documentation
```

### Key Features

1. **Multi-source job aggregation** - Scrapes from 4 different job boards
2. **Web interface** - Flask-based search and results display
3. **CSV export** - Download job listings as CSV files
4. **Caching** - In-memory caching to avoid repeated scraping
5. **Modular design** - Separate extractor modules for each job source

### Technical Stack

-   **Flask** - Web framework
-   **BeautifulSoup4** - HTML parsing
-   **Requests** - HTTP client
-   **Playwright** - Browser automation (for dynamic content)
-   **Pipenv** - Dependency management
