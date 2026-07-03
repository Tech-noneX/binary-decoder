# Binary Decoder

A small Python practice project that converts binary input into decimal form.

The current script uses a hard-coded list of bits, builds the matching powers of two, and prints the decimal result.

## Current Features

- Converts a list of `0` and `1` values into a decimal number
- Checks that the list contains only valid binary digits
- Shows the core conversion logic step by step in `simple_binary_decoder.py`

## Project Files

- `simple_binary_decoder/simple_binary_decoder.py` - main decoder script
- `requirements.txt` - Python packages currently recorded for the environment

## How To Run

From the project folder:

```bash
python simple_binary_decoder/simple_binary_decoder.py
```

The script currently decodes this value:

```python
binary = [1, 0, 0, 1, 1, 0, 0, 1]
```

To test another binary number, edit the `binary` list in `simple_binary_decoder.py`.

## Future Ideas

- Accept binary strings, such as `01001000`
- Accept space-separated binary blocks, such as `01001000 01100101`
- Decode binary into ASCII text
- Add functions and tests so the decoder is easier to reuse

## Notes

This is part of a Python learning journey, so the project is intentionally small and will grow over time.
