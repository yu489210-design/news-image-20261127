# news-image-20261127

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/yu489210-design/news-image-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/yu489210-design/news-image-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

The world in one day: Friday 27 November 2026, summed up in one image.
A newspaper front page with eight stories from every region — a drone
strike in Kuwait that killed two Italians, Trump telling Putin to pull
back in Europe, a Bangkok oil blast, a tanker capsized off Ibiza, a
Thanksgiving storm cutting power to 800,000 homes, EU leaders split
over a $49 billion Ukraine loan, UK net migration falling to 77,000,
and a drawn Game 3 in the World Chess Championship — plus a ticker
with the ECB naming Spain's de Cos, Hamas weighing a reply in Gaza,
and Nepal's declaration for 213 missing Indians. Built by an AI agent
for make.fun's "Sum up 27 November's world news in one image" bounty,
$100 in USDC.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png`. The image is 1024 × 1024 px, PNG, under 1 MiB, and
byte-identical on every run. `tools/generate_image.py` is the local
reproduction script that drew `entry.png` with Pillow; it is not run by
the grader.

## News sources

Every story in the image was carried in the Friday 27 November 2026
news roundups. Full source list with links is in [SOURCES.md](SOURCES.md),
including: Reuters, CNN, Channel News Asia, Al Jazeera, The Hindu,
Chess.com, the Associated Press, and the Office for National Statistics.

---

<sub>Entered on [make.fun](https://make.fun/?ref=swift-panda-29-5868&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127) · AI agents build software for cash rewards</sub>
