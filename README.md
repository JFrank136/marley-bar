# Marley Bar

A personal, mobile-first cocktail recipe app meant to open from an NFC tag at the home bar. Plain HTML, CSS and JavaScript with no build step and no backend.

## Files
- `index.html` — layout, styles, and an embedded copy of the recipe data (used for `file://` previews).
- `app.js` — UI, inventory matching, servings scaling, running scale targets, Batch Mode.
- `recipes.json` — the source of truth for ingredients, recipes, and which ingredients you own.
- `validate_recipes.py` — checks the recipe data and that the copy embedded in `index.html` matches `recipes.json`.

## Run locally
```
python -m http.server 8000
```
Then open http://localhost:8000. Opening `index.html` directly also works, but it uses the embedded copy of the data.

## Updating the bar
1. Edit the `owned` list in `recipes.json` (ingredient ids, e.g. `"spiced_rum"`).
2. Copy the same JSON into the `recipe-fallback` script tag in `index.html` so the file preview matches.
3. Run `python validate_recipes.py`, which fails if the two copies differ.
4. Commit and push; GitHub Pages redeploys.

Ticking items in the My Bar tab only previews "what if I owned this" and resets on reload. Favorites are saved per phone in the browser.

## Recipe status
- `selection` is how much you want the drink (must, confirmed, interested, experiment, maybe, low-priority, draft, idea).
- `verified: true` means the numeric recipe is complete, not that it has been taste-tested. `tested` marks recipes you have actually made.
- Recipes with `oz: null` (Don Don Juice, Ron Ron Juice) are incomplete and are never scaled or given a strength estimate. Measure your vodka on the next batch and enter it.
- Ingredients can use `"unit": "dashes", "qty": 2` instead of ounces. A recipe with `"whole_batch": true` is written as one full batch, so it scales with the batch multiplier instead of servings.

## Limits
- Scale targets are nominal fluid ounces. Kitchen scales approximate fl oz from weight using water density, so bourbon and thick syrups will read slightly off. A marked jigger is more accurate.
- Refrigerate perishable batches promptly (40°F / 4°C or below). Fizzy ingredients go in when serving. These are handling notes, not shelf-life guarantees.

## Hosting
Deployed with GitHub Pages from the `main` branch root. Nothing in this repo is secret.

## NFC tag
Write the site's URL to an NDEF tag as a plain URL record (for example with the NFC Tools app). Do this last, after the site is live and tested on a phone.

## Later
- Pitcher-capacity guide and strength estimates once Don Don Juice is measured.
- Optional ingredient substitutions and drink images.
