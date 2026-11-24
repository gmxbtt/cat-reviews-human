# Cat Reviews Its Human

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)

One funny single-line one-star review, written by a house cat about the
human it lives with — for the make.fun bounty
**"Make the AI Judge Laugh: Cat Reviews Its Human"** ($2 prize pool).

## The review

> One star. He refills my bowl only after I scream at the same empty bowl for twenty minutes, then acts shocked when his charger tastes like dinner.

146 characters, one line, deadpan one-star-review shape — and a complaint
only a cat would make: the food bowl is sacred, the human is slow, and the
charger pays the price.

## How it works

`main.py` writes the review text to `/output/entry.txt` (or
`$MAKEFUN_OUTPUT_DIR/entry.txt`). It asserts the gate before writing:
1–200 characters, a single line, not only whitespace. No network, no
dependencies — just the standard library.

## Run it

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
