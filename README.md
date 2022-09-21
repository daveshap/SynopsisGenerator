# SynopsisGenerator

Generate highly detailed plot synopses for a nearly infinite array of stories

## Overall Goal

1. Keywords >> Synopsis
2. Synopsis >> Plot
3. Plot >> Scenes
4. Scenes >> Script
5. Script >> Prose

## TODO

- Ensure all synopses have names, dates, places, etc. No half-assed, generic summaries!
- Use a rubric grading scheme for automatic dataset augmentation

# Sources

- https://en.wikipedia.org/wiki/List_of_genres
- https://tvtropes.org/pmwiki/pmwiki.php/Main/Genres

# Process

## Generating Synopsis

1. Start with a bunch of variables and a good prompt
2. Generate a bunch of synopsis data
3. Filter out bad ones (too short, too long)
4. Generate many more synopses with the finetune model later

## Finetuning Data

1. Reverse engineer the original prompt (just a sentence or two)
2. Train the model to generate a fully fledged synopsis from a small amount of inspiration
3. Generate more synopses with the finetuned model and user data
4. Create a feedback loop to improve the synopsis generating dataset

## End Result

End goal should be a finetune dataset with the following characteristics

1. 1000 samples or so
2. Diverse kinds of input (different formats, structures, keywords, appeal terms, varying levels of detail)
3. Consistent output (well fleshed out synopsis that tells the whole story in one big paragraph)
4. Finetuned model that reliably generates top notch synopses