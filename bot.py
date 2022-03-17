import os
# Use the package we installed
from slack_bolt import App
#from dotenv import load_dotenv

#load_dotenv()
# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# Add functionality here
@app.event("app_mention")
def handle_mention(client, event, logger):
    url = "https://studs2022.slack.com/archives/" + event["channel"]+ "/" + event["ts"]
    """ for result in client.conversations_list():
        for channel in result["channels"]:
            if channel["name"] == "name":
                conversation_id = channel["id2]
                #Print result
                print(f"Found conversation ID: {conversation_id}")
                break """
    # Store conversation history
    conversation_history = []
    # ID of the channel you want to send the message to
    result = client.conversations_history(channel="C034T8K06BC")
    latestmessage = result["messages"][0]["text"][1:-1]
    if latestmessage == url:
        return

    result = client.chat_postMessage(
        channel="#formulär",
        text=url,
        unfurl_links = True
    )
    


app.start(port=int(os.environ.get("PORT")))