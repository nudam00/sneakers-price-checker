# Sneakers Price Checker

> [!WARNING]
> **Legacy project**
>
> This project was built in 2022 as a personal tool for comparing estimated
> sneaker resale payouts. It is no longer maintained and is preserved as a
> record of an early automation project.
>
> Marketplace APIs, pages, authentication flows, and anti-bot protections have
> changed since it was released. The application is therefore unlikely to work
> without updates.
>
> This is a preserved historical snapshot, not an example of how I build
> software today. The code predates my current engineering standards and lacks
> tests, CI/CD, pre-commit checks, type checking, task automation, and modern
> separation of concerns. It is kept public to document the original product
> idea and my development path—not as a recommended implementation.

Companion project: [Sneakers Best Size Checker](https://github.com/nudam00/sneakers-best-size-checker)

## Project context

The tool combined browser automation and HTTP requests with marketplace-specific
adapters, sneaker-size conversion, currency and fee calculations, and Excel
reporting. Given products, sizes, and their acquisition costs, it compared
estimated payouts across StockX, Alias, Restocks, Klekt, WETHENEW, Hypeboost,
and Sneakit and selected the best result.

The repository remains public for historical context.

## Original workflow

1. Add SKUs, US sizes, and net acquisition prices in PLN to sheets in
   `input/stock.xlsx`.
2. Copy `input/settings.example.json` to `input/settings.json` and fill in the
   marketplace credentials and StockX fee. The legacy Alias adapter also
   expects third-party client values listed in `.env.example`.
3. Run `python main.py` and complete any interactive marketplace login or
   anti-bot checks.
4. Review marketplace payouts and the selected best prices in
   `output/prices.xlsx`.

`input/settings.json` and `.env` are ignored by Git because they may contain
credentials. Do not commit populated copies.

## Components

- `main.py` orchestrates spreadsheet input, marketplace checks, and report
  generation.
- `converters/prices.py` applies the historical marketplace fees, currency
  conversion, and best-price comparison.
- `converters/size_converter.py` maps sizes into marketplace-specific formats.
- `sites/` contains the individual marketplace adapters.
- `add.py` contains the historical browser, authentication, exchange-rate, and
  Restocks setup helpers.

## Historical setup

The dependency list is provided for reference and is intentionally unpinned
except for pandas, whose 2.0 release removed an API used by this project:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
playwright install firefox
cp input/settings.example.json input/settings.json
cp .env.example .env
python main.py
```

The Selenium adapter also contains a historical Windows-specific ChromeDriver
path that must be changed for another environment. These steps document the
original shape of the project; they do not guarantee that current marketplace
integrations will function.

## Known limitations

- Selectors and undocumented endpoints are brittle and now likely outdated.
- Authentication is interactive and may require manual anti-bot challenges.
- The code includes broad exception handling and unbounded retry loops that can
  hide failures.
- Fee and commission formulas are embedded directly in the source.
- The code has no automated tests, CI/CD, pre-commit checks, or type checking.
- `DataFrame.append`, used by the project, was removed in pandas 2.0.
- The tracked spreadsheets contain historical product and price data and are
  examples rather than a stable input or output contract.

## Status

Archived in spirit: no support, fixes, or compatibility updates are planned.
