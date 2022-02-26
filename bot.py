import os
# Use the package we installed
from slack_bolt import App
from dotenv import load_dotenv


load_dotenv()
# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# Add functionality here
@app.event("app_mention")
def handle_mention(client, event, logger):
    url = "https://studs2022.slack.com/archives/" + event["channel"]+ "/" + event["ts"]
    print(url)
    result = client.chat_postMessage(
        channel="#formulär",
        text=url,
        unfurl_links = True
    )


app.start()