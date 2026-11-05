---
name: gtm-slop-filter
description: Enforce writing rules that stop AI-generated copy from reading like AI-generated copy. Use this skill whenever producing or editing customer-facing writing: landing pages, cold email, sequences, ad copy, social posts, newsletters, launch announcements, one-pagers, scripts, or any marketing or sales copy. Also use it when the user asks to make copy sound human, less generic, less like AI, less corporate, or less like marketing, or asks to remove buzzwords, remove em dashes, cut the fluff, tighten the writing, or edit a draft they say reads like ChatGPT wrote it. Triggers include "make this sound less like AI", "rewrite this so it doesn't sound generic", "edit my landing page copy", "why does this read like slop", "punch this up", "make it human".
---

# GTM Slop Filter

Generic output is not a model problem, it is a missing-constraint problem. With no constraints, writing regresses to the mean of everything ever published, and the mean of B2B marketing copy is slop. These constraints move it off the mean.

Apply every rule below to every word of customer-facing output. When editing someone else's draft, apply them as edits and say what changed.

## Banned words

Do not use these or their obvious variants:

leverage, unlock, seamless, robust, streamline, cutting-edge, empower, elevate, revolutionize, game-changing, best-in-class, world-class, supercharge, turbocharge, harness, delve, tapestry, landscape (figurative), navigate (figurative), realm, testament, journey (unless a literal one), foster, facilitate, utilize, myriad, plethora, pivotal, crucial, vital.

When a banned word is the only word that fits, the sentence has no specific claim in it. Find the claim, or cut the sentence. Do not reach for a synonym.

## Banned structures

- No em dashes. Use a comma, or split the sentence.
- No "It's not just X, it's Y." No "In today's fast-paced world." No "Let's dive in." No "In conclusion." No "The bottom line is."
- No rule of three used as decoration ("faster, smarter, better").
- No sentence opening with "Whether you're."
- No rhetorical question as an opener.
- Do not open by restating the request.
- No emoji unless asked for.

## Sentences

- Vary length deliberately. A short one after a long one.
- One idea per sentence. Paragraphs of one to three sentences.
- Front-load the point. The reader should get it from the first clause.
- Cut every adverb that is not doing work.
- Prefer the concrete noun to the abstract one. "Churn" over "attrition dynamics." "Sales rep" over "revenue professional."

## Claims

- Specific numbers, named capabilities, and verifiable facts over adjectives.
- Never invent a statistic, customer name, testimonial, or case study. Write `[PROOF POINT NEEDED]` and keep going.
- Scope every superlative. "Only," "first," "best," and "never" get a qualifier that survives scrutiny, or they get cut.
- Never describe an unbuilt capability in the present tense. If status is unknown, ask, or mark it.

## Voice

- Write to one reader, not an audience. Second person.
- Say the uncomfortable part. Copy that refuses to acknowledge a tradeoff reads as marketing, and marketing gets skipped.
- If a sentence could appear in a competitor's copy with the company name swapped, delete it and write the version that could not.

## Writing for the ear

For anything spoken, scripts, video, voiceover, these replace the page rules.

- Short spoken sentences. One clause where you would normally write two.
- Contractions and second person. Talk to one listener.
- Front-load the point of each sentence. Listeners cannot re-read.
- Signpost with spoken connective tissue, not headers.
- Read it aloud. If you stumble or run out of breath, cut it.

## Before returning anything

Re-read the draft against every rule above and fix what breaks. Then state, in one line, which rule the draft came closest to breaking. That line is not padding. It tells the user where the copy is weakest.

## The limit of this skill

These rules govern *how* copy is written. They know nothing about the company: what shipped, what may be claimed, which proof points are real, which channels the strategy excludes. That context is what the `go-to-market-brain` skill builds and enforces. If a project has a built brain, load its control layer first and treat these rules as the floor, not the ceiling.
