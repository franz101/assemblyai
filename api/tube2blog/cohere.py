import cohere
from cohere.classify import Example


class CohereAPI:
    def __init__(self, api_key) -> None:
        self.co = cohere.Client(api_key)

    def tutorial_classifier(self, input_text):
        pred = self.co.classify(
            model="large",
            inputs=[input_text],
            examples=[
                Example("The war in ukraine is going on", "non-tutorial"),
                Example(
                    """How to find earnings and news data, and maybe we'll even classify some of this data as well. Show us how to fetch news using the Alpaca News API. Also show you how to use the free y finance package to fetch data from Yahoo. And maybe we can dive into this a little bit more in the future if we start diving into machine learning.
        A headline on Arkinvest says it sees Tesla driving EV stock to $4,600 a share. That sounds very positive, but it labels it as negative. Maybe the move is to do the opposite of what Cathy Wood says.
        Real time streaming news over WebSockets.
        """,
                    "tutorial",
                ),
                Example(
                    """ Once you're connected and authenticated, you just need to subscribe to any stock or crypto symbols that you're interested in getting news about. Here's how it looks when you start receiving news.
        In the next video in this series, we'll take a look at this Quant Rocket article that discusses whether to buy or sell stocks at Gap, up or down. Then we'll write some code to actually place some trades based on this article.""",
                    "tutorial",
                ),
                Example(
                    """What I find incredible is that despite having precise location coordinates the police did not recover it. I think we underestimate the extent to which not capturing petty thieves influences people's trust in "the system" in general.""",
                    "non-tutorial",
                ),
                Example(
                    """I have to say this reads like the Malcolm gladwell parody from the other day where a parallel is drawn between two completely unrelated things.""",
                    "non-tutorial",
                ),
            ],
        )
        return pred.generations[0].text

    def headline_generator(self, input_text):
        prompt = f"""This program generates a viral headline given an input.

Input: Testing the game sonic boom
Headline: "I played Sonic Boom, so you don't have to"
--
Input: Learning about Solidity
Headline: "14 Best Practices for Solidity developers in DeFi"
--
Input: Ask reddit about sex
Headline: "What is one sexual lesson you’ve learned that everyone should learn sooner, rather than later?"
--
Input: {input_text}
Headline:"""
        pred = self.co.generate(
            model="xlarge",
            prompt=prompt,
            max_tokens=20,
            temperature=0.1,
            stop_sequences=["--"],
        )
        return pred.generations[0].text

    def tag_generator(self, input_text):
        prompt = f"""This program generates blog tags given the video industry.
--
Video summary: {input_text}
Task: Write category tags of the video summary seperated by comma.
Tags: video,"""

        pred = self.co.generate(
            model="xlarge",
            prompt=prompt,
            max_tokens=20,
            temperature=0.1,
            stop_sequences=["--"],
        )

        return pred.generations[0].text
