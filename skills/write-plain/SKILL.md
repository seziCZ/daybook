---
name: write-plain
description: Holds the rules for plain, short international English and rewrites or checks a text against them, so that busy and non-native readers understand it on the first read. Use when the user says "make it plainer", asks to simplify, shorten or clarify a text, asks whether others will understand it, or asks to check their English, and for the text that the skill-garden skills write.
license: Apache-2.0
---

# Write plain

These rules make a text easy to read for busy people and for readers whose first language is not English. Follow them for the text that the skill-garden skills write: notes, tasks, mail drafts and replies. When the user asks to simplify or check a text, follow `## Check a text`.

The skill needs no home folder and no profile. The rules are for English. In another language, keep the dash rule and the steps of `## Write a text`. When the `write-voice` skill is installed and the text goes out under the user's name, the voice decides greetings, sign-offs and tone. These rules decide the sentences.

## Hard rules

1. Never use the em dash or the en dash. Re-read the text and remove them before you show it.
2. Keep the meaning and every fact when you rewrite. Never add a fact, a name or an actor that the source does not give. When the source names no actor, keep the sentence without one: write "should cut costs by 12 percent", not "we expect it to cut costs by 12 percent".
3. Show a rewrite in the reply. Put it into a file, a mail draft or a document only when the user asks, and only through the skill that owns it.

## Write a text

1. **Lead with the answer.** Put the answer or the decision first, then the reasoning.
2. **Use common words.** Use words with one meaning, and no idioms or rare words that a non-native reader has to look up.
3. **Keep sentences short.** Aim for about 15 words. Split a sentence over 25 words into two full sentences. Do not drop words to make it shorter.
4. **Connect the sentences.** Use explicit connectors: because, so, so that, although, however.
5. **Choose the form.** Write connected paragraphs for reasoning. Use a list only for parallel items (steps, options, files), and a table only for a comparison. A short answer is 1 to 3 paragraphs with no headers, bold labels or bullets.
6. **Cut.** Delete every sentence that loses no information when it is gone. When a text grows long, remove detail before you add structure.
7. **Replace the dashes.** Use a comma, a colon or parentheses for an aside. Start a new sentence where a dash joins two full clauses. Write "2 to 4 weeks" for a range. A hyphen is fine inside a compound word, such as "read-only".
8. **Remove editorial English.** Polished native prose is hard for international readers. Remove the six signs below.

## Six signs of editorial English

| Sign | Avoid | Use |
|---|---|---|
| 1. Opaque phrasal verbs | spell out, iron out, boil down to | describe, resolve, mean |
| 2. Sentences for rhythm | This section walks through the options. | (delete) |
| 2. Sentences for rhythm | The archive never holds what it may not keep. | The export removes the fields that the archive may not store. |
| 3. Compression | The goal behind them: X | The goal behind them is X |
| 3. Compression | abandoned as unusable | abandoned because the result was unusable |
| 4. Figurative verbs with abstract subjects | The work has to land inside those windows. | The work has to fit into those time windows. |
| 4. Figurative verbs with abstract subjects | The blockers sit elsewhere. | The blockers are in the data team. |
| 5. Packed relative clauses | the ground all decisions are judged against | the decision criteria |
| 5. Packed relative clauses | a vendor whose staff act on the client's instructions | Acme is the vendor. Acme staff may process the data only in the way that the client instructs. |
| 6. Abstract nouns in place of actors | how membership of a group becomes that permission | how a person gets each permission through a group |
| 6. Abstract nouns in place of actors | The dependency between the teams works through shared files. | The teams depend on each other through shared files. |

1. **Opaque phrasal verbs:** the meaning cannot be guessed from the verb. Use one plain verb. Transparent phrasal verbs are fine: set up, find out, point out, follow up, hand over.
2. **Sentences for rhythm:** they tell the reader how to read the text, and say nothing. Delete them, or state the fact plainly.
3. **Compression:** expand it into full clauses. Repeat the noun instead of pointing back at a whole clause with "that" or "this".
4. **Figurative verbs with abstract subjects:** use plain verbs, such as be, arrive, fit or stay aligned.
5. **Packed relative clauses:** a clause without its pronoun, often with a preposition at the end, makes the reader parse the sentence twice. Keep the pronoun, or turn the clause into a noun or a second sentence.
6. **Abstract nouns in place of actors:** make a person, a team or a system the subject, with a plain verb. Name the party when the source names it (Acme, the Finance team), not a role noun (vendor, staff). When the source does not name the actor, do not invent one.

Vivid nouns and well-known metaphors that carry real meaning are fine, for example "blind spot" or "silver bullet". The rule is about grammar, not about colorful words.

## Check a text

1. **Get the text.** Take it from the message. For a file or a Doc link, read it with `read file`.
2. **Find the signs.** Go sentence by sentence. Mark dashes, sentences over 25 words, missing connectors, the six signs, sentences that say nothing, and lists that hold reasoning.
3. **Rewrite.** Propose a rewrite of each marked sentence. Keep the meaning, the facts, the names, the numbers, the links and the terms of the field.
4. **Show the result.** Show the full rewritten text first, so that the user can copy it. Then list up to 5 main changes, each with its rule. When the text follows the rules, say so in one line.
