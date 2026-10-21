---
name: Sacked in the Morning
description: Every gameweek printed as a tabloid back page of who r/PremierLeague and r/FantasyPL are turning on, and who they love.
colors:
  paper: "#eef0f1"
  paper-2: "#dfe3e5"
  white: "#ffffff"
  ink: "#111111"
  ink-2: "#3a3a37"
  muted: "#5f5f5a"
  hair: "#c3c8cb"
  red: "#d7141a"
  red-ink: "#b80f15"
  green: "#1c7a38"
  yellow: "#ffd400"
  neutral: "#8f8f88"
typography:
  masthead:
    fontFamily: "Anton, 'Arial Narrow', sans-serif"
    fontSize: "clamp(23px, 6.8vw, 46px)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "0.01em"
  display:
    fontFamily: "Anton, 'Arial Narrow', sans-serif"
    fontSize: "clamp(64px, 23vw, 136px)"
    fontWeight: 400
    lineHeight: 0.86
    letterSpacing: "-0.01em"
  display-name:
    fontFamily: "Anton, 'Arial Narrow', sans-serif"
    fontSize: "clamp(64px, 20vw, 140px)"
    fontWeight: 400
    lineHeight: 0.86
    letterSpacing: "normal"
  page-head:
    fontFamily: "Anton, 'Arial Narrow', sans-serif"
    fontSize: "clamp(52px, 15vw, 104px)"
    fontWeight: 400
    lineHeight: 0.88
    letterSpacing: "-0.005em"
  figure:
    fontFamily: "Anton, 'Arial Narrow', sans-serif"
    fontSize: "80px"
    fontWeight: 400
    lineHeight: 0.9
  figure-verdict:
    fontFamily: "Anton, 'Arial Narrow', sans-serif"
    fontSize: "58px"
    fontWeight: 400
    lineHeight: 0.9
  section:
    fontFamily: "Anton, 'Arial Narrow', sans-serif"
    fontSize: "32px"
    fontWeight: 400
    lineHeight: 1
  headline:
    fontFamily: "Anton, 'Arial Narrow', sans-serif"
    fontSize: "27px"
    fontWeight: 400
    lineHeight: 0.95
  tab:
    fontFamily: "Anton, 'Arial Narrow', sans-serif"
    fontSize: "21px"
    fontWeight: 400
    lineHeight: 1
  name-box:
    fontFamily: "Anton, 'Arial Narrow', sans-serif"
    fontSize: "20px"
    fontWeight: 400
    lineHeight: 1.2
  deck:
    fontFamily: "'Source Serif 4', Georgia, serif"
    fontSize: "20px"
    fontWeight: 700
    lineHeight: 1.3
  page-deck:
    fontFamily: "'Source Serif 4', Georgia, serif"
    fontSize: "19px"
    fontWeight: 700
    lineHeight: 1.35
  body:
    fontFamily: "'Source Serif 4', Georgia, serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.5
    fontFeature: "tnum"
  quote:
    fontFamily: "'Source Serif 4', Georgia, serif"
    fontSize: "19px"
    fontWeight: 400
    lineHeight: 1.45
  row-name:
    fontFamily: "'Source Serif 4', Georgia, serif"
    fontSize: "16px"
    fontWeight: 700
    lineHeight: 1.2
  note:
    fontFamily: "'Source Serif 4', Georgia, serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.45
  label:
    fontFamily: "'Archivo Narrow', 'Arial Narrow', sans-serif"
    fontSize: "12px"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0.06em"
  legend:
    fontFamily: "'Archivo Narrow', 'Arial Narrow', sans-serif"
    fontSize: "14px"
    fontWeight: 500
    lineHeight: 1.3
rounded:
  none: "0px"
  round: "50%"
spacing:
  xs: "4px"
  sm: "8px"
  md: "14px"
  lg: "16px"
  column: "28px"
  section: "30px"
  page-end: "44px"
  gutter: "14px"
components:
  masthead:
    backgroundColor: "{colors.red}"
    textColor: "{colors.white}"
    typography: "{typography.masthead}"
    padding: "10px 14px 9px"
  live-flash:
    backgroundColor: "{colors.yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "6px 8px"
  strap:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    padding: "8px 14px"
  section-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.white}"
    typography: "{typography.label}"
    padding: "16px 2px 17px"
  section-bar-current:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.yellow}"
  pill-hated:
    backgroundColor: "{colors.red}"
    textColor: "{colors.white}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "6px 8px"
  pill-sell:
    backgroundColor: "{colors.red}"
    textColor: "{colors.white}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "6px 8px"
  pill-neutral:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "6px 8px"
  pill-hold:
    backgroundColor: "{colors.yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "6px 8px"
  pill-loved:
    backgroundColor: "{colors.green}"
    textColor: "{colors.white}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "6px 8px"
  pill-buy:
    backgroundColor: "{colors.green}"
    textColor: "{colors.white}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "6px 8px"
  figure-hated:
    textColor: "{colors.red-ink}"
    typography: "{typography.figure}"
  figure-sell:
    textColor: "{colors.red-ink}"
    typography: "{typography.figure}"
  figure-hold:
    textColor: "{colors.ink}"
    typography: "{typography.figure}"
  figure-loved:
    textColor: "{colors.green}"
    typography: "{typography.figure}"
  figure-buy:
    textColor: "{colors.green}"
    typography: "{typography.figure}"
  split-bar:
    height: "10px"
  split-bar-row:
    height: "8px"
  inside-strap:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    typography: "{typography.headline}"
    padding: "14px 0"
  comment-quote:
    textColor: "{colors.ink}"
    typography: "{typography.quote}"
    padding: "16px 0"
  segment:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "9px 10px 8px"
  segment-hover:
    backgroundColor: "{colors.paper-2}"
  segment-on:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.white}"
  period-select:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "9px 30px 8px 10px"
  search-field:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "9px 10px"
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.white}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "10px 14px 9px"
  tab:
    textColor: "{colors.muted}"
    typography: "{typography.tab}"
    padding: "8px 0 10px"
  tab-active:
    textColor: "{colors.ink}"
  map-club:
    backgroundColor: "{colors.paper-2}"
    rounded: "{rounded.none}"
  map-name-box:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    typography: "{typography.name-box}"
    padding: "6px 7px"
  map-name-box-hover:
    backgroundColor: "{colors.yellow}"
  map-more-box:
    backgroundColor: "{colors.paper-2}"
    textColor: "{colors.muted}"
    typography: "{typography.label}"
  kit-card:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    width: "clamp(64px, 17vw, 108px)"
  captain-armband:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.yellow}"
    rounded: "{rounded.round}"
    size: "22px"
  mini-back-page:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  mini-masthead:
    backgroundColor: "{colors.red}"
    textColor: "{colors.white}"
    padding: "7px 8px 6px"
---

# Design System: Sacked in the Morning

## Overview

**Creative North Star: "The Back Page"**

Every gameweek is printed as a tabloid back page. The most-slated player gets the splash: a pun headline in heavy condensed caps over a halftone print of his club's shirt, a byline crediting the subreddit and the comment count, a one-line deck, and the share in big verdict-coloured figures. Everyone else gets an inside-page strap. The material is newsprint and ink: a cool grey ground, black type, thick black rules, and colour only where a verdict is being called.

It is loud on purpose and honest on purpose. The voice is terrace slang and tabloid puns, but every figure is printed with the number of comments it rests on, and every verdict leads to the comments behind it. The density is a sports page read one-handed on a phone: one splash, three straps, the comments, then the full table, with a black section bar always under the thumb.

The world refuses the stats-app arrangement of avatar cards and widget dashboards, and it refuses anything that looks official: no league or FPL crests, kits, sponsor marks, colours or fonts. A club is a plain jersey in its home colours.

**Key Characteristics:**
- Cool newsprint ground, black ink, and a ladder of black rules (4px, 2px, 1px).
- One tabloid red for the masthead and every hated or sell verdict; green for loved and buy; yellow for hold and the LIVE flash.
- Anton caps for headlines and figures, Source Serif 4 for decks, body and comments, Archivo Narrow caps for straps, bylines and labels.
- Halftone prints of the club's plain jersey behind display type.
- Square corners, flat surfaces, no shadows for depth.
- Phone first; pages, not modals; every view has its own hash address.

## Colors

Newsprint and ink, with three verdict inks that each mean exactly one thing.

### Primary
- **Tabloid Red** (#d7141a): the masthead band (and the mini masthead on each archived back page), and the fill of every hated or sell verdict: pills, split-bar segments, the verdict strip on a kit card. White type on it.
- **Verdict Red Ink** (#b80f15): hated or sell as text on paper: the splash share figure, the verdict figure on a player page, "Hated 85%" in a map box, the coloured verdict in a club list. Darker than Tabloid Red so small text holds on paper.

### Secondary
- **Pitch Green** (#1c7a38): loved and buy, as a fill with white type (pills, bars, kit strips) and as text on paper (figures, verdict words). Nothing else is green.

### Tertiary
- **Flash Yellow** (#ffd400): hold as a fill (pill, bar segment), and the LIVE flash sticker. As a highlighter it marks state only: the focus ring, text selection, the skip link, the current section in the black bar, and the hover fill on a tappable map box or kit name. Always ink type on it, never white.

### Neutral
- **Newsprint** (#eef0f1): the page ground; also the fill of controls, the tagline and the mini back pages, so they sit on the paper.
- **Newsprint Shade** (#dfe3e5): the second paper: club boxes on the map, the "+N more" box, the shirt well on a kit card, segment hover, the scrollbar track.
- **White** (#ffffff): the brightest paper, for boxes a reader taps to open a player (map name boxes, kit cards) and the search field; and type on red, green and ink.
- **Ink** (#111111): all type, every rule, the section bar, the pressed segment, the button, the scrollbar thumb.
- **Soft Ink** (#3a3a37): secondary prose: notes, strap meta lines, the footer; and the neutral verdict as text.
- **Muted Ink** (#5f5f5a): quiet labels: inactive tabs, comment sources, comment counts under table values, the "+N more" label.
- **Hairline** (#c3c8cb): the 1px divider between table rows and between comments; an empty gameweek in the form guide.
- **Neutral Grey** (#8f8f88): the neutral verdict fill (pill, bar segment), with ink type.

### Named Rules
**The Verdict Ink Rule.** Red is hated or sell, green is loved or buy, yellow is hold, grey is neutral. A red, green or yellow mark on content is always a verdict, and a verdict always takes its own ink; no other meaning borrows these colours.

**The Masthead and Flash Rule.** Outside verdicts, red appears only as the masthead band, and yellow only as the LIVE flash and the state highlighter (focus, selection, current section, hover fill). Everything else is ink on newsprint.

**The Home Colours Rule.** Club colours are data, not palette. They appear only on a club's own marks: its plain jersey, the halftone print of that jersey, its name band on the club map and its chip in a page tagline, with ink or white type picked by the colour's lightness. Never as a page accent.

## Typography

**Display Font:** Anton (with Arial Narrow, sans-serif)
**Body Font:** Source Serif 4 (with Georgia, serif)
**Label/Mono Font:** Archivo Narrow (with Arial Narrow, sans-serif)

All three are self-hosted from `site/fonts/` (SIL OFL; latin and latin-ext, so Šeško, Muñoz and Ünal set correctly): Anton 400, Archivo Narrow 500 and 700, Source Serif 4 400, 700 and italic 400.

**Character:** A back page in three voices. Anton shouts the verdict in compressed caps, Source Serif 4 tells the story and quotes the fans in a sturdy news serif, and Archivo Narrow does the small print in tracked narrow caps. Numbers are tabular everywhere.

### Hierarchy
- **Display** (Anton 400, clamp(64px, 23vw, 136px), 0.86, -0.01em, caps): the splash headline only, about 90px on a 390px phone. Player and club page names use Display Name (clamp(64px, 20vw, 140px), 0.86). Both run past a generic 96px display ceiling on purpose: on a back page the splash is the page.
- **Headline** (Anton 400, 27px, 0.95, caps): inside-page straps; archive mini back pages use 30px at 0.9. Page heads for Clubs, Archive and Team are Anton clamp(52px, 15vw, 104px) at 0.88, balanced.
- **Title** (Anton 400, 32px, 1, caps): section heads under a 4px rule; table tabs (21px, 18px on phones) and map name boxes (20px, fitted 9–26px) share the face.
- **Figures** (Anton 400; 80px at 0.9 for the splash share, 58px at 0.9 for a player's per-subreddit verdict, 25px for table values): numbers are set in the headline face and take the verdict's text ink.
- **Deck** (Source Serif 4 700, 20px, 1.3, max 30ch): one bold line under the splash; page decks are 19px at 1.35, max 46ch.
- **Body** (Source Serif 4 400, 17px, 1.5): running text. Notes and the footer are 14px (1.45 and 1.5), max 62–70ch. Player names in lists are Source Serif 4 700 at 16px.
- **Quote** (Source Serif 4 italic 400, 19px, 1.45, max 62ch): a fan's comment in curly quotes; the only italic in the system.
- **Label** (Archivo Narrow 700, 12px, 1.3, 0.06em, uppercase): the strap, bylines, pills, the section bar, comment sources, the button and the select. Segment labels keep the subreddit's own case. Legends are Archivo Narrow 500 at 14px, sentence case.

### Named Rules
**The Headline Is the Verdict Rule.** A headline is written from the verdict as a pun on the player's surname ("Taxi for Dedic", "Rice? On your bike"), a new one each gameweek. Never a neutral label like "Most hated player".

**The Byline Rule.** Credits sit under the headline as a byline in label caps: subreddit · comment count · gameweek. Nothing labels a headline from above.

**The Fit, Never Cut Rule.** Display names and box names shrink toward a floor (44px for the splash, 36px for a page name, 9px in a map box) and are never truncated or ellipsised. In a map box, a name that cannot fit at its floor is not printed.

## Layout

Phone first. One column at a 14px side gutter (the safe-area inset when larger), widening to a 1180px column. On phones the black section bar is fixed to the bottom of the screen in four equal columns and the body reserves 52px for it. From 900px the bar moves under the strap and sticks to the top, its links left-aligned 30px apart.

The back page reads top to bottom: masthead (name and LIVE flash), strap (both subreddits left, update time right, over a 4px rule), splash, inside straps, "What they're saying", the table, footer. From 900px the splash and the straps sit side by side at 2fr and 1fr, 28px apart, with a 2px ink column rule.

Rhythm is tight inside a group and wide between groups: 4–8px between headline, byline and deck; 14–16px between items; 30px above each section head and its 4px rule; 44px before the footer. Sections are separated by rules, not by boxes.

Grids: a table row is rank (30px), jersey (30px), name (up to 260px), split bar, value (62px); on phones the bar drops under the name. The two per-subreddit verdicts on a player page pair up from 700px. Archive mini back pages run 2 columns, 3 from 700px and 4 from 1000px, 14px apart.

### Named Rules
**The Thumb Bar Rule.** The four sections (Back page, Clubs, Archive, Team) are always one tap away: under the thumb on phones, sticky at the top from 900px.

**The Page, Not Modal Rule.** Every view has its own hash address (`#`, `#gwN`, `#pN`, `#clubs`, `#club-XXX`, `#archive`, `#team`). A player or a club opens as a page with a back link, never as a modal.

## Elevation & Depth

Flat newsprint. Nothing casts a drop shadow. Structure comes from black rules (4px between page parts and above section heads, 2px around boxes and controls, 1px ink under straps and tab rows, 1px hairline between rows and comments) and from the two paper tones. The only layering is print over print: a halftone jersey under display type, with the letters knocked out of the dots by a soft paper halo.

### Shadow Vocabulary
- **Paper knockout** (`text-shadow: 0 0 2px var(--paper), 0 0 7px var(--paper)`): only on display type set over a halftone print (splash, page name, archive mini headline). Keeps the letters clean of dots; it is not depth.
- **Focus ring** (`outline: 3px solid var(--yellow); outline-offset: 2px; box-shadow: 0 0 0 5px var(--ink)`): a yellow ring framed in ink so it reads on paper, red and black alike.
- **Current section** (`box-shadow: inset 0 3px 0 var(--yellow)`): a 3px yellow rule along the top of the current link in the section bar.

### Named Rules
**The Flat Newsprint Rule.** Nothing floats. When something needs separating it gets a black rule or the second paper tone, never a shadow.

**The Halftone Print Rule.** A display head (the splash, a player or club page name, an archived back page) sits over one halftone print of the club's plain jersey: club-colour dots on a 2.3-unit grid in the 64-unit jersey, faded by a radial vignette and bleeding off the right edge at 50–55% opacity. White shirts print in their trim colour. On a page name the print sits under the last letters. One print per head, never behind body text.

## Shapes

Square. Every box, pill, control, field and select has square corners (0px; the select resets the platform rounding). The only circles are the red LIVE dot inside the flash and the captain's armband on the team sheet. The LIVE flash is a yellow sticker tilted 3°, the one rotated object, repeated as the "Live" tag on the current archive page.

The one drawn figure is the plain jersey: a single 64-unit silhouette in the club's home colour with contrasting collar and cuff lines, optional vertical stripes clipped to the torso, and a thin dark outline. No crests, badges, sponsors or numbers. Icons are authored 2px-stroke SVG (the back arrow, the select chevron).

### Named Rules
**The Square Corner Rule.** 0px radius everywhere. Circles are reserved for the LIVE dot and the armband.

## Components

### Masthead and LIVE flash
Shouted, then dated.
- **Masthead:** a full-width red band, the name in Anton caps, white, never wrapping, 10px above and 9px below.
- **LIVE flash:** a yellow label sticker ("Live · GW8") with a 7px red dot, 6px 8px, rotated 3°, ink type.
- **Strap:** label caps under the masthead, both subreddits left and "Updated 53 min ago" right, 8px padding, a 4px ink rule beneath.

### Navigation
- **Section bar:** black, four links in white label caps. Current: yellow text with a 3px yellow top rule. Hover: yellow text. Phones: fixed bottom, equal columns, 16px/17px padding. From 900px: sticky top, 12px/11px padding.
- **Table tabs:** Anton 21px caps (18px on phones) in muted ink over a 1px ink base; the active tab turns ink and gets a 4px rule beneath. They scroll sideways when they overflow.
- **Back link:** label caps with a 2px-stroke arrow above a page head; underline on hover.

### Verdict pills (chips)
- **Style:** label caps on a solid verdict fill, 6px 8px, square, no border. Hated and Sell red with white; Neutral grey with ink; Hold yellow with ink; Loved and Buy green with white. Archive minis use a 10px pill (3px 5px 2px).
- **State:** read-only. A pill is the verdict, not a filter.

### Verdict split bar
- Flat segments for the three answers in verdict fills, 2px apart, 10px tall (8px in table rows), each at least 2px wide, labelled for screen readers with all three percentages. On a player page a legend follows: 10px squares and Archivo Narrow 500 14px ("Negative 45%").
- A printed ruling of the split, not a progress meter: no track, no rounded ends.

### Splash
- The display headline over the halftone print, the surname emphasised; the byline; the deck; the figure (the share in Anton 80px in the verdict's text ink beside a two-line label, "negative / of 314 comments"); the split bar; a 4px rule under it all.
- **Hover:** a 5px underline 8px below the headline.
- **Motion:** the live back page prints once. On its first render the halftone dots grow from a pinprick to full size (1100ms, `cubic-bezier(.16, 1, .3, 1)`); reduced motion gets the finished print. Everything else in the system is instant.

### Inside straps
- A 34px jersey, an Anton 27px headline, a 14px serif meta line in soft ink ("r/FantasyPL · 85% sell · 488 comments"), the pill top right. 14px padding, a 1px ink rule under.
- **Hover:** a 3px underline on the headline.

### Comments
- Italic serif 19px in curly quotes, then a source line: verdict pill, subreddit and date in muted label caps, and "Read on Reddit". 16px padding, a hairline under.

### Inputs / Fields
- **Segmented switch:** a 2px ink border on paper, 2px ink dividers, label 12px in the subreddit's own case. Pressed: ink fill, white text. Hover: paper shade.
- **Period select:** label caps 13px, 2px ink border, square, an authored chevron.
- **Search field:** white, 2px ink border, serif 16px, square.
- **Focus:** the yellow ring framed in ink (see Elevation & Depth).

### Buttons
- **Primary:** ink fill, white label caps, 2px ink border, 10px 14px 9px, square ("Show all 215", "Try again"). It is the only button style.

### Club map
The signature view: every club at once, sized by talk.
- **Clubs:** a squarified map, each club sized by its comment total, boxed with a 2px ink border on paper shade, 3px apart, headed by a band in the club's home colour (ink or white type by lightness) with the club name and total when there is room. The band opens the club page. Phones draw the map 2.4 times as tall as it is wide (32px bands, 3 players per club); desktop 0.66 (24px bands, 5 players).
- **Players:** the club's most-discussed players as white name boxes sized by comment count: the surname in Anton caps fitted 9–26px, and the bigger side as verdict text ("Hated 85%") when the box is at least 80 by 46px. Hover: yellow fill.
- **"+N more":** a player whose surname cannot be set at 9px folds into one quiet box (paper shade, muted label caps) that links to the club page and is never bigger than the smallest named box. Names are fitted or omitted, never cut.
- **Club page:** one club's map with every discussed player, then the full ranked list.

### Team sheet
- A pitch with a 4px ink frame, a 2px inner line inset 10px, a penalty box, and a halftone dot field on a 7px grid. Kit cards 64–108px wide: white, 2px ink border, the jersey on paper shade, the surname in Anton 15px fitted, a verdict strip in the verdict fill. The captain wears an ink armband circle with a yellow C.

### Archive mini back pages
- Each gameweek kept as a small back page: a red mini masthead (GW number left, date or the yellow "Live" sticker right), a 30px headline over a halftone print, the share figure, then two straps with pills. 2px ink border on paper. Hover underlines the headline.

## Do's and Don'ts

### Do:
- **Do** print every figure with the number of comments it rests on, in label caps beside or under it ("of 314 comments").
- **Do** write each headline from the verdict as a pun on the surname, and credit it underneath with a byline: subreddit · comments · gameweek.
- **Do** give a verdict its own ink wherever it appears: the fill for pills, bars and kit strips, the text ink (#b80f15 for hated and sell, #1c7a38 for loved and buy, ink for hold) for figures and verdict words.
- **Do** separate with black rules: 4px between page parts and above section heads, 2px around boxes and controls, 1px hairline between rows.
- **Do** put one halftone print of the club's plain jersey behind each display head, faded off to the right, with the paper knockout on the type.
- **Do** fit names down to their floor or leave them out, and fold unnamed players on a map into one "+N more" box.
- **Do** design at 390px first: the splash headline at about 90px, the section bar under the thumb.

### Don't:
- **Don't** put red, green or yellow on anything that is not a verdict, the masthead, the LIVE flash or a focus, selection, hover or current state. Chrome is ink: no red tab rules, no red hover fills, no red word in a loved or bought headline.
- **Don't** use anything official: no Premier League or FPL crests, logos, player photos, kit designs, sponsor marks, the league's colours or its fonts. A club is a plain jersey in its home colours.
- **Don't** put a label line above a headline (eyebrow, kicker, section tag). A player's first name over his surname is part of the name; a back link or a mini masthead band is navigation.
- **Don't** truncate a name with an ellipsis or cut it at a box edge.
- **Don't** open a player or a club in a modal.
- **Don't** round corners or add drop shadows for depth; the only circles are the LIVE dot and the captain's armband.
- **Don't** fall back to the stats-app arrangement of avatar cards and widget tiles. A player is his surname and his jersey; a gameweek is a back page.
