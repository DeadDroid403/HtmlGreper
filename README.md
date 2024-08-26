# Html-Greper

HtmlGreper is a Python-based tool designed to fetch and save the HTML source code of web pages, allowing users to search for specific keywords across multiple web pages at once. This tool is particularly useful for tasks like searching for specific text, emails, or flags in bulk HTML content.


## Documentation

This documentation outlines the usage and implementation details of this HTML-Greper project. This Tool Helps You to Search a Specific Keyword or pattern in Multiple Web Pages at Once. It Saves Your Time and Efforts 

## Features

- **Fetch HTML Source:** Automatically collects and saves the HTML source of web pages listed in a file.
- **Keyword Search:** Searches for a given keyword within the saved HTML files.
- **Case Sensitivity:** Supports case-insensitive keyword searching.
- **Simple CLI Interface:** User-friendly command-line interface to provide input and control the tool's behavior.

## Requirements

- Python 3.x
- Requests Library (`pip install requests`)

## Usage

### Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/deaddroid403/HtmlGreper.git
```

Navigate to the project directory:

```bash
cd HtmlGreper
```

### Examples

- Fetch HTML Source code
```bash
python3 HtmlGreper.py -f dirlist.txt
```

- Seaching For A Keyword
```bash
python3 HtmlGreper.py -g "keyword"
```

- Combining Fetching And Searching
```bash
python3 HtmlGreper.py -f dirlist.txt -g "keyword"
```

- Case insensitive 
```bash
python3 HtmlGreper.py -f websites.txt -i -g "email"
```


## Error Handling

- The tool automatically handles issues such as missing directories or files.
- If the HTML source for a URL cannot be fetched, the tool will notify you and continue with the next URL.

## Contributing

If you'd like to contribute to `HtmlGreper`, feel free to submit a pull request or open an issue for discussion.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

