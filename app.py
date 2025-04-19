import gradio as gr  # create web-based user interfaces 
from utils import mask_pii  #handles detection and masking of PII in the email text
from models import predict_category  #function classifies the email text into a category

# function logic that Gradio can use
def classify_email(email_text):
    # Calls the mask_pii function on the input text to give entities , masked_email
    masked_email, entities = mask_pii(email_text)
    # Classifies the masked email using the model
    category = predict_category(masked_email)
    # Returns all the relevant results in a dictionary, which Gradio will format as JSON format o/p
    return {
        "input_email_body": email_text,
        "list_of_masked_entities": entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    }

# creates the Gradio UI
iface = gr.Interface(
    # use classify_email when the user submits input
    fn=classify_email,
    # text box (12 lines) for users to paste the email text
    inputs=gr.Textbox(lines=12, placeholder="Paste support email here..."),
    # output is shown in JSON format for readability
    outputs="json",
    #  title and description for the Gradio app
    title="Email Classifier for Support Team",
    description="This app masks PII and classifies support emails into categories like Billing, Tech Support, etc."
)

# Launch the App
if __name__ == "__main__":
    iface.launch()
