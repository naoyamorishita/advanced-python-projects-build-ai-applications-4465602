# import package
from textblob import TextBlob as tb

# class of chat bot
class ChatBot:
    def __init__(self):
        self.sentiment_analyzer = tb("")

    def start_chat(self):
        print("Chatbot: Hi, how can I help you?")
        # get users message and removes spaces etc
        while True:
            user_message = input("You: ").strip()
            # sentiment analysis
            self.sentiment_analyzer = tb(user_message)
            # calculate sentiment polarity score
            sentiment_score = self.sentiment_analyzer.sentiment.polarity

            # generate chat bot response based on sentiment
            if sentiment_score > 0:
                chatbot_message = f"Chatbot: That's great to hear:\n SentimentScore: {sentiment_score}"
            elif sentiment_score < 0:
                chatbot_message = f"Chatbot: I'm sorry to hear that.\n Sentiment Score: {sentiment_score}"
            else:
                chatbot_message = f"Chatbot: Hmm, can you give me more info?\n SentimentScore{sentiment_score}"
            print(chatbot_message)
            
if __name__ == "__main__":
    # Creating the chatbot and starting the chat loop.
    chatbot = ChatBot()
    chatbot.start_chat()
