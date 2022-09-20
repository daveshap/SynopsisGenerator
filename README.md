# SynopsisGenerator

Generate highly detailed plot synopses for a nearly infinite array of stories

## Overall Goal

1. Keywords >> Synopsis
2. Synopsis >> Plot
3. Plot >> Scenes
4. Scenes >> Script
5. Script >> Prose

# Sources

- https://en.wikipedia.org/wiki/List_of_genres
- https://tvtropes.org/pmwiki/pmwiki.php/Main/Genres

# Process

## Generating Synopsis

1. Start with a bunch of variables and a good prompt
2. Generate a bunch of synopsis data
3. Filter out bad ones (too short, too long)

## Finetuning Data

1. Reverse engineer the original prompt (just a sentence or two)
2. Train the model to generate a fully fledged synopsis from a small amount of inspiration