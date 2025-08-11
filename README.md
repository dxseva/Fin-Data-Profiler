# Fin-Data-Profiler
A Python toolkit for financial data extraction and performance analysis. Combines multiple API approaches for market data collection with comprehensive profiling tools for optimizing data processing workflows.

Key Techniques
The codebase demonstrates several professional development patterns:

Virtual Environment Detection - Runtime environment validation using os.environ.
Subprocess Management - Automated package installation and system command execution.
Web Scraping - Yahoo Finance data extraction with proper User-Agent headers.
Performance Profiling - Multiple profiling strategies using cProfile and pstats.
Test Fixtures - Parameterized testing with pytest fixtures.
Context Managers - Output redirection using contextlib.redirect_stdout.

Technologies

yfinance - Yahoo Finance API wrapper for financial data.
BeautifulSoup4 - HTML parsing and web scraping.
httpx - Modern HTTP client with async support.
termgraph - Command-line data visualization,
pytest - Testing framework with advanced fixtures.


Project Structure
```
src/
├── ex00/
├── ex01/
├── ex02/
├── ex03/
├── ex04/
├── ex05/
└── requirements.txt
```
ex00/ - Virtual environment detection utilities

ex01/ - Terminal-based data visualization with termgraph

ex02/ - Environment management and archiving tools

ex03/ - Web scraping implementation for financial data

ex04/ - Enhanced financial data fetching with multiple API approaches

ex05/ - Streamlined financial analysis with comprehensive testing

The ex04/ directory showcases three different approaches to financial API consumption: traditional web scraping, yfinance integration, and direct API calls using httpx. The profiling scripts demonstrate various performance analysis techniques including cumulative time, call counts, and HTTP request optimization.
